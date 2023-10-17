import cv2

class VideoCapture:
    def __init__(self, camera_streams):
        self.camera_streams = camera_streams
        self.cameras = [cv2.VideoCapture(stream) for stream in self.camera_streams]

    def get_frames(self):
        frames = []
        for cam in self.cameras:
            ret, frame = cam.read()
            if ret:
                frames.append(frame)
        return frames

    def cleanup(self):
        for cam in self.cameras:
            cam.release()
        cv2.destroyAllWindows()
