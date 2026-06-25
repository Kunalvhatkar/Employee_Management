class Employee:

    def __init__(self,name,email,department,salary):

        self.name=name

        self.email=email

        self.department=department

        self.salary=salary

    def to_dict(self):

        return {

            "name":self.name,

            "email":self.email,

            "department":self.department,

            "salary":self.salary

        }