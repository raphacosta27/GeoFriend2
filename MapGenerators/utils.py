import math
def collision(cx, cy, radius, rx, ry, rw, rh):  # circle definition
    """ Detect collision between a rectangle and circle. 
    cx, cy: circle position
    radius: circle radius
    rx, ry: rectangle position
    rw, rh: rectangle width and height
    """ 

    testX = cx
    testY = cy

    xEdge = None
    #If the circle is to the RIGHT of the square, check against the RIGHT edge. LEFT otherwise.   
    if (cx < rx):
        testX = rx        #left edge
        xEdge = "right"
    elif (cx > rx+rw): 
        testX = rx+rw     #right edge
        xEdge = "left"

    yEdge = None
    #If the circle is ABOVE the square, check against the TOP edge. BOTTOM otherwise
    if (cy < ry):
        testY = ry        #top edge
        yEdge = "bottom"
    elif (cy > ry+rh):
        testY = ry+rh     #bottom edge
        yEdge = "top"

    distX = cx-testX
    distY = cy-testY
    distance = math.sqrt( (distX*distX) + (distY*distY) )

    if (distance <= radius):
        return True, xEdge, yEdge
        
    return False, None, None

# source: http://www.jeffreythompson.org/collision-detection/circle-rect.php