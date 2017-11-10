def gen_serial(username):
	log_10 = 0
	log_14 = 0
	log_15 = 0
	log_16 = 0x88
	log_17 = 0xaa
	eax = 0
	edx = 0
	ecx = 0

	for c in username:
		hex_symbol = hex(ord(c))
		eax = int(hex_symbol, 16)
		eax = log_15
		eax = eax << 3
		log_14 += eax
		edx = int(hex_symbol, 16)
		eax = log_14
		edx = edx + eax
		eax = log_17
		eax = eax ^ edx
		log_10 = eax
		eax = log_15
		eax = eax << 2
		log_10 = log_10 + eax
		edx = int(hex_symbol, 16)
		eax = log_10
		edx = edx + eax
		eax = log_16
		eax = eax ^ edx
		log_10 = eax
		log_14 = log_14 + 0x66
		log_10 = log_10 + 0x0c9
		eax = int(hex_symbol, 16)
		log_15 = int(hex_symbol, 16)

	eax = log_14
	eax = eax >> 0x1f
	edx = eax
	edx = edx ^ log_14
	edx = edx - eax
	eax = log_10
	eax = eax << 0x1f
	ecx = eax
	eax = ecx
	eax = eax ^ log_10
	eax = eax - ecx

	return [eax, edx]


if __name__ == "__main__":
	username = input('Enter Username: ')
	code = gen_serial(username)

	print('Code: ' + '{}-{}'.format(code[0], code[1]))
