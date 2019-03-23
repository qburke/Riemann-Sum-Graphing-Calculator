# Quin Burke 2019
import Tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def func_parser(f):
    return lambda x : 1/x

def graph_sum():
    global g_frame
    g_frame.destroy()
    g_frame = tk.Frame(root)
    g_frame.pack(side=tk.RIGHT)
    b = int(upr_bnd_fld.get())
    a = int(lwr_bnd_fld.get())
    n = int(sub_int_fld.get())
    f = func_parser(func_fld.get())
  
    x_dscr = np.linspace(a,b,n+1)
    y_dscr = f(x_dscr)
    
    x_cont = np.linspace(a*.875 if a > 0 else a*1.125, b*1.125 if b > 0 else b*.875,100)
    y_cont = f(x_cont)
    
    hg = hg_mtd.get()
    dx = (b-a)/n
    alignment = 'edge'
    method = 'Left'
    if hg == 0: # Left Riemann
        x_dscr = x_dscr[:-1]
        y_dscr = y_dscr[:-1]
    elif hg == 1: # Right Riemann
        x_dscr = x_dscr[1:]
        y_dscr = y_dscr[1:]
        method = "Right"
        dx = -(b-a)/n
    elif hg == 2: # Midpoint
        x_dscr = (x_dscr[:-1] + x_dscr[1:])/2
        y_dscr = f(x_dscr)
        alignment='center'
        method = "Midpoint"

    figure = plt.Figure(figsize=(4,5), dpi=125)
    graph = figure.add_subplot(111)
    graph.plot(x_cont,y_cont,'b')
    graph.plot(x_dscr,y_dscr,'b.',markersize=8)
    graph.bar(x_dscr,y_dscr,width=dx,alpha=0.2,align=alignment,edgecolor='b')
    chart_type = FigureCanvasTkAgg(figure, g_frame)
    chart_type.get_tk_widget().pack(ipadx=50,ipady=200)
    graph.set_title(method + ' Riemann Sum with {} Sub-Intervals'.format(n))

root = tk.Tk()
root.title("Riemann Sum Graphing Calculator")
dash = tk.Frame(root)
dash.pack(side=tk.LEFT)
g_frame = tk.Frame(root)
g_frame.pack(side=tk.RIGHT)

# Function
tk.Label(dash, text="Function:").pack()
func_fld = tk.Entry(dash)
func_fld.pack()

# Lower Bound
tk.Label(dash, text="Lower Bound:").pack()
lwr_bnd_fld = tk.Entry(dash)
lwr_bnd_fld.pack()

# Upper Bound
tk.Label(dash, text="Upper Bound:").pack()
upr_bnd_fld = tk.Entry(dash)
upr_bnd_fld.pack()

# Sub-Intervals
tk.Label(dash, text="Sub-Intervals (n):").pack()
sub_int_fld = tk.Entry(dash)
sub_int_fld.pack()

# Height Generation Method
hg_mtd = tk.IntVar()
hg_mtd.set(0)

hg_mtds = ["Left", "Right", "Midpoint"]

tk.Label(dash,
  text="Select a height generation method:").pack()

for i, mtd in enumerate(hg_mtds):
    tk.Radiobutton(dash,
                   text=mtd,
                   variable=hg_mtd,
                   value=i).pack(anchor=tk.W)

# Graph It! Button
tk.Button(dash, text="Graph It!", command=graph_sum).pack()

# Error field
tk.Label(dash, text="Please enter the required information.").pack()

root.mainloop()
