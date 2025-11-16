from django.shortcuts import render
from .models import Constituency
from .models import Party
import random

# Database link
# postgresql://neondb_owner:npg_UJCHMr56yoRt@ep-raspy-water-ag4nnh5l.c-2.eu-central-1.aws.neon.tech/tag_ankle_serve_239654

def index(request):
    thought_number = random.randint(1, 5)
    if thought_number == 1:
        thought = "Every small step forward still moves you closer to where you want to be."
    elif thought_number == 2:
        thought = "You've already overcome so much—your resilience is one of your greatest strengths"
    elif thought_number == 3:
        thought = "There are good moments waiting for you today, even if you don't see them yet."
    elif thought_number == 4:
        thought = "You're allowed to grow, change, and start again whenever you need to"
    else:
        thought = "Someone's life is better because you’re in it—your presence matters."
    
    return render(request, "index.html", {"thought": thought})


def find_tax(pay):
    if pay <= 12500:
        tax = 0
    else:
        tax = (pay - 12500) * 0.2
    return tax


def valid_float(a_string):
    try:
        float(a_string)
        return True
    except (ValueError, TypeError):
        return False


def taxpage(request):
    tax = None

    if request.method == "POST":
        amount = request.POST.get("amount")
        if valid_float(amount):
            float_tax = find_tax(float(amount))
            tax = f"{float_tax:.2f}"
        else:
            tax = "error"
    return render(request, "taxpage.html", {"tax": tax})
# Create your views here.


def findyourMP(request):
    data_to_return = None
    if request.method == "POST":
        constituency_name = request.POST.get("wanted")
        data_to_return = Constituency.objects.filter(constituency_name__icontains=constituency_name)  # or whatever filter
    return render(request, "mpfind.html", {"data": data_to_return})


