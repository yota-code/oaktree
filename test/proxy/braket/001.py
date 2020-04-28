#!/usr/bin/env python3

from cc_pathlib import Path

import oaktree

from oaktree.proxy.braket import BraketProxy

u1 = oaktree.Leaf("one")
u11 = u1.grow("one-one")
u12 = u1.grow("one-two")
u12.add_text("first line")
u12.add_text("second line")

BraketProxy().save(u1, Path("test.bkt"))