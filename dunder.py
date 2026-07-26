class Book():
    def __init__(self, name='unknown', page=0):
        self.page = page
        self.name = name
        
    def open(self):
        print(f" opened the {self.name} which has {self.page} pages ")
        
    def __len__(self):
        return self.page
    
    def __str__(self):
        r = f"{self.name}, {self.page}"
        return r
b = Book('python is fun', 193)
print(b)