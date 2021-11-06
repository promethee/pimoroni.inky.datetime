#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
from inky.auto import auto
from datetime import date
from datetime import datetime
from pytz import timezone
import pytz
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

def show_time():
  draw.rectangle((0, 0, WIDTH, HEIGHT), fill=WHITE)
  now = datetime.now().astimezone(None)
  texts = [now.strftime("%b %d"), now.strftime("%H:%M")]
  margin = 4
  vertical_offsets = [margin / 4, HEIGHT / 2 + margin / 4]
  index = 0

  for text in texts:
    fontsize = 100
    font = ImageFont.truetype(RobotoMedium, fontsize)
    size = draw.textsize(text, font)
    target_size = [WIDTH - margin, HEIGHT / 2 - margin]
    while size[0] > WIDTH or size[1] > target_size[1]:
      fontsize = fontsize - 2
      font = ImageFont.truetype(RobotoMedium, fontsize)
      size = draw.textsize(text, font)
    print("using fontsize:", fontsize)
    horizontal_offset = (WIDTH / 2) - (size[0] / 2) - (margin / 2)
    draw.text((horizontal_offset, vertical_offsets[index]), text, BLACK, font)
    index += 1
  inky_display.set_image(img)
  inky_display.show(img)

draw_credits("¯\_(ツ)_/¯", HEIGHT*0.05)
draw_credits("promethee", HEIGHT*0.35)
draw_credits("@github", HEIGHT*0.65)
inky_display.set_image(img)
inky_display.show(img)
time.sleep(3)

while True:
  show_time()
  time.sleep(60)
