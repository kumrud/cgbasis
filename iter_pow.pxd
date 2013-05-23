# -*- coding: utf-8 -*-
# Horton is a development platform for electronic structure methods.
# Copyright (C) 2011-2013 Toon Verstraelen <Toon.Verstraelen@UGent.be>
#
# This file is part of Horton.
#
# Horton is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 3
# of the License, or (at your option) any later version.
#
# Horton is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>
#
#--


cdef extern from "iter_pow.h":
    bint iter_pow1_inc(long* n)

    cdef cppclass IterPow1:
        void reset(long shell_type0)
        bint inc()
        long n0[3], ibasis0

    cdef cppclass IterPow2:
        void reset(long shell_type0, long shell_type1)
        bint inc()
        long n0[3], n1[3], offset, ibasis0, ibasis1
