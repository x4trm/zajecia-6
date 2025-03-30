# Napisz program, który pobierze od użytkownika kilka liczb i wykona następujące operacje:
# Sprawdzi kolejność liczb:
# Czy tworzą ciąg rosnący (każda kolejna liczba jest większa od poprzedniej).
# Czy tworzą ciąg malejący (każda kolejna liczba jest mniejsza od poprzedniej).
# Czy są podane w losowej kolejności.
# Znajdzie najmniejszą i największą liczbę w podanym zbiorze.
# Porówna liczby:
# - Sprawdzi, czy wszystkie liczby są takie same.
# - Sprawdzi, czy wszystkie liczby są różne od siebie.
# Oceni parzystość:
# Sprawdzi, czy wszystkie liczby są parzyste.
# Sprawdzi, czy wszystkie liczby są nieparzyste.
# W przeciwnym razie stwierdzi, że liczby są mieszane (zawierają zarówno parzyste, jak i nieparzyste).


a = int(input("Podaj pierwsza liczbe: "))
b = int(input("Podaj druga liczbe: "))
c = int(input("Podaj trzecia liczbe: "))

if a < b < c:
  print("Liczby tworza ciag rosnacy")
elif a > b > c:
  print("Liczby tworza ciag malejacy")
else:
  print("Liczby tworza losowy ciag")

najmniejsza = min(a,b,c) 
najwieksza = max(a,b,c)

print(f"Najwieksza liczba: {najwieksza}, Najmniejsza liczba: {najmniejsza}")

if a == b == c:
  print("Wszystkie liczby sa takie same")
  pass
elif a != b and b != c and a != c:
  print("Wszystkie liczby sa rozne")
else: 
  print("Dwie liczby sa takie same")

parzyste = (a %2 == 0) + (b %2==0) + (c %2==0)
if parzyste == 3:
  print("Wszystkie liczby sa parzyste")
elif parzyste == 0:
  print("Wszystkie liczby sa nieparzyste")
else: 
  print("Liczby sa mieszane (parzyste i nieparzyste)")