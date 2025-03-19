class Address:
    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def get_info(self):
        return "{index}, {city}, {street}, {house} - {flat}".format(
            index=self.index,
            city=self.city,
            street=self.street,
            house=self.house,
            flat=self.flat
        )
