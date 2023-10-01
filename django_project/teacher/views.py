import sqlite3
from django.shortcuts import render

from teacher.models import Teacher


# Create your views here.
def view_teacher(request):
    conn = sqlite3.connect("db.sqlite3")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM teacher_teacher")
    results = cursor.fetchall()
    teacher_list = []
    for row in results:
        row = Teacher(row[0], row[1], row[2], row[3], row[4])
        teacher_list.append(row)
    return render(request, "view_teacher/teacher.html", {"teachers": teacher_list})
