
from queue import Queue
import random
import time

class emp:
    def __init__(self,name,level):
        self.name=name
        self.level=level
        self.available=True


class Call:
    def __init__(self,x,y):
        self.id=x
        self.duration=y


class CallCenter:
    def __init__(self):
        self.Operator=Queue(maxsize=3)
        self.Supervisor=Queue(maxsize=2)
        self.Manager=Queue(maxsize=1)
        self.calls={}

    def add_operator(self,a):
        self.Operator.put(a)

    def add_supervisor(self,a):
        self.Supervisor.put(a)

    def add_manager(self,a):
        self.Manager.put(a)

    def process_calls(self,t):
        print("CALL STARTED")
        time.sleep(t)
        print("CALL ENDED")

    def display_summary(self,i):
        print("\nCall Summary ->")
        print("ID : " ,i ,"   ", "Duration(in seconds) : " ,self.calls[i],"\n")

emp1=emp("Diwakar1","operator")
emp2=emp("Diwakar2","operator")
emp3=emp("Diwakar3","operator")
emp4=emp("Diwakar4","supervisor")
emp5=emp("Diwakar5","supervisor")
emp6=emp("Diwakar6","manager")

x=CallCenter()
x.add_operator(emp1)
x.add_operator(emp2)
x.add_operator(emp3)
x.add_supervisor(emp4)
x.add_supervisor(emp5)
x.add_manager(emp6)
f = 1
temp = 100

while 1:
    print("Enter 1 to make a call \nEnter any other to exit")
    choice=input()
    if choice=='1':
        temp += 1

        if (emp1.available == False and emp2.available == False and emp3.available == False and
                emp4.available == False and emp5.available == False and emp6.available == False):
            print("No one available for picking up calls \nPLEASE TRY AFTER SOME TIME")
            exit(1)

        z = random.randint(1, 9)

        y=Call(temp,z)
        x.calls.update({y.id:y.duration})

        emp_no = "emp" + str(f)
        f+=1
        if f>6:
            f=1
        match(emp_no):
            case "emp1":
                emp1.available = False
                x.process_calls(z)
                emp1.available = True
                x.display_summary(y.id)
            case "emp2":
                emp2.available = False
                x.process_calls(z)
                emp2.available = True
                x.display_summary(y.id)
            case "emp3":
                emp3.available = False
                x.process_calls(z)
                emp3.available = True
                x.display_summary(y.id)
            case "emp4":
                emp4.available = False
                x.process_calls(z)
                emp4.available = True
                x.display_summary(y.id)
            case "emp5":
                emp5.available = False
                x.process_calls(z)
                emp5.available = True
                x.display_summary(y.id)
            case "emp6":
                emp6.available = False
                x.process_calls(z)
                emp6.available = True
                x.display_summary(y.id)


    else:
        print("All calls that were made (in the form of { ID : duration(in seconds) }) are->")
        print(x.calls)
        exit(1)