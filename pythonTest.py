numberOfStudents = int(input("please enter the number of students: "))
scores = []
for i in range(numberOfStudents):
	studentScore = int(input("Enter the student's score: "))
	scores.append(studentScore) 
print("The lowest score is: ", min(scores))
print("The average is: ", round(sum(scores)/len(scores)))