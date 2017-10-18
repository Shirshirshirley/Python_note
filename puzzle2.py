def reverse(text):
  for i in range(len(text)/2):
    a=text[i]
    b=text[len(text)-1-i]
    text[i]=b
    text[len(text)-1-i]=a
  return text


	def reverse(text):
	    word = ""
	    l = len(text) - 1
	    while l >= 0:
	        word = word + text[l]
	        l -= 1
	    return word
