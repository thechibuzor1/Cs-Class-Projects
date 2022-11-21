class BMI:
    def __init__(self, name, age, weight, height):
        self.name = name  # name of the person
        self.age = age  # age
        self.weight = weight  # weight in pounds
        self.height = height  # height in inches

    def getBMI(self):
        self.bmi = ((self.weight) / (self.height)**2) * 703
        return self.bmi

    def getStatus(self):
        val = self.bmi
        if (val < 18.5):
            return "You are Underweight"
        elif (val > 18.5 & val < 24.9):
            return "You are Normal weight"
        elif (val > 24.9 & val < 29.9):
            return "You are Overweight"
        elif (val > 29.9):
            return "You are obese!"


jack = BMI("jack", 15, 225, 90)
print(jack.getStatus())
