import turtle
 
# turtle object
diamond_turtle = turtle.Turtle()
 
# the coordinates of each corner
shape = ((-10, -10), (-10, 10), (10, 10), (10, -10))
 
# registering the new shape
turtle.register_shape('diamond', shape)
 
# changing the shape to 'diamond'
diamond_turtle.shape('diamond')
 
# Keep the turtle window open
turtle.done()