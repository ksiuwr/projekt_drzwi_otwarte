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
| users    | Konfiguruje użytkowników mających zdalny dostęp do Raspa (po ssh)                               |
| packages | Instaluje wymagana pakiety (apt i pip) oraz aktualizuje wszystkie zainstalowane pakiety (apt)   |
| config   | Wgrywa całą konfigurację systemową potrzebną do prawidłowego działania zamka, w tym kopiuje kod |
| code     | Wrzuca nową wersję kodu, skryptów oraz bota Discord                                             |
| discord  | Wrzuca nową wersję bota Discord, instaluje jego zależności i rejestruje komendy                 |

Bot Discord potrzebuje na Raspberry Node.js (z repozytorium NodeSource) oraz pliku `Discord/.env` z `DISCORD_TOKEN`, `DISCORD_CLIENTID` i `DISCORD_GUILDID`. Ansible go nie kopiuje i nie nadpisuje, tak samo jak `Discord/node_modules`, które instaluje na miejscu `npm ci`.
