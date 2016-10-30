#!/usr/bin/env python

import os
import sys
from subprocess import Popen, PIPE
import re

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../brunnermunzel')
import brunnermunzel

def generateRSource(src, s1, s2, alt, alpha):
    f = open(src, "w")
    f.write('s1 <-c(')
    f.write(','.join(map(str, s1)))
    f.write(')\n')
    
    f.write('s2 <-c(')
    f.write(','.join(map(str, s2)))
    f.write(')\n')    

    f.write('options(digits=16)\n')
    f.write('require("lawstat")\n')
    f.write('print(brunner.munzel.test(s1, s2, alternative="%s", alpha=%f))\n' % (alt, alpha))

    f.close()

Re1 = re.compile('Statistic = (-?[0-9.]+), df = (-?[0-9.]+),')
Re1_1 = re.compile('^\s*p-value = ([0-9.]+)\s*$')
Re2 = re.compile('^\s*(-?[0-9.]+) (-?[0-9.]+)\s*$')
Re3 = re.compile('^\s*([0-9.]+)\s*$')

def runRSource(src):
    result = []
 
    cmd=['Rscript --vanilla ' +  src]
    pin, perr = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True).communicate()
    for l in pin.split('\n'):
	m = Re1.search(l)
	if m:
	    result.append(m.group(1))
	    result.append(m.group(2))
	    continue
	m = Re1_1.search(l)
	if m:
	    result.append(m.group(1))
	    continue	
	m = Re2.match(l)
	if m:
	    result.append(m.group(1))
	    result.append(m.group(2))
	    continue
	m = Re3.match(l)
	if m:
	    result.append(m.group(1))
	    continue

    return  map(float, result)
    
def calcByR(x, y, method, alpha):
    r_file='tmp.r'
    if method < 0:
	alt='less'
    elif method > 0:
	alt='greater'
    else:
	alt='two.sided'
    generateRSource(r_file, x, y, alt, alpha)
    return runRSource(r_file)

def compareResult(ri, p):
    s = ['W', 'dof', 'p', 'Pest', 'Cl', 'Ch' ]
    r = [ri[0], ri[1], ri[2], ri[5], ri[3], ri[4] ]
    i = 0
    ng = 0
    while i < len(s):
	er = abs((p[i] - r[i]) / p[i])
	if er > 256 * sys.float_info.epsilon:
	    print("%s: r=%.15f p=%0.15f er=%0.15f" % (s[i], r[i], p[i], er))
	    ng += 1
	i += 1

    return ng

x = [1,2,1,1,1,1,1,1,1,1,2,4,1,1]
y = [3,3,4,3,1,2,3,1,1,5,4]
method=0
alpha=0.05

r_result = calcByR(x, y, method, alpha)
p_result = brunnermunzel.bm_test(x, y, method, alpha)
es = compareResult(r_result, p_result)
exit(es)
