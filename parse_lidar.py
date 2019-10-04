def get_av(grp):
	summ = 0.0
	res = []

	for lst in grp:
		for el in lst:
			summ += el
		res += [summ / len(lst)]
		summ = 0
	return res

def parse_ranges(str_in):
	st = str_in[1:-1]
	lst = st.split(', ')

	grp = []
	temp = []
	cnt = 0

	for i in range(len(lst)):
		if lst[i] != 'inf':
			temp += [float(lst[i])]
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
