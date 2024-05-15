from tkinter import *

root = Tk()
root.geometry("200x300")

valor1_content = DoubleVar()
resultado_content = DoubleVar()
resultado = DoubleVar()

def subtrair(e):
    resultado.set(valor1_content.get() - resultado_content.get())

valor1_content.set(125.55)

lb_valor1 = Label(root, text="Valor 1")
lb_valor1.place(relx=0.1, rely=0.1)
lb_valor1_content = Label(root, text="", textvariable=valor1_content)
lb_valor1_content.place(relx=0.1, rely=0.2)

lb_valor2 = Label(root, text="Insere o valor 2")
lb_valor2.place(relx=0.1, rely=0.3)
valor2_entry = Entry(root, textvariable=resultado_content)
valor2_entry.place(relx=0.1, rely=0.4)
valor2_entry.bind("<KeyRelease>", subtrair)

lb_resultado = Label(root, text="Resultado")
lb_resultado.place(relx=0.1, rely=0.5)
resultado_entry = Label(root, text="", textvariable=resultado)
resultado_entry.place(relx=0.1, rely=0.6)

root.mainloop()