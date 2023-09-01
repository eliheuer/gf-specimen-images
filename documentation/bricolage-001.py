# This script is meant to be run from the root level
# of your font's git repository. For example, from a Unix terminal:
# $ python3 documentation/drawbot/image1.py --output documentation/drawbot/image1.png

# Import moduels from external python packages: https://pypi.org/
from drawbot_skia.drawbot import *

# Import moduels from the Python Standard Library: https://docs.python.org/3/library/
import subprocess
import sys
import argparse

# Constants, these are the main "settings" for the image
WIDTH, HEIGHT, MARGIN, FRAMES = 4096, 2048, 256, 1
FONT_PATH = "fonts/Bricolage_Grotesque/BricolageGrotesque-VariableFont_opsz,wdth,wght.ttf"
AUXILIARY_FONT_PATH = None
GRID_VIEW = False

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Draws a grid
def grid():
    stroke(1, 0, 0, 0.75)
    strokeWidth(2)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 2, MARGIN / 2
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(29):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(29):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))


# Draws a grid
def graphicGrid():
    fill(None)
    stroke(0.99)
    strokeWidth(4)
    STEP_X, STEP_Y = 0, 0
    INCREMENT_X, INCREMENT_Y = MARGIN / 2, MARGIN / 2
    rect(MARGIN, MARGIN, WIDTH - (MARGIN * 2), HEIGHT - (MARGIN * 2))
    for x in range(29):
        polygon((MARGIN + STEP_X, MARGIN), (MARGIN + STEP_X, HEIGHT - MARGIN))
        STEP_X += INCREMENT_X
    for y in range(13):
        polygon((MARGIN, MARGIN + STEP_Y), (WIDTH - MARGIN, MARGIN + STEP_Y))
        STEP_Y += INCREMENT_Y
    #polygon((WIDTH / 2, 0), (WIDTH / 2, HEIGHT))
    #polygon((0, HEIGHT / 2), (WIDTH, HEIGHT / 2))

# Remap input range to VF axis range
# This is useful for animation
# (E.g. sinewave(-1,1) to wght(100,900))
def remap(value, inputMin, inputMax, outputMin, outputMax):
    inputSpan = inputMax - inputMin  # FIND INPUT RANGE SPAN
    outputSpan = outputMax - outputMin  # FIND OUTPUT RANGE SPAN
    valueScaled = float(value - inputMin) / float(inputSpan)
    return outputMin + (valueScaled * outputSpan)

# Draw the page/frame and a grid if "GRID_VIEW" is set to "True"
def draw_background():
    newPage(WIDTH, HEIGHT)
    fill(0.11)
    # fill(1,0,0)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass

# Draw main text
#GRID_VIEW = True
def draw_main_text():
    fill(0.95)
    stroke(None)
    font(FONT_PATH)
    for axis, data in listFontVariations().items():
        print((axis, data))
    fontSize(530)
    fontVariations(wght = 900)
    # Adjust this line to center main text manually.
    # TODO: This should be done automatically when drawbot-skia
    # has support for textBox() and FormattedString

    #graphicGrid()
    stroke(None)

    step = 0
    wght_step = 400
    fill(0.9,0.22,0.2)
    #fill(0.25)
    fill(0.27,0.35,0.39)
    fill(0.3)
    for i in range(9):
        fontVariations(wdth = 97)
        fontVariations(wght = wght_step)
        text("Grotesque", (MARGIN*7.4, MARGIN*(step*1.5)))
        step += 1
        wght_step += 100

    fill(0.95)
    #fill(1, 0.84, 0)
    #fill(0.0, 0.9, 0.46)
    fontVariations(wdth = 75)
    #text("Bricolage", (MARGIN*0.95, MARGIN*3.5))
    fontSize(1180)
    text("Bricolage", (MARGIN*0.90, MARGIN*2.5))


# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
    #draw_divider_lines()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    current_file_name = __file__
    print("DrawBot: Done building", current_file_name)
