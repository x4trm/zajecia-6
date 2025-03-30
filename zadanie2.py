# Napisz program, który wczytuje długości 3 boków trójkąta, a następnie wyświetla w
# konsoli:
# - czy taki trójkąt może powstać (jeśli nie, nie wykonuj pozostałych kroków)
# Każdy bok musi być większy od zera, suma dwóch krótszych boków musi być dłuższa niż najdłuższy bok.
# - najkrótszy i najdłuższy bok
# - rodzaj trójkąta: równoboczny, równoramienny, różnoboczny
# - jego obwód
# - rodzaj nr 2 trójkąta: rozwartokątny, prostokątny, równokątny (= równoboczny)

# min, max 
# Twierdzenie Pitagorasa

a = float(input("Podaj dlugosc pierwszego boku: "))
b = float(input("Podaj dlugosc drugiego boku: "))
c = float(input("Podaj dlugosc trzeciego boku: "))

print(f"Podano boki: {a}, {b}, {c}")

najdluzszy_bok = max(a,b,c)
najkrotszy_bok = min(a,b,c)

print(f"Nadluzszy bok: {najdluzszy_bok}")
print(f"Najkrotszy bok: {najkrotszy_bok}")

obwod = a + b + c
print(f"Obwod wynosi: {obwod}")

sredni_bok = obwod - najkrotszy_bok - najdluzszy_bok

if najdluzszy_bok >= sredni_bok + najkrotszy_bok or a <= 0 or b <= 0 or c <=0:
  print("Podane boki nie utworza trójkata")
  exit()
  pass

# rownoboczny trojkat
if a == b == c:
  print("Trojkat rownoboczny")
  pass
# trojkat roznoboczny
elif a != b and a != c and b != c:
  print("Trojkat roznoboczny")
  pass
else: # Rownoramienny
  print("Trojakt rownoramienny")
  pass


kwadrat_najdluzszego_boku = najdluzszy_bok **2
suma_kwadratow_dwoch_bokow = sredni_bok**2 + najkrotszy_bok**2

if kwadrat_najdluzszego_boku == suma_kwadratow_dwoch_bokow:
  print("Trojkat prostokątny")
  pass
elif kwadrat_najdluzszego_boku > suma_kwadratow_dwoch_bokow:
  print("Trojkat rozwartokatny")
  pass
else:
  print("Trojkat ostrokatny")
  pass
