# decorators
# def amar(f1):
#     def exe():
#         print("exe")
#         f1()
#         print("re")
#     return exe
# @amar ## didi=amar(didi)
# def didi():
#     print("hii")
# didi()
#lambda
# a=3
# b=4
# x=lambda a,b:a+b
# print(x(a,b))
############################# oops ##############################
#classes constructors
# class employe:
#     no_of_leaves=9
#     var=10
#     def __init__(self,aname,asalary):
#         self.name=aname
#         self.salary=asalary
    
#     #self
#     def pntdetails(self):
    
#         return f"name is {self.name}\nsalary is {self.salary}"
#     ##dunder methods
#     def __add__(self,other):
#         return self.salary +other.salary
#     def __truediv__(self,other):
#         return self.salary/other.salary
#     #classmethods
#     @classmethod
#     def chnge_leaves(cls,newleaves):
#         cls.no_of_leaves=newleaves
#     #alternative classmethods
#     @classmethod
#     def frm_arrow(cls,str):
     
#         return cls(*str.split('>')) #kwargs and #args
#     @staticmethod
#     def stats():
#         # print("hii")       
# # amar=employe("amar",333)
# # snehal=employe("snehal",444)
# # amar.chnge_leaves(34)
# # print(amar + snehal)
# # print(amar / snehal)
# # print(snehal.salary)
# # print(amar.no_of_leaves)

# ##static method
# employe.stats()
##single inheritance
# class hod(employe):
    
    
#     def __init__(self,aname,asalary,hobbies):
#         self.name=aname
#         self.salary=asalary
#         self.hobbies=hobbies
#     def printprog(self):
#         return f"the hod name is {self.name} salary is {self.salary} and hobbies are {self.hobbies}"
# karan=hod("karan",66666,["computer"])

# #print(karan.printprog())
# class coach:
#     var=9
#     def __init__(self,name,nme_of_coaching):
#         self.name=name
        
#         self.name_of_coaching=nme_of_coaching
#     def pntdetail(self):
#         return f"the hod name is {self.name}  coaching names are {self.name_of_coaching}"
#     def __repr__(self):
#         return f"coach('{self.name}' ,'{self.name_of_coaching}')"
# #multiple inheritance      
# class coolguy(coach,employe):
#     pass

# karana=coach("karn",["allen"])
# # print(karana)
# # print(rohan.pntdetail())
# # print(amar.pntdetails())
# # print(coolguy.var)
# ###abstract method
# from abc import ABC,abstractmethod
# class nm(ABC):
#     @abstractmethod
#     def printcube(self):
#         return 0
# class no:
#     type="number"
#     def __init__(self):
#         self.no=5

#     def printcube(self):
#         return f"CUBE IS {self.no**3} AND SQUARE IS {self.no**2} "
# a=no()
# # print(a.printcube())
# class students:
#     def __init__(self,fnme,lnme):
#         self.fname=fnme
#         self.lname=lnme
#         #self.email=f"{fnme}{lnme}@gmail.com"
#     def dir(self):
#         return f"these students is {self.fname}  {self.lname}"
#     @property
#     def gmail(self):
#         if self.fname==None or self.lname==None:
#             return "email invalid "
#         return f"u r email is {self.fname}_{self.lname}@gmail.com"
#     @gmail.setter
#     def gmail(self,str):
#         x=str.split("@")[0]
#         self.fname=x.split("_")[0]
#         self.lname=x.split("_")[1]
#     @gmail.deleter
#     def gmail(self):
#         self.fname=None
#         self.lname=None
    
# gurav=students("gurav","deshpande")
# garyy=students("garry","stokes")
# gurav.fname='Soumya'
# gurav.gmail="amar_khamkar@gmail.com"
# # print(gurav.fname)
# # print(gurav.gmail)
# del gurav.gmail
# # print(gurav.gmail)
# import inspect
# # print(inspect.getmembers(gurav))
# ###genrators
# f=1
# def gen(n):
#     for i in range(1,n):
#         yield i
# g=gen(5)
# for i in  g:
#     f=f*i
# # print(f)
# ###comprehensions
# dict1={i:f"item {i}" for i in range(100,1000) if i%100==0}
# dict2={value:key for key,value in dict1.items()}

# # print(dict1 , "\n",dict2)
# ##set comprehensions
# clothes={dress for dress in['dress1',"dress2",'dress2','dress1']}#set value do not return repeated values
#print(clothes)
# ##function cache
# import time
# from functools import lru_cache
# @lru_cache(maxsize=4)#saves last 4 values
# def imp_work(n):
#     time.sleep(n) 
#     return n
# if __name__ == "__main__":
#     print("we")
#     imp_work(3)
#     imp_work(5)
#     imp_work(2)
#     imp_work(1)
#     print("done..calling again")
#     imp_work(3)#so it wont take these time which already saved
#     print("done")  
# ###coroutine ->will take 4 s after first call then it ll run instantly
# import time
# def searcher():
#     book="hi these is amar"
#     time.sleep(4)
#     while True:
#         text=(yield)
#         if text in book:
#             print('text is in the book')
#         else:
#             print('text is not in the book')
# search=searcher()
# next(search)
# search.send("hi")
# input("press any key")
# search.send('these')
# input("press any key")
# search.send('not')
###os module
# import os
# print(os.getcwd())
# os.chdir("c://")
# print(os.getcwd())
# f=open("water.py")
# print(os.listdir("C:\Users\HP\Downloads\imgs\gallery\flappy"))
# os.mkdir("amruta")
# os.makedirs('amruta/amar')
# os.rename("main.py" , "od.py")
# print(os.path.join("c:/","main.py"))  
# print(os.path.exists("c://"))
# path=str(input()))
# file=str(input())
# format=str(input())
# i=1

    
# for root,dirs,files in os.walk("C:\\Users\\HP\\Downloads\\imgs\\gallery\\flappy"):
#     for filename in files:
#         if filename[0].lower():

#             os.rename(filename,f"{i}.{filename[0].upper()}{filename[1:100]}")
#             # print(filename[1:100],end="")
#         # else:
#         #     print(f"{i}.{filename}")



    
        
#         # print(i,filename)
#         i+=1
# import requests
# x={'sms':2,'mms':3}
# r=requests.get("https://xkcd.com/1906/",params=x)
# print(r.text)          
# print(r.url)
# print(r.status_code)
# print(r.headers("content-type"))
# import jsons
# data='{"v1":"amae","v2":"snehal"}'
# parsed=jsons.loads(data)
# print(parsed["v1"])
# data1={
#         'a':'A',
#         'fruits':['apple','msngo']
# }
# toocnrtjavas=json.dumps(data1)
# print(toocnrtjavas)



# from newsapi import NewsApiClient

# # Init
# newsapi = NewsApiClient(api_key='1e632e3030644ce1a3e8079a317afd5c')

# # /v2/top-headlines
# top_headlines = newsapi.get_top_headlines(q='covid-19',
#                                         #   sources='google-news',
#                                           category='health',
#                                           language='en',
#                                           country='in')

# # /v2/everything
# all_articles = newsapi.get_everything(q='covid-19',
#                                       sources='google-news',
#                                       domains='news.google.com',
#                                       from_param='2020-06-05',
#                                       to='2020-06-16',
#                                       language='en',
#                                       sort_by='relevancy',
#                                       page=2)


# # /v2/top-headlines

# # /v2/sources
# sources = newsapi.get_sources()
# # def speak(str):
# #     from win32com.client import Dispatch
# #     speak=Dispatch("SAPI.spvoice")
# #     speak.Speak(str)
# # speak()
# import pickle
# # lst=['amar','didi','deep']
# # fiel='meandmy_friends.pkl'
# # fiob=open(fiel,'wb')
# # pickle.dump(lst,fiob)
# # fiob.close()
# file="meandmy_friends.pkl"
# fbo=open(file,"rb")
# lst=pickle.load(fbo)
# print(lst)
# import re
# str="hi i am amr i am in 2nd yr my no is 91-9930201171 and my emails are amarkhamkar6@gmail.com and amar1@gmail.com"
# # a=str.split('.com')
# print (a)

# pt=re.compile(r'@gmail.com')
# pt=re.compile(r".1171")
# pt=re.compile(r"^hi")
# pt=re.compile(r"1171$")
# # pt=re.compile(r"a{1}")

# pt=re.split(".com",str)
# print(pt)
# pt=re.compile(r"\d{2}-\d{10}")
# matches=pt.finditer(str)
# for match in  matches:
#     print(match) 
# import amarr
# a=input("name")
# b=input("how much do u earn")
# if int(b)==0:
#     raise ZeroDivisionError("b is 0 stopping the program")
# if a.isnumeric():
#     raise Exception ("nos are not allowed")
# print(f"hello {a}")
# try:
#     print(d)
# except Exception as e:
#     if a=='amar':
    
    
#         raise ValueError('AMAR IS BLOCKED')
#     if i
#     print("varible is notn defined")
# import module_does_not_exist
##command line utlity
# import argparse 
# import sys
# def calc(args):
#     if args.o=="add":
#         return args.x +args.y
#     if args.o=="mul":
#         return args.x *args.y
#     if args.o=="div":
#         return args.x /args.y
#     else:
#         return "invalid entry"
# if __name__ == "__main__":
#     parser=argparse.ArgumentParser()
#     parser.add_argument('--x',type=float,defaults=1.0,
    
#                         help="enter first no.please contact amr")
#     parser.add_argument('--y',type=float,defaults=3.0,
    
#                         help="enter second no please contact amr")
#     parser.add_argument('--o',type=str,defaults=add,
    
#                         help="enter second no please contact amr")
#     args=parser.parse_args()
#     sys.stdout.write(str(calc(args)))
###TO MAKE OUR MODULE/package
# from setuptools import setup
# setup(name="maar",
# version="0.1",
# description="this is",
# Long_description="long description",
# authot="amar",
# packages['maar']
# install_requires=[])
# n=str(input("in which yr u born/what is ur age"))

# # l=str(input("give us a no after we can te

# x=len(n)
# if x>=4:
#     print("after 100 yrs u  r in the yr",int(n)+100)
# # l=str(input("give us a no after we can tell u "))
# # if l:
# #     print("after n of yrs ur in the year",int(n)+int(l))
# if x<3:
#     print(f" after 100 yrs u r in year {-int(n)+2020+100} ")
# n=int(input("how many apples harry got? "))
# mn=int(input('enter the minimum range'))
# mx=int(input('enter the maximum range'))
# for i in range(mn,mx+1):
#     if n%i==0:
#         print(f"{i} is a divisor of {n}")
#     else:
        
#         print(f"{i} is not a divisor of {n}")
# n=str(input("enter u r random no ?i can tell u the next pallindrome no"))
# print(n[::-1])

# for i in range(1,6):
#     n=str(input("enter u r random no ?i can tell u the next pallindrome no"))

    
#     x=n[::-1]
#     if n==x:
#         print('the no that u have enter itself a palindrome try next one')
#     if n!=x:
#         while 1:
#             y=int(n)
            
#             x=str(y)[::-1]
#             if x==str(y):
#                 print('this is ur next pallindrome')
#                 break
#             else:
#                 y+=1
#     i+=1
    
import pygame
pygame.init()
win=pygame.display.set_mode((200,200))
black=[255,255,255]
    




