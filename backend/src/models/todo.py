class Todo:
    def __init__(self, id: int, title: str, completed: bool = False):
        self.id = id
        self.title = title
        self.completed = completed

    def update(self, title: str = None, completed: bool = None):
        if title is not None:
            self.title = title
        if completed is not None:
            self.completed = completed

    def delete(self):
        # Logic to delete the todo item
        pass