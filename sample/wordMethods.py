from word import Word

abc=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
words=[]

for chr in abc:
    word=Word(chr,[0,0,0,0,0],0,True)
    words.append(word)

# for i in words:
#     Word.print(i)

def printWords(words):
  for word in words:
    Word.print(word)

german="docs/wordsFive.txt"


def arrayWords(text):
  arrayWords=text.split("\n")
  return arrayWords

fichero = open(german,encoding='ISO-8859-1')
germanWords=arrayWords(fichero.read())

# print(germanWords)



#MIrar bien por si sirve
#Devuelve el numero de veces de un char en un array

# print(germanWords)
#Devuelve el numero de veces de un char en un array
def countCharsArray(char,array):
    count=0
    for word in array:
        if char in word:
            if(len(word)>count):
                count=len(word)
    return count+1
   
#devuelve un char repetido 
def multiChars(char,count):
    charCount=""
    for i in range(0,count):
        charCount+=char
    return charCount
#devuelve un char repetido según el númerod e veces que esté en un array
def charMultipleArray(char,array):
    count=countCharsArray(char,array)
    return multiChars(char,count)
#devuelve un array con los char de un string
def arrayChar(word):
    chars=[]
    for chr in word:
        if chr not in chars:
            chars.append(chr)
        else:
            chars.append(charMultipleArray(chr,chars))           
    return chars

#devuelve un array de array con los chars
def charsGerman(words):
  arrayWords=[]
  for word in words:
    arrayWords.append(arrayChar(word))
  return arrayWords

def dictionaryChars(words):
  arrayWords=charsGerman(words)
  dictionaryGerman={}
  for arrayChars in arrayWords:
    for chrs in arrayChars:
      if(chrs in dictionaryGerman):
        dictionaryGerman[chrs]+=1
      else:
        dictionaryGerman[chrs]=1
  return dictionaryGerman



prueba=['aalst','aalte','aappo','aarau']
print( charMultipleArray('a','aaaalst'))
print(arrayChar('aaaaaalst'))
print(dictionaryChars(germanWords))

