import math
import cv2
import depthai as dai
from flask import Flask, render_template, send_file

app = Flask(__name__)

# Function to convert millimeters to inches
def convert_milli_to_inch(x):
    x = x / 10
    return x / 25.4

# Define the function to capture images using the OAK camera and compute dimensions
def capture_image_and_compute():
    # Start defining a pipeline
    pipeline = dai.Pipeline()

    # Define a source - color camera
    cam = pipeline.createColorCamera()
    cam.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)

    # Create output
    xout = pipeline.createXLinkOut()
    xout.setStreamName("video")
    cam.video.link(xout.input)

    # Connect and start the pipeline
    with dai.Device(pipeline) as device:
        # Output queue will be used to get the frames from the output defined above
        q = device.getOutputQueue(name="video", maxSize=1, blocking=True)

        # Get the frames from the camera
        frame = None
        while True:
            in_video = q.get()
            frame = in_video.getCvFrame()
            cv2.imshow("OAK Camera", frame)
            
            # Press 's' to capture the image
            key = cv2.waitKey(1) & 0xFF
            if key == ord("s"):
                # Save the captured frame to a file named "object_image.png"
                cv2.imwrite("object_image_web.png", frame)
                break

        # Release the camera
        cv2.destroyAllWindows()

        # Read the captured image
        image = cv2.imread("object_image_web.png")

        # Check if the image was read successfully
        if image is None:
            print("Error: Failed to read the image.")
            return None

        # Select ROI
        roi = cv2.selectROI("Select ROI", image)

        # Extract coordinates and dimensions of the ROI
        x, y, w, h = roi
        print(x, y, w, h)

        # Draw the selected ROI on the image
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Display the image with the selected ROI
        cv2.imshow("Selected ROI", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Define the parameters
        FX = 460.54
        FY = 482.08
        Z = 80  # Adjusted Z value accordingly (8 cms)

        # Draw the rectangle on the image
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)

        # Draw a line from Image_point1 to Image_point2
        Image_point1x = x
        Image_point1y = y
        Image_point2x = x + w
        Image_point2y = y + h
        cv2.line(image, (Image_point1x, Image_point1y), (Image_point1x, Image_point2y), (0, 0, 255), 8)

        # Calculate the real-world coordinates of the points
        Real_point1x = Z * (Image_point1x / FX)
        Real_point1y = Z * (Image_point1y / FY)
        Real_point2x = Z * (Image_point2x / FX)
        Real_point2y = Z * (Image_point2x / FY)

        # Print the real-world coordinates
        print("Real Point 1 (x, y):", Real_point1x, Real_point1y)
        print("Real Point 2 (x, y):", Real_point2x, Real_point2y)

        # Calculate the distance between the points
        dist = math.sqrt((Real_point2y - Real_point1y) ** 2 + (Real_point2x - Real_point1x) ** 2)

        # Convert the distance to inches
        val = round(convert_milli_to_inch(dist * 2), 5)

        # Print the diameter of the green vicks bottle circle in centimeters
        print("Diameter of circular object:", val * 2.54, "cm")

        # Define the position for the text
        text_x = x - 200
        text_y = y + (h // 2) + 5

        # Draw the text on the image
        cv2.putText(image, str(val) + " inches", (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Define the output file path
        output_image_path = "annotated_image_web.png"

        # Save the annotated image
        cv2.imwrite(output_image_path, image)

        # Print a message indicating the image is saved
        print("Annotated image saved as:", output_image_path)

        # Prepare the output information string
        output_info = f"Real-world coordinates (Point 1): {Real_point1x}, {Real_point1y}<br>" \
                      f"Real-world coordinates (Point 2): {Real_point2x}, {Real_point2y}<br>" \
                      f"Diameter of the circle object: {val * 2.54} cm"

        return output_info

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_capture', methods=['POST'])
def start_capture():
    # Run the Python code to capture the image and compute dimensions
    output_info = capture_image_and_compute()
    return render_template('result.html', output_info=output_info)

@app.route('/object_image_with_text')
def get_image():
    return send_file('annotated_image_web.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
