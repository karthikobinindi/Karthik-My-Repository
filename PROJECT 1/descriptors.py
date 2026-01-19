class MarksDescriptor:
    def __set__(self, obj, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks should be between 0 and 100")
        obj._marks = value

    def __get__(self, obj, objtype):
        return obj._marks


class SalaryDescriptor:
    def __get__(self, obj, objtype):
        raise PermissionError("Access Denied: Salary is confidential")

    def __set__(self, obj, value):
        obj._salary = value
