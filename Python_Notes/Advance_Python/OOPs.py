class Student:
    #blueprint
    Schoolname="Maharashtra school" # class level veriable use when the value is commom for all objects
    def __init__ (self, name, marks, attendance):
        self.name= name
        self.mark= marks
        self.attendance= attendance
    def calculate_grade(self):
        if self.mark >= 90:
            return "A"
        elif self.mark >= 75:
            return "B"
        else:
            return "C"

s1= Student("Rohit",85,92)
s2= Student("Manish",94,96)
print(s1.calculate_grade())
print(s1.name)
print(s2.name)
print(s1.Schoolname)

#1- class is a blueprint, object is a real time data holder
#2 - init runs automatically object
#3- self > refer curret object
#4- instance unique per objects
#5- class veriables > are common/ shared with all objects
#6 - methon inside class > object data own

# Encapsulation




