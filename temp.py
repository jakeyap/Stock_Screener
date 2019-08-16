# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 20:22:37 2019

@author: Yong Keong
"""

import matplotlib.pyplot as plt
import numpy as np
import generate_test_data as tester


roelist = data['roe']
roelist
roe_bands = math_tools.generate_bollinger_bands(roelist,1,5)
roe_bands['bollinger_mid']