#MoraByte2027 - MemKey/0.2 (Windows nt 10; x64)

try:
	import pyhibp, random
	import string, os
	import platform, sys
	import hashlib, re

	from pyhibp import pwnedpasswords as pw

	size = 10
	if len(sys.argv) >= 2:
		size = int(sys.argv[1])+2
		if size <= 2:
			size = 6

	time = 0

	user      = os.getlogin()
	is_64bits = sys.maxsize > 2**32

	if is_64bits: bit = 'x64'
	else: bit = 'x32'

	del is_64bits

	System = "({0} {1} {2}; {3})".format(platform.system(), os.name, platform.release(), bit)

	Creator = """MoraByte2027"""

	Ver = '0.2'

	agent = "{0} - MemKey/{1} {2}".format(Creator, Ver, System)

	print(agent)

	pyhibp.set_user_agent(ua=agent)

	paswrd   = ''
	password = ''
	done     = False

	while not done:
		for i in range(random.randint(3, 6)):

			for i in range(random.randint(12,120)):

				randomchar = random.choice(string.punctuation+string.digits+string.ascii_letters)

				paswrd += randomchar

			password += paswrd

		password = int(hashlib.sha224(password.encode(), usedforsecurity=True).hexdigest(),16)
		password = hex(int(hashlib.sha256(str(password).encode(), usedforsecurity=True).hexdigest(),16) + password)[2:size]

		resp = pw.is_password_breached(password=password)
		ok   = not ((re.search(r"[a-z]", password) is None) or (re.search(r"\d", password) is None) or (len(password) <= 11))
		if ok and not resp:
			print("Password: {0} (Strong)".format(password))
			done = True
		elif not resp:
			print("Password: {0} (Weak)".format(password))
			done = True
		else:
			time += 1
		if time >= 75: raise TimeoutError('Please up the Password Length.')
except KeyboardInterrupt: pass
