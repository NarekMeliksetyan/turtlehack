def parse_ranges(ranges):
	res = []
	temp = []
	cnt = 0

	for el in ranges:
		temp += el
		cnt += 1
		if cnt == 15:
			res += [temp]
			temp = []
			cnt = 0

	return res

l = input().split(' ')
res = parse_ranges(l)
print (res)
