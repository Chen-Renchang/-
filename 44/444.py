class Student:
    def __init__(self, fio, age, group_number, average_score):
        self.fio = fio
        self.age = age
        self.group_number = group_number
        self.average_score = average_score

    def print_info(self):
        return f"ФИО: {self.fio}, Возраст: {self.age}"

    def scholarship_amount(self):
        if self.average_score == 5:
            return 6000
        elif self.average_score < 5:
            return 4000
        else:
            return 0

    def compare_scholarship(self, other):
        if self.scholarship_amount() > other.scholarship_amount():
            return "больше"
        elif self.scholarship_amount() < other.scholarship_amount():
            return "меньше"
        else:
            return "равно"


class Aspirant(Student):
    def __init__(self, fio, age, group_number, average_score, research_work):
        super().__init__(fio, age, group_number, average_score)
        self.research_work = research_work

    def scholarship_amount(self):
        if self.average_score == 5:
            return 8000
        elif self.average_score < 5:
            return 6000
        else:
            return 0


# Пример использования
student1 = Student("Иванов Иван Иванович", 20, "1-20", 4.8)
aspirant1 = Aspirant("Петров Петр Петрович", 25, "2-15", 5, "Исследование методов машинного обучения")

# Вывод информации
student1_info = student1.print_info()
aspirant1_info = aspirant1.print_info()

# Размер стипендии
student1_scholarship = student1.scholarship_amount()
aspirant1_scholarship = aspirant1.scholarship_amount()

# Сравнение стипендий
comparison = aspirant1.compare_scholarship(student1)

# Adding print statements
print(student1_info)
print(aspirant1_info)
print(f"Размер стипендии студента: {student1_scholarship}")
print(f"Размер стипендии аспиранта: {aspirant1_scholarship}")
print(f"Сравнение стипендий: аспирант {comparison} студента")
