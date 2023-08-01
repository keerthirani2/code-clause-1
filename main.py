import cv2
import numpy as np

class ColorDetector:
    def __init__(self):
        # Define color ranges for multiple colors (in HSV format)
        self.color_ranges = {
            'red': ([0, 100, 100], [10, 255, 255]),
            'orange': ([11, 100, 100], [20, 255, 255]),
            'yellow': ([21, 100, 100], [30, 255, 255]),
            'green': ([31, 100, 100], [80, 255, 255]),
            'light green': ([81, 100, 100], [100, 255, 255]),
            'blue': ([101, 100, 100], [130, 255, 255]),
            'purple': ([131, 100, 100], [160, 255, 255]),
            'pink': ([161, 100, 100], [170, 255, 255]),
            'gray': ([0, 0, 50], [180, 50, 220]),
            'black': ([0, 0, 0], [180, 255, 50]),
            'white': ([0, 0, 200], [180, 30, 255])
        }

    def detect_colors(self, image):
        # Convert the image from BGR to HSV color space
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Initialize an empty list to store detected colors and their positions
        detected_colors = []

        # Iterate through each color range
        for color, (lower, upper) in self.color_ranges.items():
            lower_color = np.array(lower, dtype=np.uint8)
            upper_color = np.array(upper, dtype=np.uint8)

            # Create a mask for the current color range
            color_mask = cv2.inRange(hsv, lower_color, upper_color)

            # Find contours in the color mask
            contours, _ = cv2.findContours(color_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Find the largest contour for each color
            max_area = 0
            largest_contour = None
            for contour in contours:
                area = cv2.contourArea(contour)
                if area > max_area:
                    largest_contour = contour
                    max_area = area

            # If a contour is found, store its position
            if largest_contour is not None:
                x, y, w, h = cv2.boundingRect(largest_contour)
                detected_colors.append((color, x, y, w, h))

        return detected_colors

def main():
    # Access the camera feed (by default, it uses the first available camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to access the camera.")
        return

    detector = ColorDetector()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Call the detect_colors method to detect colors in the frame
        detected_colors = detector.detect_colors(frame)

        # Show the detected colors and their names
        result_frame = frame.copy()
        for color, x, y, w, h in detected_colors:
            # Draw the outline box around the detected color region on the main screen
            cv2.rectangle(result_frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(result_frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        cv2.imshow('Color Detection', result_frame)

        # Exit the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
