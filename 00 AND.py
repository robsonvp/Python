ingles = input("Sabe falar inglês? (SIM/NAO) ").upper()
python = input("Sabe programar Python? (SIM/NAO) ").upper()

if python == "SIM" and ingles == "NAO":
    print("Treinamento")
elif python == "SIM" and ingles == "SIM":
    print("Aprovado")
else:
    print("Reprovado")
