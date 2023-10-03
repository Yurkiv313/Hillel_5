from django.shortcuts import render

from teacher.models import Teacher


# Create your views here.
def view_teacher(request):
    k = Teacher.objects.all().values()

    return render(request, "view_teacher/teacher.html", {"teachers": k})
