
str_polz=input("Введите строку: ")#запрос строки от пользователя
allSogl="бвгджзйклмнпрстфхцчшщ"#обозначение согласных

soglasn=0#счетчик согласных
ind=[]#задаем значение переменной

for i in range(len(str_polz)):#цикл 
    lowerStr=str_polz[i].lower()#делаем буквы все нижнего регистра
    if lowerStr in allSogl:#проверка есть ли в строке согласные 
        ind.append(i)#добавление элемента 
        soglasn+=1#увеличение счетчика согласных 
        
print("индексы согласных :  ", ind)#вывод индексов согласных
print("Кол-во согласных в вашей строке: ", soglasn )#вывод на экран информации о согласных

