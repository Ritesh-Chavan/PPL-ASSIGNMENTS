count = 0
num = 2
arr = []
while (count < 10):
	arr_a = []
	arr_b = []
	num2 = 0
	snum = snum2 = 0
	s = 0

	for i in range (1, num):
		if (num % i == 0):
			arr_a.append (i)

	for j in range (0, len (arr_a)):
		snum = snum + arr_a[j]
	
	num2 = snum
	
	for k in range (1, snum):
		if (snum % k == 0):
			arr_b.append (k)

	for l in range (0, len (arr_b)):
		snum2 = snum2 + arr_b[l]

	if (num == snum2 and num2 == snum):
		if (num != num2 and  num not in arr):
			arr.append (num)
			arr.append (num2)
			print (num, num2)
			count = count +1
	num = num + 1
