from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import reverse

# Create your views here.
expected_price = 600
error = 0
def index(request):
    if "your_bid" not in request.session:
        request.session["your_bid"] = 0
    file = open("product/templates/product/data.txt", "r")
    val = int(file.readline())
    file.close()
    return render(request, "product/index.html", {
        "your_bid": request.session["your_bid"],
        'highest_bid': val,
        "expected_price": expected_price,
        "error": error
    })

def update(request):
    resp = 0
    if request.method == "POST":
        file = open("product/templates/product/data.txt", "r")
        val = int(file.readline())
        file.close()
        
        if request.POST.get('bid') == "" or int(request.POST.get('bid')) <= val:
             resp = 1
        else:
            request.session["your_bid"] = int(request.POST.get('bid'))
            if request.session["your_bid"] > val:
                file = open("product/templates/product/data.txt", "w")
                val = request.session["your_bid"]
                file.write(str(val))
    global error
    error = resp
    return HttpResponseRedirect(reverse("product:index"))
