class student:
    def __init__(self,name,id,contact,branch,year,place):
        self.name=name
        self.id=id
        self.contact=contact
        self.branch=branch
        self.year=year
        self.place=place
    def display(self):
        print("----student details-----")
        print("name:", self.name)
        print("id:", self.id)
        print("contact:", self.contact)
        print("branch:", self.branch)
        print("year:", self.year)
        print("place:", self.place)
s1=student(
    "swetha",
    192319072,
    983748202,
    "bme",
    2023,
    "andhra"
)

s2=student(
    "kavi",
    192319064,
    458288574,
    "bme",
    2023,
    "andhra"
)

s3=student(
    "ramya",
    192319027,
    245781239,
    "bme",
    2023,
    "tirupathi"
)

s1.display()
s2.display()
s3.display()