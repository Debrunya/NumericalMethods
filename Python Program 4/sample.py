# -*- coding: utf-8 -*-
"""
@author: znahar
"""


import matplotlib.pyplot as plt
import numpy as np
import nstetc as ns


def calculation(data):
    n = int(data['n'])
    m = int(data['m'])
    T = float(data['T'])
    
    vector = np.array(ns.NonStatETC(n, m, 0.0, 1.0, 0.0, T))
    zgrid = vector.transpose()
    
    xs = np.linspace(0, 1, n+1)
    ys = np.linspace(0, T, m+1)
    xgrid, ygrid = np.meshgrid(xs, ys)
    
    h = 1.0/n
    tau = T/m
    
    calcdata = {'xgrid': xgrid,
                'ygrid': ygrid,
                'zgrid': zgrid,
                'n': n,
                'm': m,
                'h': h,
                'tau': tau}
    
    return calcdata

    
def check_grid(data):
    n = int(data['n'])
    m = int(data['m'])
    T = float(data['T'])
    
    h = 1.0/n
    tau = T/m
    
    if (tau>h**2/6):
        error = 'Не удовлетворяется условие сходимости!!!'
        
        norm_tau =  h**2/6
        norm_m = int(T//norm_tau)+100
        
        message = {'norm_m': norm_m,
                   'error': error}
        
    else:
        message = {'norm_m': '-1',
                   'error': '-1'}
    
    return message


def plot_figure(data):    
    fig = plt.figure(figsize = (10, 10))
    fig.suptitle('Искомая поверхность u(x, t)', fontsize=14)
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_xlabel('X', labelpad = 7.0, fontsize = 14)
    ax.set_ylabel('time', labelpad = 8.0, fontsize = 14)
    ax.set_zlabel('Тemp', labelpad = 9.0, fontsize = 14)
    
    ax.plot_surface(data['xgrid'], data['ygrid'], data['zgrid'], rcount = 200, ccount = 100, cmap = 'plasma')
    ax.view_init(45, -135)

    plt.show()
    

def plot_layer(data):    
    fig = plt.figure(figsize = (10, 10))
    T = data["l"]*data["tau"]
    fig.suptitle(f'Искомый слой u(x, {T:.4f})', fontsize=14)
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('X', labelpad = 7.0, fontsize = 14)
    ax.set_ylabel('Тemp', labelpad = 9.0, fontsize = 14)
    ax.set_xlim(-0.02, 1.02)
    ax.set_ylim(-1.02, 1.02)
    
    xs = data['xgrid'][0]
    ys = data['zgrid']
    ax.plot(xs, ys[data["l"]], color = 'green', lw = 3.0)

    plt.show()


