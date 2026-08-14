# Calculator Application

A **Calculator Application** built with Python that performs basic arithmetic operations — addition, subtraction, multiplication, and division — through a clean, modern graphical interface. The project demonstrates fundamental Python programming concepts including functions, conditional statements, loops, user input handling, operators, and robust error handling.

## Preview

A sleek, dark-themed calculator interface inspired by modern mobile calculators, featuring a live expression display, smooth hover effects, and full keyboard support.

## Features

- **Basic Arithmetic Operations** — Addition, Subtraction, Multiplication, Division
- **Modern GUI** — Dark-themed interface built with Tkinter
- **Live Expression Display** — Shows the running expression above the result
- **Keyboard Support** — Type numbers and operators directly using your keyboard
- **Additional Functions**:
  - `C` — Clear all
  - `⌫` — Backspace (delete last digit)
  - `±` — Toggle positive/negative sign
  - `%` — Percentage conversion
- **Error Handling** — Gracefully handles invalid input and division by zero without crashing
- **Responsive Design** — Resizable window with buttons that scale accordingly

## Key Concepts Demonstrated

- Python Programming Fundamentals
- Functions & Modular Code Design
- Conditional Statements
- Loops
- Event-Driven Programming (GUI)
- Operators
- Error Handling (`try` / `except`)

## Technology Used

- **Language:** Python 3
- **GUI Library:** Tkinter (built into Python — no extra installation required)

## Project Structure

```
Calculator-Application/
│
├── Calculator_Application.py   # Main application file
└── README.md                   # Project documentation
```

## Getting Started

### Prerequisites

Make sure you have **Python 3** installed on your system. Tkinter comes pre-installed with most Python distributions.

Check your Python version:
```bash
python3 --version
```

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Calculator-Application.git
   ```
2. Navigate into the project folder:
   ```bash
   cd Calculator-Application
   ```

### Usage

Run the application with:
```bash
python3 Calculator_Application.py
```

## How It Works

1. Enter numbers using the on-screen buttons or your keyboard.
2. Select an operation (`+`, `-`, `×`, `÷`).
3. Press `=` (or **Enter**) to see the result.
4. Press `C` (or **Esc**) at any time to clear and start a new calculation.
5. If an invalid operation is attempted (e.g., dividing by zero), the app displays a clear error message instead of crashing.

## Keyboard Shortcuts

| Key           | Action          |
|---------------|-----------------|
| `0-9`, `.`    | Enter numbers   |
| `+ - * /`     | Operators       |
| `Enter`       | Calculate (`=`) |
| `Backspace`   | Delete last digit |
| `Esc`         | Clear all       |

## Future Improvements

- Add support for advanced operations (square root, power, memory functions)
- Add calculation history panel
- Add light/dark theme toggle

## Author

**Malika**
AI & ML Engineer | Full Stack Developer

## License

This project is open source and available for personal and educational use.
