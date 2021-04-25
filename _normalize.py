#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata

def normalize(string):
    string = string.lower()
    string = unicodedata.normalize('NFD', string)
    string = string.encode('ascii', 'ignore')
    string = string.decode("utf-8")
    return string