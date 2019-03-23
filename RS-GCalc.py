# Quin Burke 2019
import Tkinter as tk
import numpy as np
import matplotlib.pyplot as plt

def func_parser(f):
    return lambda x : 1/x

def graph_sum():
    b = int(upr_bnd_fld.get())
    a = int(lwr_bnd_fld.get())
    n = int(sub_int_fld.get())
    f = func_parser(func_fld.get())
  
    x_dscr = np.linspace(a,b,n+1)
    y_dscr = f(x_dscr)
  
    x_cont = np.linspace(a-1,b+1,100)
    y_cont = f(x_cont)
  
    plt.figure(figsize=(15,5))
    plt.plot(x_cont,y_cont,'b')
    hg = hg_mtd.get()
    dx = (b-a)/n
    alignment = 'edge'
    if hg == 0: # Left Riemann
        x_dscr = x_dscr[:-1]
        y_dscr = y_dscr[:-1]
    elif hg == 1: # Right Riemann
        x_dscr = x_dscr[1:]
        y_dscr = y_dscr[1:]
        dx = -(b-a)/n
    elif hg == 2: # Midpoint
        x_dscr = (x_dscr[:-1] + x_dscr[1:])/2
        y_dscr = f(x_dscr)
        alignment='center'
    plt.plot(x_dscr,y_dscr,'b.',markersize=8)
    plt.bar(x_dscr,y_dscr,width=dx,alpha=0.2,align=alignment,edgecolor='b')
    plt.title('Left Riemann Sum with {} Sub-Intervals'.format(n))
    plt.show() # embed in window later
  
root = tk.Tk()

# Function
tk.Label(root, text="Function:").pack()
func_fld = tk.Entry(root)
func_fld.pack()

# Lower Bound
tk.Label(root, text="Lower Bound:").pack()
lwr_bnd_fld = tk.Entry(root)
lwr_bnd_fld.pack()

# Upper Bound
tk.Label(root, text="Upper Bound:").pack()
upr_bnd_fld = tk.Entry(root)
upr_bnd_fld.pack()

# Sub-Intervals
tk.Label(root, text="Sub-Intervals (n):").pack()
sub_int_fld = tk.Entry(root)
sub_int_fld.pack()

# Height Generation Method
hg_mtd = tk.IntVar()
hg_mtd.set(0)

hg_mtds = ["Left", "Right", "Midpoint"]

tk.Label(root,
  text="Select a height generation method:",
  padx=20).pack()

for i, mtd in enumerate(hg_mtds):
    tk.Radiobutton(root,
                   text=mtd,
                   padx=20,
                   variable=hg_mtd,
                   value=i).pack(anchor=tk.W)

# Graph It! Button
tk.Button(root, text="Graph It!", command=graph_sum).pack()

# Error field
tk.Label(root, text="Please enter the required information.").pack()

# function in math type?

# graph of function with rectangles

root.mainloop()
