from configparser import ConfigParser, ExtendedInterpolation
from shutil import copyfile
import os

config = ConfigParser(interpolation=ExtendedInterpolation())
config.read('config.ini')
texturedir = config.get('Gen', 'texturedir')
TextureMainFolder = config.get('Gen', 'MainTexturedir')

try:
    os.mkdir(TextureMainFolder)
except:
    pass

texture_folders = os.listdir(texturedir)
texture_folders.sort()
N = 0
for i, folder in enumerate(texture_folders):
    texdir = texturedir+folder+"/"
    print(i," ",texdir)
    textures = os.listdir(texdir)
    textures.sort()

    for j, texture in enumerate(textures):
        N = N+1
        os.rename(texdir+texture, TextureMainFolder+"{}.png".format(N))

