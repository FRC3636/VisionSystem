# Variables
horizontalFOV = 51.889
xSize = 320

# Find angle of target
class targetAngle:
    
    def __init__(self):
        pass

    def findAngle(self, xpos):
        # Check to make sure it is finding a Goal
        if(xpos == 0):
            return(0)

        # Find degree per pixel
        pixelDeg = horizontalFOV / xSize

        # Find degrees to x
        xAngle = pixelDeg * xpos

        # Subtract half of FOV to make it be negative if below 50%
        targetAngle = xAngle - (horizontalFOV / 2)
                
        # Round to nearest tenth
        targetAngle = int(targetAngle * 10) / 10
        

        # Return targetAngle
        return(targetAngle)
    
    def findPercentage(self, xpos):
        
        # Find percent
        xPercent = int(xpos / xsize) * 100
        
        # Return x percent
        return(xPercent)
