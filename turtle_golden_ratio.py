import turtle as t
import numpy as np

GOLDEN_RATIO = 0.5 * (1 + np.sqrt(5))
ITERS_IN_CIRCLE = 10
LEFT = 360/ITERS_IN_CIRCLE
TIMES = 125
FORWARD_INIT = 1

t1 = t.Turtle()
t1.pensize(width=2)
t1.color('purple')

forward = FORWARD_INIT
for _ in range(TIMES):
    t1.forward(forward)
    t1.left(LEFT)
    forward *= GOLDEN_RATIO**(1/ITERS_IN_CIRCLE)

t.done()
