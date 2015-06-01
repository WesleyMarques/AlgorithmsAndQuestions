#The algorithm search the max longest increasing subsequence of a list

def SSCMax(A,N):
	c = [0 for i in range(N)]
	for m in range(N):
		c[m] = 1
		for i in range(m-1,-1,-1):
			if A[i] <= A[m] and c[i]+1 > c[m]:
				c[m] = c[i]+1
	return c	
