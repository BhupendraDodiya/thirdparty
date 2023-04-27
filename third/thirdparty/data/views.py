from django.shortcuts import render
import requests
from django.http import HttpResponse

# Create your views here.
def showdata(request):
    data = requests.get('http://tanveerpp.pythonanywhere.com/product/')
    data = data.json()
    return HttpResponse(data)

def showone(request):
    id = '390'
    data = requests.get('http://tanveerpp.pythonanywhere.com/product/'+id)
    data = data.json()
    print(data)
    return HttpResponse(data)

def createdata(request):
    name = 'norde 5 '
    price = '19999'
    cat = 'mobile'
    cmp = 'one+'
    res = {'name':name,'price':price,'cat':cat,'cmp':cmp}
    requests.post('http://tanveerpp.pythonanywhere.com/product/',res)
    data = requests.get('http://tanveerpp.pythonanywhere.com/product/')
    return HttpResponse(data)

def updatedata(request):
    id = '399'
    name = 'norde r1 '
    price = '19999'
    cat = 'mobile'
    cmp = 'one plus'
    res = {'name':name,'price':price,'cat':cat,'cmp':cmp}
    requests.put('http://tanveerpp.pythonanywhere.com/product/'+id+'/',res)
    data = requests.get('http://tanveerpp.pythonanywhere.com/product/')
    return HttpResponse(data)



def deletedata(request):
    id = '405'
    requests.delete('http://tanveerpp.pythonanywhere.com/product/'+id)
    data = requests.get('http://tanveerpp.pythonanywhere.com/product/')
    return HttpResponse(data)


