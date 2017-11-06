def gen_serial(username):
	log_10 = 0
	log_14 = 0
	log_15 = 0
	eax = ''
	edx = ''
	ecx = ''

	for c in username:
		hex_symbol = hex(ord(c))
		eax = hex_symbol
		eax = log_15
		eax = eax << 2
		log_10 = log_10 + eax
		eax = hex_symbol
		edx = log_10
		edx = edx - int(eax, 16)
		eax = 0x0fa
		eax = eax ^ edx
		log_10 = eax
		eax = log_15
		eax = eax << 3
		log_14 = log_14 + eax
		eax = hex_symbol
		edx = log_14
		edx = edx - int(eax, 16)
		eax = 0x11
		eax = eax ^ edx
		log_10 = eax
		log_15 = int(hex_symbol, 16)

	eax = log_14
	eax = eax >> 0x1f
	edx = eax
	edx = edx ^ log_14
	edx = edx - eax
	eax = log_10
	eax = eax >> 0x1f
	ecx = eax
	eax = ecx
	eax = eax ^ log_10
	eax = eax - ecx

	return [eax, edx]


if __name__ == "__main__":
	username = input('Enter Username: ')
	code = gen_serial(username)

	print('Code: ' + '{}-{}'.format(code[0], code[1]))
