# Object-Oriented Programming

Two projects demonstrating OOP principles at different levels of complexity.

## Projects

### 1. Restaurant System (`restaurant_system/`)
A CLI-based restaurant management application.

**OOP concepts:** Composition (`Main` owns `Restaurant`), encapsulation (private state via methods), abstraction (each method does one thing), separation of concerns across `MenuItem`, `Order`, `Restaurant`, `Main`.

**Run:** `python restaurant_system/main.py`

---

### 2. Library Management System (`library_system/`) ⭐
A full OOP project with a real architecture.

**OOP concepts demonstrated:**
- **Abstract base class** — `LibraryItem` defines the interface all items must implement
- **Interface / Mixin** — `Reservable` applied only to `Book` and `DVD` (not `Magazine`)
- **Inheritance hierarchy** — `LibraryItem → Book / Magazine / DVD`
- **Custom exceptions** — `ItemNotAvailableError`, `UserNotFoundError`, etc. in `exceptions/`
- **Persistence** — JSON data storage/loading in `data/`
- **Encapsulation** — state changes only through controlled methods (`borrow`, `return_item`, `reserve`)

**Run:** `python library_system/main.py`

**Class diagram (Mermaid):**
```
LibraryItem (abstract)
    ├── Book      implements Reservable
    ├── Magazine
    └── DVD       implements Reservable

Library manages → [LibraryItem], [User]
```
