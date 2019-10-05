def get_av(grp):
	summ = 0.0
	res = []

	for lst in grp:
		for el in lst:
			summ += el
		res += [summ / len(lst)]
		summ = 0
	return res

def parse_ranges(tup):
	cnt = 0
	grp = []
	temp = []

	for el in tup:
		if el != 'inf':
			temp += [float(el)]
		cnt += 1
		if cnt == 15:
			cnt = 0
			grp += [temp]
			temp = []
	return get_av(grp)

def main():
	str_in = input()
	res = parse_ranges(str_in)
	for el in res:
		print(el)

main()
