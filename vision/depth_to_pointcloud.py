import open3d as o3d
import numpy as np
import cv2


def depth_to_pointcloud(depth_map, image_path):

    # Load original image
    color = cv2.imread(image_path)
    color = cv2.cvtColor(color, cv2.COLOR_BGR2RGB)

    h, w = depth_map.shape

    points = []
    colors = []

    # Scale factor for visualization
    depth_scale = 0.01

    for y in range(h):
        for x in range(w):

            z = depth_map[y, x] * depth_scale

            X = (x - w / 2) * z / w
            Y = (y - h / 2) * z / h

            points.append([X, Y, z])

            colors.append(color[y, x] / 255.0)

    points = np.array(points)
    colors = np.array(colors)

    # Create Open3D point cloud
    pc = o3d.geometry.PointCloud()

    pc.points = o3d.utility.Vector3dVector(points)
    pc.colors = o3d.utility.Vector3dVector(colors)

    # Visualize
    o3d.visualization.draw_geometries([pc])