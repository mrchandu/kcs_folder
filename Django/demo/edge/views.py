from django.shortcuts import render
#from models import edge

def student_show(request):
    #student = edge.objects.order_by('roll_no')
    return render(request, 'student/student_show.html', {'student': student})
