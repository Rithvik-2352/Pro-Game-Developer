class Employee ():
    def __init__ (self, type, education, age, name, gender, address):
        self.type = type
        self.education= education
        self.age = age
        self.name = name
        self.gender = gender 
        self.adress = address
    def description (self):
        return (f"Type: {self.type}, Education: {self.education}, Age: {self.age}, Name: {self.name}, Gender: {self.gender}, Adress: {self.adress}")
class Developer (Employee):
    def __init__ (self, type, education, age, name, gender, address, prog_lang, salary):
        super() .__init__ (type, education, age, name, gender, address)
        self.prog_lang= prog_lang
        self.salary = salary 
    def description (self):
        Desc = super(). description ()
        print (f"{Desc}, Programming Language: {self.prog_lang}, Salary: {self.salary}")

d1 = Developer ("Developer","MIT", 25, "Bob", "Male", "1228 Smith Dr.", "Python", "$200k")
d1.description ()