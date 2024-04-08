library = []
book = input('Enter the name of a book you own: \n')
library.append(book)
book = input("Enter the name of another book you own (or press 'Enter' to skip): \n")
if book:
    library.append(book)
print(f'Your Library: {library}')

wishlist = []
book = input('Enter the name of a book you wish to have in the future: \n')
wishlist.append(book)
book = input('Enter the name of another book you wish to have (or press "Enter" to skip): \n')
if book:
    wishlist.append(book)
print(f'Your Wishlist: {wishlist}')

acquired = []
book = input("Enter the name of a book from your Wishlist that you've acquired (or press 'Enter' to skip):\n")
acquired.append(book)
if book in wishlist:
    wishlist.remove(book)
    library.append(book)
print(f"Updated library: {library}")
print(f"Updated wishlist: {wishlist}")

donate = []
book = input("Enter the name of a book from your library you wish to donate (or press 'Enter' to skip):\n")
donate.append(book) 
if book in library:
    library.remove(book)
print(f"Finally, library after Donations: {library}")
