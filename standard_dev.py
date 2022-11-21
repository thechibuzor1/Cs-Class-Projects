def standard_deviation(num):
    mean = sum(num) / len(num)  
    numbers = []
    for i in num:
        numbers.append(abs(i-mean))  
    numbersq = []
    for i in numbers:
        numbersq.append(i*i)
    variance = sum(numbersq) / len(num)
    sd = variance ** 0.5
    return sd   
        


num = input("enter the numbers (seperated by space): ")
num_split = num.split()
for i in range(len(num_split)):
    num_split[i] = int(num_split[i])    

print(standard_deviation(num_split))