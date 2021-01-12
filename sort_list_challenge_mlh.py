#write code to sort a list

books = ["Pride and Prejudice", 
"The Book Thief", 
"1984",
"A Wrinkle in Time",
"Unbroken",
"Tinker Tailor Soldier Spy",
"Girls in Pants",
"The Hobbit",
"Animal Farm",
"Emma"]

print("\nThis is the list unsorted: "+str(books))

#sort out list alphabetically
books.sort()
print("\nThis is the list sorted alphabetically: "+str(books))

#sort out list descending
books.sort(reverse=True)
print("\nThis is the list sorted in descending order: "+str(books))




