#!/usr/bin/python

from pylab import *
from numpy import *

T=2
N=2000
t = linspace(0, T, N)

ds1 = sin(2 * pi * t)

ds2 = 0.5 * sin(2 * pi * 10 * t)

ds3 = ds1 + ds2

ds5 = 2 * 0.2 * (2 * rand(t.shape[0]) - 1)

f = rfft(ds5)
f100 = copy(f)
f100[100 * T:] = 0
ds4 = sqrt((f * f.conj()).sum() / (f100 * f100.conj()).sum()) * irfft(f100)

ds6 = ds1 + ds2 + ds5

ds71 = movavg(ds6, 10)

ds72 = movavg(ds6, 100)

ds8 = zeros((t.shape[0], 16))
for i in range(ds8.shape[1]):
	z = 2 * 0.2 * (2 * rand(t.shape[0]) - 1)
	ds8[:,i] = ds1 + ds2 + z

ds91 = ds8[:,:4].mean(1)
ds92 = ds8.mean(1)

figure(figsize=(12, 3))
plot(t, ds1)
plot(t, ds2)
plot(t, ds3)
savefig("ds1-3.png")

figure(figsize=(12, 6))
subplot(2,1,1)
plot(t, ds5)
ylim(-1, 1)
subplot(2,1,2)
plot(t, ds4)
ylim(-1, 1)
savefig("ds4-5.png")

figure(figsize=(12,9))
subplot(3,1,1)
plot(t, ds6)
subplot(3,1,2)
plot(t[:ds71.shape[0]], ds71)
subplot(3,1,3)
plot(t[:ds72.shape[0]], ds72)
savefig("ds6-7.png")

figure(figsize=(12,9))
subplot(3,1,1)
plot(t, ds8[:,0])
subplot(3,1,2)
plot(t, ds91)
subplot(3,1,3)
plot(t, ds92)
savefig("ds8-9.png")
