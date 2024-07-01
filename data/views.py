from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
import pandas as pd

# Create your views here.
def index(request):
    return render(request, 'data/index.html')
def upload(request):
    
    if request.method == "POST":
        file = request.FILES['my_file']
        df = pd.read_csv(file)
        ht = df.set_table_attributes('class="table-style"').to_html()
    return HttpResponse(ht)