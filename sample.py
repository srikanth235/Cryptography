from Crypto.Cipher import AES
from Crypto import Random
from Crypto.Util import Counter
def strxor(a, b):     # xor two strings of different lengths
            if len(a) > len(b):
                 return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
            else:
                 return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])

key= ['140b41b22a29beb4061bda66b6747e14'.decode('hex'), 
'140b41b22a29beb4061bda66b6747e14'.decode('hex'), 
'36f18357be4dbd77f050515c73fcf9f2'.decode('hex'), 
'36f18357be4dbd77f050515c73fcf9f2'.decode('hex')]
text = ['4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'.decode('hex'), 
'5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'.decode('hex'),
'69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'.decode('hex'),
'770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'.decode('hex')
]
for i in range(0,4):
    msg = ''
    iv = text[i][0:16]
    txt = text[i][16:]
    if i < 2:
        cipher = AES.new(key[i], AES.MODE_CBC, iv)
        msg = cipher.decrypt(txt)
    else:
       num_blocks = len(txt)/16 + (0 if len(txt)%16 == 0 else 1)
       for j in range(num_blocks):
         cipher = AES.new(key[i],AES.MODE_ECB, iv)
         block = strxor(cipher.encrypt(iv)[0:len(txt[16*j:16*j+16])], txt[16*j:16*j+16])
         iv = iv.encode('hex')
         print iv,
         iv = iv[:28] + str(hex(int(iv[-4:], 16) + 1))[-4:]
         print iv
         iv = iv.decode('hex')
         msg = msg + block
    print msg
