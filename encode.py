alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text,shift):
  newtext1=[]
  for i in range(len(text)):
    for j in range(len(alphabet)):
      if text[i] == alphabet[j]:
            newtext1 += alphabet[j+shift]
  return newtext1


def decrypt(text,shift):
  newtext2=[]
  for i in range(len(text)):
    for j in range(len(alphabet)):
      if text[i] == alphabet[j]:
            newtext2 += alphabet[j-shift]
  return newtext2

#if text == "encode":
print(encrypt(text,shift))
#elif text == "decode":
print(decrypt(text,shift))


