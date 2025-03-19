class Smartphone:
    def __init__(self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def get_info(self):
        return "{brand} - {model}. {number}".format(
            brand=self.brand,
            model=self.model,
            number=self.number
        )
