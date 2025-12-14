from django.shortcuts import render

def power(request):
    power = ""
    if request.method == "POST":
        intensity = float(request.POST.get("intensity"))
        resistance = float(request.POST.get("resistance"))
        power = intensity ** 2 * resistance

    return render(request, "myapp/my.html", {"power": power})


