from textblob import TextBlob
a = str(input("Enter the word/sentence you want to check: "))
b = TextBlob(a)
print("Corrected text: "+str(b.correct()))
