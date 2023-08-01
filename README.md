# code-clause-1
# Color Detection Project

!["C:\Users\Hp\Videos\Captures\Color detection – main.py 2023-08-01 20-41-19.mp4"](demo.gif)

## Description

This Color Detection project is a real-time system that identifies various colors using Python and OpenCV. It uses the computer's camera to capture live video and detects colors like red, orange, yellow, green, light green, blue, purple, pink, grey, black, white, and more. The detected colours are outlined on the screen, and their names are displayed.

## Key Features

- Real-time color detection from the camera feed.
- Accurate color range definitions using the HSV color space.
- Displaying outline boxes around the detected color regions.

## Installation

1. Clone the repository to your local machine:
2. git clone https://github.com/keerthirani2/code-clause-1
3. Install the required dependencies: pip install opencv-python numpy

## Usage

1. Run the main Python script:

python main.py

2. The color detection will start, and the camera feed will display the detected colors with their names and outline boxes.

3. Press 'q' to exit the application.

## Color Ranges

The color ranges for different colors are defined in the `ColorDetector` class in the `main.py` file. These ranges are specified in the HSV color space to achieve accurate color detection. You can modify the color ranges to suit your specific use case or add new colors as needed.

## Acknowledgments

I want to thank the OpenCV community and various online tutorials that provided valuable insights into color detection techniques. Their resources were instrumental in building this project.

## Next Steps

In future updates, I plan to add more features, such as object tracking and color-based object recognition, to enhance the functionality of the Color Detection system.
