# brunnermunzel
A python module implements the Brunner-Munzel test.

version 0.1
WARNING: THIS IS UNDER DEVELOPMENT

# SYNOPSYS

    bm_test(x, y, ttype=0, alpha=0.05)

# DESCRIPTION
This function implements the Brunner-Munzel test.
Arguments 'x' and 'y' are list/scipy array whose type is integer or floaing point.

Run Brunner-Munzel test aginst 2 list of samples, X and Y.

All of element in both X and Y must be valid number.

You can select phypothesis by specifying negative, 0, or positive integer to 'ttype'. 0 is for null hypothesis, -1 or smaller integer is for less hypotesis, 1 or bigger for greater one. Default is 0.

'alpha' is the confidential level. Devault is 0.05. Its for 95% confidential interval.

# RETUEN VALUE
This function returns a tuple of (W, dof, p, Pest), where
  W: test statisfic
  dof: degree of freedom
  p: p-value
  Pest: numerial list of the range of given condifidential level.

# NOTE
The implementation is based on the description in next URL.
<http://oku.edu.mie-u.ac.jp/~okumura/stat/brunner-munzel.html>
