# Лабораторна робота 5

##### 1-4. Почитав про docker-compose та Flask.
##### 5. Створив папки my_app та tests і закинув туди файли.
##### 6. Перевірив чи працює сайт та запустив тести які успішно були пройдені:
![image alt](screenshot/1.png)
![image alt](screenshot/2.png)
##### 7-8. Створив два Dockerfile та Makefile, та заповнив їх.
###### - STATES:= app tests це змінні яким присвоюється значення (динамічно);
###### - REPO:= skorik-19/first_repository це репозиторій на Docker;
###### - .PHONY: $(STATES) це несправжні цілі;
###### - run виконує команди;
###### - docker-prune очищує ресурси.
