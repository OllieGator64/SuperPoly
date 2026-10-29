class car:
    def __init__(self, color, manufacturer, model, year):
        self.color = color
        self.manufacturer = manufacturer
        self.model = model
        self.year = year

car1 = car("red", "honda", "civc", "2000")
car2 = car("leopard-print", "flints", "stone", "-1000")


class solid:
    def surfaceArea(self):
        return "Undefined"

    def volume(self):
        return "Undefined"

class cube(solid):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def surfaceArea(self):
        return(((self.length * self.width) * (self.length * self.height) * (self.height * self.width)) * 2)

    def volume(self):
        return(self.length * self.width * self.height)

class sphere(solid):
    def __init__(self, radius):
        self.radius = radius

    def surfaceArea(self):
        return (4 * 3.14 * self.radius**2)

    def volume(self):
        return ((4/3) * 3.14 * self.radius**3)

shapes = [cube(2, 3, 5), sphere(5)]
for shape in shapes:
    print("Area: ", shape.surfaceArea())
for shape in shapes:
    print("Volume: ", shape.volume())


class Employee:
    def __init__(self):
        pass

    def describe(self):
        print("I am an employee")

class Manager(Employee):
    def __init__(self):
        pass

    def describe(self):
        super().describe()
        print("I manage a team")

Steve = Manager()
Steve.describe()


class Account:
    def __init__(self, accountNumber, balance):
        self.accountnumber = accountNumber
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber, balance)
        self.interestRate = interestRate

    def displayAccount(self):
        print(self.accountnumber)
        print(self.balance)
        print(self.interestRate)

    def addInterest(self):
        self.balance += (self.balance*self.interestRate)

Acc1 = SavingsAccount(1,2,0.5)
Acc1.displayAccount()
Acc1.addInterest()
Acc1.displayAccount()