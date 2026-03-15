# Vision-Based Drone Navigation

This project explores vision-based environment perception for drone navigation.

Pipeline:

Image → Depth Estimation → Environment Mapping → Navigation

## Installation

```bash
git clone https://github.com/Udyan31/Vision-Based-Drone-Navigatioon.git
cd Vision-Based-Drone-Navigatioon

python -m venv drone_env
drone_env\Scripts\activate

pip install -r requirements.txt
git clone https://github.com/LiheYoung/Depth-Anything.git

python main.py
