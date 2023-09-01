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
FONT_PATH = "fonts/Rubik/Rubik-VariableFont_wght.ttf"
AUXILIARY_FONT_PATH = None
GRID_VIEW = False

# Handel the "--output" flag
# For example: $ python3 documentation/image1.py --output documentation/image1.png
parser = argparse.ArgumentParser()
parser.add_argument("--output", metavar="PNG", help="where to write the PNG file")
args = parser.parse_args()

# Draws a grid
def grid():
    stroke(1, 0, 0, 1)
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
    fill(0.025)
    fill(0.12)
    rect(-2, -2, WIDTH + 2, HEIGHT + 2)
    if GRID_VIEW:
        grid()
    else:
        pass

# Draw main text
#GRID_VIEW = True
def draw_main_text():
    fill(0.99)
    fill(0.96)
    stroke(None)
    font(FONT_PATH)
    # for axis, data in listFontVariations().items():
    #     print((axis, data))
    fontSize(512)
    fontVariations(wght = 900)
    # Adjust this line to center main text manually.
    # TODO: This should be done automatically when drawbot-skia
    # has support for textBox() and FormattedString

    text("Rubik", ((MARGIN-4)+MARGIN*1.4, MARGIN*2.25))
    text("بالعربي", ((MARGIN*13.58), MARGIN*4.3))
    fontSize(110)
    #fontVariations(wght = 500)
    #text("“IN ARABIC”", ((MARGIN*10.32), MARGIN*3.85))
    fontVariations(wght = 800)
    text("“IN ARABIC”", ((MARGIN*10.23), MARGIN*3.85))

# Divider lines
def draw_divider_lines():
    stroke(1)
    strokeWidth(4)
    lineCap("round")
    line((MARGIN+64, HEIGHT - MARGIN*1.5), (WIDTH - MARGIN-64, HEIGHT - MARGIN*1.5))
    line((MARGIN+64, MARGIN + (MARGIN / 2)), (WIDTH - MARGIN-64, MARGIN + (MARGIN / 2)))
    stroke(None)

# Build and save the image
if __name__ == "__main__":
    draw_background()
    draw_main_text()
    #draw_divider_lines()
    # Save output, using the "--output" flag location
    saveImage(args.output)
    current_file_name = __file__
    print("DrawBot: Done building", current_file_name)
