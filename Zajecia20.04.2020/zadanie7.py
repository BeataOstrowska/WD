class Parzyste:
    def __init__(self, data):
        self.data = data
        self.index = -2
    def __iter__(self):
        return self
    def __next__(self):
        a=len(self.data) 
        if a%2!=0:
            a=a-1
        if self.index>=a:
            raise StopIteration
        self.index=self.index + 2
        return self.data[self.index]
anna=Parzyste("205200135")
print(list(anna))
