import tkinter as tk
import tkinter.messagebox

from map.toy_calculator import main_window


class CalculatorButton(tk.Button):
    """A button with callback, to be used with a CalculatorGrid widget."""

    def __init__(self, master, callback=None, **kwargs):
        # self.callback = kwargs.pop('callback', None)
        self.callback = callback
        super().__init__(master, **kwargs)
        self.config(command=self.on_click)

    def on_click(self):
        if self.callback:
            self.callback(self['text'])


class CalculatorGrid(tk.Frame):

    keys = [[('C', 1), ('CE', 1)],
            [('7', 1), ('8', 1), ('9', 1), ('+', 1)],
            [('4', 1), ('5', 1), ('6', 1), ('-', 1)],
            [('1', 1), ('2', 1), ('3', 1), ('*', 1)],
            [('0', 1), ('=', 2), ('/', 1)],
            ]

    allowed_chars = [key[0] for key_row in keys for key in key_row]
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        max_columns = max(len(row) for row in CalculatorGrid.keys)
        self.result = tk.Entry(self)
        self.result.grid(row=0, column=0, columnspan=max_columns, sticky="nsew")

        # Add the buttons
        keypad = tk.Frame(self)
        keypad.grid(row=1, column=0, sticky='nsew')

        row = 0
        for key_row in CalculatorGrid.keys:
            col = 0
            for key in key_row:
                btn = CalculatorButton(keypad, text=key[0], width=2,
                                callback=self.on_click)
                btn.grid(row=row, column=col, columnspan=key[1], sticky=tk.E + tk.W)
                col += key[1]
            row += 1


    def on_click(self, char: str):
        if char == '=':
            if self.result.get() and all(caption in CalculatorGrid.allowed_chars
                                         for caption in self.result.get()):
                try:
                    answer = str(eval(self.result.get()))
                except SyntaxError:
                    tk.messagebox.showerror("Error", "Your calculation isn't valid.:")
                except ZeroDivisionError:
                    tk.messagebox.showerror("Error", "You can't divide by zero.")
                else:
                    self.result.delete(0, tk.END)
                    self.result.insert(0, answer)
            elif char == 'C':
                self.result.delete(0, tk.END)
        elif char == 'CE':
            self.result.delete(len(self.result.get()) - 1, tk.END)
        else:
            self.result.insert(tk.END, char)



def test():
    def clicked(caption: str):
        print(f'{caption} was clicked')

    main_window = tk.Tk()
    main_window.title("CalculatorButton test")
    main_window.geometry('640x480')

    btn = CalculatorButton(main_window, callback=clicked, text='Test')
    btn.grid(row=0, column=0, sticky='nsew')

    main_window.mainloop()


if __name__ == '__main__':
    test()
