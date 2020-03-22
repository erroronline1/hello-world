################################################################################
# simplified translation from latin characters to unicode representation of
# circular gallifreyan
# by error on line 1 (erroronline.one)
#
# gallifreyan is based on television series doctor who by bbc
# translation is based on loren shermans alphabet of circular gallifreyan
# http://shermansplanet.com/gallifreyan/guide.pdf
#
# conversion of phonetic c for english only
#
# this only gives impressions of character composing
################################################################################

preset={
#sample presets
	"sample": "coward any day"
}

signs=[
#valid phonemes
	#vowels
	"a", "e", "i", "o", "u",
	#b-stem
	"b", "ch", "d", "g", "h", "f",
	#j-stem
	"j", "ph", "k", "l", "n", "p", "m",
	#t-stem
	"t", "wh", "sh", "r", "v", "w", "s",
	#th-stem
	"th", "gh", "y", "z", "qu", "x", "ng",
	#special
	"c","q"
]

def sign(char):
#circular gallifreyan signs
	#vowels
	if char == "a":
		return "₀"
	elif char == "e":
		return "ѳ"
	elif char == "i":
		return "⫰"
	elif char == "o":
		return "°"
	elif char == "u":
		return "⫯"
	#b-stem
	elif char == "b":
		return "ᘯ"
	elif char == "ch":
		return "ᘯ ∶"
	elif char == "d":
		return "ᘯ ∴"
	elif char == "g":
		return "ᘯ𝄖"
	elif char == "h":
		return "ᘯ𝄗"
	elif char == "f":
		return "ᘯ𝄘"
	#j-stem
	elif char == "j":
		return "⍜"
	elif char == "ph":
		return "⍜ ⋅"
	elif char == "k":
		return "⍜ ∶"
	elif char == "l":
		return "⍜ ∴"
	elif char == "n":
		return "⍜𝄖"
	elif char == "p":
		return "⍜𝄗"
	elif char == "m":
		return "⍜𝄘"
	#t-stem
	elif char == "t":
		return "⁔"
	elif char == "wh":
		return "⁔⋅"
	elif char == "sh":
		return "⁔∶"
	elif char == "r":
		return "⁔∴"
	elif char == "v":
		return "⁔𝄖"
	elif char == "w":
		return "⁔𝄗"
	elif char == "s":
		return "⁔𝄘"
	#th-stem
	elif char == "th":
		return "⦵"
	elif char == "gh":
		return "⦵ ⋅"
	elif char == "y":
		return "⦵ ∶"
	elif char == "z":
		return "⦵ ∴"
	elif char == "qu":
		return "⦵𝄖"
	elif char == "x":
		return "⦵𝄗"
	elif char == "ng":
		return "⦵𝄘"
	#c and q have their representation in names only. they are not used widely and will be replaced mostly.
	elif char == "c":
		return "⍜ ∷",
	elif char == "q":
		return "⦵∷"
	else:
		return False

def characters(sentence):
	# set up array of gallifreyan character groups
	# phonetical correction of c and q according to best practice
	words = sentence.split()
	out = []
	for word in words:
		out.append([])
		pointer = 0
		while pointer < len(word):
			two = word[pointer:pointer+2]
			one = word[pointer:pointer+1]
			if two in signs:
				# phonetic correction of c at the end
				if pointer == len(word)-1 and two == "c":
					two = "k"
				out[-1].append(two)
				pointer += 2
			elif one in signs:
				# phonetic correction of c within words
				if one in ["e","i","y"] and pointer>0 and out[-1][-1] == "c":
					out[-1][-1] = "s"
				elif pointer>0 and out[-1][-1] == "c":
					out[-1][-1] = "k"
				out[-1].append(one)
				pointer += 1
			else:
				raise ValueError('character {0} not processable, translation aborted.'.format(one or two))
		out[-1] = group(out[-1])
	return out

def group(word):
	# group vowels and multiple consonants if suitable 
	place = []
	for i in range(len(word)):
		if ((i>0 and not (word[i] == "a" and word[i-1] in ["t","wh","sh","r","v","w","s"]) and #no "a" grouped to these consonants simply because i do not like that personally
			not (word[i] in ["a","e","i","o","u"] and word[i-1] in ["a","e","i","o","u"] and  word[i] != word[i-1]) and #no grouped different vowels
			(word[i] in ["a","e","i","o","u"] or word[i] == word[i-1]))):
			place[-1].append(word[i])
		else:
			place.append([word[i]])
	return place


print("unicode circular gallifreyan translator\nfor latin characters only and without digits and punctuation.\ngiving you hints on how to combine and draw the letters.\nbypass to sample value by just pressing enter.")
text = input("type single sentence: ")

if text == "":
	text = preset["sample"]

for word in characters(text):
	print (word)
	for group in word:
		for letter in group:
			print (sign(letter), end="")
		print ("   ", end="")
	print ("\n")
