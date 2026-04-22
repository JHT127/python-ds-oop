
from models.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, item_id, title, publisher, year, issue_number, pages):
        super().__init__(item_id, title, publisher, year)
        self.issue_number = issue_number
        self.pages = pages

    def display_info(self):
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return (f"Magazine: {self.title} ({self.year})\n"
                f"Issue Number: {self.issue_number}, Pages: {self.pages}\n"
                f"Publisher: {self.author}\n"
                f"Status: {status}")