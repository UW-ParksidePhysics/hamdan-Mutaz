from vpython import *

scene.background = color.black
scene.width = 600
scene.height = 600
scene.forward = vector(-.5, -.3, -1)
scene.title = "Vector figure of r_vec = -0.5x + -0.3y + -1.0z"

scene.caption = """To rotate "camera", drag with right button or Ctrl-drag.
To zoom, drag with middle button or Alt/Option depressed, or use scroll wheel.
  On a two-button mouse, middle is left + right.
To pan left/right and up/down, Shift-drag.
Touch screen: pinch/extend to zoom, swipe or two-finger rotate."""

xaxis = cylinder(color=color.magenta, pos=vector(0, 0, 0), axis=vector(10, 0, 0), radius=0.3)
xlbl = label(pos=vector(11, 0, 0), text="x", color=color.magenta, opacity=0, height=30, box=0)
yaxis = cylinder(color=color.yellow, pos=vector(0, 0, 0), axis=vector(0, 10, 0), radius=0.3)
ylbl = label(pos=vector(0, 11, 0), text="y", color=color.yellow, opacity=0, height=30, box=0)
zaxis = cylinder(color=color.cyan, pos=vector(0, 0, 0), axis=vector(0, 0, 10), radius=0.3)
xlbl = label(pos=vector(0, 0, 11), text="z", color=color.cyan, opacity=0, height=30, box=0)

r = arrow(pos=vector(0, 0, 0), axis=vector(2, 10, 7), color=color.red, shaftwidth=0.5)
rlbl = label(pos=vector(2, 10, 7), text="03/03/1999 & 01/23/2000", color=color.red, opacity=0, height=30, box=0)
© 2020 GitHub, Inc.
