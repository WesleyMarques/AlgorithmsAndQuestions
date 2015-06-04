valCustos = []

def maxSum():
    finish = maxC = valCustos[0]
    for x in valCustos[1:]:
        finish = max(x, finish + x)
        maxC = max(maxC, finish)
    return maxC

while True:
	try:
		n = int(raw_input())
	except EOFError:
		break
	c = int(raw_input())
	valCustos = []
	for i in range(n):
		valCustos.append(int(raw_input())-c)
	resu = maxSum()
	if resu < 0:
		print 0
	else:
		print resu