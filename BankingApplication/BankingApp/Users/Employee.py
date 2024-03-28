from BankingApplication.BankingApp.Users.Person import Person


class Employee(Person):
    def __init__(self, name, age, address, employee_id, role):
        super().__init__(name, age, address)
        self._employee_id = employee_id
        self._role = role

    def display_info(self):
        print(f"EMPLOYEE INFO:")
        print(f"Name: {self._name}")
        print(f"Age: {self._age}")
        print(f"Address: {self._address}")
        print(f"Employee ID: {self._employee_id}")
        print(f"Role: {self._role}")
        print()
