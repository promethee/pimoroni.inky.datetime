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
WIDTH, HEIGHT = inky_display.resolution
SMALL_DISPLAY = WIDTH == 212

COLOR = inky_display.colour
BLACK = inky_display.BLACK
WHITE = inky_display.WHITE

font_smiley = ImageFont.truetype("CODE2000.TTF", 28 if SMALL_DISPLAY else 72)
font = ImageFont.truetype(RobotoMedium, 16 if SMALL_DISPLAY else 64)

img = Image.new("P", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(img)

inky_display.set_border(inky_display.BLACK)
inky_display.h_flip = os.environ.get('FLIP_H', SMALL_DISPLAY)
inky_display.v_flip = os.environ.get('FLIP_V', SMALL_DISPLAY)

draw.rectangle((0, 0, WIDTH, HEIGHT), fill=WHITE)

def draw_credits(text, h):
  text_w, text_h = draw.textsize(text, font=font)
  x,y = 16, (h - int(text_h*0.25))
  draw.text((x, y), text, font=font_smiley, fill=BLACK)

def show_time():
  draw.rectangle((0, 0, WIDTH, HEIGHT), fill=WHITE)
  now = datetime.now().astimezone(None)
  small_texts = [now.strftime("%b %d"), now.strftime("%H:%M")]
  big_texts = [
    now.strftime("%A"),
    now.strftime("%b %d"),
    now.strftime("%H:%M"),
  ]
  texts = small_texts if SMALL_DISPLAY else big_texts
  n_texts = len(texts)
  margin = 2 if SMALL_DISPLAY else 8
  index = 0

  for text in texts:
    fontsize = 100
    font = ImageFont.truetype(RobotoMedium, fontsize)
    size = draw.textsize(text, font)
    target_size = [WIDTH - margin, int(HEIGHT/n_texts) - (margin*2)]
    while size[0] > WIDTH or size[1] > target_size[1]:
      fontsize = fontsize - 2
      font = ImageFont.truetype(RobotoMedium, fontsize)
      size = draw.textsize(text, font)
    horizontal_offset = (WIDTH/2) - (size[0]/2) - (margin/2)
    vertical_offset = (int(HEIGHT/n_texts)*index) + margin
    draw.text((horizontal_offset, vertical_offset), text, BLACK, font)
    index += 1

  inky_display.set_image(img)
  inky_display.show(img)

draw_credits("¯\_(ツ)_/¯", HEIGHT*0.05)
draw_credits("promethee", HEIGHT*0.35)
draw_credits("@github", HEIGHT*0.65)
inky_display.set_image(img)
inky_display.show(img)
time.sleep(1 if SMALL_DISPLAY else 2)

while True:
  show_time()
  time.sleep(60)
