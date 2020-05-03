#print the variable address
a = 1500
print(id(a))


def update(list):
    print(id(list))

    list[1] = 25
    print(id(list))
    print(list)

list=[10,20,30]
print(id(list))
update(list)

#Pass the argument
#1)Formal Argument
#2)Actual Argument
def person(name,age=18): #formal argument
    print(name)
    print(age)
person("Parth",22) #Acutal Argument,Position
person(age=20,name="Lopy") #Keyword
person(name="Money") #Default






