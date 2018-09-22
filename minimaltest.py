#!/usr/bin/env python

import math
import random
import cairo

w,h = 350,350

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32,w,h)
ctx = cairo.Context(surface)

def test_pattern():
    #ctx.translate(0,0)
    for x in range(0,100):
        for y in range(0,100):
            x += math.cos(y) - math.sin(y)
            y += math.cos(y) - math.sin(x)
            ctx.set_source_rgb(random.random(),0.35,0.35)
            ctx.rectangle(x+10,y+10,100,100)
            ctx.fill()

test_pattern()
surface.write_to_png("test_pattern.png")
