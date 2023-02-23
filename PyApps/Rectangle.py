#making the rectangle class

class Rectangle:
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
#functions to get the data-members       
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
#setting the data-members in the methods    
    def setX(self,value):
        if value > 0:
            self.x = value
            return True
        else:
            return False
    
    def setY(self,value):
        if value > 0:
            self.y = value
            return True
        else:
            return False

    
    def setWidth(self,value):
        if value > 0:
            self.width = value
            return True
        else:
            return False
    
    def setHeight(self,value):
        if value > 0:
            self.height = value
            return True
        else:
            return False
        
        
#Getting the area method and perimetr methods
        
    def getArea(self):
        area = self.width * self.height
        return area
    
    def getPerimeter(self):
        p = self.height * 2 + self.width * 2
        return p
        
