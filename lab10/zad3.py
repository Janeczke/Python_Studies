def bezpowt(sl):
    l=list(sl.values())
    if len(l) > len(set(l)):
        return 0
    else:
        return 1
sl={"Imię":"Jakub","Nazwisko":"Momot","Rok":"2000"}
if bezpowt(sl) == 1:
    print("Funkcja zwróciła wartość 1,więc w słowniku nie ma powtórzeń")
else:
    print("Funkcja zwróciła wartość 0,więc w słowniku występują powtórzenia")