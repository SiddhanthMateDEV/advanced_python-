class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

class square(rectangle):
    def __init__(self, length, width):
        super().__init__(length,width)
    
    def area(self):
        return self.length*self.width
    
class cube(rectangle):
    def __init__(self,length,width,height):
        super().__init__(length,width)
        self.height = height

    def volume(self):
        return self.length*self.width*self.height
    

        

rr = rectangle(3,3)

sq = square(3,3)

cu = cube(3,3,3)

square_area = sq.area()
cube_area = cu.volume()


print(cube_area)
print(square_area)
