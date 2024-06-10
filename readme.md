# README

## Python

### Описание

Скрипт обрабатывает показатели трёх компаний (A, B, C) из Excel файла и рассчитывает среднее значение показателя за предыдущий год от выбранной даты.

### Файлы
- `data_processing.py`: Скрипт для обработки данных.
- `indicators.xlsm`: Excel файл с данными.
- `requirements.txt`: Список зависимостей.

### Запуск

1. **Установите зависимости:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Запустите скрипт:**
    ```sh
    python data_processing.py
    ```

3. **Введите данные:**
    - Название компании (A, B, или C).
    - Дату в формате `дд.мм.гггг`.

---

## SQL

### Описание

Задания связаны только с базой данных Northwind. AdventureWorksDW2014 не удалось успешно развернуть на машине.

### Файлы

- `Dockerfile`: Конфигурация Docker.
- `Notebook.ipynb`: Jupyter Notebook с заданиями.
- `SQLQuery_1.sql`, `SQLQuery_2.sql`: Конфигурация Northwind DB.

