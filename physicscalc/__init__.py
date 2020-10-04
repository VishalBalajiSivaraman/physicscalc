# Module name:electronicscalc
# Short description: Physicscalc (or) Physics Calculator is a package that houses the  functions which can simplify ,solve any problem related to all the various concepts involved in physics and much more...!
# Developers:  Vishal Balaji Sivaraman (@The-SocialLion) 
# Contact email address: vb.sivaraman_official@yahoo.com 
# Modules required:math

# Command to install electronics-calc:
# >>> pip install physicscalc

# Essential modules
import math as mt
import numpy as np
import vectoralg as vg

def relative_error(M,E):
  print("Relative error")
  return M/E

def area(L,B):
  print("Area:",L*B)
  

def error_muldiv(a,b,c,d):
  x=((a/c)+(b/d))
  return x

def error_addsub(a,b):
  p=(a+b)
  return p

def percentage_error(M,E):
  print("Percentage Error:",(M/E)*100,"%")

def absolute_error(a,n):
  if len(a)==n:
    A=np.array(a)
    S=np.sum(A)
    E=S/n
    print("absolute error",E)
  else:
    print("error try again")



def meanabsolute_error(a,n):
  if(len(a)==n):
    b=[]
    for i in a:
      b.append(abs(i))
    A=np.array(b)
    S=np.sum(A)
    M=S/n
    print("mean absolute error",M)
  else:
    print("error try again")


 

