class Shoe:
    def __init__(self, brand="", size=0):
        self.brand = brand
        self.size = size

    def get_brand(self):
        print("Retrieving brand.")
        return self._brand

    def set_brand(self, brand):
        if isinstance(brand, str) and 1 <= len(brand) <= 50:
            print(f"Setting brand to {brand}.")
            self._brand = brand
        else:
            print("Brand must be a string between 1 and 50 characters.")

    def get_size(self):
        print("Retrieving size.")
        return self._size

    def set_size(self, size):
        if not isinstance(size, int):
            print("size must be an integer")
        elif 1 <= size <= 20:
            print(f"Setting size to {size}.")
            self._size = size
        else:
            print("Size must be a number between 1 and 20.")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

    brand = property(get_brand, set_brand)
    size = property(get_size, set_size)
