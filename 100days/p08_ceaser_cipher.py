from p08_module import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
again = input("Type 'yes' if you want to continue program, type 'no' to finish:\n").lower()
len_alpha = len(alphabet)
shift = shift % len_alpha
len_text = len(text)

def in_alpha(letter):
	if letter in alphabet:
		True
	else:
		False

def encrypt(text, shift):
	cipher_text = ""
	for n in range(len_text):
		position = alphabet.index(text[n])
		if position + shift >= len_alpha:
			position -= len_alpha
		cipher_text += alphabet[position + shift]
	print(f"The encoded text is {cipher_text}.")

def decrypt(text, shift):
	plain_text = ""
	for n in range(len_text):
		position = alphabet.index(text[n])
		if position - shift < 0:
			position += len_alpha
		plain_text += alphabet[position - shift]
	print(f"The decoded text is {plain_text}.")

# if direction == "encode":
# 	encrypt(text, shift)
# else:
# 	decrypt(text, shift)

def ceaser(text, shift, direction):
	result = ""
	for n in range(len_text):
		position = alphabet.index(text[n])
		if direction == "encode":
			if position + shift >= len_alpha:
				position -= len_alpha
			result += alphabet[position + shift]
		else:
			if position - shift < 0:
				position += len_alpha
			result += alphabet[position - shift]
	print(f"The {direction}d text is {result}.")

# ceaser(text, shift, direction)

def ceaser2(text, shift, direction):
	result = ""
	if direction == "decode":
		shift *= -1
	for n in range(len_text):
		position = alphabet.index(text[n])
		if position + shift >= len_alpha:
			position -= len_alpha
		result += alphabet[position + shift]
	print(f"The {direction}d text is {result}.")

# ceaser2(text, shift, direction)

def ceaser3(text, shift, direction):
	result = ""
	if direction == "decode":
		shift *= -1
	for char in text:
		if char not in alphabet:
			result += char
		else:
			position = alphabet.index(char)
			if position + shift >= len_alpha:
				position -= len_alpha
			result += alphabet[position + shift]
	print(f"The {direction}d text is {result}.")


ceaser3(text, shift, direction)

while again == "yes":
	direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
	text = input("Type your message:\n").lower()
	shift = int(input("Type the shift number:\n"))
	again = input("Type 'yes' if you want to continue program, type 'no' to finish:\n").lower()
	len_alpha = len(alphabet)
	shift = shift % len_alpha
	len_text = len(text)
	ceaser3(text, shift, direction)

print("Goodbye!")