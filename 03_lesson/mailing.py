class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def get_info(self):
        return ("Отправление {track} из {address_1} в {address_2}. "
                "Стоимость {cost} рублей.").format(
            track=self.track,
            cost=self.cost,
            address_1=self.from_address.get_info(),
            address_2=self.to_address.get_info()
        )
