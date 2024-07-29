import tkinter as tk
from tkinter import font

# Insere os valores clicados
def insert_text(value, event=None):
    resp.insert(tk.END, value)

# Calcula
def calc(event=None):
    try:
        # Pegando o conteúdo da caixa de texto
        text = resp.get("1.0", tk.END).strip()
        # Avaliando a expressão
        result = eval(text)
        # Limpando a caixa de texto e inserindo o resultado
        resp.delete("1.0", tk.END)
        resp.insert(tk.END, str(result))
    except Exception as e:
        resp.delete("1.0", tk.END)
        resp.insert(tk.END, "Error")

# Negativa o valor
def trocaSinal():
    try:
        # Pegando o conteúdo da caixa de texto
        text = resp.get("1.0", tk.END).strip()
        if text:
            # Verifica se o número é negativo
            if text.startswith('-('):
                # Remove o sinal de menos
                text = text[2:3]
            else:
                # Adiciona o sinal de menos
                text = '-(' + text + ')'
            # Limpando a caixa de texto e inserindo o novo valor
            resp.delete("1.0", tk.END)
            resp.insert(tk.END, text)
    except Exception as e:
        resp.delete("1.0", tk.END)
        resp.insert(tk.END, "Error")

# Configura as entradas da janela
wws = tk.Tk()
wws.title("Calculator")
wws.geometry("400x450+200+250")
wws.resizable(False, False)
wws.bind("<Return>", calc)
for char in "1234567890*/-+.":
    wws.bind(char, lambda event, char=char: insert_text(char))

B_width=6
B_height=2

fonte_padrao = font.nametofont("TkDefaultFont")
fonte_padrao.configure(size=15, family="Arial")

containerVisor = tk.Frame(wws)
containerVisor.pack(padx=0, pady=5)

# Cria um Text widget dentro do Frame
resp = tk.Text(containerVisor, height=1, width=20, font=("Arial", 23), borderwidth=5)
resp.grid(row=0, column=0, padx=0, pady=5)

containerClear = tk.Frame(wws)
containerClear.pack(padx=0, pady=5)
button7 = tk.Button(containerClear, text="CA", width=B_width, height=B_height, command=lambda: resp.delete('1.0', tk.END))
button7.grid(row=0, column=0, padx=5, pady=0)
button8 = tk.Button(containerClear, text="C", width=B_width, height=B_height, command=lambda: resp.delete('1.0', tk.END))
button8.grid(row=0, column=1, padx=5, pady=0)
button9 = tk.Button(containerClear, text="Del", width=B_width, height=B_height, command=lambda: resp.delete('end-2c', tk.END))
button9.grid(row=0, column=2, padx=5, pady=0)
buttonDiv = tk.Button(containerClear, text="/", width=B_width, height=B_height, command=lambda: insert_text("/"))
buttonDiv.grid(row=0, column=3, padx=5, pady=0)

container7A9 = tk.Frame(wws)
container7A9.pack(padx=0, pady=5)
button7 = tk.Button(container7A9, text="7", width=B_width, height=B_height, command=lambda: insert_text("7"))
button7.grid(row=0, column=0, padx=5, pady=0)
button8 = tk.Button(container7A9, text="8", width=B_width, height=B_height, command=lambda: insert_text("8"))
button8.grid(row=0, column=1, padx=5, pady=0)
button9 = tk.Button(container7A9, text="9", width=B_width, height=B_height, command=lambda: insert_text("9"))
button9.grid(row=0, column=2, padx=5, pady=0)
buttonDiv = tk.Button(container7A9, text="*", width=B_width, height=B_height, command=lambda: insert_text("*"))
buttonDiv.grid(row=0, column=3, padx=5, pady=0)

container4A6 = tk.Frame(wws)
container4A6.pack(padx=0, pady=5)
button4 = tk.Button(container4A6, text="4", width=B_width, height=B_height, command=lambda: insert_text("4"))
button4.grid(row=0, column=0, padx=5, pady=0)
button5 = tk.Button(container4A6, text="5", width=B_width, height=B_height, command=lambda: insert_text("5"))
button5.grid(row=0, column=1, padx=5, pady=0)
button6 = tk.Button(container4A6, text="6", width=B_width, height=B_height, command=lambda: insert_text("6"))
button6.grid(row=0, column=2, padx=5, pady=0)
buttonMult = tk.Button(container4A6, text="-", width=B_width, height=B_height, command=lambda: insert_text("-"))
buttonMult.grid(row=0, column=3, padx=5, pady=0)

container1A3 = tk.Frame(wws)
container1A3.pack(padx=0, pady=5)
button1 = tk.Button(container1A3, text="1", width=B_width, height=B_height, command=lambda: insert_text("1"))
button1.grid(row=0, column=0, padx=5, pady=0)
button2 = tk.Button(container1A3, text="2", width=B_width, height=B_height, command=lambda: insert_text("2"))
button2.grid(row=0, column=1, padx=5, pady=0)
button3 = tk.Button(container1A3, text="3", width=B_width, height=B_height, command=lambda: insert_text("3"))
button3.grid(row=0, column=2, padx=5, pady=0)
buttonSub = tk.Button(container1A3, text="+", width=B_width, height=B_height, command=lambda: insert_text("+"))
buttonSub.grid(row=0, column=3, padx=5, pady=0)

container0 = tk.Frame(wws)
container0.pack(padx=0, pady=5)
button0 = tk.Button(container0, text="0", width=B_width, height=B_height, command=lambda: insert_text("0"))
button0.grid(row=0, column=0, padx=5, pady=0)
buttonV = tk.Button(container0, text=".", width=B_width, height=B_height, command=lambda: insert_text("."))
buttonV.grid(row=0, column=1, padx=5, pady=0)
buttonE = tk.Button(container0, text="+/-", width=B_width, height=B_height, command=trocaSinal)
buttonE.grid(row=0, column=2, padx=5, pady=0)
buttonSub = tk.Button(container0, text="=", width=B_width, height=B_height, command=calc)
buttonSub.grid(row=0, column=3, padx=5, pady=0)

wws.mainloop()