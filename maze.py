import random
import sys
from picture import Picture, Colour

class Maze(object):
    """docstring for Maze ."""
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[Cell(x,y) for y in range(height)] for x in range(width)]



    def wall_to_east(self, cell):
        wall = Wall(cell, self.grid[cell.x+1][cell.y])
        cell.walls['east'] = wall
        self.grid[cell.x+1][cell.y].walls['west'] = wall



    def wall_to_south(self, cell):
        wall = Wall(cell, self.grid[cell.x][cell.y+1])
        cell.walls['south'] = wall
        self.grid[cell.x][cell.y+1].walls['north'] = wall

    def generate(self):
        for y in range(self.height-1):
            for x in range(self.width-1):
                cell = self.grid[x][y]
                self.wall_to_east(cell)
                self.wall_to_south(cell)

        for y in range(self.height-1):
            cell = self.grid[self.width-1][y]
            self.wall_to_south(cell)

        for x in range(self.width-1):
            cell = self.grid[x][self.height - 1]
            self.wall_to_east(cell)

        start = self.grid[0][0]
        start.visited = True
        wall_list = []
        for wall in start.walls.values():
            if(wall is not None):
                wall_list.append(wall)

        while wall_list:
            wall = random.choice(wall_list)
            cell1 = wall.cell1
            cell2 = wall.cell2

            if cell1.visited ^ cell2.visited: #if only one is visited/not visisted
                unvisited_cell = cell2 if cell1.visited else cell1
                wall.passage = True
                unvisited_cell.visited = True

                for adjacent_wall in unvisited_cell.walls.values():
                    if adjacent_wall and not adjacent_wall.passage:
                        wall_list.append(adjacent_wall)
            wall_list.remove(wall)

    def to_picture(self):
        pic = Picture(self.width*4+1, self.height*4+1)
        for j in range(self.height):
            for i in range(self.width):

                for y in range(1+j*4,4+j*4):
                    for x in range(1+i*4,4+i*4):
                        pic.pixels[x][y].grey_scale(255)

                n = self.grid[i][j].walls['north']
                s = self.grid[i][j].walls['south']
                e = self.grid[i][j].walls['east']
                w = self.grid[i][j].walls['west']
                if(n and n.passage):
                    pic.pixels[i*4+2][j*4+2-2].set_colour(Colour.WHITE)
                if(s and s.passage):
                    pic.pixels[i*4+2][j*4+2+2].set_colour(Colour.WHITE)
                if(e and e.passage):
                    pic.pixels[i*4+2+2][j*4+2].set_colour(Colour.WHITE)
                if(w and w.passage):
                    pic.pixels[i*4+2-2][j*4+2].set_colour(Colour.WHITE)



        return pic

class Cell(object):
    """docstring for Cell."""

    def __init__(self, x, y, walls=None):
        self.visited = False
        self.x = x
        self.y = y
        self.walls = {
            'north' : None,
            'south' : None,
            'east'  : None,
            'west'  : None
        }



class Wall(object):

    id = 0

    def __init__(self, cell1=None, cell2=None, passage=False):
        self.cell1 = cell1
        self.cell2 = cell2
        self.passage = passage
        self.id = Wall.id
        Wall.id+=1


def main():
    maze = Maze(int(sys.argv[1]),int(sys.argv[2]))
    maze.generate()
    pic = maze.to_picture()
    pic.to_PNG(sys.argv[3])

if __name__ == '__main__':
    main()
