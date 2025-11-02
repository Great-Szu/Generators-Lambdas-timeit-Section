import tkinter as tk
import tkinter.messagebox

keys = [[('C', 1), ('CE', 1)],
        [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
        [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
        [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
        [('0', 1), ('=', 2), ('/', 1)],
        ]


def btn_click(char):
    if char == '=':
        if result.get():
            try:
                answer = str(eval(result.get()))
            except SyntaxError:
                tk.messagebox.showerror("Error", "Your calculation isn't valid.:")
            except ZeroDivisionError:
                tk.messagebox.showerror("Error", "You can't divide by zero.")
            else:
                result.delete(0, tk.END)
                result.insert(0, answer)
    elif char == 'C':
        result.delete(0, tk.END)
    elif char == 'CE':
        result.delete(len(result.get()) - 1, tk.END)
    else:
        result.insert(tk.END, char)

main_window_padding = 8

main_window = tk.Tk()
main_window.title("Calculator")
main_window.geometry('640x480-8-200')
main_window['padx'] = main_window_padding

result = tk.Entry(main_window)
result.grid(row=0, column=0, sticky='nsew')

keypad = tk.Frame(main_window)
keypad.grid(row=1, column=0, sticky='nsew')

row = 0
for key_row in keys:
    col = 0
    for key in key_row:
        btn = tk.Button(keypad, text=key[0], width=2,
                        command=lambda char=key[0]: btn_click(char))
        btn.grid(row=row, column=col, columnspan=key[1], sticky=tk.E + tk.W)
        col += key[1]
    row += 1

main_window.update()
main_window.minsize(keypad.winfo_width() + main_window_padding * 2, result.winfo_height() + keypad.winfo_height())
# main_window.maxsize(keypad.winfo_width() + main_window_padding * 2, result.winfo_height() + keypad.winfo_height())

main_window.mainloop()
