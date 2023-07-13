import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

seconds = 0
minutes = 0

def toggle_strike():
    if strike_var.get() == 1:
        text_label.config(font=("Arial", 12, "normal"), fg="black")
    else:
        text_label.config(font=("Arial", 12, "overstrike"), fg="gray")

def update_numbers():
    global seconds
    global minutes
    seconds += 1
    seconds_label['text'] = seconds
    seconds_label.after(1000, update_numbers)
    if seconds == 60:
        seconds = 0
        minutes += 1
        if minutes == 25:
            messagebox.showinfo("Pomodoro Concluido")
        minutes_label['text'] = minutes
        button_start.configure(state=tk.ACTIVE)


def start_update():
    button_start.configure(state=tk.DISABLED)
    update_numbers()

def button_func():
    entry_input_text = entry_input.get()
    text_label['text'] = entry_input_text

# Criando a janela principal
window = tk.Tk()
window.title('YagoPomodoro')
window.geometry('500x250')

# Configuração do tema
style = ttk.Style()
style.theme_use('darkly')


frame_timer = tk.Frame(window)
frame_timer.pack()


minutes_label = ttk.Label(frame_timer, text="00", font=("Arial", 25))
minutes_label.pack(side=tk.LEFT, pady=20)
division_label = ttk.Label(frame_timer, text=":", font=("Arial", 25))
division_label.pack(side=tk.LEFT, padx=5)
seconds_label = ttk.Label(frame_timer, text="00", font=("Arial", 25))
seconds_label.pack(side=tk.LEFT)


frame_todo = tk.Frame(window)
frame_todo.pack()



strike_var = tk.IntVar()
strike_var.set(0)

button_start = ttk.Button(frame_todo, text="Iniciar", command=start_update)
button_start.pack(pady=20)

entry_input = tk.Entry(frame_todo)
entry_input.pack()
button_send = tk.Button(frame_todo, text='send', command=button_func)
button_send.pack(pady=5)

# Checkbox para marcar/desmarcar o texto
strike_checkbox = tk.Checkbutton(frame_todo, variable=strike_var, command=toggle_strike)
strike_checkbox.pack(side=tk.LEFT,pady=10)

# Label para exibir o texto
text_label = tk.Label(frame_todo, text="Texto a ser riscado", font=("Arial", 12, "normal"), fg="black")
text_label.pack(side=tk.LEFT)


window.mainloop()
