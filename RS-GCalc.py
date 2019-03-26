# Quin Burke 2019
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import parser

# Importing mathematical functions and constants individually for UX
from numpy import sin, cos, tan, arcsin, arccos, arctan, log as ln, log10 as log, e, pi

# Converts user input into a mathematical function
def func_parser(f):
    code = parser.expr(func_fld.get().replace('^','**')).compile()
    return lambda x : eval(code)

def graph_sum():
    # Reset right frame and get input
    global g_frame
    g_frame.destroy()
    g_frame = tk.Frame(root)
    g_frame.pack(side=tk.RIGHT)
    b = int(upr_bnd_fld.get())
    a = int(lwr_bnd_fld.get())
    n = int(sub_int_fld.get())
    f = func_parser(func_fld.get())
  
    # Preps data
    x_dscr = np.linspace(a,b,n+1)
    y_dscr = f(x_dscr)
    
    axis_pad = int((a-b)/8)
    x_cont = np.linspace(a - axis_pad, b + axis_pad, 100)
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

    # Calculates sum and reports it to user
    sum_text.set('Sum = ' + str(sum(map(lambda x : float(x)*abs(dx), y_dscr))))
    
    # Creates figure and sets color
    figure = plt.Figure(figsize=(4,5), dpi=125)
    figure.patch.set_facecolor(WINDOW_BG)
    graph = figure.add_subplot(111)
    graph.set_facecolor(FIELD_BG)
    
    # Plots the function, the height generators, and the rectangle estimations
    graph.plot(x_cont, y_cont, FUNC_CURVE)
    graph.plot(x_dscr, y_dscr, '.b', markersize=8)
    graph.bar(x_dscr, y_dscr, width=dx, alpha=0.2, align=alignment,edgecolor=RECTANGLES)
    chart_type = FigureCanvasTkAgg(figure, g_frame)
    chart_type.get_tk_widget().pack(ipadx=50,ipady=200)
    graph.set_title(method + ' Riemann Sum with {} Sub-Intervals'.format(n))

# Color Constants
LABEL_TEXT = '#191919'
FIELD_TEXT = '#373737'
FIELD_BG = '#FFFAFF'
FUNC_CURVE = '#0A2463'
RECTANGLES = '#3E92CC'
WINDOW_BG = '#E8EBF0'

# Size Constants
FIELD_WIDTH = 40
PADX = 20

# Font Constants
LABEL_FONT=('MS Sans Serif', '14')
INPUT_FONT=('MS Sans Serif', '12')

# Configure Window
root = tk.Tk()
root.title("Riemann Sum Graphing Calculator")
root.geometry('960x540')
root.pack_propagate(0)
root.configure(background=WINDOW_BG)
dash = tk.Frame(root, bg=WINDOW_BG)
dash.pack(side=tk.LEFT)
g_frame = tk.Frame(root)
g_frame.pack(side=tk.RIGHT)

# Function
tk.Label(dash, text="Function (in terms of x):", fg=LABEL_TEXT, bg=WINDOW_BG, font=LABEL_FONT).pack(anchor=tk.W, padx=PADX)
func_fld = tk.Entry(dash, fg=FIELD_TEXT, bg=FIELD_BG, font=INPUT_FONT, width=FIELD_WIDTH, justify='center')
func_fld.pack(anchor=tk.W, padx=PADX)

# Lower Bound
tk.Label(dash, text="Lower Bound:", fg=LABEL_TEXT, bg=WINDOW_BG, font=LABEL_FONT).pack(anchor=tk.W, padx=PADX)
lwr_bnd_fld = tk.Entry(dash, fg=FIELD_TEXT, bg=FIELD_BG, font=INPUT_FONT, width=FIELD_WIDTH, justify='center')
lwr_bnd_fld.pack(anchor=tk.W, padx=PADX)

# Upper Bound
tk.Label(dash, text="Upper Bound:", fg=LABEL_TEXT, bg=WINDOW_BG, font=LABEL_FONT).pack(anchor=tk.W, padx=PADX)
upr_bnd_fld = tk.Entry(dash, fg=FIELD_TEXT, bg=FIELD_BG, font=INPUT_FONT, width=FIELD_WIDTH, justify='center')
upr_bnd_fld.pack(anchor=tk.W, padx=PADX)

# Sub-Intervals
tk.Label(dash, text="Sub-Intervals (n):", fg=LABEL_TEXT, bg=WINDOW_BG, font=LABEL_FONT).pack(anchor=tk.W, padx=PADX)
sub_int_fld = tk.Entry(dash, fg=FIELD_TEXT, bg=FIELD_BG, font=INPUT_FONT, width=FIELD_WIDTH, justify='center')
sub_int_fld.pack(anchor=tk.W, padx=PADX)

# Height Generation Method
hg_mtd = tk.IntVar()
hg_mtd.set(0)

hg_mtds = ["Left", "Right", "Midpoint"]

tk.Label(dash,
  text="Select a height generation method:", fg=LABEL_TEXT, bg=WINDOW_BG, font=LABEL_FONT).pack(anchor=tk.W, padx=PADX)

for i, mtd in enumerate(hg_mtds):
    tk.Radiobutton(dash,
                   text=mtd,
                   variable=hg_mtd,
                   value=i,
                   fg=LABEL_TEXT,
                   bg=WINDOW_BG,
                   font=INPUT_FONT).pack(anchor=tk.W, padx=PADX)

# Graph It! Button
tk.Button(dash, text="Graph It!", command=graph_sum, fg=FIELD_BG, bg=FUNC_CURVE, font=LABEL_FONT, width=int(FIELD_WIDTH/2)+2).pack(pady=25)

# Sum
sum_text = tk.StringVar()
sum_text.set('Sum = ')
sum_field = tk.Label(dash, textvariable=sum_text, fg=RECTANGLES, bg=WINDOW_BG, font=LABEL_FONT)
sum_field.pack(anchor=tk.W, padx=PADX)

# Error field
# tk.Label(dash, text="Please enter the required information.").pack()

root.mainloop()
