import art
print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(original_text, shift_amount, encode_or_decode):
  decipher_text = ""
  if encode_or_decode == "decode":
        shift_amount *= -1

  for letter in original_text:
    if letter not in alphabet:
      decipher_text += letter

    else:
      shifting_position = alphabet.index(letter) + shift_amount
      shifting_position %= len(alphabet)
      decipher_text += alphabet[shifting_position]

  print(f"here is your {encode_or_decode}d text: {decipher_text}")

should_continue = True

while should_continue:
  direction =  input("Type 'encode' to  encrypt, Type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  ceasar(original_text = text, shift_amount = shift, encode_or_decode= direction)

  restart = input("Type 'Yes' if you want to go again. Otherwise type 'No' ").lower()
  if restart == "no":
    should_continue = False
    print("Goodbye")