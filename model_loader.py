from ultralyticsplus import YOLO

class ModelLoader:
    def __init__(self, model_directory):
        self.model = YOLO(model_directory)

    def configure_model(self):
        # Set model parameters
        self.model.overrides['conf'] = 0.25
        self.model.overrides['iou'] = 0.45
        self.model.overrides['agnostic_nms'] = False
        self.model.overrides['max_det'] = 1000
