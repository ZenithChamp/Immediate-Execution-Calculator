# Immediate-Execution Pocket Calculator Engine

A lightweight, terminal-based sequential execution calculator built from scratch in Python. This project simulates the exact functional logic of a physical hardware pocket calculator, processing intermediate states sequentially rather than parsing full expressions via traditional BODMAS/PEMDAS ordering.

## 🚀 Key Features
- **Sequential Execution:** Tracks inputs using a dynamic accumulator state model.
- **Immediate Execution:** Computes running totals instantly upon subsequent operator inputs, perfectly mirroring physical desktop counters.
- **Robust Boundary Handling:** Safeguards against runtime crashes by checking for empty string sequences and managing termination interrupts (`Cc`) safely.
- **Float Precision Operations:** Supports clean decimal processing across standard operations (`+`, `-`, `*`, `/`, `^`).

## 🛠️ Tech Stack & Concepts Used
- **Language:** Python 3
- **Concepts:** Control Flow Systems, State Buffering, Error/Boundary Handling, System I/O Management.

## 💻 How to Run Locally

1. Clone this repository to your machine.
2. Open your terminal inside the project directory and execute:
   ```bash
   python IECalculator.py
   ```
3. Type `C` and press `Enter` to initialize the engine.
4. Input digits, operators (`+`, `-`, `*`, `/`, `^`), or `=` sequentially, pressing `Enter` after each key.
