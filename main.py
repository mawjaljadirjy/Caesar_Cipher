from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
play="yes"
while play=="yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
 
  shift= shift%len(alphabet)
  
  def caeser(text,shift,direction):
    caeser_cipher=[]
    new_text=[]
    if direction=="encode":
      caeser_cipher = alphabet[shift:] + alphabet[:shift]
    elif direction=="decode":
      caeser_cipher = alphabet[-shift:] + alphabet[:-shift]  
    for char in text:
      if char in alphabet:
        text_index=alphabet.index(char)
        new_text.append(caeser_cipher[text_index])
      else:
        new_text.append(char)
    print(f"The {direction}d text is: "+"".join(new_text))     

  caeser(text,shift,direction)
  play=input("Type 'yes' if you want to go again. Otherwise type 'no': ").lower()
else:
  play="no"
  print("Good Bye!")
  
