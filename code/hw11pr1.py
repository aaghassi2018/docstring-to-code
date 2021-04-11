GlowScript 2.7 VPython
#
# physics_starter.py
#
# Building an interaction with 3D graphics using python
#   Documentation: http://www.glowscript.org/docs/GlowScriptDocs/index.html
#   Examples:      http://www.glowscript.org/#/user/GlowScriptDemos/folder/Examples/
#

scene.bind('keydown', keydown_fun)     # Function for key presses
scene.bind('click', click_fun)         # Function for mouse clicks
scene.background = 0.8*vector(1, 1, 1) # Light gray (0.8 out of 1.0)
scene.width = 640                      # Make the 3D canvas larger
scene.height = 480


# +++ Start of OBJECT_CREATION section


# The ground is represented by a box (vpython's rectangular solid)
# http://www.glowscript.org/docs/GlowScriptDocs/box.html
# Note that this time we save the thing constructed by "box" in
# a variable named "ground".
ground = box(size = vector(20, 1, 20), pos = vector(0, -1, 0), color = .4*vector(1, 1, 1))

# Show our x and z axes (for labeling and intuition-building)
# http://www.glowscript.org/docs/GlowScriptDocs/label.html
x_axis = arrow(axis = vector(5, 0, 0), color = vector(0, 0, .5))  # dark blue
x_axis_label = label(pos = vec(6, 0, 0), text = 'x', color = vector(0, 0, .5))
# x_axis_text = text(pos = vec(7, 0, 0), text = 'x', color = vector(0, 0, .5))
z_axis = arrow(axis = vector(0, 0, 5), color = vector(0, .5, 0))  # dark green
z_axis_label = label(pos = vec(0, 0, 6), text = 'z', color = vector(0, .5, 0))

# Make a sphere, which is something we will animate.
# http://www.glowscript.org/docs/GlowScriptDocs/sphere.html
# Again, we save the sphere as "ball" so that we can manipulate it later.
ball = sphere(size = 1.0*vector(1, 1, 1), color = vector(0.8, 0.5, 0.0))   # ball is an object of class sphere
ball.vel = vector(4.2, 0, 0)           # This is the initial velocity
print("velocity is now:", ball.vel)    # Printing works as usual


# +++ End of OBJECT_CREATION section


# +++ Start of ANIMATION section

# Other constants
RATE = 30                # The number of times the while loop runs each second
dt = 1.0/RATE            # The time step each time through the while loop
scene.autoscale = False  # Avoids changing the view automatically
scene.forward = vector(0, -3, -2)  # Ask for a bird's-eye view of the scene...
origin = vector(0, 0, 0) # It's nice to have a name for the origin location

# This is the "event loop" or "animation loop"
# Each pass through the loop will animate one step in time, dt
#
while True:

    rate(RATE)   # Maximum number of times per second the while loop runs

    # +++ Start of PHYSICS UPDATES -- update all positions here, every time step


    ball.pos = ball.pos + ball.vel*dt      # distance = rate*time


    # +++ End of PHYSICS UPDATES -- be sure new objects are updated appropriately!


    # +++ Start of COLLISIONS -- check for collisions & do the "right" thing


    # If the ball ventures too far, restart it with a random velocity
    if mag(ball.pos - origin) > 10.0:      # mag == magnitude of a vector
        ball.pos = vector(0, 0, 0)         # Reset the ball.pos (position)
        ball.vel = 4.2*vector.random()     # Set a random velocity
        ball.vel.y = 0.0                   # With no y component (no vertical)
        print("velocity is now:", ball.vel)


    # +++ End of COLLISIONS



# +++ Start of EVENT_HANDLING section -- separate functions for
#                                keypresses and mouse clicks...

def keydown_fun(event):
    """This function is called each time a key is pressed."""
    key = event.key
    print("key pressed:", key)    # Print which key was pressed...

    if key in 'cC':               # Redo the sphere's color...
        ball.color = randcolor()  # Shows how to call your own function...

    elif key in 'rR':             # Redo the sphere's velocity...
        ball.pos = vector(0, 0, 0)         # Reset the ball.pos (position)
        ball.vel = 4.2*vector.random()     # Set a random velocity
        ball.vel.y = 0.0                   # With no y component (no vertical)
        print("velocity is now:", ball.vel)


def click_fun(event):
    """This function is called each time the mouse is clicked."""
    print("event is", event.event, event.which)

# +++ End of EVENT_HANDLING section



# +++ Other functions can go here...

def randcolor():
    """Returns a vector of (r, g, b), randomly selected from 0.0 to 1.0."""
    r = random(0.0, 1.0)   # This is different than Python's random.uniform
    g = random(0.0, 1.0)   # But only a little bit...
    b = random(0.0, 1.0)
    return vector(r, g, b) # A color is a three-element tuple
    # See the next example for implementations of choice and randint