#!/usr/bin/python

from pylab import *
from numpy import *

N = 1000

s10 = rand(N,10) < 0.25
s100 = rand(N,100) < 0.25
s1000 = rand(N,1000) < 0.25
s = (s10, s100, s1000)

h0 = (3,1)
_h0 = (13,3)

for i in range(len(s)):
	_s = s[i]
	L = _s.shape[1]

	n0 = (_s == 0).sum(1)
	n1 = L - n0

	# Plot number of zeros probability distribution
	figure(1, figsize=(12,9))
	subplot(311 + i)
	hist(n0, range(_s.shape[1] + 1), normed=1)

	# Plot chi2 probability distribution for H0: 3:1

	nh0 = float(L) * h0[0] / sum(h0)
	nh1 = L - nh0
	chi2 = (n0 - nh0)**2 / nh0 + (n1 - nh1)**2 / nh1
	n = (chi2 < 3.841).sum()

	figure(2, figsize=(12,9))
	subplot(311 + i)
	hist(chi2, arange(0, 10, 0.2), normed=1)
	x1,x2 = xlim()
	y1,y2 = ylim()
	text(x1 + .75 * (x2 - x1), y1 + .75 * (y2 - y1),
		"N | (chi ^ 2 < 3.841) = %d" % n)
	text(x1 + .75 * (x2 - x1), y1 + .5 * (y2 - y1),
		"max(chi ^ 2) = %.3f" % chi2.max())

	# Plot chi2 probability distribution for H0: 13:3

	nh0 = float(L) * _h0[0] / sum(_h0)
	nh1 = L - nh0
	chi2 = (n0 - nh0)**2 / nh0 + (n1 - nh1)**2 / nh1
	n = (chi2 < 3.841).sum()

	figure(3, figsize=(12,9))
	subplot(311 + i)
	hist(chi2, 50, normed=1)
	x1,x2 = xlim()
	y1,y2 = ylim()
	text(x1 + .75 * (x2 - x1), y1 + .75 * (y2 - y1),
		"N | (chi ^ 2 < 3.841) = %d" % n)
	text(x1 + .75 * (x2 - x1), y1 + .5 * (y2 - y1),
		"max(chi ^ 2) = %.3f" % chi2.max())

figure(1)
savefig("zeros-dist.png")
figure(2)
savefig("chi2-3:1-dist.png")
figure(3)
savefig("chi2-13:3-dist.png")
