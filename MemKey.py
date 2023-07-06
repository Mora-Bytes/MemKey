try:
	import pyhibp, random
	import string, os
	import platform, sys
	import hashlib

	from pyhibp import pwnedpasswords as pw

	size = 10
	if len(sys.argv) >= 2:
		size = int(sys.argv[1])+2

	user = os.getlogin()
	is_64bits = sys.maxsize > 2**32

	if is_64bits: bit = 'x64'
	else: bit = 'x32'

	del is_64bits

	System = "({0} {1} {2}; {3})".format(platform.system(), os.name, platform.release(), bit)

	Creator = """MoraByte2027"""

	Ver = '0.1'

	agent = "{0} - MemKey/{1} {2}".format(Creator, Ver, System)

	print(agent)

	pyhibp.set_user_agent(ua=agent)

	paswrd = ''
	password = ''
	done = False

	while not done:
		for i in range(random.randint(3, 6)):

			for i in range(random.randint(12,120)):

				randomchar = random.choice(string.punctuation+string.digits+string.ascii_letters)

				paswrd += randomchar

			password += paswrd

		password = int(hashlib.sha224(password.encode(), usedforsecurity=True).hexdigest(),16)
		password = hex(int(hashlib.sha256(str(password).encode(), usedforsecurity=True).hexdigest(),16) + password)[2:size]

		resp = pw.is_password_breached(password=password)
		if not resp:
			print("Password: {0}".format(password))
			done = True
except KeyboardInterrupt: pass
