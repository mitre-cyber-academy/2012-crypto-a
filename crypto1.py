import base64
import sys

def xor(d, key):
	return ''.join([chr(ord(c) ^ key) for c in d])

if __name__ == "__main__":
	if sys.argv[1] == 'create':
		f = open('crypto1')
		data = f.read()
		f.close()
		out = open('challenge', 'w')
		out.write(base64.b64encode(xor(data, 0xAA)))
		out.close()
	elif sys.argv[1] == 'solve':
		with open('challenge') as f:
			data = f.read()
			data = xor(base64.b64decode(data), 0xAA)
			out = open('solved', 'w')
			out.write(data)
			out.close()	
	
		
