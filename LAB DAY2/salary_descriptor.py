class PositiveSalary:
    def __get__(self, obj, objtype=None):
        return obj._salary

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError("Salary must be a positive number")
        obj._salary = value
