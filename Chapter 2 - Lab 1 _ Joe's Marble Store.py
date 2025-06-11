First_Name = input ("Enter your first name: ")
Last_Name = input ("Enter your last name: ")
Number_of_Marbles = int(input ('Enter the number of marbles you ' +
                               'wish to purchase: '))
Single_Marble_Cost = 1.20
Total_Cost = Single_Marble_Cost * Number_of_Marbles

#print() creates a empty line to create empty lines of text
print()
#Next 5 print lines create order confirmation
print (f'Order prepared for {First_Name} ' +
       f'{Last_Name}')
print()
print (f'{Number_of_Marbles} marbles ordered ' +
       f'@ ${Single_Marble_Cost:,.2f}')
print()
print (f'Total cost is ${Total_Cost:,.2f}')
print()
#Prints the number of Marbles that (FIRST + LAST Name) would like.
print (f'{First_Name} {Last_Name} would like ' +
       f'{Number_of_Marbles} marbles at $1.20 per marble ' +
       f'and a total of ${Total_Cost:,.2f}')
