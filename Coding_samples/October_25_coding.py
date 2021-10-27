# in-class coding from Monday, October 25

# more functions
def get_days():
    """
    asks user for start day and end day in from mm/dd/yyyy
    :return: list containing start date (day of year, year) and end date
    (day of year, year)
    """
    start = input("Please enter the start date - e.g., your date of birth - in form mm/dd/yyyy")
    finish = input("Please enter the end date - e.g., today's date - in form mm/dd/yyyy")
#    print(start,finish)
    start_list = start.split('/')
    finish_list = finish.split('/')
    for i in range(len(start_list)):
        start_list[i] = int(start_list[i])
        finish_list[i] = int(finish_list[i])
#    print(start_list,finish_list)
#    print(answer)
    result_list = []
    result_list.append(start_list)
    result_list.append(finish_list)
    return result_list

def calculate_day(month, day):
    date = (month-1)*30 + day
    if month == 1 or month == 4 or month == 5:
        return date
    elif month == 3:
        return date-1
    elif month ==2 or month == 6 or month == 7:
        return date+1
    elif month == 8:
        return date+2
    elif month == 9 or month == 10:
        return date+3
    else:
        return date+4

def calc_age(start_day, start_year, end_day, end_year):
    if end_day >= start_day:
        age = 365*(end_year - start_year) + (end_day - start_day)
    else:
        age = 365 *(end_year - start_year - 1) + (365 + end_day - start_day)
    return age

if __name__ == "__main__":

    answer  = get_days()
    print(answer)
#     print(start_list, finish_list)
    data_list = []
    for i in range(len(answer)):
        month = answer[i][0]
        day = answer[i][1]
        day_of_year = calculate_day(month,day)
        temp_list = []
        temp_list.append(day_of_year)
        temp_list.append(answer[i][2])
        data_list.append(temp_list)
 #   print(data_list)
 #       print(month, day, "day of year is", day_of_year)
    the_answer = calc_age (data_list[0][0], data_list[0][1], data_list[1][0],data_list[1][1])
    print ("the answer is that you are ", the_answer, " days old")
