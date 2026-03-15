import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import torch
import cv2
import numpy as np


class DepthEstimator:

    def __init__(self):

        # Load MiDaS depth model
        self.model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.model.to(self.device)
        self.model.eval()

        # Load preprocessing transforms
        transforms = torch.hub.load("intel-isl/MiDaS", "transforms")
        self.transform = transforms.small_transform


    def estimate_depth(self, image_path):

        # Read image
        img = cv2.imread(image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        input_batch = self.transform(img).to(self.device)

        with torch.no_grad():

            prediction = self.model(input_batch)

            prediction = torch.nn.functional.interpolate(
                prediction.unsqueeze(1),
                size=img.shape[:2],
                mode="bicubic",
                align_corners=False,
            ).squeeze()

        depth_map = prediction.cpu().numpy()

        return depth_map