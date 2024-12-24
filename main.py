from collections import namedtuple

# 1- masala

# Car = namedtuple('Car', ('brand', "model", 'year', 'price'))
#
# cars = [
#     Car(brand="BMW", model="M5 COMPITION", year=2024, price="150000$"),
#     Car(brand="BMW", model="i8", year=2024, price="200000$"),
#     Car(brand="Toyota", model="Supra", year=2020, price="90000$")
#         ]
# l = []
# for car in cars:
#     if car.year > 2020:
#         l.append(car)
# for i in l:
#     print(f"Brand: {i.brand}\nModel: {i.model}\nYear: {i.year}\nPrice: {i.price}\n")


# 2-masala


# Player = namedtuple('Player', ('name', 'position', 'score'))
#
# players = [
#     Player(name='Feruzjon', position='ss', score=83),
#     Player(name='Diyorbek', position='CF', score=82),
#     Player(name='Dilshod', position='AMF', score=70),
#     Player(name='Boburbek', position='CB', score=69),
#     Player(name='Ozodbek', position='GK', score=50)
#         ]
# a = max(players, key=lambda player: player.score)
# print(f"Eng yuqori natija: {a.name} ({a.position}) - {a.score} ball")


# 3-masala


# Book = namedtuple('Book', ('title', 'author', 'year', 'price'))
#
# books = [
#     Book(title='Otkan kunlar', author='Abdulla Qodiriy', year=2016, price=55000),
#     Book(title='Mehrobdan chayon', author='Abdulla Qodiriy', year=2017, price=50000),
#     Book(title='Dunyoning ishlari', author='Otkir Hoshimov', year=1982, price=60000),
#     Book(title='Oq kema', author='Chingiz Aytmatov', year=2019, price=22000),
#     Book(title='Qor qoynida lola', author='Utkir Hoshimov', year=1976, price=70000)
# ]
#
# s = 0
# for i in books:
#     if i.year > 2015:
#         s += i.price
# print(f"2015-yildan kiyin chiqarilgan kitoblarning umumiy narxi: {s}")


# 4-masala


# Employee = namedtuple('Employee', ('name', 'position', 'salary', 'experience'))
#
# employees = [
#     Employee(name='Feruzjon', position='Dasturchi', salary=2000, experience= 3),
#     Employee(name='Dilshod', position='Trader', salary=1500, experience= 6),
#     Employee(name='Diyor', position='Dasturchi', salary=1000, experience= 7),
#     Employee(name='Boburbek', position='Dasturchi', salary=700, experience= 2)
# ]
# print("Tajribali ishchilar:")
# for i in employees:
#     if i.experience > 5:
#         print(f"{i.name} - Tajribasi: {i.experience}")
# a = max(employees, key=lambda employee: employee.salary)
# print(f"Eng yuqori maosh: {a.name} ({a.salary})")


# 5-masala


# Competition = namedtuple('Competition', ('team', 'points'))
#
# competitions = [
#     Competition(team='Real Madrid', points=90),
#     Competition(team='Barcelona', points=85),
#     Competition(team='Manchester City', points=92),
#     Competition(team='Manchester Yunayted', points=70)
# ]
#
# a = max(competitions, key=lambda competition: competition.points)
# print(f"Eng kuchli jamoa: Team: {a.team} - {a.points} ochko")


# 6 - masala

# Weather = namedtuple('Weather', ('city', 'temperature', 'humidity'))
#
# weathers = [
#     Weather(city='Toshkent', temperature=40, humidity='10%'),
#     Weather(city='Navoiy', temperature=35, humidity='5%'),
#     Weather(city='Buxoro', temperature=30, humidity='2%'),
#     Weather(city='Samarqand', temperature=24, humidity='0%')
# ]
# print("Issiq shaharlar:")
# for i in weathers:
#     if i.temperature > 25:
#         print(f"{i.city} - {i.temperature} C")


# 7-masala


# Student = namedtuple('Student', ('name', 'math_score', 'english_score'))
#
# students = [
#     Student(name='Feruzjon', math_score=100, english_score=20),
#     Student(name='Diyorbek', math_score=99, english_score=40),
#     Student(name='Dilshod', math_score=80, english_score=50),
#     Student(name='Bobur', math_score=60, english_score=40)
# ]
#
# a = max(students, key=lambda student: student.math_score)
# print(f"Eng yuqori matematika bahosi: {a.name} ({a.math_score})")







# Student = namedtuple('Student', ('ismi', 'yoshi', 'kursi'))
#
# students = [
#     Student(ismi='Feruzjon', yoshi=20, kursi=3),
#     Student(ismi='Feruz', yoshi=20, kursi=3),
#     Student(ismi='Isfandiyor', yoshi=19, kursi=2),
#     Student(ismi='Diyorbek', yoshi=19, kursi=2)
# ]
# s = 0
# for i in students:
#     s += i.yoshi
# a = s / len(students)
# print(f"Studentlar yoshlaring o'rtachasi: {a}")




















