# Module name:physicscalc
# Short description: Physicscalc (or) Physics Calculator is a package that houses the  functions which can simplify ,solve any problem related to all the various concepts involved in physics and much more...!
# Developers:  Vishal Balaji Sivaraman (@The-SocialLion) 
# Contact email address: vb.sivaraman_official@yahoo.com 
# Modules required:math

# Command to install physicscalc:
# >>> pip install physicscalc

# Essential modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy as sp 
from scipy import interpolate as ie
import math as mt

# speed() - Returns the value of speed using the given parameters
# Syntax: speed(D,T)
# D: Value of Distance , T:Value of time
# Return type: float

def speed(D,T):
  print("Speed",D/T)
  
# relative_error() - Returns the value of relative error using the given parameters
# Syntax: relative_error(M,E)
# M: value of Mean absolute error , E: value of Absolute error
# Return type: float

def relative_error(M,E):
  print("Relative error",M/E)
  
# density() - Returns the value of Density using the given parameters
# Syntax: density(M,V)
# M: value of Mass , V: value of Volume
# Return type: float

def density(M,V):
  print("Density:",M/V)
  
# volume() - Returns the value of volume using the given parameters
# Syntax: volume(L,B,H)
# L: value of Length , B: value of Breadth ,H: value of Height
# Return type: float

def volume(L,B,H):
  print("Volume:",L*B*H)
  
# area() - Returns the value of area using the given parameters
# Syntax: area(L,B)
# L: value of Length , B: value of Breadth 
# Return type: float

def area(L,B):
  print("Area:",L*B)
  
# error_muldiv() - Returns the value of error using the given parameters
# Syntax: error_muldiv(a,b,c,d)
# a: value of del-a , b: value of  del-b ,c: value of a ,d: value of b
# Return type: float 

def error_muldiv(a,b,c,d):
  x=((a/c)+(b/d))
  return x

# error_addsub() - Returns the value of error using the given parameters
# Syntax: error_addsub(a,b)
# a: value of del-a , b: value of  del-b 
# Return type: float 

def error_addsub(a,b):
  p=(a+b)
  return p

# percentage_error() - Returns the value of percentage error using the given parameters
# Syntax: percentage_error(M,E)
# M: value of Mean absolute error , E: value of Absolute error
# Return type: float

def percentage_error(M,E):
  print("Percentage Error:",(M/E)*100,"%")
  
# absolute_error() - Returns the value of absolute error using the given parameters
# Syntax: absolute_error(M,E)
# a: list of error values , n: number of terms 
# Return type: float
  
def absolute_error(a,n):
  if len(a)==n:
    A=np.array(a)
    S=np.sum(A)
    E=S/n
    print("absolute error",E)
  else:
    print("error try again")
    
# meanabsolute_error() - Returns the value of mean absolute error using the given parameters
# Syntax: meanabsolute_error(M,E)
# a: list of error values , n: number of terms 
# Return type: float    
 
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


 

