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


    def update(self, data, source='exit'): ## default set to exit for the unit test
        for key, value in data.items():
            print(f"{key}:{value}")
        if source == 'exit':
            self.message = "Goodbye"
        elif source == 'entry':
            return self.message


    def __str__(self):
        return f"Display {self.id}: {self.message}"
