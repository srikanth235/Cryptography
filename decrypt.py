import binascii
def strxor(a, b):     # xor two strings of different lengths
	    if len(a) > len(b):
		 return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
            else:
		 return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])
def xor():
     f = open('ciphers')
     result = ''
     ciphers = []
     answer = '32510ba9babebbbefd001547a810e67149caee11d945cd7fc81a05e9f85aac650e9052ba6a8cd8257bf14d13e6f0a803b54fde9e77472dbff89d71b57bddef121336cb85ccb8f3315f4b52e301d16e9f52f904'
     answer = binascii.unhexlify(answer)
     for line in enumerate(f):
	 line = (line[0], line[1][:-1])
	 ciphers.append(binascii.unhexlify(line[1]))
	 if not result:
             result = line[1].decode('hex')
	 else:
             result = strxor(result, line[1].decode('hex'))
     for c1 in enumerate(ciphers):
	     for c2 in enumerate(ciphers):
		 if c2[0] > c1[0]:
		     k=strxor('We can factor the number 15 with quantum computers. We can also factor the number 15 with a dog trained to bark three times', strxor(c1[1], c2[1])) 
     print strxor('We can factor the number 15 with quantum computers. We can also factor the number 15 with a dog trained to bark three times', strxor(ciphers[0], answer))
xor()
answer = binascii.unhexlify('6c73d5240a948c86981bc294814d')
print strxor('attack at dusk', strxor(answer, 'attack at dawn')).encode('hex')
print '5'.encode('hex')
print '1'.encode('hex')
print strxor('05','01')
