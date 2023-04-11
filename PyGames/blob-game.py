import math

KIND_PLAYER = 1
KIND_FOOD = 2
KIND_AI = 3

class Blob:

    def __init__(self, mass, x, y, world_width, world_height, kind):
        self.mMass = float(mass)  # mass
        self.mX = float(x)        # x position
        self.mY = float(y)        # y position
        self.mDx = 0.             # portion of speed that comes from x
        self.mDy = 0.             # portion of speed that comes from y
        self.mKind = kind         # kind of blob
        self.mAlive = True        # blob's life status

        # size of the world, used for bounding motion
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height
        # used to scale the speed to tune game play
        self.mSpeedMultiplier = 10.0
        # used to scale the display size of blobs
        self.mRadiusMultiplier = 5.0
        # used to make sure 1 frame's motion doesn't overshoot the destination
        self.mDestinationSpeed = 0.0
        return
    
    def getMass(self):
        return self.mMass
    def getX(self):
        return self.mX
    def getY(self):
        return self.mY
    def getAlive(self):
        return self.mAlive
    def getKind(self):
        return self.mKind
    
    def getSpeed(self):
        speed1 = self.mDestinationSpeed
        speed2 = self.mSpeedMultiplier / math.log(self.mMass)
        return min(speed1, speed2)
    
    def getRadius(self):
        return self.mRadiusMultiplier * math.sqrt(self.mMass / math.pi)
    
    def __ne__(self, other):
        if self.mX != other.mX or self.mY != other.mY:
            return True
        else:
            return False
        
    
    def __gt__(self, other):
        return self.mMass / other.mMass >= 1.25
    
    def __iadd__(self, other):
        self.mMass += other.mMass
        other.mMass = 0
        other.mAlive = False
        return self

    def __xor__(self, other):
    # Calculate the distance between the centers of the two blobs
        distance = math.sqrt((self.mX - other.mX) ** 2 + (self.mY - other.mY) ** 2)
    # Find the largest of the two radii
        largest_radius = max(self.getRadius(), other.getRadius())
    # Check if there is a collision
        if largest_radius > distance:
            return True
        else:
            return False
        
    def __ilshift__(self, position):
        # Calculate difference between desired x and y positions
        dx = position[0] - self.mX
        dy = position[1] - self.mY
        
       
        distance = math.sqrt(dx**2 + dy**2)
        self.mDestinationSpeed = distance
        
 
        if distance > 0:
            self.mDx = dx / distance
            self.mDy = dy / distance
        else:
            self.mDx = 0.0
            self.mDy = 0.0
        
        return self
    
    def __irshift__(self, distance):
        # Update mX and mY based on mDx and mDy
        self.mX += self.mDx * distance
        self.mY += self.mDy * distance
        
        # Check if mX or mY are out of bounds and adjust if necessary
        if self.mX + self.getRadius() > self.mWorldWidth:
            self.mX = self.mWorldWidth - self.getRadius()
        elif self.mX - self.getRadius() < 0:
            self.mX = self.getRadius()
            
        if self.mY + self.getRadius() > self.mWorldHeight:
            self.mY = self.mWorldHeight - self.getRadius()
        elif self.mY - self.getRadius() < 0:
            self.mY = self.getRadius()
        
        return self
