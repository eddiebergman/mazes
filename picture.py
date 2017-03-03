import png
from enum import Enum

class Picture(object):

    def __init__(self, width, height):
        self.width = width;
        self.height = height;
        self.pixels = [0] * (width*height*3)

    def colour_pixel(self, x, y, colour):
        index = (y*self.width + x)*3
        self.pixels[index] = colour[0]
        self.pixels[index+1] = colour[1]
        self.pixels[index+2] = colour[2]

    def to_PNG(self, name):
        f = open(name, 'wb')
        w = png.Writer(self.width, self.height)
        w.write_array(f, self.pixels)
        f.close()

class Psuedo_Pixel(object):

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
    BLUE    = (0,0,255)
    BLACK   = (0,0,0)
    WHITE   = (255,255,255)

def main():
    pic = Picture(100,100)
    for y in range(100):
        for x in range(100):
            pic.colour_pixel(x,y,Colour.RED)
    pic.to_PNG("out.png")

if __name__ == '__main__':
    main()
