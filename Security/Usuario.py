import tkinter as tk
import webbrowser
import pandas as pd
import os

# Función que se ejecutará al presionar el botón "Registrarse"
def register():
    name = entry_name.get()
    password = entry_password.get()
    data = {'Nombre': [name], 'Contraseña': [password]}
    df = pd.DataFrame(data)
    df.to_excel('DatosUsuarios.xlsx', index=False)
    print("Se ha registrado el usuario:")
    print("Nombre:", name)
    print("Contraseña:", password)

# Función que se ejecutará al presionar el botón "Ingresar"
def login():
    filename = os.path.abspath('DatosUsuarios.xlsx')
    df = pd.read_excel(filename)
    webbrowser.open('file://' + filename)
    df.close()

# Creamos la ventana principal
root = tk.Tk()
root.title("Registro de Usuario Security")
root.geometry("300x200")
root.configure(bg='green')
root.resizable(False, False)

# Creamos los widgets necesarios
label_name = tk.Label(root, text="Nombre:", bg='green', fg='white')
label_name.grid(row=0, column=0, padx=5, pady=5)
entry_name = tk.Entry(root, bg='white', fg='black')
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_password = tk.Label(root, text="Contraseña:", bg='green', fg='white')
label_password.grid(row=1, column=0, padx=5, pady=5)
entry_password = tk.Entry(root, show="*", bg='white', fg='black')
entry_password.grid(row=1, column=1, padx=5, pady=5)

button_register = tk.Button(root, text="Registrarse", bg='green', fg='white', command=register)
button_register.grid(row=2, column=0, padx=5, pady=5)
button_login = tk.Button(root, text="Ingresar", bg='green', fg='white', command=login)
button_login.grid(row=2, column=1, padx=5, pady=5)

# Agregamos los bordes negros a los widgets
for child in root.winfo_children():
    child.configure(highlightbackground="black", highlightthickness=1)

# Ejecutamos el loop principal de la ventana
root.mainloop()
