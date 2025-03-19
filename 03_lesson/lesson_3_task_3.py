from address import Address
from mailing import Mailing

deliver = Mailing(
    Address(
        "123123",
        'Moscow',
        "Pushkina",
        'Kolotushkina',
        'N/A'
    ),
    Address(
        "321321",
        'St.Petersburg',
        "Kolotushkina",
        'Pushkina',
        'N/A'
    ),
    100500,
    "YJ124141KCH154"
)

print(deliver.get_info())
