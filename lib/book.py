#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self._page_count = page_count  # Store page_count as a private attribute with an underscore

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, new_page_count):
        if isinstance(new_page_count, int):
            self._page_count = new_page_count
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
    
        