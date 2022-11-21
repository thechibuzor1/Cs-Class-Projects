""" SUMMARY: HEXADECIMAL CONVERTER 
        CSC212
        NAME: IGBUDU CHIBUZOR MOSES
        MATRIC NO.: 210805501 """


num = int(input("ENTER THE DECIMAL NUMBER: ")) #user inputs the decimal number
sum = "" #an empty string to collect the calcuations
while (num != 0): #while looop
    d = num % 16 #get the remainder after every iteration of the loop
    if d == 10: 
        d = "A"
    if d == 11:
        d = "B"
    if d == 12:
        d = "C"
    if d == 13:
        d = "D"
    if d == 14:
        d = "E"
    if d == 15:
        d = "F"
        
    sum += str(d) #add the remainder to the empty string
    num = int(num/16) #get the next number to divide by 16
    
print(sum[::-1])#print the string reversed