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

All of elements in both X and Y must be valid number.

You can select hypothesis by specifying negative, 0, or positive integer to 'ttype'. 0 is for null hypothesis, -1 or smaller integer is for less hypotesis, 1 or bigger for greater one. Default is 0.

'alpha' is the confidential level. Devault is 0.05. Its for 95% confidential interval.

# RETERN VALUE
This function returns a tuple of (W, dof, p, Pest), where
  W: test statisfic
  dof: degree of freedom
  p: p-value of the test
  Pest: Estimated effect size. 
  Cl: Low boundary of the range of numerial list of the range of given condifidential level.
  Ch: High boundary of the range of numerial list of the range of given condifidential level.

# Example

    x = [1,2,1,1,1,1,1,1,1,1,2,4,1,1]
    y = [3,3,4,3,1,2,3,1,1,5,4]
    (W, dof, p, Pest, Cl, Ch) = bm_test(x, y)
    print (W, dof, p, Pest, Cl, Ch)

This prints following result on your console.

   (3.1374674823029505, 17.682841979481548, 0.0057862086661515377, 0.78896103896103909, 0.59521686425374498, 0.98270521366833319)


# References
The implementation is based on the description in next URL.
<http://oku.edu.mie-u.ac.jp/~okumura/stat/brunner-munzel.html>
