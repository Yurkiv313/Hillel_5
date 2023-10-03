import datetime
from django.http import HttpResponse
from faker import Faker
from django.shortcuts import render


# Create your views here.
def one_user(request):
    fake = Faker()
    x = []
    min_date = datetime.date(2000, 1, 1)
    max_date = datetime.date(2006, 12, 31)
    student = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "birth": fake.date_between_dates(date_start=min_date, date_end=max_date),
        "phone": fake.phone_number(),
        "address": fake.address(),
    }
    x.append(student)
    return render(request, "students_generate/student.html", {"students": x})


def students_generate(request):
    queryprms = request.GET
    count = queryprms.get("count", "1")
    if not count.isdigit() or (int(count) < 0 or int(count) > 100):
        return HttpResponse("Введіть додатнє число не більше 100")

    fake = Faker()
    c = int(count)
    x = []
    min_date = datetime.date(2000, 1, 1)
    max_date = datetime.date(2006, 12, 31)
    for _ in range(c):
        user = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "birth": fake.date_between_dates(date_start=min_date, date_end=max_date),
            "phone": fake.phone_number(),
            "address": fake.address(),
        }
        x.append(user)
    return render(request, "students_generate/student.html", {"students": x})

