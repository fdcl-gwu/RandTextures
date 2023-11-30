import os
import time
import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from randimage import get_random_image
from configparser import ConfigParser, ExtendedInterpolation
from tqdm import tqdm

def genRandomShip(fig, frame, texturesFolder):
    img = get_random_image((480,640))
    
    plt.imshow(img)
    plt.axis('off')
    fig.savefig(texturesFolder+'/{}.png'.format(frame), bbox_inches='tight', pad_inches=0)
    plt.clf()


if __name__ == '__main__':
    fig = plt.figure(frameon=False)
    fig.set_size_inches(12.8,9.6)

    config = ConfigParser(interpolation=ExtendedInterpolation())
    config.read('config.ini')
    texturedir = config.get('Gen', 'texturedir')
    N = config.getint('Gen', 'N')
    listdir = os.listdir(texturedir)
    if len(listdir) == 0:
        texturesFolder = texturedir+"textures_1"
    else:
        texturesFolder = texturedir+"textures_{}".format(len(listdir)+1)
    os.mkdir(texturesFolder)

    for frame in tqdm(range(1,N+1)):
        genRandomShip(fig, frame, texturesFolder)

