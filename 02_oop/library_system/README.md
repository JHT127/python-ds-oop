# Library Management System

A Python OOP implementation of a library management system with abstraction, interfaces, and exception handling.

## Features
- Manage Books, Magazines, and DVDs
- User registration and management
- Borrow/return/reserve items
- Persistent data storage (JSON)
- Comprehensive error handling

## How to Run (PyCharm)
1. **Clone the repository** or download the project files
2. **Open in PyCharm**:
   - File → Open → Select the project folder
3. **Set up Python interpreter**:
   - PyCharm should detect Python automatically
   - If not: File → Settings → Project → Python Interpreter → Add interpreter
4. **Run the application**:
   - Right-click `main.py` → Run
   - Or use the green run button in PyCharm

## Design Decisions

### 1. Class Structure
```mermaid
classDiagram
    class LibraryItem{
        <<abstract>>
        +item_id
        +title
        +author
        +year
        +is_available
        +display_info()*
        +borrow()
        +return_item()
    }
    
    class Reservable{
        <<interface>>
        +reserve()*
        +cancel_reservation()*
    }
    
    LibraryItem <|-- Book
    LibraryItem <|-- Magazine
    LibraryItem <|-- DVD
    Reservable <|.. Book
    Reservable <|.. DVD
    
    class Library{
        +items
        +users
        +borrow_item()
        +return_item()
        +reserve_item()
    }
    
    class User{
        +user_id
        +name
        +email
        +borrowed_items
        +reserved_items
    }