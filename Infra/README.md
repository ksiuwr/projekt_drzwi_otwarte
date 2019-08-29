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
Ta komenda spowoduje wrzucenie zmienionych oraz nowych plików z kodem na Raspberry.