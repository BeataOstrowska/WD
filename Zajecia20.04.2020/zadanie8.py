class Samogloski:
    def __init__(self, data):
        self.data = data
        self.index = -1
        self.sam=['a','e','i','o','u','y']

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data)-1:
            raise StopIteration
        self.index = self.index + 1
        if self.data[self.index] in self.sam:
            return self.data[self.index] 
anna=Samogloski("qwertyuiopasdfghjklzxcvbnm")
print(list(anna))
print(isinstance(anna,Samogloski)) 
    


