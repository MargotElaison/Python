from smartphone import Smartphone

catalog = [
    Smartphone("brand", "model", "number"),
    Smartphone("brand1", "model1", "number1"),
    Smartphone("brand2", "model2", "number2"),
    Smartphone("brand3", "model3", "number3"),
    Smartphone("brand4", "model4", "number4"),
]

for phone in catalog:
    print(phone.get_info())
