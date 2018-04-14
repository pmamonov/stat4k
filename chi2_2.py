#!/usr/bin/python

import sys
from pylab import *
from numpy import *

CHI2P05 = 3.841

def chi2(h0, s):
	l = s.shape[-1]
	nh0, nh1 = float(h0[0]) * l / sum(h0), float(h0[1]) * l / sum(h0)
	n1 = s.sum(-1)
	n0 = l - n1
	_chi2 = (n0 - nh0)**2 / nh0 + (n1 - nh1)**2 / nh1
	return _chi2

def adj_samp_len(s, cond, h0):
	STEP = 10

	N = s.shape[0]
	L = 100

	ns = [L for i in range(N)]
	ok = [0 for i in range(N)]
	c2 = zeros(N)
	while sum(ok) < len(ok):
		print "\r ok=%4d nmax=%5d" % (sum(ok), max(ns)),
		sys.stdout.flush()
		for i in xrange(N):
			if not ok[i]:
				c2[i] = chi2(h0, s[i,:ns[i]])
				if cond(c2[i]):
					ok[i] = 1
				else:
					if ns[i] < LMAX:
						ns[i] += STEP
					else:
						ok[i] = 1
	return ns, c2
	
if __name__ == "__main__":
	N = 1000
	L = 100
	ia = arange(N)
	bins = 50

	s = rand(N, 2 * L) < 0.25
	
	figure(1, figsize=(12,9))
	for h0 in ((3,1), (13,3)):
		s1 = s[:,:L]
		s1_chi2 = chi2(h0, s1)
		
		is2 = ia[s1_chi2 <= CHI2P05]
		s2 = s[is2, :]
		s2_chi2 = chi2(h0, s2)
		
		is3 = ia[s1_chi2 > CHI2P05]
		s3 = s[is3, :]
		s3_chi2 = chi2(h0, s3)
		
		clf()

		subplot(3,1,1)
		hist(s1_chi2, bins=bins, normed=False)
		x1,x2 = xlim()
		y1,y2 = ylim()
		text(x1 + 0.7 * (x2 - x1),
			y1 + 0.7 * (y2 - y1),
			"N | (chi2 < 3.84): %d / %d" % (
				(s1_chi2 < CHI2P05).sum(), s1_chi2.shape[0]))

		subplot(3,1,2)
		hist(s2_chi2, bins=bins, normed=False)
		x1,x2 = xlim()
		y1,y2 = ylim()
		text(x1 + 0.7 * (x2 - x1),
			y1 + 0.7 * (y2 - y1),
			"N | (chi2 < 3.84): %d / %d" % (
				(s2_chi2 < CHI2P05).sum(), s2_chi2.shape[0]))

		subplot(3,1,3)
		hist(s3_chi2, bins=bins, normed=False)
		x1,x2 = xlim()
		y1,y2 = ylim()
		text(x1 + 0.7 * (x2 - x1),
			y1 + 0.7 * (y2 - y1),
			"N | (chi2 < 3.84): %d / %d" % (
				(s3_chi2 < CHI2P05).sum(), s3_chi2.shape[0]))
		
		savefig("chi2-2_%d-%d.png" % h0)

	h0 = (3,1)
	N = 1000
	LMAX = 10000
	s = rand(N, LMAX) < 0.25
	
	ns, c2 = adj_samp_len(s, lambda x: x > 3.841, h0)
	
	figure(1, figsize=(12,10))
	clf()

	subplot(2,1,1)
	hist(c2, bins=bins, normed=False)
	xlabel("Chi2")
	x1,x2 = xlim()
	y1,y2 = ylim()
	text(x1 + 0.7 * (x2 - x1),
		y1 + 0.7 * (y2 - y1),
		"N | (chi2 > 3.84): %d / %d" % (
			(c2 > 3.841).sum(), c2.shape[0]))

	subplot(2,1,2)
	hist(ns, bins=bins, normed=False)
	xlabel("N")

	savefig("chi2-2_greater-3.841.png")

	ns, c2 = adj_samp_len(s, lambda x: x < 0.445, h0)
	
	figure(1, figsize=(12,10))
	clf()

	subplot(2,1,1)
	hist(c2, bins=bins, normed=False)
	xlabel("Chi2")
	x1,x2 = xlim()
	y1,y2 = ylim()
	text(x1 + 0.7 * (x2 - x1),
		y1 + 0.7 * (y2 - y1),
		"N | (chi2 < 0.445): %d / %d" % (
			(c2 < 0.445).sum(), c2.shape[0]))

	subplot(2,1,2)
	hist(ns, bins=bins, normed=False)
	xlabel("N")

	savefig("chi2-2_less-0.445.png")

	ns, c2 = adj_samp_len(s, lambda x: x < 0.064, h0)
	
	figure(1, figsize=(12,10))
	clf()

	subplot(2,1,1)
	hist(c2, bins=bins, normed=False)
	xlabel("Chi2")
	x1,x2 = xlim()
	y1,y2 = ylim()
	text(x1 + 0.7 * (x2 - x1),
		y1 + 0.7 * (y2 - y1),
		"N | (chi2 < 0.064): %d / %d" % (
			(c2 < 0.064).sum(), c2.shape[0]))

	subplot(2,1,2)
	hist(ns, bins=bins, normed=False)
	xlabel("N")

	savefig("chi2-2_less-0.064.png")
