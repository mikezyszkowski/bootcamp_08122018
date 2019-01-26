class Employee():

    def __init__(self, name, last_name, hourly_rate):
        self.name = name
        self.last_name = last_name
        self.hourly_rate = hourly_rate
        self._registered_time = 0

    def register_time(self, hours):
        if hours > 8:
            self._registered_time += 8 + (hours - 8) * 2
        else:
            self._registered_time += hours

    def pay_salary(self):
        salary = self._registered_time * self.hourly_rate
        return salary


def test_employee_initialization():
        employee = Employee("Jan", "Kowalski", 100)
        assert employee.name == "Jan"
        assert employee.last_name == "Kowalski"
        assert employee.hourly_rate == 100


def test_register_time():
        employee = Employee("Jan", "Kowalski", 100)
        employee.register_time(5)
        employee.register_time(5)
        assert employee.pay_salary() == 1000
        assert employee.pay_salary() == 0


def test_pay_salary():
        employee = Employee("Jan", "Kowalski", 100)
        employee.register_time(5)
        assert employee.pay_salary() == 500
        assert employee_pay_salary() == 0


def test_pay_salary_over_hours():
        employee = Employee("Jan", "Kowalski", 100)
        employee.register_time(10)
        assert employee.pay_salary() == 800 + 400
        assert employee.pay_salary() == 0