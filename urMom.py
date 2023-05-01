from tkinter import *
from tkinter import ttk

main = Tk()
main.state("zoomed")
main.title("Yo mama's so fat, when she fell I didn't laugh, but the sidewalk cracked up.")

nb = ttk.Notebook(main)

# TABS
tab1 = Frame(nb)
tab2 = Frame(nb)

# TABS TEXT
nb.add(tab1, text="YO MAMA")
nb.add(tab2, text= "SWAG QUOTES")

nb.pack(fill="both")
mainloop()