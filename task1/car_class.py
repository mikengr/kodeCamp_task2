from .vehicle_class import Vehicle

class Car(Vehicle):
    def __init__(self, engine_type, num_of_wheels, capacity, max_velocity, model, year_of_manufacture, cost) -> None:
        super().__init__(engine_type, num_of_wheels, capacity, max_velocity)
        self.year = year_of_manufacture
        self.model = model
        self.cost = cost

    def retail_price(self):
        profit_margin = 1.2
        return f"{self.cost * profit_margin}"

    def second_hand_value(self, distance, number_of_owners):
        depr_rate = 0.012 / number_of_owners
        return f"{(self.mileage(distance) * depr_rate) + (self.cost * 0.1)}"
    
    def rentals(self, duration):
        rate = self.cost * 0.025
        return f"{rate * duration}"