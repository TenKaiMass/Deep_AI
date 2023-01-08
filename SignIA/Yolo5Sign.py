
import os 

from matplotlib import pyplot as plt
import numpy as np
import cv2
from PIL import Image
import torch
import gradio as gr


from typing import List

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse

import cv2
import io
import numpy as np

import torch
import cv2
from PIL import Image

import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

path = './data/images'
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp5/weights/best.pt', force_reload=True)
fig, ax = plt.subplots(2,4, figsize=(20,10))
imgs = os.listdir('./data/images')
imgname = np.random.choice(imgs)
img = cv2.imread(f'./data/images/{imgname}')
results = model(img).show

