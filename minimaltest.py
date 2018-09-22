#!/usr/bin/env python

import math
import cairo

w,h = 350,350

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,w,h)
ctx = cairo.Context(surface)

ctx.scale(w,h)

def test_pattern():
    for i in range(0,12):
         for j in range(0,12):
            i += Math.cos(j) + 10
            j += Math.sin(i) + 10
            ctx.set_source_rgb(0.6,0.3,0.2)
            ctx.move_to(i,j)
            ctx.rectangle(i,j,10,10)
            ctx.fill()

test_pattern()
surface.write_to_png("test_pattern.png")
