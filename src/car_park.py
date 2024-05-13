class CarPark: # pascal case good for classes
    def __init__(self,
                 location = "Unknown",
                 capacity = 0,
                 plates = None,
                 sensors = None,
                 displays = None):
        self.location = location
        self.capacity = capacity
        self.plates = []
        self.sensors = []
        self.displays = []