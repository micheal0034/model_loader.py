import os
from model_loader import ModelLoader
from video_capture import VideoCapture
from inference import Inference


class CCTVSystem:
    def __init__(self, model_path, camera_streams, save_image_directory):
        self.model_loader = ModelLoader(model_path)
        self.video_capture = VideoCapture(camera_streams)
        self.inference = Inference(self.model_loader.model)
        self.save_image_directory = save_image_directory

    def run(self):
        try:
            while True:
                frames = self.video_capture.get_frames()
                if not frames:
                    break

                self.model_loader.configure_model()
                detection_results = self.inference.detect_objects(frames)
                self.inference.render_results(frames, detection_results, self.save_image_directory)

        except KeyboardInterrupt:
            pass

        finally:
            self.video_capture.cleanup()

if __name__ == "__main__":
    # Define the model path, camera streams, and class IDs
    model_path = 'utils/hemletYoloV8.pt'
    camera_streams = ['utils/demo - Trim.mp4']
    save_image_directory = 'Output'
    # person_class_id = 0  # Replace with the actual class ID for 'person'
    # headhat_class_id = 1  # Replace with the actual class ID for 'headhat'

    # Create the save image directory if it doesn't exist
    os.makedirs(save_image_directory, exist_ok=True)

    # Create an instance of the CCTVSystem class
    cctv_system = CCTVSystem(model_path, camera_streams, save_image_directory)

    # Run the CCTV monitoring system
    cctv_system.run()



