# Raporty ze spotkań
---

### Spotkanie #1 - 12.03.2019

Na pierwszym spotkaniu omówiliśmy założenia projektu i przypomnieliśmy sobie ogólny pomysł, który powstał pół roku temu.
Rozpisaliśmy i omówiliśmy dokładnie tematy związane z:
* Dokumentacją
* Fizyczną modyfikacją istniejących drzwi
* Wydrukiem puszek (druk 3D)
* Złożeniem układu

A także skonfigurowaliśmy tablicę na trello i przepisaliśmy omówione taski do niej (z podziałem na w/w kategorie)

### Spotkanie #2 - 19.03.2019

Dziś ogarnęliśmy repozytorium na GitHubie i omówiliśmy kwestie nie rozwiązane na poprzednim spotkaniu. Dodatkowo omówiliśmy jak podłączymy cały układ.

### Spotkanie #3 - 28.03.2019

Na dzisiejszym spotkaniu zlutowaliśmy nóżki do czytnika RFID (przy współpracy z Continuum) oraz podłączyliśmy go do Raspa. Napisaliśmy prosty skrypt odczytujące dane z kart Mifare, a także ustaliliśmy co należy jeszcze dokupić (przetwornica).

### Spotkanie #4 - 04.04.2019

Dzisiaj opisaliśmy za pomocą skryptów Ansible większą część obecnej już na Raspie konfiguracji oraz dodaliśmy konta dla członków projektu. Dogadaliśmy sprawy układu elektronicznego i zrobiliśmy więcej zdjęć przedstawiających nas przy pracy.

### Spotkanie #5 - 11.04.2019

Na dzisiejszym spotkaniu przedyskutowaliśmy sprawę bazy danych, postawiliśmy SQLite i stworzyliśmy pierwsze skrypty. Dodatkowo ogarnęliśmy techniczne aspekty montażu zamka.

### Spotkanie #6 - 25.04.2019

Dziś podłączyliśmy zamek do Raspa tworząc jednocześnie działający układ. Do tego stworzyliśmy bazę danych i zrobiliśmy MVP: odblokowywanie zamka po przyłożeniu autoryzowanej karty i blokowanie go po okresie dwóch sekund. Pobawiliśmy się układem sprawdzając czy zachowuje się jak powinien i przedyskutowaliśmy dalszy plan działania.

### Spotkanie #7 - 09.05.2019

Dzisiaj zajęliśmy się oprogramowaniem: ustaliliśmy architekturę całego systemu (3 procesy komunikujące się z sobą) i zaimplementowaliśmy skrypt realizujący nadawanie praw do otwierania drzwi dla nowej osoby. Dodatkowo rozszerzyliśmy bazę danych o informacje kiedy ostatnio dany użytkownik otwierał drzwi.

### Spotkanie #8 - 18.05.2019

Dzisiejsze spotkanie miało charakter informacyjno-dyskusyjny. Omówiliśmy aktualny stan projektu, dalszy kierunek rozwoju oprogramowania oraz zadania i problemy związane z montażem. Przedyskutowaliśmy też pomysły zmian i stworzyliśmy listę zadań do zrobienia na kolejnych spotkaniach.
