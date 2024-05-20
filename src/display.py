class Display:
    def __init__(self,
                 id,
                 car_park,
                 message = " ",
                 is_on = False
                 ):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def update(self, data):
        for key, value in data.items():
            print(f"{key}:{value}")
        self.message = "Goodbye" ## may need to elaborate this
        ## may need to get to the end of the dictionary, then it will '=' goodbye.
    def __str__(self):
        return f"Display {self.id}: {self.message}"



