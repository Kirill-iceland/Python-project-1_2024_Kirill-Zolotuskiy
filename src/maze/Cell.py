class Cell:
    left_wall: bool = False
    right_wall: bool = False
    top_wall: bool = False
    bottom_wall: bool = False

    def __init__(self, walls: int): # 1000 = left, 0100 = top, 0010 = right, 00001 = bottom, 
        self.left_wall   = (walls & 0b1000 != 0)
        self.top_wall    = (walls & 0b100  != 0)
        self.right_wall  = (walls & 0b10   != 0)
        self.bottom_wall = (walls & 0b1    != 0)
