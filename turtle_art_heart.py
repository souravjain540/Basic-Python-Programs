# heart shape in turtle 
import turtle  # import turtle 
turtle.pensize(3) # setting pen size 
turtle.speed(10) # speed ranging from 1-10 
turtle.color('red') # color to be filled in final image 
turtle.pencolor('black') # pen color for border
turtle.begin_fill() # start filling the image 
turtle.left(50) # moving turtle to 50deg left 
turtle.forward(100) # going 100 step forward 
turtle.circle(50,210) # making a arc for 210step 
turtle.right(150) # turning pointer 150deg right 
turtle.circle(50,210) # second arc 
turtle.forward(120) # move forward 120 step 
turtle.end_fill() # end fill 
turtle.done() # necessary to keep turtle windwo open even after it is donw with making full art 