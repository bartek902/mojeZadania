from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Widok 1: Prosty tekst
def hello(request):
    return HttpResponse("Witaj w Django!")

# Widok 2: Dynamiczny z tekstem
def hello_name(request, name):
    return HttpResponse(f"Witaj, {name}!")

# Widok 3: Dynamiczny z szablonem
def hello_template(request, name):
    return render(request, "witaj/hello.html", {"name": name})

# Widok 4: Zadanie domowe - aktualna data i czas
def current_time(request):
    now = datetime.now()
    # Formatowanie: Dzisiaj jest: 22.09.2025, godzina: 18:42
    formatted_time = now.strftime("Dzisiaj jest: %d.%m.%Y, godzina: %H:%M")
    return render(request, "witaj/time.html", {"time_string": formatted_time})