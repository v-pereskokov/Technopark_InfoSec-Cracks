def gen_serial(username):
	hash = 0x1fca055
	magic = 0x289056d
	solt = 0x4d
	ltm = 0xe2 # less then 'm'
	mtm = 0xa1 # more or equals then 'm'
	middle = 'm'

	for c in username:
		tmp = int(hex(ord(c)), 16) ^ ltm if c <= middle else mtm
		tmp = tmp + solt
		hash = hash + tmp - 0xff - 1

	return magic ^ hash

if __name__ == "__main__":
	username = input('Enter Username: ')
	print('Code: ' + str(gen_serial(username)))
