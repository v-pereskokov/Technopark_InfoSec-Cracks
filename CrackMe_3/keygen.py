def gen_serial(username):
	hash = 0x455FAD
	magic = 0x2A47D56
	solt = 1
	ltm = 0x13 # less then 'm'
	mtm = 0x88 # more or equals then 'm'
	middle = 'm'

	for c in username:
		tmp = int(hex(ord(c)), 16) ^ (ltm if c <= middle else mtm)
		tmp = tmp + solt
		tmp = (tmp if c <= middle else tmp - 0xff - 1)
		hash = hash + tmp

	return magic ^ hash

if __name__ == "__main__":
	username = input('Enter Username: ')
	print('Code: ' + str(gen_serial(username)))
