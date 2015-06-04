listIn = []
k = 0
def solve(i,res,t):
	if len(res) == k:
		return t
	for j in range(len(listIn[i:])):
		if listIn[j] > res[-1]:
			res.append(listIn[j])
			resu = solve(j,res[:],t+1)



while True:
	n,k = map(int,raw_input().split())
	if n == 0 and k == 0:
		break
	listIn = map(int,raw_input().split())
	for i in range(1,len(listIn)):
		solve(i,[listIn[i]],1)
	print listIn,n
	print SSCMax(listIn,n)