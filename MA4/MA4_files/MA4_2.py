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
	f = Integer(5)
	print(f.fib())
	for i in range(10,16):
		tstart1 = time.perf_counter()
		executor = ProcessPoolExecutor(max_workers=5)
		executor.submit(fib_py, i)
		tstop1 = time.perf_counter()
		a = tstop1-tstart1
		lst1.append(i)
		lst2.append(a)
	plt.plot(lst1, lst2,'bo')
	plt.savefig('fibonacci_timing2')
	plt.show()

if __name__ == '__main__':
	main()
