# Quin Burke 2019
from tkinter import * as tk

def graph_sum():
  upr_bnd_fld.get()

root = tk.Tk()

hg_mtd = tk.IntVar()
hg_mtd.set(0)

hg_mtds = ["Left", "Right", "Midpoint"]

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

# Interval Width
Label(master, text="Interval Width (dx):").pack()
int_wid_fld = Entry(master)
int_wid_fld.pack()

# Height Generation Method
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
