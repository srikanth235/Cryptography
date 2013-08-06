from Crypto.Hash import SHA256
def calculate(b):
    hash = SHA256.new()
    hash.update(b)
    print hash.hexdigest()
    return hash.digest()
f=open("intro")
text=f.read()
blocks = [text[i:min(i+1024,len(text))] for i in range(0,len(text),1024)]
hash=''
for b in reversed(blocks):
      hash=calculate(b+hash)

