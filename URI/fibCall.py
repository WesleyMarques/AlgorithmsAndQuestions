
fibs = {0:0, 1:1}
calls = {0:1, 1:1}

fib = [-1 for i in range(45)]
fib[0],fib[1] = 0,1
call = [-1 for i in range(45)]
call[0],call[1] = 1,1

def fibo(num):
	if num in fibs:
		return fibs[num], calls[num]
	else:
		first = fibo(num-1)
		second = fibo(num-2)
		fibs[num] = first[0] + second[0]
		calls[num] =  first[1] + second[1] +1
		return fibs[num], calls[num]

def fibonacci(x):
	if fib[x] != -1:
		return fib[x],call[x]
	else:
		f = fibonacci(x-1)
		s = fibonacci(x-2)
		fib[x] = f[0]+s[0]
		call[x] = f[1]+s[1]+1
		return fib[x],call[x]

for a in range(40):
	print a
	fibT, callsf = fibonacci(a)
	fibr, callr  = fibo(a)
	if fibT != fibr or callr != callsf:
		print "erro:",a,fibT,fibr,callsf,callr
		break



