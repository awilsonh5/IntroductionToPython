"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Andrew Wilson.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

blue = rg.SimpleTurtle('turtle')
blue.paint_bucket = rg.PaintBucket('blue')
blue.speed = 40
black = rg.SimpleTurtle('turtle')
black.paint_bucket = rg.PaintBucket('black')
black.speed = 40

blue.forward(200)
blue.left(90)
blue.forward(200)
blue.left(90)

black.forward(200)
black.left(90)
black.forward(200)
black.left(90)
black.forward(10)

for k in range(10):
    blue.begin_fill()
    black.begin_fill()
    blue.draw_square(10)
    blue.end_fill()
    black.draw_square(10)
    black.end_fill()
    blue.forward(20)
    black.forward(20)

black.backward(10)
blue.left(90)
black.left(90)

blue.forward(10)

for k in range(10):
    blue.begin_fill()
    black.begin_fill()
    blue.draw_square(10)
    blue.end_fill()
    black.draw_square(10)
    black.end_fill()
    blue.forward(20)
    black.forward(20)

blue.backward(10)
blue.left(90)
black.left(90)
black.forward(10)

for k in range(10):
    blue.begin_fill()
    black.begin_fill()
    blue.draw_square(10)
    blue.end_fill()
    black.draw_square(10)
    black.end_fill()
    blue.forward(20)
    black.forward(20)

black.backward(10)
blue.left(90)
black.left(90)
blue.forward(10)

for k in range(10):
    blue.begin_fill()
    black.begin_fill()
    blue.draw_square(10)
    blue.end_fill()
    black.draw_square(10)
    black.end_fill()
    blue.forward(20)
    black.forward(20)
window.close_on_mouse_click()
