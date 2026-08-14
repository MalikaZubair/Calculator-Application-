"""
Calculator Application - Graphical Interface
----------------------------------------------
A modern, dark-themed calculator built with Tkinter.

Concepts demonstrated:
    - Functions
    - Conditional statements
    - Loops
    - Event-driven programming (GUI)
    - Operators
    - Error handling (try/except)
"""

import tkinter as tk
from tkinter import font


# ---------------------------------------------------------------------------
# Color palette (modern dark theme)
# ---------------------------------------------------------------------------
BG_MAIN = "#1e1e2e"
BG_DISPLAY = "#181825"
FG_DISPLAY = "#ffffff"
FG_EXPRESSION = "#a6adc8"

BTN_NUMBER = "#313244"
BTN_NUMBER_HOVER = "#45475a"
FG_NUMBER = "#ffffff"

BTN_OPERATOR = "#89b4fa"
BTN_OPERATOR_HOVER = "#74a8f9"
FG_OPERATOR = "#1e1e2e"

BTN_FUNCTION = "#585b70"
BTN_FUNCTION_HOVER = "#6c6f85"
FG_FUNCTION = "#ffffff"

BTN_EQUALS = "#a6e3a1"
BTN_EQUALS_HOVER = "#94dd8d"
FG_EQUALS = "#1e1e2e"

FG_ERROR = "#f38ba8"


class Calculator(tk.Tk):
    """Main calculator application window."""

    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("360x560")
        self.minsize(320, 500)
        self.configure(bg=BG_MAIN)

        # State
        self.expression = ""      # full expression shown above the result
        self.current = ""         # current number being typed
        self.reset_next_input = False

        self._build_fonts()
        self._build_display()
        self._build_buttons()
        self._bind_keys()

    # -------------------------------------------------------------------
    # UI construction
    # -------------------------------------------------------------------
    def _build_fonts(self):
        self.font_expression = font.Font(family="Helvetica", size=16)
        self.font_display = font.Font(family="Helvetica", size=40, weight="bold")
        self.font_button = font.Font(family="Helvetica", size=18)

    def _build_display(self):
        display_frame = tk.Frame(self, bg=BG_DISPLAY)
        display_frame.pack(fill="both", expand=False, padx=0, pady=0)

        self.expression_label = tk.Label(
            display_frame,
            text="",
            anchor="e",
            bg=BG_DISPLAY,
            fg=FG_EXPRESSION,
            font=self.font_expression,
            padx=20,
            pady=5,
        )
        self.expression_label.pack(fill="x")

        self.result_label = tk.Label(
            display_frame,
            text="0",
            anchor="e",
            bg=BG_DISPLAY,
            fg=FG_DISPLAY,
            font=self.font_display,
            padx=20,
            pady=15,
        )
        self.result_label.pack(fill="x")

    def _build_buttons(self):
        btn_frame = tk.Frame(self, bg=BG_MAIN)
        btn_frame.pack(fill="both", expand=True)

        # (label, row, col, colspan, type)
        # type: "num", "op", "func", "eq"
        layout = [
            ("C", 0, 0, 1, "func"),
            ("⌫", 0, 1, 1, "func"),
            ("%", 0, 2, 1, "func"),
            ("÷", 0, 3, 1, "op"),

            ("7", 1, 0, 1, "num"),
            ("8", 1, 1, 1, "num"),
            ("9", 1, 2, 1, "num"),
            ("×", 1, 3, 1, "op"),

            ("4", 2, 0, 1, "num"),
            ("5", 2, 1, 1, "num"),
            ("6", 2, 2, 1, "num"),
            ("-", 2, 3, 1, "op"),

            ("1", 3, 0, 1, "num"),
            ("2", 3, 1, 1, "num"),
            ("3", 3, 2, 1, "num"),
            ("+", 3, 3, 1, "op"),

            ("±", 4, 0, 1, "func"),
            ("0", 4, 1, 1, "num"),
            (".", 4, 2, 1, "num"),
            ("=", 4, 3, 1, "eq"),
        ]

        for i in range(5):
            btn_frame.rowconfigure(i, weight=1)
        for j in range(4):
            btn_frame.columnconfigure(j, weight=1)

        style_map = {
            "num": (BTN_NUMBER, BTN_NUMBER_HOVER, FG_NUMBER),
            "op": (BTN_OPERATOR, BTN_OPERATOR_HOVER, FG_OPERATOR),
            "func": (BTN_FUNCTION, BTN_FUNCTION_HOVER, FG_FUNCTION),
            "eq": (BTN_EQUALS, BTN_EQUALS_HOVER, FG_EQUALS),
        }

        self.buttons = {}
        for (label, row, col, span, kind) in layout:
            bg, hover, fg = style_map[kind]
            btn = tk.Button(
                btn_frame,
                text=label,
                font=self.font_button,
                bg=bg,
                fg=fg,
                activebackground=hover,
                activeforeground=fg,
                bd=0,
                relief="flat",
                cursor="hand2",
                command=lambda l=label: self.on_button(l),
            )
            btn.grid(
                row=row, column=col, columnspan=span,
                sticky="nsew", padx=6, pady=6, ipady=10,
            )
            # Simple hover effect
            btn.bind("<Enter>", lambda e, b=btn, c=hover: b.config(bg=c))
            btn.bind("<Leave>", lambda e, b=btn, c=bg: b.config(bg=c))
            self.buttons[label] = btn

    def _bind_keys(self):
        self.bind("<Key>", self.on_key_press)

    # -------------------------------------------------------------------
    # Event handling
    # -------------------------------------------------------------------
    def on_key_press(self, event):
        key = event.char
        keysym = event.keysym

        if key in "0123456789.":
            self.on_button(key)
        elif key == "+":
            self.on_button("+")
        elif key == "-":
            self.on_button("-")
        elif key == "*":
            self.on_button("×")
        elif key == "/":
            self.on_button("÷")
        elif key == "%":
            self.on_button("%")
        elif keysym in ("Return", "KP_Enter"):
            self.on_button("=")
        elif keysym == "BackSpace":
            self.on_button("⌫")
        elif keysym == "Escape":
            self.on_button("C")

    def on_button(self, label):
        if label.isdigit() or label == ".":
            self._input_digit(label)
        elif label in ("+", "-", "×", "÷"):
            self._input_operator(label)
        elif label == "=":
            self._calculate()
        elif label == "C":
            self._clear()
        elif label == "⌫":
            self._backspace()
        elif label == "±":
            self._toggle_sign()
        elif label == "%":
            self._percent()

    # -------------------------------------------------------------------
    # Core calculator logic
    # -------------------------------------------------------------------
    def _input_digit(self, digit):
        if self.reset_next_input:
            self.current = ""
            self.reset_next_input = False

        # Avoid multiple leading zeros / multiple decimal points
        if digit == "." and "." in self.current:
            return
        if self.current == "0" and digit != ".":
            self.current = digit
        else:
            self.current += digit

        self._update_display()

    def _input_operator(self, op):
        if self.current == "" and self.expression == "":
            return  # nothing to operate on yet

        if self.current != "":
            self.expression += self.current
            self.current = ""

        # Replace trailing operator if user presses another operator
        if self.expression and self.expression[-1] in "+-×÷ ":
            self.expression = self.expression.rstrip("+-×÷ ").rstrip()

        self.expression += f" {op} "
        self.reset_next_input = False
        self._update_display()

    def _calculate(self):
        if self.current != "":
            self.expression += self.current
            self.current = ""

        if not self.expression:
            return

        try:
            # Translate display symbols into valid Python operators
            safe_expr = self.expression.replace("×", "*").replace("÷", "/")

            result = self._safe_eval(safe_expr)

            # Format nicely: drop trailing .0 for whole numbers
            if result == int(result):
                result = int(result)
            else:
                result = round(result, 10)

            self.result_label.config(text=str(result), fg=FG_DISPLAY)
            self.expression_label.config(text=self.expression + " =")
            self.current = str(result)
            self.expression = ""
            self.reset_next_input = True

        except ZeroDivisionError:
            self._show_error("Cannot divide by zero")
        except Exception:
            self._show_error("Invalid expression")

    def _safe_eval(self, expr):
        """
        Safely evaluate a simple arithmetic expression containing only
        numbers, spaces, and the operators + - * /.
        """
        allowed_chars = set("0123456789.+-*/() ")
        if not set(expr) <= allowed_chars:
            raise ValueError("Invalid characters in expression")

        # Basic division-by-zero check happens naturally via ZeroDivisionError
        return eval(expr, {"__builtins__": {}}, {})

    def _clear(self):
        self.expression = ""
        self.current = ""
        self.reset_next_input = False
        self.result_label.config(text="0", fg=FG_DISPLAY)
        self.expression_label.config(text="")

    def _backspace(self):
        if self.current:
            self.current = self.current[:-1]
        elif self.expression:
            self.expression = self.expression.rstrip()
            self.expression = self.expression[:-1].rstrip()
            self.expression = self.expression + " " if self.expression else ""
        self._update_display()

    def _toggle_sign(self):
        if self.current:
            if self.current.startswith("-"):
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
            self._update_display()

    def _percent(self):
        if self.current:
            try:
                value = float(self.current) / 100
                self.current = str(int(value) if value == int(value) else value)
                self._update_display()
            except ValueError:
                pass

    def _update_display(self):
        self.expression_label.config(text=self.expression, fg=FG_EXPRESSION)
        display_text = self.current if self.current else (
            "0" if not self.expression else ""
        )
        self.result_label.config(text=display_text or "0", fg=FG_DISPLAY)

    def _show_error(self, message):
        self.result_label.config(text=message, fg=FG_ERROR)
        self.expression = ""
        self.current = ""
        self.reset_next_input = True


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()