class car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def display_info(self):
            print(f"brand: {self.brand}, model: {self.model}")

class bike(car):
    def __init__(self,brand,model,engine_size):
        super().__init__(brand,model)
        self.engine_size = engine_size
    def display_info(self):
        super().display_info()
        print(f"engine size: {self.engine_size}")
        
bike1 = bike("Yamaha","R15",150)
bike1.display_info()