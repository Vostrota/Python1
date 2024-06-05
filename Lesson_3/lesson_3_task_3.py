from address import Address 
from mailing import Mailing

to_address = Address("123007", "Москва", "Полины Осипенко", "2", "518")
from_address = Address ("630080", "Новосибирск", "Первомайская", "102", "54")
mailing = Mailing(to_address, from_address, 342, "ADJDF1345")

print(f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")
