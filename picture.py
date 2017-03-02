import png
from enum import Enum

class Picture(object):

    def __init__(self, width, height,r=0,g=0,b=0):
        self.width = width;
        self.height = height;
        self.pixels = [[Pixel(r,g,b) for y in range(height)] for x in range(width)]

    def get_pixel(self, x, y):
        return self.pixels[x][y]

    def to_PNG(self, name):
        p = [[0 for x in range(self.width*3)] for x in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                pixel = self.pixels[x][y]
                p[y][x*3+0] = pixel.r
                p[y][x*3+1] = pixel.g
                p[y][x*3+2] = pixel.b
        f = open(name, 'wb')
        w = png.Writer(self.width, self.height)
        w.write(f, p)
        f.close()

class Pixel(object):

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def grey_scale(self, value):
        self.r = value
        self.g = value
        self.b = value

    def set_colour(self, colour):
        self.r = colour[0]
        self.g = colour[1]
        self.b = colour[2]

class Colour(object):
    RED     = (255,0,0)
    GREEN   = (0,255,0)
    RED     = (0,0,255)
    BLACK   = (0,0,0)
    WHITE   = (255,255,255)
