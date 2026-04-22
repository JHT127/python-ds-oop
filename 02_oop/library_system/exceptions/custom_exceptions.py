
class LibraryError(Exception):
    """Base class for library exceptions"""
    pass

class ItemNotFoundError(LibraryError):
    """Raised when an item is not found in the library"""
    pass

class UserNotFoundError(LibraryError):
    """Raised when a user is not found in the system"""
    pass

class ItemNotAvailableError(LibraryError):
    """Raised when trying to borrow an unavailable item"""
    pass

class ItemAlreadyAvailableError(LibraryError):
    """Raised when trying to return an already available item"""
    pass

class ItemNotBorrowedError(LibraryError):
    """Raised when trying to return a non-existent borrowed item"""
    pass

class ItemAlreadyBorrowedError(LibraryError):
    """Raised when trying to borrow an already borrowed item"""
    pass

class ItemAlreadyReservedError(LibraryError):
    """Raised when trying to reserve an already reserved item"""
    pass

class ItemNotReservedError(LibraryError):
    """Raised when trying to cancel a non-existent reservation"""
    pass

class ItemAvailableError(LibraryError):
    """Raised when trying to reserve an available item"""
    pass

class InvalidItemTypeError(LibraryError):
    """Raised when an invalid item type is encountered"""
    pass