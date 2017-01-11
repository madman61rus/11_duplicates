# Anti-Duplicator

Данная программа ищет в указанной папке дубликаты файлов и если они
найдены, выводит их на экран. Критерием дублирования является название
файла и его размер

### Как использовать

Для запуска программы, ей необходимо указать путь, по которому
нужно искать дубликаты, с помощью ключа -p или --path

Пример использования программы
```
python dublicates.py -p ~/test_path
```

Пример вывода на консоль
```
Найден дубликат файла python-learn.txt, путь /home/vkompaniec/PycharmProjects/11_duplicates/test/3/33/python-learn.txt, размер 7848
Найден дубликат файла python-learn.txt, путь /home/vkompaniec/PycharmProjects/11_duplicates/test/2/python-learn.txt, размер 7848
Найден дубликат файла statement (5).pdf, путь /home/vkompaniec/PycharmProjects/11_duplicates/test/1/statement (5).pdf, размер 112624
Найден дубликат файла statement (5).pdf, путь /home/vkompaniec/PycharmProjects/11_duplicates/test/1/11/statement (5).pdf, размер 112624
Найден дубликат файла statement (5).pdf, путь /home/vkompaniec/PycharmProjects/11_duplicates/test/statement (5).pdf, размер 112624
Найден дубликат файла Алексей Юхнин_Презентация.pdf, путь /home/vkompaniec/PycharmProjects/11_duplicates/test/1/11/Алексей Юхнин_Презентация.pdf, размер 472681
Найден дубликат файла Алексей Юхнин_Презентация.pdf, путь /home/vkompaniec/PycharmProjects/11_duplicates/test/1/Алексей Юхнин_Презентация.pdf, размер 472681
```

# Цели проекта

Этот код написан в целях обучения. Курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
