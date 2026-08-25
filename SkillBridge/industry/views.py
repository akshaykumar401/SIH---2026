from django.shortcuts import render

# Create your views here.
def industry_dashboard(request):
    return render(request, "industry_dashboard.html")
