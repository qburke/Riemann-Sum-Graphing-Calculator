from tkinter import * as tk

root = tk.Tk()

hg_mtd = tk.IntVar()
hg_mtd.set(0)

hg_mtds = ["Left", "Right", "Midpoint"]

# function
# upper bound
# lower bound
# n (sub-intervals)
# width of sub-intervals

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

# Graph it! Button
# Error field

# function in math type
# graph of function with rectangles

root.mainloop()
