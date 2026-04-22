# Python Fundamentals

Entry-level assignments covering core Python: logic, file I/O, and a first taste of OOP through inheritance.

## Assignments

### `leap_year/`
Two implementations of leap year detection — one verbose step-by-step, one concise one-liner — plus a multiplication table generator. Demonstrates conditional logic and the value of simplifying boolean expressions.

### `file_analysis/`
- **`word_counter.py`** — reads any text file, counts total words, finds the most frequent word, writes results to an output file
- **`prime_numbers_analyzer.py`** — generates primes up to a user-specified limit using trial division, outputs to file

### `vending_machine/`
A vending machine that reads products from a text file (`products.txt`) and displays items with type-specific info. First use of inheritance: `Product` base class → `Candy`, `Drink`, `Snack` subclasses. Demonstrates polymorphic `display_info()`.

**Run:** `python vending_machine/main.py`
