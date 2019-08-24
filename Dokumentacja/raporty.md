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

### Spotkanie #9 - 21.05.2019

Na dzisiejszym spotkaniu w dalszym ciągu rozwijajiśmy aplikację. Dodaliśmy logowanie błędów, powydzielaliśmy moduły i zmieniliśmy sockety na unixowe. Pomęczyliśmy się z flake8, naprawiliśmy kilka błędów i zaplanowaliśmy dalszą pracę.

### Spotkanie #10 - 30.05.2019

Dziś udało się nam skończyć MVP - nasza aplikacja umożliwia już otwieranie zamka na podstawie odczytania karty i rekordu w bazie, dodawanie nowych użytkowników i obsługę ewentualnych błędów. Popracowaliśmy nad jakością naszego kodu i zaplanowaliśmy następne spotkanie.

### Spotkanie #11 - 06.06.2019

Podczas dzisiejszego spotkania zrobiliśmy ostatnie zakupy, a także stworzyliśmy skrypt do włączania i wyłączania aplikacji.

### Spotkanie #12 - 13.06.2019

Na dzisiejszym spotkaniu testowo zamontowaliśmy szyld oraz dopracowaliśmy skrypt do włączania i wyłączania aplikacji.

### Spotkanie #13 - 24.08.2019

Szczęśliwa 13 - to właśnie numer spotkania, na którym skończyliśmy montaż. Udało się nam przymocować zamek i pudełka z układami, dopasować profil drzwiowy do zamka, wmontować klamkę z gałką i przeprowadzić testy integracyjne. Zamek działa, ale w projekcie przyda się jeszcze kilka małych poprawek i feacherów czym zajmiemy się w przyszłości.
