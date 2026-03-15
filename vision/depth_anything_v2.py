import cv2
import torch
import sys

sys.path.append("./Depth-Anything")

from depth_anything.dpt import DepthAnything


class DepthAnythingV2:

    def __init__(self):

        self.model = DepthAnything.from_pretrained(
            "LiheYoung/depth_anything_vits14"
        ).eval()

    def estimate_depth(self, image_path):
        image = cv2.imread(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        image = cv2.resize(image, (518, 518))

        image = image.astype("float32") / 255.0
        image = torch.from_numpy(image).permute(2, 0, 1).unsqueeze(0)

        with torch.no_grad():
            depth = self.model(image)

        depth = depth.squeeze().cpu().numpy()
        depth = depth / depth.max()

        return depth