from django.shortcuts import render

# Create your views here.
def instution_dashboard(request):
    return render(request, "instution_dashboard.html")
