##############################################################################################333
#FONKSİYONLAR,KOŞULLAR,DÖNGÜLER,COMPREHENSIONS#####################################
#-Fonksiyonlar(Functions)
#print("a")
#print("a","b")
#print("a","b",sep="__")

def calculate(x):
    print(x*2)

    calculate(5)


def summer(arg1,arg2):



    print(arg1+arg2)
    summer(7,8)
    summer(8,7)
    summer(arg2=8,arg1=7)




"""Parameters
--------------------
arg1:int,float
arg2:int,float

Returns
--------------------
"""

def say_hi():

        print("Merhaba")
        print("hi")
        print("hello")

say_hi()

def say_hi(string):
    print(string)
    print("Hi")
    print("Hello")

say_hi("miuul")


def multiplication(a,b):
    c=a*b
    print(c)

multiplication(10,9)

#girilen değerleri liste içinde saklayacak bir yöntem

list_store=[]
def add_element(a,b):
    c=a*b
    list_store.append(c)
    print(list_store)

    add_element(1,8)
    add_element(18,8)
    add_element(180,10)
##################################################33
#Ön Tanımlı Argümanlar/Parametreler(Default Parameters/Arguments)
##############################################################
def divide(a,b):
    print(a/b)

    divide(1,2)

def divide(a,b=1):
    print(a/b)
    divide(1)

def say_hi(string="Merhaba"):
        print(string)
        print("Hi")
        print("Hello")

say_hi("mrb")

###############################################################################################3
######################Ne Zaman Fonksiyon Yazma İhtiyacımız Olur?###############################
###############################################################################################
#varm,moisture,charge
(56+15)/80
(17+45)/70
(52+45)/80
#DRY

def calculate1(varm,moisture,charge):
    print((varm+moisture)/charge)
    calculate1(98,12,78)

def calc2(varm,moisture,charge):
    return(varm,moisture)/charge
calc2(100,40,60)*12
a=calc2(100,40,60)*1


def calc3(varm,moisture,charge):
    varm=varm*2
    moisture=moisture*2
    charge=charge*2
    output=(varm+moisture)/charge
    return varm,moisture,charge,output

#################################################################################################################
#######################Fonksiyon İçerisinden Fonksiyon Çağırmak##############################################
############################################################################################################
def cal4(varm,moisture,charge):
    return int((varm+moisture)/charge)
cal4(90,12,12)*10


def standardization(a,p):
    return a*10/100*p*p

standardization(45,5)

def all_calculation(varm,moisture,charge,p):
    a=calculate(varm,moisture,charge)
    b=standardization(a,p)
    print(b*10)

    all_calculation(1,3,5,19,12)

def all_calc1(varm,moisture,charge,a,p):
    print(calculate(varm,moisture,charge))
    b=standardization(a,p)
    print(b*10)
    all_calc1(1,3,5,19,12)

list_store=[1,2]
type(list_store)
def add_element(a,b):
    c=a*b
    list_store.append(c)
    print(list_store)
    add_element(1,8)
#-Koşullar(Conditions)
#TRUE-FALSE'U HATIRLAYALIM
1==1
1==2
#If
if 1==1:
    print("something")
 if 1==2:
    print("something")

    number=11
    if number==10:
        print("number is 10")

        number=10
        number=20

    def number_check(number):
        if number==10:
            print("number is 10")

            number_check(12)


def number_check_1(number):
    if number>10:
         print("greater than 10")
    elif number<10:
         print("less than 10")
    else:
         print("equal to 10")

number_check_1(10)

#-Döngüler(Loops)

#for Loop

students=["John","Mark","Venessa","Mariam"]
students[2]
students[1]
students[0]

for student in students:
    print(student)

for student in students:
    print(student.upper())


salaries=[1000,2000,3000,4000,5000]
for salary in salaries:
    print(salary)

for salary in salaries:
    print(salary*20/100+salary)

for salary in salaries:
    print(salary * 30 / 100 + salary)

for salary in salaries:
    print(salary * 50 / 100 + salary)

def new_salary(salary,rate):
    return int(salary*rate/100+salary)

new_salary(1500,10)
new_salary(2000,20)

for salary in salaries:
    print(new_salary(salary,10))

salaries2=[10700,25000,30400,40300,50200]
for salary in salaries2:
    print(new_salary(salary,15))

for salary in salaries:
    if salary>=3000:
        print(new_salary(salary,10))
    else:
        print(new_salary(salary,20))


salaries=[1000,2000,3000,4000,5000]
for salary in salaries:
    if salary==3000:
        break
    print(salary)

for salary in salaries:
    if salary==3000:
        continue
        print(salary)

number=1
while number<5:
    print(number)
    number+=1

    ######################################################################################
    # Enumerate:Otomatik Counter/Indexer ile for loop
    #######################################################################################
    students=["John","Mark","Venessa","Mariam"]
    for student in students:
        print(student)
        A=[]
        B=[]
        for index,student in enumerate(students):
                 if index%2==0:
                      A.append(student)
                 else:
                     B.append(student)
    #UYGULAMA /MÜLAKAT SORUSU:ENUMERATE
    #########################################################################################33
    ########UYGULAMA-MÜLAKAT SORUSU#################################################################
    ###############################################################################################
    #divide_students fonksiyonu yazınız
    #Çift indexte yer alan öğrencileri bir listeye alınız
    #Tek indexte yer alan öğrencileri başka bir listeye alınız.
    #fakat bu iki liste de tek bir liste olarak return olsun.

    students=["John","Mark","Vanessa","Mariam"]

    def divide_students(students):
     groups=[[],[]]
     for index,student in enumerate(students):
             if index%2==0:
                 groups[0].append(student)
             else:
                  groups[1].append(student)
                  print(groups)
                  return  groups
                  st=divide_students(students)
                  st[0]
                  st[1]
##############################################################################################
#Alternating Fonksiyonunun Enumerate İle Yazılması
##############################################################################################
def alternating_with_enumerate(string):
    new_string=" "
    for i,letter in enumerate(string):
        if i%2==0:
                  new_string+=letter.upper()
        else:
             new_string+=letter.lower()
             print(new_string)
    alternating_with_enumerate("hi my name is sibel and i am learning Python")

    ##################################################################################
    #Zip
    #####################################################################################

    students1=["John","Mark","Venessa","Mariam"]
    departments= ["mathematics", "statistics", "physics", "astronomy"]
    ages=[23,30,26,22]

    list(zip(students1,departments,ages))

    ############################################################################
    #lambda,map,filter,reduce
    ############################################################################
    def summer(a,b):
        return a+b
    summer(1,3)*9
    new_sum=lambda a,b:a+b
    new_sum(4,5)


    #map
    salaries=[1000,2000,3000,4000,6000]
    def new_salary(x):
        return x*20/100+x
    new_salary(1000)
    for salary in salaries:
        print(new_salary(salary))
list(map(new_salary,salaries))

#del new_sum
list(map(lambda x:x*20/100+x,salaries))
list(map(lambda x:x**2,salaries))

#Filter
list_store=[1,2,3,4,5,6,7,8,9,10]
list(filter(lambda x:x%2==0,list_store))


#-Comphrehensions