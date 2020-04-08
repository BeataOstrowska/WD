#Słowniki i zamiana klucza z wartoscią
skroty={"PZU": "Państwowy Zakład Ubezpieczeń",
        "ZUS": "Zakład Ubezpieczeń Społecznych",
        "PKO": "Powszechna Kasa Oszczędności"}
odwrocone={value: key for key, value in skroty.items()}
print("Orginalny słownik")
print(skroty)
print("Słownik odwrócony")
print(odwrocone)