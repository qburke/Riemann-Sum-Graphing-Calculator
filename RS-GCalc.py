# Quin Burke 2019
from tkinter import * as tk
import numpy as np
import matplotlib.pyplot as plt

def func_parser(f):
  return lambda x : x

def graph_sum():
  b = int(upr_bnd_fld.get())
  a = int(lwr_bnd_fld.get())
  n = int(sub_int_fld.get())
  f = func_parser(func_fld.get())
  
  x = np.linspace(a,b,n+1)
  y = f(x)
  
  X = np.linspace(a,b,100)
  Y = f(X)
  
  plt.figure(figsize=(15,5))
  plt.plot(X,Y,'b')
  if hg_mtd == 0: # Left Riemann
    x = x[:-1]
    y = y[:-1]
  elif hg_mtd == 1: # Right Riemann
    x = x[1:]
    y = y[1:]
  elif hg_mtd == 2: # Midpoint
    x = (x[:-1] + x[1:])/2
    y = f(x_mid)
  plt.plot(x,y,'b.',markersize=8)
  plt.bar(x,y,width=(b-a)/N,alpha=0.2,align='edge',edgecolor='b')
  plt.title('Left Riemann Sum with {} Sub-Intervals'.format(n))
  plt.show() # embed in window later
  
root = tk.Tk()

# Function
Label(master, text="Function:").pack()
func_fld = Entry(master)
func_fld.pack()

# Upper Bound
Label(master, text="Upper Bound:").pack()
upr_bnd_fld = Entry(master)
upr_bnd_fld.pack()

# Lower Bound
Label(master, text="Lower Bound:").pack()
lwr_bnd_fld = Entry(master)
lwr_bnd_fld.pack()

# Sub-Intervals
Label(master, text="Sub-Intervals (n):").pack()
sub_int_fld = Entry(master)
sub_int_fld.pack()

# Height Generation Method
hg_mtd = tk.IntVar()
hg_mtd.set(0)

hg_mtds = ["Left", "Right", "Midpoint"]

tk.Label(root,
  text="Select a height generation method:",
  justfiy=tk.LEFT,
  padx=20).pack()

for i, mtd in enumerate(hg_mtds):
  tk.Radiobutton(root,
    text=mtd,
    padx=20
    variable=hg_mtd,
    value=i).pack(anchor=tk.W)

# Graph It! Button
Button(master, text="Graph It!", command=graph_sum).grid(row=3, column=1, sticky=W, pady=4)

# Error field
Label(master, text="Please enter the required information.").pack()

# function in math type?

# graph of function with rectangles

root.mainloop()


# Note: pyinstaller to make exe
