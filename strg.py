letter =  '''Dear <|NAME|>,
Greetings from ABC Coding house
You Are Selected!
Date = <|Date|>
'''
name = input("Enter your Name\n")
date = input("Enter Date\n")
letter = letter.replace("<|NAME|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)

