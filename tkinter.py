import tkinter as tk
from platform import python_version
def main(args):
    root = tk.Tk()
    root.geometry("170x200+30+30")
    l1= tk.Label(root, text="texto superior", bg="red", fg="white").place(x = 30, y = 10, width=120, height=25)
    l2= tk.Label(root, text="texto intermediario", bg="yellow", fg="black").place(x = 10, y = 100, width=150, height=25)
    l3= tk.Label(root, text="texto inferior", bg="green", fg="white").place(x = 20, y = 170, width=170, height=25)

    root.mainloop()
    return 0
if __name__ == '__main__':
    import sys
    print (python_version())
    sys.exit(main(sys.argv))