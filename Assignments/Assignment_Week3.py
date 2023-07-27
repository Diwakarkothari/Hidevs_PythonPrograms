import pickle

#writing to a pickle file
"""mylist=["Ayush","Dev","Diwakar"]
file="demopickle.pkl"
fileobj=open(file,'wb')
pickle.dump(mylist,fileobj)
fileobj.close()

#reading from a pickle file
file="demopickle.pkl"
fileobj=open(file,'rb')
x=pickle.load(fileobj)
print(x)"""

"""file="Problem2.pxl"

class AddressBook:
    def __init__(self):
        self.contacts = set()
        self.fname=list()
        self.lname=list()
        self.street=list()

    def add_contact(self, fname, lname, street_address, city, state, country, mobile, email):
        if email in self.contacts or mobile in self.contacts:
            print("Duplicate Found")
            return

        info = {
            "fname": fname,
            "lname": lname,
            "StreetAddress": street_address,
            "City": city,
            "State": state,
            "Country": country,
            "mobile": mobile,
            "email": email
        }

        self.contacts.add(email)
        self.contacts.add(mobile)

        self.fname.append(fname)
        self.lname.append(lname)
        self.street.append(street_address)

        print("Contact added successfully.")
        return info

    def count(self,fname,lname,street):
        count1=0
        count2=0
        count3=0
        if fname in self.fname:
            count1 +=1
        if lname in self.lname:
            count2 +=1
        if street in self.street:
            count3 +=1
        print(f"occurence of {fname} is {count1}")
        print(f"occurence of {lname} is {count2}")
        print(f"occurence of {street} is {count3}")

    def saving_in_disk(self):
        fileobj=open(file,'wb')
        pickle.dump(self.contacts,fileobj)
        fileobj.close()
        print("data saved successfully")

    def reading_data_from_disk(self):
        o2=open(file,'rb')
        x=pickle.load(o2)
        o2.close()
        return x


fname = input("First Name: ")
lname = input("Last Name: ")
street_address = input("Street Address: ")
city = input("City: ")
state = input("State: ")
country = input("Country: ")
mobile = input("Mobile Number: ")
email = input("Email: ")

x=AddressBook()
y=x.add_contact(fname, lname, street_address, city, state, country, mobile, email)
print(y)
x.saving_in_disk()
z=x.reading_data_from_disk()
print(z)
x.count(fname,lname,street_address)"""


file = "Problem1.pxl"


class Details:
    def __init__(self):
        self.namelist = list()
        self.doblist = list()
        self.info = dict()

    def set_details(self, name, dob):
        self.namelist.append(name)
        self.doblist.append(dob)
        self.info = {
            name: dob
        }
        fileobj = open(file,'wb')
        pickle.dump(self.info, fileobj)
        fileobj.close()

    def get_details(self, name):
        if name=="Secret":
            return name
        else:
            return self.info.get(name)


x = Details()

name = input("Enter name: ")
dob = input("Enter DOB: ")

x.set_details(name, dob)
temp=input("Enter name to fetch DOB: ")
y = x.get_details(temp)
print("DOB-> ",y)





















