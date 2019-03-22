import tkinter as tk

root = tk.Tk()

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

root.mainloop()
