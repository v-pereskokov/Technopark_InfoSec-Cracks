def gen_serial(username):
	hash = 0x0e8e804
	magic = 0x050cfced
	ltm = 0x13 # less then 'm'
	mtm = 0x18 # more or equals then 'm'
	middle = 'm'

	for c in username:
		tmp = int(hex(ord(c)), 16) ^ (ltm if c <= middle else mtm)
		tmp = tmp + (0x58 if c <= middle else -0x4d)
		tmp = (tmp - 0xff - 1 if tmp >= 0xa0 else tmp)
		hash = hash + tmp

	return magic ^ hash

if __name__ == "__main__":
	username = input('Enter Username: ')
	print('Code: ' + str(gen_serial(username)))
