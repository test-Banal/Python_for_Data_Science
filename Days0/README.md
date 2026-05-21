# Python for Data Science - Module 00: Starting

Introduction to Python fundamentals through the first module of the 42 **Python for Data Science Piscine**.

This module focuses on:
- Python syntax and data types
- Functions
- Argument parsing
- Error handling
- List comprehensions and lambda
- Dictionaries
- Iterators and generators
- Creating a Python package

> Python version required: **3.10** :contentReference[oaicite:0]{index=0}

---

## Project Structure

```bash
.
├── ex00/
├── ex01/
├── ex02/
├── ex03/
├── ex04/# Python for Data Science - Module 00: Starting

Introduction to Python fundamentals through the first module of the 42 **Python for Data Science Piscine**.

This module focuses on:
- Python syntax and data types
- Functions
- Argument parsing
- Error handling
- List comprehensions and lambda
- Dictionaries
- Iterators and generators
- Creating a Python package

> Python version required: **3.10** :contentReference[oaicite:0]{index=0}

---

## Project Structure

```bash
.
├── ex00/
├── ex01/
├── ex02/
├── ex03/
├── ex04/
├── ex05/
├── ex06/
├── ex07/
├── ex08/
└── ex09/
```

---

## General Rules

- No global variables allowed. :contentReference[oaicite:1]{index=1}  
- Explicit imports only.  
- No uncaught exceptions.  
- From ex05 onward:
  - use a `main()`
  - use docstrings
  - follow flake8 norm (`norminette=flake8`) :contentReference[oaicite:2]{index=2}

---

# Exercises

## ex00 — First Python Script

**Goal:** manipulate basic Python containers:

- list  
- tuple  
- set  
- dictionary

Learn how mutable and immutable structures behave.

**File:**
```bash
Hello.py
```

---

## ex01 — First Use of Package

**Goal:** work with time and date formatting.

Topics:
- `time`
- `datetime`
- scientific notation
- formatting output

**File:**
```bash
format_ft_time.py
```

---

## ex02 — First Function Python

**Goal:** create a function that detects object types.

Topics:
- functions
- return values
- type inspection
- conditional logic

**File:**
```bash
find_ft_type.py
```

---

## ex03 — NULL not found

**Goal:** handle Python “null-like” values:

- `None`
- `NaN`
- `0`
- empty string
- `False`

Topics:
- special values
- edge cases
- type handling

**File:**
```bash
NULL_not_found.py
```

---

## ex04 — The Even and the Odd

**Goal:** parse command line arguments and validate input.

Topics:
- `sys.argv`
- assertions
- integer conversion
- odd/even logic

**File:**
```bash
whatis.py
```

---

## ex05 — First Standalone Program

**Goal:** build a complete autonomous Python program.

Analyze a string and count:

- upper letters
- lower letters
- punctuation
- spaces
- digits

Topics:
- character classification
- input handling
- main function structure

**File:**
```bash
building.py
```

---

## ex06 — ft_filter

### Part 1

Recode Python's built-in `filter()` using:

- list comprehension

**File:**
```bash
ft_filter.py
```

---

### Part 2

Filter words longer than N from a string.

Must use:
- lambda
- list comprehension

**File:**
```bash
filterstring.py
```

---

## ex07 — Dictionaries SoS

**Goal:** encode text into Morse code.

Topics:
- dictionaries
- mapping
- string parsing

**File:**
```bash
sos.py
```

---

## ex08 — Loading...

Recreate a simplified `tqdm`.

Topics:
- generators
- `yield`
- terminal output
- progress bars

**File:**
```bash
Loading.py
```

---

## ex09 — My First Package Creation

Create a real Python package installable with:

```bash
pip install
```

Topics:
- package structure
- build artifacts
- wheel / tar.gz
- package metadata

---

## Run

Example:

```bash
python ex04/whatis.py 42
```

---

## Validation

Peer evaluation + Deepthought. :contentReference[oaicite:3]{index=3}

---

## Skills Practiced

- Python fundamentals  
- Functional programming  
- Error handling  
- CLI programs  
- Iterators  
- Package creation

---

## Author

42 Python for Data Science Piscine  
Login: your_login