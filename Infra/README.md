# Infrastruktura

W tym folderze znajdują się skrypty Ansibla odpowiadające za konfiguracje Raspberry.

Uruchamianie:
```
ansible-playbook -i <Rasp IP address>, rasp.yml 
```

Aby przyśpieszyć proces można ograniczyć się jedynie do pewnego podzbioru czynności, np.:
```
ansible-playbook -i <Rasp IP address>, rasp.yml --tags code
```
Ta komenda spowoduje wrzucenie zmienionych oraz nowych plików z kodem zamka na Raspberry PI.

Zdefiniowane są następujące tagi:

| Tag      | Czynność                                                                                        |
|----------|-------------------------------------------------------------------------------------------------|
| users    | Konfiguruje użytkowników mająchych zdalny dostęp do Raspa (po ssh)                              |
| packages | Instaluje wymagana pakiety (apt i pip) oraz aktualizuje wszystki zainstalowane pakiety (apt)    |
| config   | Wgrywa całą konfigurację systmową potrzebną do prawidłowego działania zamka, w tym kopiuje kod  |
| code     | Wrzuca nową wersję kodu oraz skryptów                                                           |
