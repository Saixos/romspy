from .levels import sigma_stretch_sc, sigma_stretch_cs, get_z_levels
from .interpolate import vert_interpolate
from numpy.ctypeslib import ndpointer
import ctypes

"""
Author: Nicolas Munnich
License: GNU GPL2+
"""

# Setup C function calling
lib = ctypes.cdll.LoadLibrary('./linear.so')

gen_vert_bil = lib.interp_weights
gen_vert_bil.restype = None
gen_vert_bil.argtypes = [
    ndpointer(ctypes.c_float),  # Current h array
    ctypes.c_ulonglong,  # h array length
    ndpointer(ctypes.c_float),  # 3D array describing heights at each point, dims z, y, x
    # 3D array has dimensions z, y, x
    ctypes.c_ulonglong,  # len(y) * len(x)
    ctypes.c_ulonglong,  # len(z)
    ndpointer(ctypes.c_float),  # 4D array containing weights of shape z, y, x, w
]
interp_bil = lib.interp_with_weights
interp_bil.restype = None
interp_bil.argtypes = [
    ndpointer(ctypes.c_float),  # 4D weight array z, y, x, w
    ndpointer(ctypes.c_float),  # 3D original array h, y, x
    ndpointer(ctypes.c_float),  # 3D target array z, y, x
    ctypes.c_ulonglong,  # len(z) * len(y) * len(x)
]
bil_weight_extra_len = 3
