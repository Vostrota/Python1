from smartphone import Smartphone

catalog = []
Phone1 = Smartphone("Apple", "IPhone 15 Pro Max", "7-999-999-99-99")
Phone2 = Smartphone("Samsung", "Samsung Galaxy S24 Ultra", "7-988-888-88-88")
Phone3 = Smartphone("Xiaomi", "Xiaomi 13", "7-987-777-77-77")
Phone4 = Smartphone("OPPO", "Oppo Reno 11 Pro", "7-987-666-66-66")
Phone5 = Smartphone("Huawei", "Huawei Pura 70 Ultra Ultra", "7-987-655-55-55")

catalog.append(Phone1)
catalog.append(Phone2)
catalog.append(Phone3)
catalog.append(Phone4)
catalog.append(Phone5)

for Phone in catalog:
    print(f"{Phone.brand} {Phone.model} {Phone.number}")