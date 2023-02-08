
#Python Alıştırmalar
#Görev1:Veri yapılarının tiplerini inceleyiniz.
x=8
type(x)

y=3.2
type(y)

z=8j+18
type(z)

a="Hello World."
type(a)

b=True
type(b)

c=23<22
type(c)

l=[1,2,3,4,"String",3.3,False]
type(l)

d={"Name":"Jake","Age":[27,56],"Address":"Downtown"}
type(d)

t=("Machine Learning","Data Science")
type(t)

s={"Python","Machine Learning","Data Science","Python"}
type(s)

text = "The goal is to turn data into information and information into insights."
text.upper().replace(",", " ").replace(".", " ").split()

lst=["D","A","T","A","S","C","I","E","N","C","E"]
len(lst)

lst[0]
lst[10]

data_list=lst[0:4]
data_list

lst.pop(8)
lst

lst.append(101)
lst

lst.index(8, "N")
lst

dict={'Christian':["America",18],
      'Daisy':["England",12],
      'Antonio':["Spain",22],
      'Dante':["Italy",25]}
dict.keys()
dict.values()
dict.update({"Daisy":["England",13]})
dict

dict["Daisy"][1]=14
dict

dict.update({"Ahmet":["Turkey",24]})
dict

dict.pop("Antonio")
dict


l=[2,13,18,93,22]
    def func(list):
             cift_list=[]
             tek_list=[]
            for i in list:
                if i%2==0:
                         cift_list.append(i)
                 else:
                         tek_list.append(i)
                        return cift_list,tek_list
         cift,tek=func(l)

ogrenciler=["Ali","Veli","Ayse","Talat","Zeynep","Ece"]
for i,x in enumerate(ogrenciler):
    if i<3:
       i+=1
       print("Muhendislik Fakultesi",i,".ogrenci",x)
    else:
       i-=2
    print("Tip Fakultesi",i,".ogrenci",x)

ders_kodu=["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi=[3,4,2,4]
kontenjan=[30,75,150,25]
for ders_kodu,kredi,kontenjan in zip(ders_kodu,kredi,kontenjan):
    print(f"Kredisi{kredi} olan {ders_kodu} kodlu dersin kontenjanı {kontenjan} kişidir.")

kume1=set(["data","python"])
kume2=set(["data","function","qcut","lambda","python","miuul"])
def kume(set1,set2):
    if set1.issuperset(set2):
        print(set1.intersection(set2))
    else:
        print(set2.difference(set1))
    kume(kume1,kume2)
    kume(kume2,kume1)