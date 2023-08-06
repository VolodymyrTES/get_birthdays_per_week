from datetime import datetime

users = [{'name': 'Slavik', 'birth': datetime(year=1991, month=8, day=14)},
         {'name': 'Vova', 'birth': datetime(year=1990, month=8, day=15)},
         {'name': 'Bob', 'birth': datetime(year=1987, month=8, day=16)},
         {'name': 'Julia', 'birth': datetime(year=1998, month=9, day=17)},
         {'name': 'Fara', 'birth': datetime(year=1998, month=8, day=16)},
         {'name': 'Vika', 'birth': datetime(year=2000, month=8, day=8)},
         {'name': 'Tonya', 'birth': datetime(year=2000, month=8, day=12)}]

def get_birthdays_per_week(users):

    current_date = datetime.now() #сьогоднішня дата
    list_of_birthdays = [i.get('birth')  for i in users] # список дати народжень користувачів
    list_of_names = [i.get('name') for i in users] # списко імен користувачів 
    
    monday = ''
    tuesday =''
    wednesday =''
    thursday =''
    friday = '' 

    m = 0
    for birth in list_of_birthdays:

        day_1 = datetime(year=current_date.year, month=birth.month, day=birth.day) 
        week_of_birt = day_1.strftime("%U") #тиждень дати народження
        week_now = current_date.strftime("%U") #тиждень поточний
        day_of_the_week = day_1.strftime("%A") # день тиждня 

        if current_date.month <= (day_1.month+1) and int(week_of_birt) == (int(week_now)+1) and day_1.day > current_date.day:  
            if day_of_the_week in ['Monday','Sunday']:
                monday += list_of_names[m]+ ', '
            if day_of_the_week == 'Tuesday':
                tuesday += list_of_names[m]+ ', '
            if day_of_the_week == 'Wednesday':
                wednesday += list_of_names[m]+ ', '
            if day_of_the_week == 'Thursday':
                thursday += list_of_names[m]+ ', '
            if day_of_the_week == 'Friday':
                friday += list_of_names[m]+ ', '
        elif current_date.month <= (day_1.month+1) and int(week_of_birt) == (int(week_now)) and day_1.day > current_date.day:    
            if day_of_the_week == 'Saturday':
                monday += list_of_names[m]+ ', '
        m+=1

    list = {'Monday':monday, 'Tuesday':tuesday, 'Wednesday':wednesday, 'Thursday':thursday, "Friday":friday}
    
    for key,value in list.items():
        if value != '':
            print(f'{key}: {value[:-2]}')
            
get_birthdays_per_week(users)
