# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 12:16:23 2016

@author: patricia
"""
from idtxl import idtxl_utils as utils

def test_swap_chars():
    s = utils.swap_chars('psr',0,1)
    assert s == 'spr', 'Chars were not swapped correctly.'


if __name__ == '__main__':
    test_swap_chars()
