from django.shortcuts import render

# Create your views here.
def faculty_dashboard(request):
    return render(request, "faculty_dashboard.html")
