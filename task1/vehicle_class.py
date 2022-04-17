class Vehicle:
    def __init__(self, engine_type, num_of_wheels, tank_capacity, max_velocity) -> None:
        self.engine = engine_type
        self.wheels = num_of_wheels
        self.capacity = tank_capacity
        self.velocity = max_velocity

    def mileage(self, distance):
        return f"{distance/self.capacity}"

    def accelaration(self, time):
        return f"{self.velocity/time}"

    def transmission(self):
        return f"{self.engine}"
