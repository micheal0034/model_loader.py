Certainly! Here's a detailed README for your CCTV monitoring system project:

# CCTV Monitoring System README

## Overview

This CCTV Monitoring System is a Python-based application designed to monitor multiple camera streams, detect objects using the YOLO (You Only Look Once) object detection model, and save images with detected objects to a specified directory. The system is configured to detect and highlight objects of interest in real-time video streams.

## Features

- **Multi-Camera Support:** The system supports monitoring multiple camera streams simultaneously.

- **Object Detection:** It uses the YOLO model to perform real-time object detection in each camera stream.

- **Object Highlighting:** Detected objects are highlighted in the video feed for easy identification.

- **Image Saving:** Images with detected objects are saved to a specified directory.

- **Configurable:** You can configure various parameters such as confidence thresholds and maximum detections.

## Prerequisites

Before running the CCTV Monitoring System, ensure you have the following prerequisites:

- Python 3.x installed on your system.

- Required Python packages, which can be installed using `pip`:

  ```bash
  pip install ultralyticsplus opencv-python-headless pillow
  ```

## Usage

1. **Clone the Repository:**

   Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/your-cctv-project.git
   ```

2. **Directory Structure:**

   Ensure your project directory has the following structure:

   ```
   your-cctv-project/
   ├── CCTVSystem.py
   ├── model_loader.py
   ├── inference.py
   ├── video_capture.py
   ├── utils/
   │   ├── best.pt
   │   └── demo.mp4
   ├── Output/
   └── README.md
   ```

   - `CCTVSystem.py`: The main script that runs the CCTV monitoring system.

   - `model_loader.py`: Loads and configures the YOLO object detection model.

   - `inference.py`: Handles object detection and result rendering.

   - `video_capture.py`: Manages video capture from multiple camera streams.

   - `utils/`: Directory containing the YOLO model file (`best.pt`) and a sample video (`demo.mp4`).

   - `Output/`: Directory where images with detected objects will be saved.

3. **Configuration:**

   Edit `CCTVSystem.py` to configure the following:

   - `model_path`: Set the path to your YOLO model file (e.g., `'utils/best.pt'`).

   - `camera_streams`: Specify the camera stream URLs or video file paths to monitor. Replace `'http://camera_stream_url'` with your camera stream URLs.

   - `save_image_directory`: Set the directory where images with detected objects will be saved (e.g., `'Output'`).

4. **Run the System:**

   To start the CCTV monitoring system, run the following command:

   ```bash
   python CCTVSystem.py
   ```

   The system will begin processing the camera streams, detecting objects, and saving images as required.

5. **Stopping the System:**

   To stop the system gracefully, press `Ctrl + C` in the terminal.

6. **Output Images:**

   The images with detected objects will be saved in the `Output/` directory.

## Customization

You can customize the system further by modifying the `ModelLoader` and `Inference` classes in the respective Python files (`model_loader.py` and `inference.py`) to adjust detection parameters and object filtering logic.

## License

This CCTV Monitoring System is provided under the [MIT License](LICENSE).

## Acknowledgments

- This project uses the YOLO object detection model from UltralyticsPlus (https://github.com/Ultralytics/ultralyticsplus).

- Portions of this code are based on OpenCV and Pillow libraries.

Feel free to reach out with any questions or issues. Happy monitoring!

---

This README provides an overview of your CCTV Monitoring System, installation instructions, usage guidelines, and customization options. You can further enhance this README with detailed instructions for specific configuration options or additional features as needed.