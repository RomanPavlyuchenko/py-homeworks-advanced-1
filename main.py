from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime


def get_date():
    print(datetime.now().date())


if __name__ == '__main__':
    get_date()
    calculate_salary()
    get_employees()
