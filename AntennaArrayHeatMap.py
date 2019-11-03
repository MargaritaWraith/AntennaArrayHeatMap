# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
try:
	os.chdir(os.path.join(os.getcwd(), '..\\..\..\AppData\Local\Temp'))
	print(os.getcwd())
except:
	pass
# %% [markdown]
# # Распределение поля в апертуре антенной решётки
# 
# Определим библиотеки с кодом из которых мы будем работать

# %%
import numpy as np
from math import *
import matplotlib.pyplot as plt

to_rad = pi/180
to_deg = 180/pi

# %% [markdown]
# ## Параметры решётки

# %%
# Параметры
f0 = 3 #ГГц
lmd = 30.0/f0 #см
k = 2*pi/lmd

Nx = 50
Ny = 50
dx = 0.8*lmd/2
dy = 0.6*lmd/2

# Пьедесталы
deltaX = 0.3
deltaY = 0.8

# Апертура
Lx = (Nx-1) * dx
Ly = (Ny-1) * dy

# print(pi%3)

# %% [markdown]
# ## Функции амплитудно-фазового распределения

# %%
def A(_x, _L, _DeltaX):
    return _DeltaX+(1-_DeltaX)*((cos(pi*_x/_L))**2)

def A_xy(_x,_y):
    return A(_x, Lx, deltaX)*A(_y, Ly, deltaY)

def Psi(_x,_y,_z,_th,_phi):
    return (k*((_x*cos(_phi) + _y*sin(_phi))*sin(_th) + _z*cos(_th)))%(2*pi)


# %%
th = 15*to_rad
phi = 10*to_rad
a = []
psi = []
X = np.zeros(Nx)
Y = np.zeros(Ny)
for _i in range(Nx):
    a.append([])
    psi.append([])
    x = _i*dx - Lx/2
    X[_i] = x
    for _j in range(Ny):
        y = _j*dy - Ly/2
        a[_i].append(A_xy(x,y))
        psi[_i].append(Psi(x,y,0,th,phi))

for _i in range (Ny):
    Y[_i] = _i * dy - Ly/2


# %%
# a = np.random.random((16, 16))
plt.imshow(a, cmap='hot', interpolation='nearest')
plt.show()


# %%


