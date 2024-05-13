class CarPark: ## pascal case good for identifying classes
    def __init__(self,
                 location = "Unknown",
                 capacity = 0,
                 plates = None,
                 sensors = None,
                 displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []  ## this is better
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):         ## makes it better to represent the instance
        return f"Car Park location = {self.location} capacity = {self.capacity}. "
