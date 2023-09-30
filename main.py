from datetime import date, datetime, timedelta

def get_period(start_date:date, days:int):
    week = {}
    for _ in range(days + 1):
        week[start_date.day, start_date.month] = start_date.year
        start_date += timedelta(1)

    return week



def get_birthdays_per_week(users):
    if len(users) == 0:
        users = {}
    else:

        start_date = date.today()
        period = get_period(start_date, 7)


        week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday")

        monday = []
        tuesday = []
        wednesday = []
        thursday = []
        friday = []
        b_day_weekly = [monday, tuesday, wednesday, thursday, friday]


        for user in users:
            b_day: date = user["birthday"]
            if (b_day.day, b_day.month) in list(period):

                if date(start_date.year, b_day.month, b_day.day).weekday() == 0:
                    monday.append(user["name"] )

                elif date(start_date.year, b_day.month, b_day.day).weekday() == 1:
                    tuesday.append(user["name"] )

                elif date(start_date.year, b_day.month, b_day.day).weekday() == 2:
                    wednesday.append(user["name"] )

                elif date(start_date.year, b_day.month, b_day.day).weekday() == 3:
                    thursday.append(user["name"] )

                elif date(start_date.year, b_day.month, b_day.day).weekday() == 4:
                    friday.append(user["name"] )

                else:
                    monday.append(user["name"] )

            b_day_dct = weekend_move(start_date, 7, b_day_weekly)

                
        users = {}
        for item in b_day_dct.items():

            if len(item[1]) > 0:
                users[item[0]] = item[1]
         

    return users


def weekend_move(day: date, days:int, birthdays:list):
    week_days = ("Monday","Tuesday","Wednesday","Thursday","Friday")
    b_day_dct = {}
    
    i = 0
    for _ in range(days+1):
        
        if (day + timedelta(i)).weekday() <= 4:
            b_day_dct[week_days[(day + timedelta(i)).weekday()]] = birthdays[(day + timedelta(i)).weekday()]
            i += 1
        else:
            i += 1
        
    return b_day_dct



if __name__ == "__main__":
    users = [
            {
                "name": "John",
                "birthday": (date.today() + timedelta(days=5)),
            },
            {
                "name": "Doe",
                "birthday": (date.today() + timedelta(days=6)),
            },
            {"name": "Alice", "birthday": (date.today() + timedelta(days=3))},
        ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
  
     
    

