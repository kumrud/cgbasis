# -*- coding: utf-8 -*-
# HORTON: Helpful Open-source Research TOol for N-fermion systems.
# Copyright (C) 2011-2017 The HORTON Development Team
#
# This file is part of HORTON.
#
# HORTON is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# HORTON is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
# --
"""The parameters for initializing GOBasis objects for testing.
Taken from HORTON 2's IOData module, originally stripped from fchk files etc.
"""

from numpy import array

h3_hfs_321g_fchk = (array([[0.0000000000000000e+00, 0.0000000000000000e+00,
                            1.3228082900000000e+00],
                           [0.0000000000000000e+00, 0.0000000000000000e+00,
                            0.0000000000000000e+00],
                           [1.6199729399999999e-16, 0.0000000000000000e+00,
                            -1.3228082900000000e+00]]),
                    array([0, 0, 1, 1, 2, 2]),
                    array([2, 1, 2, 1, 2, 1]),
                    array([0, 0, 0, 0, 0, 0]),
                    array([5.4471780000000001, 0.82454724, 0.18319158,
                           5.4471780000000001, 0.82454724, 0.18319158,
                           5.4471780000000001, 0.82454724, 0.18319158]),
                    array([0.156284979, 0.9046908769999999, 1.,
                           0.156284979, 0.9046908769999999, 1.,
                           0.156284979, 0.9046908769999999, 1.]))
h3_pbe_321g_fchk = (array([[0.0000000000000000e+00, 0.0000000000000000e+00,
                            1.3228082900000000e+00],
                           [0.0000000000000000e+00, 0.0000000000000000e+00,
                            0.0000000000000000e+00],
                           [1.6199729399999999e-16, 0.0000000000000000e+00,
                            -1.3228082900000000e+00]]),
                    array([0, 0, 1, 1, 2, 2]),
                    array([2, 1, 2, 1, 2, 1]),
                    array([0, 0, 0, 0, 0, 0]),
                    array([5.4471780000000001, 0.82454724, 0.18319158,
                           5.4471780000000001, 0.82454724, 0.18319158,
                           5.4471780000000001, 0.82454724, 0.18319158]),
                    array([0.156284979, 0.9046908769999999, 1.,
                           0.156284979, 0.9046908769999999, 1.,
                           0.156284979, 0.9046908769999999, 1.]))
monosilicic_acid_hf_lan_fchk = (array([[4.7638793200000001e-02, 1.8048573599999999e-04,
                                        -3.0662173700000000e-02],
                                       [-1.1379140900000000e+00, -2.2816393800000000e-03,
                                        2.8866866899999999e+00],
                                       [-9.3265467099999999e-01, 2.5724992800000002e+00,
                                        -1.5595740499999999e+00],
                                       [-9.3329098799999999e-01, -2.5695700399999999e+00,
                                        -1.5637504700000000e+00],
                                       [3.1933658800000000e+00, -2.8496137399999999e-04,
                                        1.1488686600000000e-01],
                                       [-2.9651975099999999e+00, -4.2678546199999999e-03,
                                        3.0736195199999998e+00],
                                       [-4.9170544199999999e-01, 4.2119835300000004e+00,
                                        -8.5823660499999999e-01],
                                       [-2.7422719299999998e+00, -2.8074937599999998e+00,
                                        -1.7763646000000000e+00],
                                       [4.0161827600000004e+00, -1.4056498799999999e+00,
                                        9.6425984399999998e-01]]),
                                array([0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 6, 7, 8]),
                                array([3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),
                                array([0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0]),
                                array([1.2220000000000000e+00, 2.5950000000000001e-01,
                                       9.3100000000000002e-02, 2.5800000000000001e+00,
                                       2.9840000000000000e-01, 8.8499999999999995e-02,
                                       1.3070932099999999e+02, 2.3808866099999999e+01,
                                       6.4436083100000001e+00, 5.0331513200000000e+00,
                                       1.1695961200000000e+00, 3.8038896000000000e-01,
                                       5.0331513200000000e+00, 1.1695961200000000e+00,
                                       3.8038896000000000e-01, 1.3070932099999999e+02,
                                       2.3808866099999999e+01, 6.4436083100000001e+00,
                                       5.0331513200000000e+00, 1.1695961200000000e+00,
                                       3.8038896000000000e-01, 5.0331513200000000e+00,
                                       1.1695961200000000e+00, 3.8038896000000000e-01,
                                       1.3070932099999999e+02, 2.3808866099999999e+01,
                                       6.4436083100000001e+00, 5.0331513200000000e+00,
                                       1.1695961200000000e+00, 3.8038896000000000e-01,
                                       5.0331513200000000e+00, 1.1695961200000000e+00,
                                       3.8038896000000000e-01, 1.3070932099999999e+02,
                                       2.3808866099999999e+01, 6.4436083100000001e+00,
                                       5.0331513200000000e+00, 1.1695961200000000e+00,
                                       3.8038896000000000e-01, 5.0331513200000000e+00,
                                       1.1695961200000000e+00, 3.8038896000000000e-01,
                                       3.4252509099999999e+00, 6.2391373000000006e-01,
                                       1.6885540399999999e-01, 3.4252509099999999e+00,
                                       6.2391373000000006e-01, 1.6885540399999999e-01,
                                       3.4252509099999999e+00, 6.2391373000000006e-01,
                                       1.6885540399999999e-01, 3.4252509099999999e+00,
                                       6.2391373000000006e-01, 1.6885540399999999e-01]),
                                array([-0.274463915, 0.6166933020000001, 0.558089893,
                                       -0.039783808, 0.521981461, 0.587364502,
                                       0.154328967, 0.535328142, 0.444634542,
                                       -0.0999672292, 0.399512826, 0.700115469,
                                       0.155916275, 0.607683719, 0.391957393,
                                       0.154328967, 0.535328142, 0.444634542,
                                       -0.0999672292, 0.399512826, 0.700115469,
                                       0.155916275, 0.607683719, 0.391957393,
                                       0.154328967, 0.535328142, 0.444634542,
                                       -0.0999672292, 0.399512826, 0.700115469,
                                       0.155916275, 0.607683719, 0.391957393,
                                       0.154328967, 0.535328142, 0.444634542,
                                       -0.0999672292, 0.399512826, 0.700115469,
                                       0.155916275, 0.607683719, 0.391957393,
                                       0.154328967, 0.535328142, 0.444634542,
                                       0.154328967, 0.535328142, 0.444634542,
                                       0.154328967, 0.535328142, 0.444634542,
                                       0.154328967, 0.535328142, 0.444634542]))
n2_hfs_sto3g_fchk = (array([[0.0000000000000000e+00, 0.0000000000000000e+00,
                             1.0506877299999999e+00],
                            [1.2867213700000000e-16, 0.0000000000000000e+00,
                             -1.0506877299999999e+00]]),
                     array([0, 0, 0, 1, 1, 1]),
                     array([3, 3, 3, 3, 3, 3]),
                     array([0, 0, 1, 0, 0, 1]),
                     array([99.1061689999999942, 18.0523124000000017, 4.88566024,
                            3.7804558799999999, 0.878496645, 0.285714374,
                            3.7804558799999999, 0.878496645, 0.285714374,
                            99.1061689999999942, 18.0523124000000017, 4.88566024,
                            3.7804558799999999, 0.878496645, 0.285714374,
                            3.7804558799999999, 0.878496645, 0.285714374]),
                     array([0.154328967, 0.535328142, 0.444634542, -0.0999672292,
                            0.399512826, 0.700115469, 0.155916275, 0.607683719,
                            0.391957393, 0.154328967, 0.535328142, 0.444634542,
                            -0.0999672292, 0.399512826, 0.700115469, 0.155916275,
                            0.607683719, 0.391957393]))
co_ccpv5z_cart_hf_g03_fchk = (array([[0., 0., 0.188972613],
                                     [2.6456165899999999, 0.377945227, -0.188972613]]),
                              array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
                              array([10, 10, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                     1, 1, 1, 1, 10, 10, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1,
                                     1, 1, 1, 1, 1, 1, 1, 1]),
                              array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5, 0, 0,
                                     0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 5]),
                              array([2.9493000000000000e+04, 4.4171009999999997e+03,
                                     1.0052230000000000e+03, 2.8470089999999999e+02,
                                     9.2865430000000003e+01, 3.3511789999999998e+01,
                                     1.3041800000000000e+01, 5.3575359999999996e+00,
                                     2.2793380000000001e+00, 9.9399000000000004e-01,
                                     2.9493000000000000e+04, 4.4171009999999997e+03,
                                     1.0052230000000000e+03, 2.8470089999999999e+02,
                                     9.2865430000000003e+01, 3.3511789999999998e+01,
                                     1.3041800000000000e+01, 5.3575359999999996e+00,
                                     2.2793380000000001e+00, 9.9399000000000004e-01,
                                     4.3347100000000000e-01, 9.5565999999999998e-02,
                                     4.4657000000000002e-02, 2.0632999999999999e-02,
                                     1.1250000000000000e+01, 2.5000000000000000e+00,
                                     6.5000000000000002e-01, 2.5000000000000000e-01,
                                     1.0000000000000001e-01, 3.9000000000000000e-02,
                                     1.7000000000000001e-02, 5.5000000000000004e-01,
                                     2.8999999999999998e-01, 1.4000000000000001e-01,
                                     6.0999999999999999e-02, 3.4999999999999998e-01,
                                     2.2000000000000000e-01, 1.1000000000000000e-01,
                                     3.2000000000000001e-01, 1.6000000000000000e-01,
                                     3.2000000000000001e-01, 2.1140000000000000e+05,
                                     3.1660000000000000e+04, 7.2020000000000000e+03,
                                     2.0400000000000000e+03, 6.6639999999999998e+02,
                                     2.4200000000000000e+02, 9.5530000000000001e+01,
                                     4.0229999999999997e+01, 1.7719999999999999e+01,
                                     8.0050000000000008e+00, 2.1140000000000000e+05,
                                     3.1660000000000000e+04, 7.2020000000000000e+03,
                                     2.0400000000000000e+03, 6.6639999999999998e+02,
                                     2.4200000000000000e+02, 9.5530000000000001e+01,
                                     4.0229999999999997e+01, 1.7719999999999999e+01,
                                     8.0050000000000008e+00, 3.5379999999999998e+00,
                                     1.4580000000000000e+00, 5.8870000000000000e-01,
                                     2.3240000000000000e-01, 2.4190000000000001e+02,
                                     5.7170000000000002e+01, 1.8129999999999999e+01,
                                     6.6239999999999997e+00, 2.6219999999999999e+00,
                                     1.0569999999999999e+00, 4.1760000000000003e-01,
                                     1.5740000000000001e-01, 7.7599999999999998e+00,
                                     3.0320000000000000e+00, 1.1850000000000001e+00,
                                     4.6300000000000002e-01, 5.3979999999999997e+00,
                                     2.0779999999999998e+00, 8.0000000000000004e-01,
                                     4.3380000000000001e+00, 1.5129999999999999e+00,
                                     2.9950000000000001e+00]),
                              array([2.0099981900000000e-05, 1.5744985800000000e-04,
                                     8.2521592400000001e-04, 3.4694802100000001e-03,
                                     1.2434072100000000e-02, 3.8714798500000001e-02,
                                     1.0292419100000000e-01, 2.2285966600000001e-01,
                                     3.6719986999999998e-01, 3.8633840200000003e-01,
                                     -1.5637376600000001e-05, -1.1467409499999999e-04,
                                     -5.9943276999999996e-04, -2.5384674699999998e-03,
                                     -9.1009531799999994e-03, -2.8772773000000001e-02,
                                     -7.7811586000000002e-02, -1.7829736800000001e-01,
                                     -3.2398038099999998e-01, -4.9988523000000001e-01,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     2.9517231700000000e-02, 2.2313407299999999e-01,
                                     8.4461578599999998e-01, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 2.7168460599999999e-05,
                                     2.1003309900000000e-04, 1.1034574800000000e-03,
                                     4.6311775899999996e-03, 1.6474536500000001e-02,
                                     5.0274191400000001e-02, 1.2877014400000000e-01,
                                     2.6282246300000001e-01, 3.8090704199999997e-01,
                                     2.9233890600000001e-01, -1.7193724600000000e-05,
                                     -1.3468417599999999e-04, -6.9921146700000002e-04,
                                     -2.9544550099999999e-03, -1.0554081300000000e-02,
                                     -3.2991891900000000e-02, -8.7868529500000001e-02,
                                     -1.9936696800000001e-01, -3.5531404999999999e-01,
                                     -4.3045635799999998e-01, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 6.3608427599999998e-03,
                                     5.1127971699999997e-02, 2.4153427699999999e-01,
                                     7.8576722200000004e-01, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00]))
h_sto3g_fchk = (array([[0., 0., 0.]]),
                array([0]),
                array([3]),
                array([0]),
                array([3.4252509099999999, 0.6239137300000001, 0.168855404]),
                array([0.154328967, 0.535328142, 0.444634542]))
water_hfs_321g_fchk = (array([[0.0000000000000000e+00, 1.4812372599999999e+00,
                               -8.3791363799999996e-01],
                              [0.0000000000000000e+00, 0.0000000000000000e+00,
                               2.0947841000000000e-01],
                              [-1.8139924700000000e-16, -1.4812372599999999e+00,
                               -8.3791363799999996e-01]]),
                       array([0, 0, 1, 1, 1, 1, 1, 2, 2]),
                       array([2, 1, 3, 2, 2, 1, 1, 2, 1]),
                       array([0, 0, 0, 0, 1, 0, 1, 0, 0]),
                       array([5.4471780000000001e+00, 8.2454724000000001e-01,
                              1.8319157999999999e-01, 3.2203699999999998e+02,
                              4.8430799999999998e+01, 1.0420600000000000e+01,
                              7.4029400000000001e+00, 1.5762000000000000e+00,
                              7.4029400000000001e+00, 1.5762000000000000e+00,
                              3.7368400000000002e-01, 3.7368400000000002e-01,
                              5.4471780000000001e+00, 8.2454724000000001e-01,
                              1.8319157999999999e-01]),
                       array([0.156284979, 0.9046908769999999, 1.,
                              0.0592393934, 0.351499961, 0.707657921,
                              -0.404453583, 1.2215617599999999, 0.244586107,
                              0.853955373, 1., 1.,
                              0.156284979, 0.9046908769999999, 1.]))
co_ccpv5z_pure_hf_g03_fchk = (array([[0., 0., 0.188972613],
                                     [2.6456165899999999, 0.377945227, -0.188972613]]),
                              array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1,
                                     1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
                              array([10, 10, 1, 1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                                     1, 1, 1, 1, 10, 10, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1,
                                     1, 1, 1, 1, 1, 1, 1, 1]),
                              array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, -2, -2, -2, -2, -3, -3,
                                     -3, -4, -4, -5, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, -2, -2,
                                     -2, -2, -3, -3, -3, -4, -4, -5]),
                              array([2.9493000000000000e+04, 4.4171009999999997e+03,
                                     1.0052230000000000e+03, 2.8470089999999999e+02,
                                     9.2865430000000003e+01, 3.3511789999999998e+01,
                                     1.3041800000000000e+01, 5.3575359999999996e+00,
                                     2.2793380000000001e+00, 9.9399000000000004e-01,
                                     2.9493000000000000e+04, 4.4171009999999997e+03,
                                     1.0052230000000000e+03, 2.8470089999999999e+02,
                                     9.2865430000000003e+01, 3.3511789999999998e+01,
                                     1.3041800000000000e+01, 5.3575359999999996e+00,
                                     2.2793380000000001e+00, 9.9399000000000004e-01,
                                     4.3347100000000000e-01, 9.5565999999999998e-02,
                                     4.4657000000000002e-02, 2.0632999999999999e-02,
                                     1.1250000000000000e+01, 2.5000000000000000e+00,
                                     6.5000000000000002e-01, 2.5000000000000000e-01,
                                     1.0000000000000001e-01, 3.9000000000000000e-02,
                                     1.7000000000000001e-02, 5.5000000000000004e-01,
                                     2.8999999999999998e-01, 1.4000000000000001e-01,
                                     6.0999999999999999e-02, 3.4999999999999998e-01,
                                     2.2000000000000000e-01, 1.1000000000000000e-01,
                                     3.2000000000000001e-01, 1.6000000000000000e-01,
                                     3.2000000000000001e-01, 2.1140000000000000e+05,
                                     3.1660000000000000e+04, 7.2020000000000000e+03,
                                     2.0400000000000000e+03, 6.6639999999999998e+02,
                                     2.4200000000000000e+02, 9.5530000000000001e+01,
                                     4.0229999999999997e+01, 1.7719999999999999e+01,
                                     8.0050000000000008e+00, 2.1140000000000000e+05,
                                     3.1660000000000000e+04, 7.2020000000000000e+03,
                                     2.0400000000000000e+03, 6.6639999999999998e+02,
                                     2.4200000000000000e+02, 9.5530000000000001e+01,
                                     4.0229999999999997e+01, 1.7719999999999999e+01,
                                     8.0050000000000008e+00, 3.5379999999999998e+00,
                                     1.4580000000000000e+00, 5.8870000000000000e-01,
                                     2.3240000000000000e-01, 2.4190000000000001e+02,
                                     5.7170000000000002e+01, 1.8129999999999999e+01,
                                     6.6239999999999997e+00, 2.6219999999999999e+00,
                                     1.0569999999999999e+00, 4.1760000000000003e-01,
                                     1.5740000000000001e-01, 7.7599999999999998e+00,
                                     3.0320000000000000e+00, 1.1850000000000001e+00,
                                     4.6300000000000002e-01, 5.3979999999999997e+00,
                                     2.0779999999999998e+00, 8.0000000000000004e-01,
                                     4.3380000000000001e+00, 1.5129999999999999e+00,
                                     2.9950000000000001e+00]),
                              array([2.0099981900000000e-05, 1.5744985800000000e-04,
                                     8.2521592400000001e-04, 3.4694802100000001e-03,
                                     1.2434072100000000e-02, 3.8714798500000001e-02,
                                     1.0292419100000000e-01, 2.2285966600000001e-01,
                                     3.6719986999999998e-01, 3.8633840200000003e-01,
                                     -1.5637376600000001e-05, -1.1467409499999999e-04,
                                     -5.9943276999999996e-04, -2.5384674699999998e-03,
                                     -9.1009531799999994e-03, -2.8772773000000001e-02,
                                     -7.7811586000000002e-02, -1.7829736800000001e-01,
                                     -3.2398038099999998e-01, -4.9988523000000001e-01,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     2.9517231700000000e-02, 2.2313407299999999e-01,
                                     8.4461578599999998e-01, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 2.7168460599999999e-05,
                                     2.1003309900000000e-04, 1.1034574800000000e-03,
                                     4.6311775899999996e-03, 1.6474536500000001e-02,
                                     5.0274191400000001e-02, 1.2877014400000000e-01,
                                     2.6282246300000001e-01, 3.8090704199999997e-01,
                                     2.9233890600000001e-01, -1.7193724600000000e-05,
                                     -1.3468417599999999e-04, -6.9921146700000002e-04,
                                     -2.9544550099999999e-03, -1.0554081300000000e-02,
                                     -3.2991891900000000e-02, -8.7868529500000001e-02,
                                     -1.9936696800000001e-01, -3.5531404999999999e-01,
                                     -4.3045635799999998e-01, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 6.3608427599999998e-03,
                                     5.1127971699999997e-02, 2.4153427699999999e-01,
                                     7.8576722200000004e-01, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00, 1.0000000000000000e+00,
                                     1.0000000000000000e+00]))
water_ccpvdz_pure_hf_g03_fchk = (array([[0., 0., 0.188972613],
                                        [0., 0.188972613, 1.7952398300000001],
                                        [1.69257101, -0.188972613, -0.5984063469999999]]),
                                 array([0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2]),
                                 array([7, 7, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1]),
                                 array([0, 0, 0, 1, 1, -2, 0, 0, 1, 0, 0, 1]),
                                 array([1.1720000000000000e+04, 1.7590000000000000e+03,
                                        4.0080000000000001e+02, 1.1370000000000000e+02,
                                        3.7030000000000001e+01, 1.3270000000000000e+01,
                                        5.0250000000000004e+00, 1.1720000000000000e+04,
                                        1.7590000000000000e+03, 1.1370000000000000e+02,
                                        3.7030000000000001e+01, 1.3270000000000000e+01,
                                        5.0250000000000004e+00, 1.0129999999999999e+00,
                                        3.0230000000000001e-01, 1.7699999999999999e+01,
                                        3.8540000000000001e+00, 1.0460000000000000e+00,
                                        2.7529999999999999e-01, 1.1850000000000001e+00,
                                        1.3010000000000000e+01, 1.9620000000000000e+00,
                                        4.4460000000000000e-01, 1.2200000000000000e-01,
                                        7.2699999999999998e-01, 1.3010000000000000e+01,
                                        1.9620000000000000e+00, 4.4460000000000000e-01,
                                        1.2200000000000000e-01, 7.2699999999999998e-01]),
                                 array([7.1186443399999999e-04, 5.4852019899999998e-03,
                                        2.7909929600000001e-02, 1.0513320800000001e-01,
                                        2.8400249000000000e-01, 4.5167394599999999e-01,
                                        2.7320812600000000e-01, -3.0612309399999999e-07,
                                        -6.1762339799999996e-05, -4.1572706900000001e-03,
                                        -1.4100088400000000e-02, -1.2613848100000000e-01,
                                        -1.0961459799999999e-01, 1.0986883300000001e+00,
                                        1.0000000000000000e+00, 6.2679166300000005e-02,
                                        3.3353656599999998e-01, 7.4123964200000003e-01,
                                        1.0000000000000000e+00, 1.0000000000000000e+00,
                                        3.3498726399999998e-02, 2.3480080100000000e-01,
                                        8.1368295800000001e-01, 1.0000000000000000e+00,
                                        1.0000000000000000e+00, 3.3498726399999998e-02,
                                        2.3480080100000000e-01, 8.1368295800000001e-01,
                                        1.0000000000000000e+00, 1.0000000000000000e+00]))
ch3_hf_sto3g_fchk = (array([[0.358528636, 0.360868439, 0.360868439],
                            [-0.307236803, -0.309472858, 2.16905613],
                            [-0.307236803, 2.16905613, -0.309472858],
                            [2.16078891, -0.315607772, -0.315607772]]),
                     array([0, 0, 0, 1, 2, 3]),
                     array([3, 3, 3, 3, 3, 3]),
                     array([0, 0, 1, 0, 0, 0]),
                     array([71.6168373000000003, 13.0450963000000009, 3.5305121599999998,
                            2.94124936, 0.683483096, 0.222289916,
                            2.94124936, 0.683483096, 0.222289916,
                            3.4252509099999999, 0.6239137300000001, 0.168855404,
                            3.4252509099999999, 0.6239137300000001, 0.168855404,
                            3.4252509099999999, 0.6239137300000001, 0.168855404]),
                     array([0.154328967, 0.535328142, 0.444634542, -0.0999672292,
                            0.399512826, 0.700115469, 0.155916275, 0.607683719,
                            0.391957393, 0.154328967, 0.535328142, 0.444634542,
                            0.154328967, 0.535328142, 0.444634542, 0.154328967,
                            0.535328142, 0.444634542]))
water_sto3g_hf_g03_fchk = (array([[0., 0., 0.],
                                  [0., 0., 1.7952398300000001],
                                  [1.69257101, 0., -0.5984063469999999]]),
                           array([0, 0, 0, 1, 2]),
                           array([3, 3, 3, 3, 3]),
                           array([0, 0, 1, 0, 0]),
                           array([130.7093209999999885, 23.8088660999999995, 6.4436083100000001,
                                  5.03315132, 1.16959612, 0.38038896,
                                  5.03315132, 1.16959612, 0.38038896,
                                  3.4252509099999999, 0.6239137300000001, 0.168855404,
                                  3.4252509099999999, 0.6239137300000001, 0.168855404]),
                           array([0.154328967, 0.535328142, 0.444634542, -0.0999672292,
                                  0.399512826, 0.700115469, 0.155916275, 0.607683719,
                                  0.391957393, 0.154328967, 0.535328142, 0.444634542,
                                  0.154328967, 0.535328142, 0.444634542]))
li_h_3_21G_hf_g09_fchk = (array([[0., 0., 1.11419479],
                                 [0., 0., -3.3425843799999999]]),
                          array([0, 0, 0, 0, 0, 1, 1]),
                          array([3, 2, 2, 1, 1, 2, 1]),
                          array([0, 0, 1, 0, 1, 0, 0]),
                          array([3.6838200000000001e+01, 5.4817200000000001e+00,
                                 1.1132700000000000e+00, 5.4020500000000005e-01,
                                 1.0225500000000000e-01, 5.4020500000000005e-01,
                                 1.0225500000000000e-01, 2.8564500000000000e-02,
                                 2.8564500000000000e-02, 5.4471780000000001e+00,
                                 8.2454724000000001e-01, 1.8319157999999999e-01]),
                          array([0.0696686638, 0.381346349, 0.681702624,
                                 -0.263126406, 1.14338742, 0.161545971,
                                 0.915662835, 1., 1.,
                                 0.156284979, 0.9046908769999999, 1.]))
water_ccpvdz_cart_hf_g03_fchk = (array([[0., 0., 0.188972613],
                                        [0., 0.188972613, 1.7952398300000001],
                                        [1.69257101, -0.188972613, -0.5984063469999999]]),
                                 array([0, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2]),
                                 array([7, 7, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1]),
                                 array([0, 0, 0, 1, 1, 2, 0, 0, 1, 0, 0, 1]),
                                 array([1.1720000000000000e+04, 1.7590000000000000e+03,
                                        4.0080000000000001e+02, 1.1370000000000000e+02,
                                        3.7030000000000001e+01, 1.3270000000000000e+01,
                                        5.0250000000000004e+00, 1.1720000000000000e+04,
                                        1.7590000000000000e+03, 1.1370000000000000e+02,
                                        3.7030000000000001e+01, 1.3270000000000000e+01,
                                        5.0250000000000004e+00, 1.0129999999999999e+00,
                                        3.0230000000000001e-01, 1.7699999999999999e+01,
                                        3.8540000000000001e+00, 1.0460000000000000e+00,
                                        2.7529999999999999e-01, 1.1850000000000001e+00,
                                        1.3010000000000000e+01, 1.9620000000000000e+00,
                                        4.4460000000000000e-01, 1.2200000000000000e-01,
                                        7.2699999999999998e-01, 1.3010000000000000e+01,
                                        1.9620000000000000e+00, 4.4460000000000000e-01,
                                        1.2200000000000000e-01, 7.2699999999999998e-01]),
                                 array([7.1186443399999999e-04, 5.4852019899999998e-03,
                                        2.7909929600000001e-02, 1.0513320800000001e-01,
                                        2.8400249000000000e-01, 4.5167394599999999e-01,
                                        2.7320812600000000e-01, -3.0612309399999999e-07,
                                        -6.1762339799999996e-05, -4.1572706900000001e-03,
                                        -1.4100088400000000e-02, -1.2613848100000000e-01,
                                        -1.0961459799999999e-01, 1.0986883300000001e+00,
                                        1.0000000000000000e+00, 6.2679166300000005e-02,
                                        3.3353656599999998e-01, 7.4123964200000003e-01,
                                        1.0000000000000000e+00, 1.0000000000000000e+00,
                                        3.3498726399999998e-02, 2.3480080100000000e-01,
                                        8.1368295800000001e-01, 1.0000000000000000e+00,
                                        1.0000000000000000e+00, 3.3498726399999998e-02,
                                        2.3480080100000000e-01, 8.1368295800000001e-01,
                                        1.0000000000000000e+00, 1.0000000000000000e+00]))
