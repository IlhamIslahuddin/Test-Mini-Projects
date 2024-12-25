import turtle
import random

# Set up the screen and the turtle
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(width=600,height=600)
point = turtle.Turtle() 
point.speed(0)

border_left = -250
border_right = 250
border_top = 250
border_bottom = -250

# Function to simulate the random walk
def crazy_draw(steps):
    for _ in range(steps):
        # Make a random turn (between 0 and 360 degrees)
        point.left(random.randint(0, 360))
        
        point.forward(50)
        current_x, current_y = point.position()

        x, y = point.position()

        # Ensure the point stays within the boundaries
        if x < border_left:
            point.setx(border_left)
        elif x > border_right:
            point.setx(border_right)

        if y < border_bottom:
            point.sety(border_bottom)
        elif y > border_top:
            point.sety(border_top)

if __name__ == "__main__":
    crazy_draw(2000) #number of lines drawn
    screen.mainloop()
