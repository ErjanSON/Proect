Пользовательская документация

Инструкции по использованию системы:
Система заказа пиццы предоставляет возможность заказа различных видов пицц и управления заказами. Для взаимодействия с системой, следуйте инструкциям ниже:

1. **Запуск программы:**
    - Запустите скрипт программы.
    - Введите пароль (pass) для доступа к функциям заказа и сохранения истории продаж.

2. **Основное меню:**
    - Выберите тип пиццы или другой продукт из представленного списка, используя соответствующую команду (например, `S` - мини пицца, `M` - средняя пицца и т.д.).
    - Выберите начинку для пиццы, если это требуется.
    - Посмотрите свой заказ с ценами.

3. **Оплата:**
    - Выберите тип оплаты (`наличные` или `безналичные`).
    - При выборе `наличных` введите сумму оплаты.
    - При необходимости получите сдачу, если оплата производится наличными.

4. **Сохранение истории:**
    - После завершения заказа, для сохранения истории продаж введите любой символ, чтобы данные были сохранены в файле sales_history.txt 

Описание команд и их функций:
- `S` - Выбрать мини пиццу.
- `M` - Выбрать среднюю пиццу.
- `L` - Выбрать большую пиццу.
- `B` - Выбрать гренки.
- `D` - Показать текущий заказ.
- `Q` - Принять заказ и завершить оформление.

Техническая документация

Описание архитектуры системы:
Система заказа пиццы построена на простой консольной архитектуре, использующей Python. Включает в себя следующие компоненты:
- **Функции заказа:** Отвечают за выбор пиццы, начинок и отображение заказа.
- **Функции оплаты:** Реализуют возможность выбора типа оплаты и расчета сдачи (при наличной оплате).
- **Управление историей продаж:** Система сохраняет информацию о заказах, включая время, состав заказа, стоимость и тип оплаты.
- **Проверка пароля:** Для доступа к функциям заказа и сохранения истории продаж требуется ввод пароля (pass).

Инструкции по установке и настройке:
Для использования системы заказа пиццы:
1. **Установка Python:**
    - Убедитесь, что на вашем компьютере установлен Python (рекомендуемая версия Python 3).
2. **Скачивание программы:**
    - Скачайте файл скрипта с кодом программы.
3. **Запуск программы:**
    - Откройте скрипт программы в среде разработки или запустите его через командную строку.
4. **Ввод пароля:**
    - При запуске программы будет запрошен пароль (pass) для доступа к функциям заказа и сохранения истории продаж.
