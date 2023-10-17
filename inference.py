import os
import cv2
from ultralyticsplus import render_result
from PIL import Image
import numpy as np
import time
import torch
save_image = 'Output2'

class Inference:
    def __init__(self, model):
        self.model = model

    def detect_objects(self, frames):
        results = []
        for frame in frames:
            results.append(self.model.predict(frame))
        return results

    def render_results(self, frames, results, save_image_directory):
        save_image = 'Output'
        for i, result in enumerate(results):
            print(f"CCTV Result {i + 1}:")

            # Extract boxes
            boxes = result[0].boxes if result and len(result) > 0 else None
            for j, box in enumerate(boxes):
                if isinstance(box, torch.Tensor) and box.numel() == 0:
                    output_path = os.path.join(save_image)
                    cv2.imwrite(output_path, frames[i])
                    # Save the image here when a non-empty box is found
                    # unique_filename = f"{int(time.time())}_camera_{i + 1}_box_{j + 1}.jpg"
                    # output_path = os.path.join(save_image_directory, unique_filename)
                    # cv2.imwrite(output_path, frames[i])

                    cv2.imshow(f"Rendered Image {i + 1}", frames[i])
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

        # rendered_image = render_result(model=self.model, image=frames[i], result=result[0])


