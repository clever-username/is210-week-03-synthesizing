#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Contains expectations."""


import inquisition

LEN_SPAN = len('Spanish')

INDEX_SPAN = inquisition.SPANISH.index('Spanish')

SLICE_LT = inquisition.SPANISH[0:INDEX_SPAN]

SLICE_RT = inquisition.SPANISH[INDEX_SPAN + LEN_SPAN:]

FLEMISH = SLICE_LT + 'Flemish' + SLICE_RT
