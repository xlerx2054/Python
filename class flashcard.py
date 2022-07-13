from lib2to3.pgen2 import driver


class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):
       
        #we will return a string
        return self.word+'('+self.meaning+')'
       
flash = []
print("welcome to flashcard application")
 
#the following loop will be repeated until
#user stops to add the flashcards
while(True):
    word = input("enter the name you want to add to flashcard : ")
    meaning = input("enter the meaning of the word : ")
     
    flash.append(flashcard(word, meaning))
    option = input("Enter yes to continue and no to stop: ")
     
    if(option == 'No' or option == 'no'):
        break
    elif (option == 'Yes' or option == 'yes'):
        continue

# printing all the flashcards
print("\nYour flashcards")
for i in flash:
    print(">>>>", i)



