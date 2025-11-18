import re

patron=r"ola" #tiene que empezar por r
texto="ola"
if re.match(patron,"oladam2"): #busca coincidencia la principio de la cadena con que empiece por le patron vale
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.search(patron,"loladam2"): #busca coincidencia de la cadena donde sea
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.fullmatch(r"ola",texto): #busca coincidencia exacta tiene que ser igual
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

print(re.fullmatch(patron,"ola")) #no devuelve boolean, solo un objecto o none

if re.fullmatch(r"[0-9]{3,5}","123445"): #NUM DEL 0 AL NUEVE, QUE SE REPITAN DE 3 A 5 VECES MAX
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.fullmatch(r"[0-9]+","123445"): #+,*,?(0 o 1)
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.fullmatch(r"[0-9]{8}[A-Za-zÑñ]","12344578s"): #min y may y ñs
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.fullmatch(r"[1-9]|1[0-2]","12"): #| (o) la primera tiene que ser 1 y la segunda cifra 0,1o2
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.fullmatch(r"(\w+)","123_srgg"): #w admite cualquier caracter alfanumerico y el underscore
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.fullmatch(r"[0-9]?","54"): #tiene que aparecer 0 veces o 1
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.fullmatch(r"[^5]{2}","34"): #el ^ es para que no sea 5 y que sólo sea 1 caracter(si pongo {2} tengo que poner dos numeros que no sean 5
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.fullmatch(r"[^H][^O]","FO"):
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")

if re.fullmatch(r"[678][0-9]{8}","618736987"): #[678] SIGNIFICA QUE TIENE QUE HABER UN SOLO NUMERO QUE SEA 6,7 U 8
    print("Hay coincidencia")
else:
    print("NO hay coincidencia")