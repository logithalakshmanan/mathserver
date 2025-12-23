# Ex.04 Design a Website for Server Side Processing
# Date:28.11.2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :
```
my.html

<!DOCTYPE html>
<html>
<head>
    <title>Electric Power Calculator</title>

    <style>
        body{
            min-height:100vh;
            display:flex;
            justify-content:center;
            align-items:center;
            background: linear-gradient(120deg, #1d2671, #c33764);
            font-family: Arial, sans-serif;
        }

        .box{
            width:380px;
            padding:35px;
            background:white;
            border-radius:15px;
            box-shadow:0 10px 25px rgba(0,0,0,0.3);
            text-align:center;
        }

        h2{
            color:#333;
            margin-bottom:20px;
        }

        label{
            display:block;
            text-align:left;
            margin-top:15px;
            color:#555;
        }

        input{
            width:100%;
            padding:10px;
            margin-top:5px;
            border-radius:8px;
            border:1px solid #ccc;
        }

        button{
            width:100%;
            margin-top:25px;
            padding:12px;
            background:#1d2671;
            color:white;
            border:none;
            border-radius:10px;
            font-size:16px;
            cursor:pointer;
        }

        button:hover{
            background:#c33764;
        }

        .result{
            margin-top:20px;
            font-size:18px;
            color:#222;
        }
    </style>
</head>

<body>

<div class="box">
    <h2>Electric Power Calculator</h2>

    <form method="POST">
        {% csrf_token %}

        <label>Intensity (I)</label>
        <input type="number" name="intensity" step="any" required>

        <label>Resistance (R)</label>
        <input type="number" name="resistance" step="any" required>

        <button type="submit">Calculate</button>
    </form>

    {% if power != "" %}
        <div class="result">
            <strong>Power:</strong> {{ power }} Watts
        </div>
    {% endif %}
</div>

</body>
</html>

views.py

from django.shortcuts import render

def power(request):
    power = ""
    if request.method == "POST":
        intensity = float(request.POST.get("intensity"))
        resistance = float(request.POST.get("resistance"))
        power = intensity ** 2 * resistance

    return render(request, "myapp/my.html", {"power": power})

    from django.contrib import admin
from django.urls import path, include

urls.py
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("myapp.urls")),
]
```

    

# SERVER SIDE PROCESSING:
![alt text](<Screenshot (137).png>)
# HOMEPAGE:
![alt text](<Screenshot (135).png>)
# RESULT:
The program for performing server side processing is completed successfully.
