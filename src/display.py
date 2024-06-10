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


    def update(self, data, car_incoming=False): ## default set to exit for the unit test
        for key, value in data.items():
            print(f"{key}:{value}")
        if car_incoming == False :
            self.message = "Goodbye"
        elif car_incoming == True :
            return self.message


    def __str__(self):
        return f"Display {self.id}: {self.message}"
