import pandas as pd
print(pd.__version__)


from temp import student

a = student("GKS",20)
a.display()




class person:
    def __init__(self,h,w,age):
        self.height = h
        self.weight = w
        self.age = age


class Pankhuri(person):

    def __init__(self,g,name,b,h,w,age):

        super().__init__(h,w,age)
        self.gender=g
        self.name=name
        self.bank_bal = b


obj = Pankhuri("F","kunnu",200000,5,45,22)
print('Gender :',obj.gender)
print('Name :',obj.name)
print('Bank BAlance :$',obj.bank_bal)
print('height :',obj.height)
print('weight :',obj.weight)
print('Age :',obj.age)







def sum(a,b):
  return a+b

print(sum(3,5))


def sum(a,b,c):
  return a+b+c
print(sum(3,8,9))