# Copyright 2013 Advanced Micro Devices, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice (including the next
# paragraph) shall be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from __future__ import print_function, division, absolute_import
import os

from genclbuiltins import gen, NEGNAN
from math import cos, exp, log, log10, pow, sin, sqrt, tan, pi

CLC_VERSION_MIN = {
    'half_cos' : 10,
    'half_divide' : 10,
    'half_exp' : 10,
    'half_exp2' : 10,
    'half_exp10' : 10,
    'half_log' : 10,
    'half_log2' : 10,
    'half_log10' : 10,
    'half_powr' : 10,
    'half_recip' : 10,
    'half_rsqrt' : 10,
    'half_sin' : 10,
    'half_sqrt' : 10,
    'half_tan' : 10,
}

DATA_TYPES = ['float']

F = {
    'float' : 'float'
}

M_PI_F = float.fromhex('0x1.921fb6p+1')

tests = {
    'half_cos' : {
        'arg_types' : [F, F],
        'function_type': 'ttt',
        'values' : [
            # using libm cosf(3.0f * M_PI / 2.0f) == 0x1.99bc5cp-27
            # which is different form what python gives us
            [1.0, cos(M_PI_F / 2),    -1.0, float.fromhex('0x1.99bc5cp-27'),        1.0,    cos(1.12345), cos(7), cos(8), cos(pow(2,20)), cos(pow(2,24)), cos(pow(2,120)), float("nan")], # Result
            [0.0, M_PI_F / 2, pi,   3 * M_PI_F / 2, 2 * pi, 1.12345, 7, 8, pow(2,20), pow(2,24), pow(2,120), float("nan")] # Arg0
        ],
        'tolerance' : 8192
    },
    'half_divide' : {
        'arg_types' : [F, F, F],
        'function_type': 'ttt',
        'values' : [
            [1.0, 1.0/4.0,  1/6.0, 1/6.25 , float("nan"), 1/16.0,  float("inf"), 1/7.0, 1/pi], # Result
            [1.0, 1.0, 1.0, 1.0, float("nan"), 1.0, 1.0, 1.0, 1.0], # Arg0
            [1.0, 4.0, 6.0, 6.25, float("nan"), 16.0, 0.0, 7.0, pi], # Arg1
        ],
        'tolerance' : 8192
    },
    'half_exp' : {
        'arg_types' : [F, F],
        'function_type': 'ttt',
        'values' : [
            [1.0, exp(0.95), exp(pi), exp(-pi), float("inf"), float.fromhex('0x1.66fe8ap+4')], # Result
            [0.0, 0.95, pi, -pi, float("inf"), float.fromhex('0x1.8e2cp+1')]  # Arg0
        ],
        'tolerance' : 8192
    },
    'half_exp10' : {
        'arg_types' : [F, F],
        'function_type': 'ttt',
        'values' : [
            [1.0,  10 ** 0.95, 10 ** pi, 10 ** -pi, float("inf"), float.fromhex('0x1.4298593c335e3p+10')], # Result
            [0.0, 0.95, pi, -pi, float("inf"), float.fromhex('0x1.8e2cp+1')]  # Arg0
        ],
        'tolerance' : 8192
    },
    'half_exp2' : {
        'arg_types' : [F, F],
        'function_type': 'ttt',
        'values' : [
            [1.0,  2 ** 0.95, 2 ** pi, 2 ** -pi, float("inf"), float.fromhex('0x1.146b7fd8431e3p+3')], # Result
            [0.0, 0.95, pi, -pi, float("inf"), float.fromhex('0x1.8e2cp+1')]  # Arg0
        ],
        'tolerance' : 8192
    },
    'half_log' : {
        'arg_types': [F, F],
        'function_type': 'ttt',
        'values': [
            [log(0.5), float("-inf"), log(1.e-15), float("nan")], #Result
            [0.5,      0.0,           1.e-15,      float("nan")]  #Arg0
        ],
        'tolerance' : 8192
    },
    'half_log10' : {
        'arg_types': [F, F],
        'function_type': 'ttt',
        'values': [
            [log10(0.5), float("-inf"), log10(1.e-15), float("nan")],
            [0.5,        0.0,           1.e-15,        float("nan")]
        ],
        'tolerance' : 8192
    },
    'half_log2' : {
        'arg_types': [F, F],
        'function_type': 'ttt',
        'values': [
            [log(0.5, 2), float("-inf"), log(1.e-15, 2), float("nan")], #Result
            [0.5,         0.0,           1.e-15,         float("nan")]  #Arg0
        ],
        'tolerance' : 8192
    },
    'half_powr' : {
        'arg_types': [F, F, F],
        'function_type': 'ttt',
        'values': [
            [pow(0, 1.0), pow(3, 10.0), pow(11, -3.0), pow(1234.5, 10), pow(2147483647, -1.0), 0.0], # Result
            [0,      3,   11, 1234.5, 2147483647,    2147483647], # Arg0
            [1.0, 10.0, -3.0,     10,       -1.0, float("-inf")] # Arg1
        ],
        'tolerance' : 8192
    },
    'half_recip' : {
        'arg_types': [F, F],
        'function_type': 'ttt',
        'values': [
            [1.0, 1.0/4.0,  1/6.0, 1/6.25 , float("nan"), 1/16.0,  float("inf"), 1/7.0, 1/pi], # Result
            [1.0, 4.0, 6.0, 6.25, float("nan"), 16.0, 0.0, 7.0, pi], # Arg1
        ],
        'tolerance' : 8192
    },
    'half_rsqrt' : {
        'arg_types': [F, F],
        'function_type': 'ttt',
        'values': [
            [1.0, 1.0/2.0,  1/6.0, 1/2.5 , float("nan"), 1/4.0,  float("inf"), 1/sqrt(7.0), 1/sqrt(pi)], # Result
            [1.0, 4.0, 36.0, 6.25, float("nan"), 16.0, 0.0, 7.0, pi], # Arg1
        ],
        'tolerance': 8192
    },
    'half_sin' : {
        'arg_types' : [F, F],
        'function_type': 'ttt',
        'values' : [
            [0.0, 1.0,   sin(M_PI_F), -1.0,       sin(2 * M_PI_F),    sin(2.234567), sin(7), sin(8), sin(pow(2,20)), sin(pow(2,24)), sin(pow(2,120)), float("nan")], # Result
            [0.0, pi / 2, pi, 3 * pi / 2, 2 * pi, 2.234567, 7, 8, pow(2,20), pow(2,24), pow(2,120), float("nan")] # Arg0
        ],
        'tolerance': 8192
    },
    'half_sqrt' : {
        'arg_types': [F, F],
        'function_type': 'ttt',
        'values': [
            [1.0, 2.0,  6.0, 2.5 , float("nan"), 4.0,  sqrt(0.0), sqrt(7.0), sqrt(pi)], # Result
            [1.0, 4.0, 36.0, 6.25, float("nan"), 16.0, 0.0, 7.0, pi], # Arg1
        ],
        'tolerance': 8192
    },
    'half_tan' : {
        'arg_types': [F, F],
        'function_type': 'ttt',
        'values': [
            [0.0, 1.0,  tan(M_PI_F), sqrt(3), -1.0,   tan(2.234567), float("nan") ], # Result
            [0.0, pi/4, M_PI_F,  pi/3,    3*pi/4, 2.234567 ,     float("nan") ], # Arg1
        ],
        'tolerance': 8192
    },
}


def main():
    dirName = os.path.join("cl", "builtin", "half_math")

    testDefs = {}
    functions = sorted(tests.keys())
    for dataType in DATA_TYPES:
        for fnName in functions:
            testDefs[(dataType, fnName)] = tests[fnName]

    gen(DATA_TYPES, CLC_VERSION_MIN, functions, testDefs, dirName)


if __name__ == '__main__':
    main()
