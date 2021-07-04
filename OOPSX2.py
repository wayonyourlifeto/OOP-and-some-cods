class Human:

    #atribute of class
    name = 'Dmitry,'
    activity = 'programmer'
    age = 18

    #methods
    def HumanBegginnerProgrammer(self):
        print('this is first interview')

    def HumanMiddleProggrammer(self):
        print('1 year expirence')
human_a = Human()
human_b = Human()
human_a.HumanBegginnerProgrammer()
print(human_a.name, 'Years old', human_b.age, 'and his activity', human_b.activity)

#continue
class HumanMiddle:

    #create method of class
    def DmitryMiddleBackend(self, name, activity, age):
        print('After 1 year he will be better for programming')
        self.name = name
        self.activity = activity
        self.age = age

human_a = HumanMiddle()
human_a.DmitryMiddleBackend('Dmitry', 'Backend-Django', '21')
print(human_a.name, 'would like to be a', human_a.activity, 'He already learning')
print('and this age that great opportonuty for learning a programming', human_a.age)

#static method
class HumanMiddle:

    @staticmethod
    def HumanMiddleBackend():
        print('and he is training! he himself believes!')

HumanMiddle.HumanMiddleBackend()

#__init__
class DmitryMiddle:

    #atribute of class
    year_count = 0
    hour_count = 1
    day_count = 6
    #create method of class
    def __init__(self):
        DmitryMiddle.year_count +=1
        print('let\'s count, how many year he can study it', DmitryMiddle.year_count)
        print('And how many hource?', DmitryMiddle.hour_count)
        print('And of course how many day\'s in one week?', DmitryMiddle.day_count)

human_a = DmitryMiddle()

#local and global variable
class DmitryMiddle:

    #atribute of class
    message = 'I say hello you!, you will be better every day!'

    #method of class
    def DmityWantToBeMiddle(self):
        print('I believe, you can do it! I\'m sure!')

human_a = DmitryMiddle()
human_a.DmityWantToBeMiddle()
print('read this -', human_a.message)

#Just its my fantasy
class DmitryWillBeMiddle:

    #method of class with 3 arguments
    def DmitryHaveConfidence(self, words, confidence, warrior):
        print('don\'t, fear, no distractions, the ability what doesn\'t matter truly slide.. -Tyler Durden')
        self.words = words
        self.confidence = confidence
        self.warrior = warrior

human_a = DmitryWillBeMiddle()
human_a.DmitryHaveConfidence('Read this!', 'Believe this!', 'don\'t fear!')
print('First - ', human_a.words, 'second -', human_a.confidence, 'and conclusion -', human_a.warrior)

#continue at 03.07.2021
class TrainYouSelf:

    #atribute of class
    LSD = 'mkg'
    LSD_count = 250

    #method of class
    def LsdMicroDoze(self):
        print('MicroDosing LSD Microdoze LSD can change your mind and worldview')

    def LsdMicroDoze2(self):
        print('and you need cut your mark-LSD, max 20mkg 1 part')

LSD_a = TrainYouSelf()
LSD_b = TrainYouSelf()
LSD_a.LsdMicroDoze()
print('Max doze you need', LSD_a.LSD, 'is', LSD_b.LSD_count)
LSD_b.LsdMicroDoze2()

#example code of OOP
class Employee:
    'Common base class for all employees'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print('Total Employee %d' % Employee.empCount)

    def displayEmployee(self):
        print('Name :', self.name, ', Salary :', self.salary)

emp1 = Employee('Maria', 2000)
"This would create first object of Employee class"
emp2 = Employee('Max', 5000)
"This would create second object of Employee class"
emp1.displayEmployee()
emp2.displayEmployee()
print('Total Employee %d' %Employee.empCount)

#built-in class attributes of class Employee:
print("Employee.__doc__", Employee.__doc__)
print("Employee.__name__", Employee.__name__)
print("Employee.__module__", Employee.__module__)
print("Employee.__bases__", Employee.__bases__)
print("Employee.__dict__", Employee.__dict__)

#Parent and child class
class Parent:
    ParentAttr = 100

    #method
    def __init__(self, ):
        print('its __init__ method')

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print('Parent attribute :', Parent.parentAttr)

#Child class - Parent
class Child(Parent):

    def childMethod(self):
        print('Calling child construction')

c = Child()
c.childMethod()
c.parentMethod()
c.setAttr(2000)
c.getAttr()

#next
class Tyler:

    def __init__(self, wasted, life, freedom):
        self.first = wasted
        self.second = life
        self.next = freedom
        print('are you wasting your life?')
f1 = Tyler('What are you asking yourself?', 'What matter for you?', 'are you know about it?')
print(f1.first, ': I told myself, what i want for my life?')
print (f1.second, ': And everyday i ask what is matter for me?')
print(f1.next, ': if you do it, what you really want, you are not wasting you life.')

#again it my classes
class MySelf:
    def FreeMy(self, answer):
        print('i do it, and my idea created me.')
        self.answer = answer

class MySelftwo(MySelf):
    def FreeMytwo(self, answertwo):
        print('i think its doesn\'t matter anything.')
        self.answertwo = answertwo

class MySelfthree(MySelftwo):
    def FreeMythree(self, answerthree):
        print('What will I regret when i die?')
        self.answerthree = answerthree

class YourSelf(MySelfthree):
    def __init__(self, matter, ability, foryou):
        print('So many arguments told me, you will become a freedom, if you do not distraction')
        self.first = matter
        self.second = ability
        self.three = foryou

f1 = MySelftwo()
f1.FreeMy('it is good')
print(f1.FreeMy, ': Yes, i feel good')
f1.FreeMytwo('Are you know what you need to do?')
print(f1.answertwo, ': Yes i know')
f2 = MySelfthree()
f2.FreeMythree('And are you going to do it?')
print(f2.answerthree, ': Yes, I\'m')
f3 = YourSelf('You know', 'You are have got ability', 'And you know what you need')
print(f3.first, ': These are the questions that destroy me ')
print(f3.second, ': my ability is what I can what is don\'t matter for me truly slide.')
print(f3.three, ': I know what need')
