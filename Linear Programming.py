#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:04:32 2021

@author: clarapilven
"""
from scipy.optimize import linprog

chicken_price = 0.013 
beef_price = 0.008
mutton_price = 0.010

rice_price = 0.002
wheat_price = 0.005
gel_price = 0.001

contribution = [[0.1, 0.08, 0.001, 0.002], 
                [0.2, 0.1, 0.005, 0.005], 
                [0.15, 0.11, 0.003, 0.007], 
                [0.0, 0.01, 0.1, 0.008], 
                [0.04, 0.01, 0.15, 0.0], 
                [0.0, 0.0, 0.0, 0.0]]



#%%

obj = [0.013, 0.008,0.010, 0.002, 0.005, 0.001]

inequations_left_side = [[-0.1, -0.2, -0.15, -0.0, -0.4, -0.0],
                         [-0.08, -0.1, -0.11, -0.01, -0.01, -0.0], 
                        [0.0001, 0.005, 0.003, 0.1, 0.15, 0.0], 
                        [0.002, 0.005, 0.007, 0.008, 0.0, 0.0]]

inequation_right_side = [-0.08*100, -0.06*100, 0.02*100, 0.004*100]


equation_left_side = [[1, 1, 1, 1, 1, 1]]
equaltion_right_side = [100]

bound = [(0, float("inf")), 
         (0, float("inf")), 
         (0, float("inf")),
         (0, float("inf")),
         (0, float("inf")),
         (0, float("inf"))]

res = linprog(obj, 
              A_ub=inequations_left_side, b_ub=inequation_right_side,
              A_eq=equation_left_side, b_eq=equaltion_right_side, 
              bounds=bound,
              method='interior-point', callback=None, options=None, x0=None
              )
print(res)
print("")
print("prix minimum : " + str(round(res.fun, 5)))