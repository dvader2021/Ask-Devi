# color functionality 

# uses webcolor module for color names

import colorsys
import numpy as np
import webcolors

# convert list to tuple
def convert(list):
    return tuple(list)


def rgb2hex(val):
    """
    Takes tuple and converts to hex value.
    """
    conversion = '#%02x%02x%02x' % val
    return conversion


def hex2rgb(val):
    """
    Takes hex string and converts to rgb tuple.
    """
    hexNum = val.strip('#')
    hexLen = len(hexNum)
    conversion = tuple(int(hexNum[i:i+hexLen//3], 16) for i in range(0, hexLen, hexLen//3))
    return conversion

def complimentary(hexval):
    """
    Takes hex value converts to rgb tuple and produces complimentary color.
    """
    val = hex2rgb(hexval)
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 150 and 210 degrees
    deg_180_hue = h + (180.0 / 360.0)
    color_180_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    return color_180_rgb

# split complementary color
# A split-complementary color scheme is a three-color combination that consists of a base color and two colors that are 150  degrees and 210 degrees apart from the base color respectively

def splitComplimentary(hexval):
    """
    Takes hex value converts to rgb tuple and produces list of split complimentary colors.
    """
    val = hex2rgb(hexval)
    #value has to be 0 x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 150 and 210 degrees
    deg_150_hue = h + (150.0 / 360.0)
    deg_210_hue = h + (210.0 / 360.0)
    #convert to rgb
    color_150_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_150_hue, l, s)))
    color_210_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_210_hue, l, s)))
    return [color_150_rgb, color_210_rgb]


# Analogous Color
# Analogous color schemes are created by pairing one main color with the two colors directly next to it on the color wheel. We can specify the angle between the main color and the other two colors

def analogous(hexval, d):
    """
    Takes hex value and angle (out of 100) converts to rgb tuple and produces list of analogous colors)
    """
    val = hex2rgb(hexval)
    analogous_list = []
    #set color wheel angle
    d = d /360.0
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #rotate hue by d
    h = [(h+d) % 1 for d in (-d, d)]
    for nh in h:
        new_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(nh, l, s)))
        analogous_list.append(new_rgb)
    return analogous_list

# Triadic Color
# Triadic colors are a combination of three colors that consists of a main color and two colors that are 120 degrees and 240 degrees apart from the main color respectively
def triadic(hexval):
    """
    Takes hex value converts to rgb tuple and produces list of triadic colors.
    """
    val = hex2rgb(hexval)
    #value has to be 0 < x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_120_hue = h + (120.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_120_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_120_hue, l, s)))
    color_240_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_120_rgb, color_240_rgb]

# Tetradic Color
# Tetradic colors are four-color combination that consists of a main color and three colors that are 90 degrees, 180 degrees, and 270 degrees apart from the main color respectively
def tetradic(hexval):
    """
    Takes hex value converts to rgb tuple and produces list of tetradic colors.
    """
    val = hex2rgb(hexval)
    #value has to be 0 <span id="mce_SELREST_start" style="overflow:hidden;line-height:0;"></span>&lt; x 1 in order to convert to hls
    r, g, b = map(lambda x: x/255.0, val)
    #hls provides color in radial scale
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    #get hue changes at 120 and 240 degrees
    deg_60_hue = h + (60.0 / 360.0)
    deg_180_hue = h + (180.0 / 360.0)
    deg_240_hue = h + (240.0 / 360.0)
    #convert to rgb
    color_60_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_60_hue, l, s)))
    color_180_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_180_hue, l, s)))
    color_240_rgb = list(map(lambda x: round(x * 255),colorsys.hls_to_rgb(deg_240_hue, l, s)))
    return [color_60_rgb, color_180_rgb, color_240_rgb]

def getColorName(hexVal):
    color_name=''
   
    try:
        color_name= webcolors.hex_to_name(hexVal)
    except:
        color_name = "white"
    
    return color_name

def getHexCode(colorName):
    hex_val=''
   
    try:
        hex_val= webcolors.name_to_hex(colorName)
    except:
        hex_val = "#d71868"
    
    return hex_val

    