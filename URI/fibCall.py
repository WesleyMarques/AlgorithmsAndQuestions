fib = [-1 for i in range(40)]
fib[0],fib[1] = 0,1
call = [-1 for i in range(40)]
call[0],call[1] = 1,1
def fibonacci(x):
	if x in fib:
		print x
		print fib[:5],call[:5]
		return fib[x],call[x]
	else:
		f = fibonacci(x-1)
		s = fibonacci(x-2)
		raw_input()
		fib[x] = f[0]+s[0]
		call[x] = f[1]+s[1]
		print x,f,s
		print fib[:5],call[:5]
		return fib[x],call[x]
	

N = int(raw_input())
for i in range(N):
	x = int(raw_input())
	fibT, calls = fibonacci(x)
	print fibT,calls


