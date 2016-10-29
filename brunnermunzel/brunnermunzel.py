#!/usr/bin/env python
#
# Copyright (C) 2016 Yukishige Shibata <y-shibat@mtd.biglobe.ne.jp>
# All rights reserved.
#
# See LICENCE.txt
import math
import scipy.stats

def _calc_S2(R, Ri, Ravr):
    num_elem = len(Ri)
    if len(Ri) != len(R):
	raise "number of lements in sample and its rank must be same."

    s = 0.0
    i = 0
    while i < num_elem:
	v = (R[i] - Ri[i] - Ravr + (1.0 * num_elem + 1) / 2)
	v2 = v * v
	s += v2
	i += 1

    return s / (num_elem - 1)


def bm_test(x, y, ttype=0, alpha=0.05):
    """This function implements the Brunner-Munzel test.
    Arguments 'x' and 'y' are list/scipy array whose type is integer or floaing point.

Run Brunner-Munzel test aginst 2 list of samples, X and Y.

    All of element in both X and Y must be valid number.

    You can select phypothesis by specifying negative, 0, or positive integer to 'ttype'.
    0 is for null hypothesis, -1 or smaller integer is for less hypotesis, 1 or bigger for greater one.
    Default is 0.

    'alpha' is the confidential level. Devault is 0.05. Its for 95% confidential interval.

    This function returns a tuple of (W, dof, p, Pest), where
       W: test statisfic
       dof: degree of freedom
       p: p-value
       Pest: numerial list of the range of given condifidential level.

    The implementation is based on the description in next URL.
      http://oku.edu.mie-u.ac.jp/~okumura/stat/brunner-munzel.html
    """

    N_x = len(x)
    N_y = len(y)

    R_total = scipy.stats.rankdata(x +  y, method='average')
    R_x = R_total[:N_x]
    R_y = R_total[N_x:]

    Ravr_x = sum(R_x) / N_x
    Ravr_y = sum(R_y) / N_y

    Pest = (Ravr_y - Ravr_x) / (N_x + N_y) + 0.5

    Ri_x = scipy.stats.rankdata(x, method='average')
    Ri_y = scipy.stats.rankdata(y, method='average')

    S2_x = _calc_S2(R_x, Ri_x, Ravr_x)
    S2_y = _calc_S2(R_y, Ri_y, Ravr_y)

    W = ((N_x * N_y) * (Ravr_y - Ravr_x)) / ((N_x + N_y) * math.sqrt(N_x * S2_x + N_y * S2_y))

    nS2_x = N_x * S2_x
    nS2_y = N_y * S2_y

    f_hat_num = (nS2_x + nS2_y) * (nS2_x + nS2_y)
    f_hat_den = (nS2_x * nS2_x) / (N_x - 1) + (nS2_y * nS2_y) / (N_y - 1)
    f_hat = f_hat_num / f_hat_den

    int_t = scipy.stats.t.ppf(1 - (alpha/2), f_hat) * math.sqrt((S2_x / (N_x * N_y * N_y)) + (S2_y / (N_x * N_x * N_y)))
    C_l = Pest - int_t
    C_h = Pest + int_t

    if ttype < 0:
	p_value = scipy.stats.t.cdf(W, f_hat)
    elif ttype > 0:
	p_value = 1 - scipy.stats.t.cdf(W, f_hat)
    else:
	pt_g = scipy.stats.t.cdf(abs(W), f_hat)
	pt_l = 1 - scipy.stats.t.cdf(abs(W), f_hat)
	if pt_g < pt_l:
	    p_value = 2 * pt_g
	else:
	    p_value = 2 * pt_l

    return (W, f_hat, p_value, Pest, C_l, C_h)

if __name__ == '__main__':
    # Simple test code.
    x = [1,2,1,1,1,1,1,1,1,1,2,4,1,1]
    y = [3,3,4,3,1,2,3,1,1,5,4]

    (W, dof, p, Pest, Cl, Ch) = bm_test(x, y)
    print (W, dof, p, Pest, Cl, Ch)

    exit(0)
#### EOF ###
