alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
  ans=""
  for i in range(len(text)):
    if text[i] in alphabet:
      y=alphabet.index(text[i])
      if y+shift>25:
        print((y+shift)%26)
        ans=ans+alphabet[(y+shift)%26]
      elif y+shift<26:
        ans=ans+alphabet[y+shift]

  print(ans)
def decrypt(text,shift):
  ans=""
  for i in range(len(text)):
    if text[i] in alphabet:
      y=alphabet.index(text[i])
      if y-shift<0:
        ans=ans+alphabet[26+(y-shift)]
      elif y-shift>=0:
        ans=ans+alphabet[y-(shift)]

  print(ans)
  
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if direction=="encode":
  encrypt(text,shift)
else:
  decrypt(text,shift)

