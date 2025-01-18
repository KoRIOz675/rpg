from pygame import *
from json import *

# initialize Pygame
init()

# Setup interface variables
screenWidth = 720
screenHeight = 480
screenSize = (screenWidth, screenHeight)
backgroundColor = "#e0e3e8"

# Setup interface information
screen = display.set_mode(screenSize)

# Setup base game variables
clock = time.Clock()
fps = 60

# Init varaibles
run = True