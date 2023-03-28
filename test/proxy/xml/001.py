#!/usr/bin/env python3

from cc_pathlib import Path

import oaktree

from oaktree.proxy.xml import XmlProxy

g_svg = oaktree.Leaf("svg", nam={'xmlns':"http://www.w3.org/2000/svg", 'width':"100mm", 'height':"100mm", 'viewBox':"0 0 100 100", 'version':"1.1"})
g_rect = g_svg.grow('rect', nam={'width':40, 'height':30, 'x':20, 'y':50})

print(XmlProxy().save(g_svg))
XmlProxy().save(g_svg, Path("001.svg"))