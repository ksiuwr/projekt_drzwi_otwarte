# Projekt Drzwi Otwarte

[![CircleCI](https://circleci.com/gh/ksiuwr/projekt_drzwi_otwarte.svg?style=shield)](https://circleci.com/gh/ksiuwr/projekt_drzwi_otwarte)

## Opis

To repozytorium zawiera dokumentację oraz kod powstały podczas projektu **Drzwi Otwarte**. Projekt ma na celu skonstruowanie i zamontowanie autorskiego systemu kontroli dostępu do pokoju Koła Studentów Informatyki. 

## Konstrukcja

Projekt bazuje na Raspberry PI z czytnikiem kart RFID/NFC PN532 sterującym elektrozaczepem przy pomocy przekaźnika SRD-05. Całość jest umieszcona w dwóch puszkach elektrycznoinstalacyjnych, z których mniejsza z czytnikiem jest umieszczona po zewnętrznej stronie, a większa z Raspberry oraz przekaźnikiem po stronie wewnętrznej. Do autoryzacji użytkowników używamy ich legitymacji studenckich. 

## Infrastruktura 

Na Raspberry jest zainstalowany Raspbian Lite. Wszystkie rzeczy potrzebne do uruchomienia projektu na Raspie zostały opiane przy pomocy skryptów w Ansible. 

## Oprogramowanie

Obsługa zamka jest realizowan poprzez 3 aplikacje napisane w Pythonie, komunikujące się za pomocą socketów Unixowych:
* `reader` - prosta aplikacja odczytująca dane z przyłożonych kart 
* `worker` - główna aplikacja odpowiedzialna za obsługę zamka
* `adder` - prosty skrypt ułatwiający dodawanie nowych użytkowników

Dwie pierwsze (`reader` i `worker`) są uruchamiane jako serwisy systemowe.

Kod sformatoawny jest zgodnie z PEP8 (`flake8`) oraz otypowany przy pomocy `mypy`.

## Zespół

Nad projektem pracują studenci UWR, członkowie Koła Studentów Informatyki.

* [Bożydar](https://github.com/Bozydarek/)
* [REDACTED]
* [REDACTED]
* [REDACTED]
