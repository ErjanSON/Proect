from os import system,name;
from datetime import datetime
Order_Choice = [];
Order_Cost = [];   
Order_Toppings = [];
Order_Toppings_Cost = [];
Sales_History = [];

# Проверка пароля--------------------------------------------------------------------------------------------------------------------------------------
def Check_Password():
    password = "pass"
    entered_password = input("Введите пароль: ")

    if entered_password == password:
        return True
    else:
        print("Неверный пароль!")
        return False


#Принятия заказа--------------------------------------------------------------------------------------------------------------------------------------
def Display_Order():
    if not Check_Password():
        return

    system('cls');
    
    Items_Total = 0;
    Toppings_Total = 0;
    Item_Number = 0;
    Topping_Number = 0;

    print("\nВаш заказ:");

    for x in Order_Choice:    
        Topping_Number = 0;
        print("\n---------------------------------------------------------------");     
        print("Товар: ",(Item_Number+1),"\b.",x,"  Цена:",Order_Cost[(Item_Number)]);
        Items_Total = Items_Total + Order_Cost[Item_Number];

        NumToppings = len(Order_Toppings[Item_Number]);
        print("\n         ","Количество",NumToppings,"Начинка:\n");

        for y in Order_Toppings[Item_Number]:
            print("         ",(Topping_Number+1),"\b.",y,"  Цена:",Order_Toppings_Cost[Item_Number][Topping_Number]);
            Toppings_Total = Toppings_Total + Order_Toppings_Cost[Item_Number][Topping_Number]; 
            Topping_Number = Topping_Number + 1;  
       
        Item_Number = Item_Number + 1; 
    
    Total_Cost = Items_Total + Toppings_Total;
    print("\n---------------------------------------------------------------"); 
    print("\nОбщее позиции:","$",Items_Total);
    print("Общее начинки:","$",Toppings_Total);
    print("Итого:","$",Total_Cost);        

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Работа с наличными и безналичными платежами--------------------------------------------------------------------------------------------------------------------------------------
    payment_type = input("\nВыберите тип оплаты (наличные / безналичные): ").lower()

    if payment_type == "наличные":
        cash_amount = float(input("Введите сумму наличными: "))
        change = cash_amount - Total_Cost
        if change >= 0:
            print(f"Ваша сдача: {change:.2f}")
        else:
            print("Недостаточно средств!")
            return
    elif payment_type == "безналичные":
        print("Оплата прошла успешно.")
    else:
        print("Неправильный тип оплаты!")
        return

    Sales_History.append({
        "Time": current_time,
        "Order": Order_Choice.copy(),
        "Order_Cost": Order_Cost.copy(),
        "Order_Toppings": Order_Toppings.copy(),
        "Order_Toppings_Cost": Order_Toppings_Cost.copy(),
        "Total_Cost": Total_Cost,
        "Payment_Type": payment_type,
        "Change": change if payment_type == "наличные" else None
    })

    Save_Sales_History()


    ContinueIT = input("\nДля продолжения введите любой символ:");
    ContinueIT = " ";

# Отчетность--------------------------------------------------------------------------------------------------------------------------------------
def Save_Sales_History():
    if not Check_Password():
        return
    
    with open("sales_history.txt", "a") as file:
        for sale in Sales_History:
            file.write(f"Time: {sale['Time']}\n")
            file.write("Order:\n")
            for i, item in enumerate(sale['Order']):
                file.write(f"{item}: ${sale['Order_Cost'][i]}\n")
                if item != "Гренки":
                    file.write("  Начинка:\n")
                    for j, topping in enumerate(sale['Order_Toppings'][i]):
                        file.write(f"    {topping}: ${sale['Order_Toppings_Cost'][i][j]}\n")
            file.write(f"Итого: ${sale['Total_Cost']}\n")
            file.write("\n\n")

#Выбор начинки--------------------------------------------------------------------------------------------------------------------------------------
def Pizza_Toppings():
    
    Toppings_Complete = "FALSE";
    Current_Toppings_Selection = [];
    Current_Toppings_Cost = [];

    while Toppings_Complete != "TRUE":
          print("\n------------------Меню------------------");
          print("|                                        |");
          print("|       (E)Сырный соус         ($1)      |");
          print("|       (X)Острый соус         ($0)      |");
          print("|       (B)Ананас              ($5)      |");
          print("|       (T)Помидоры            ($1)      |");
          print("|       (O)Оливки              ($1)      |");
          print("|       (G)Огурцы              ($1)      |");
          print("|       (J)Халапеньо           ($1)      |");     
          print("|       (P)Пеперони            ($2)      |");
          print("|       (S)Сосиски             ($2)      |");
          print("|       (H)Ветчика             ($2)      |");
          print("|       (C)Курица              ($2)      |");
          print("|       (A)Анчоусы             ($2)      |");
          print("|       (Q)Выход                         |");
          print("|                                        |");
          print("------------------------------------------","\n");
          CHOICE = input("Выберите позицию: ");
          CHOICE = CHOICE.upper();

          if CHOICE == 'E': 
               Current_Toppings_Selection.append("Сырный соус");
               Current_Toppings_Cost.append(1);
               print("Сырный соус."); 
          elif CHOICE == 'X': 
               Current_Toppings_Selection.append("Острый соус");
               Current_Toppings_Cost.append(0);
               print("Острый соус");               
          elif CHOICE == 'B': 
               Current_Toppings_Selection.append("Ананас");
               Current_Toppings_Cost.append(5);
               print("Ананас.");
          elif CHOICE == 'T': 
               Current_Toppings_Selection.append("Помидоры");
               Current_Toppings_Cost.append(1);               
               print("Помидоры.");  
          elif CHOICE == 'O': 
               Current_Toppings_Selection.append("Оливки");
               Current_Toppings_Cost.append(1);               
               print("Оливки.");
          elif CHOICE == 'G': 
               Current_Toppings_Selection.append("Огурцы");
               Current_Toppings_Cost.append(1);
               print("Огурцы");
          elif CHOICE == 'J': 
               Current_Toppings_Selection.append("Халапеньо");
               Current_Toppings_Cost.append(1);
               print("Халапеньо.");
          elif CHOICE == 'P': 
               Current_Toppings_Selection.append("Пеперони");
               Current_Toppings_Cost.append(2);               
               print("Пеперони.");  
          elif CHOICE == 'S': 
               Current_Toppings_Selection.append("Сосиски");
               Current_Toppings_Cost.append(2);               
               print("Сосиски.");
          elif CHOICE == 'H': 
               Current_Toppings_Selection.append("Ветчика");
               Current_Toppings_Cost.append(2);
               print("Ветчика");
          elif CHOICE == 'C': 
               Current_Toppings_Selection.append("Курица");
               Current_Toppings_Cost.append(2);               
               print("Курица.");
          elif CHOICE == 'A': 
               Current_Toppings_Selection.append("Анчоусы");
               Current_Toppings_Cost.append(2);
               print("Анчоусы");               
          elif CHOICE == 'Q': 
               print("Меню .");
               
               if len(Current_Toppings_Selection) < 1:
                  print("Не выбрано.");
                  Current_Toppings_Selection.append("Не выбрано.");
                  Current_Toppings_Cost.append(0);

               Toppings_Complete = "TRUE";                  
          else: 
               print("Неверная позиция.");

    Order_Toppings.append(Current_Toppings_Selection);
    Order_Toppings_Cost.append(Current_Toppings_Cost);       


#Выбор позиции заказа--------------------------------------------------------------------------------------------------------------------------------------
def Pizza_Main():
    
    system('cls');

    Order_Complete = "FALSE";   

    print("\n---------Добро пожаловать!-----------","\n");

    while Order_Complete != "TRUE":
          print("\n--------------Меню-----------------");
          print("|                                   |");
          print("|       (S)Мини Пицца               |");
          print("|       (M)Средняя Пицца            |");
          print("|       (L)Большая Пицца            |");
          print("|       (B)Гренки                   |");
          print("|       (D)Показать заказ           |");
          print("|       (Q)Принять заказ            |");
          print("|                                   |");
          print("-------------------------------------","\n");
          CHOICE = input("Выберите: ");
          CHOICE = CHOICE.upper();

          if CHOICE == 'S': 
               Order_Choice.append("Мини Пицца");
               Order_Cost.append(15);
               print("Мини Пицца.");
               Pizza_Toppings(); 
          elif CHOICE == 'M': 
               Order_Choice.append("Средняя Пицца");
               Order_Cost.append(20);
               print("Средняя Пицца.");
               Pizza_Toppings(); 
          elif CHOICE == 'L': 
               Order_Choice.append("Большая Пицца");
               Order_Cost.append(25);               
               print("Большая Пицца.");
               Pizza_Toppings();   
          elif CHOICE == 'B':   
               Order_Choice.append("Гренки");
               Order_Cost.append(5);               
               NO_Toppings_Selection = [];
               NO_Toppings_Cost = [];          
               NO_Toppings_Selection.append("Гренки без начинки.");
               NO_Toppings_Cost.append(0);
               Order_Toppings.append(NO_Toppings_Selection);
               Order_Toppings_Cost.append(NO_Toppings_Cost);             
               print("Гренки.");
          elif CHOICE == 'D': 
               Display_Order();             
          elif CHOICE == 'Q': 
               Display_Order();
               print("\nЗаказ принят!.\n");
               Order_Complete = "TRUE";                 
          else: 
               print("Неверно введенные позиции.") 


    print("\nПриятного аппетита!\n");

Pizza_Main();