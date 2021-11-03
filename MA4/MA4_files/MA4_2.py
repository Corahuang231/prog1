#!/usr/bin/env python3

from integer import Integer
import time
import matplotlib.pyplot as plt
from concurrent.futures import ProcessPoolExecutor
def fib_py(n):
	if n<=1:
		return 1
	else:
	 return (fib_py(n-1)+fib_py(n-2))

def main():
	lst1 = []
	lst2 = []
	lst3 = []
	a = Integer(6)
	print(a.fib())
	f = Integer(47)
	print(f.fib())
	for i in range(30,46):
		tstart1 = time.perf_counter()
		f = Integer(i)
		f.fib()
		tstop1 = time.perf_counter()
		a = tstop1-tstart1
		lst1.append(i)
		lst2.append(a)
		tstart2 = time.perf_counter()
		fib_py(i)
		tstop2 = time.perf_counter()
		b = tstop2-tstart2
		lst3.append(b)
	plt.plot(lst1, lst2,'bo')
	plt.savefig('fibonacci_timingC++')
	plt.plot(lst1, lst3, 'bo')
	plt.savefig('fibonacci_timing_pure python')

if __name__ == '__main__':
	main()
