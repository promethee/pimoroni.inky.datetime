#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from inky.auto import auto
from PIL import Image, ImageDraw, ImageFont, ImageColor
from fonts.ttf import RobotoMedium

inky_display = auto(ask_user=True, verbose=True)
inky_display.h_flip = os.environ.get('FLIP_H', True)
inky_display.v_flip = os.environ.get('FLIP_V', True)

WIDTH, HEIGHT = inky_display.resolution
COLOR = inky_display.colour
BLACK = inky_display.BLACK
WHITE = inky_display.WHITE

font_smiley = ImageFont.truetype("CODE2000.TTF", 28)
font = ImageFont.truetype(RobotoMedium, 16)

img = Image.new("P", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

draw.rectangle((0, 0, WIDTH, HEIGHT), fill=WHITE)

def draw_credits(text, h):
  text_w, text_h = draw.textsize(text, font=font)
  x,y = 16, (h - int(text_h * 0.25))
  draw.text((x, y), text, font=font_smiley, fill=BLACK)

draw_credits("¯\_(ツ)_/¯", HEIGHT*0.05)
draw_credits("promethee", HEIGHT*0.35)
draw_credits("@github", HEIGHT*0.65)
inky_display.set_image(img)
inky_display.show(img)

