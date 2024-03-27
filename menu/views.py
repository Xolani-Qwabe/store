from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f'''<br>
    <br>Path: {path}
    <br>Address: {address}
    <br>Scheme: {scheme}
    <br>Method: {method}
    <br>User agent: {user_agent}
    <br>Path info: {path_info}
    <br> Response header: {response.headers}
    
    '''
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def menu(request, dish):
    items = {
        'pasta': 'Pasta is a type of noodle',
        'falafel': 'Falafel are deep fried patties or balls',
        'cheesecake': 'Cheesecake is a type of dessert'
    }
    
    description = items[dish]
    return HttpResponse(f'<h2> {dish} </h2>' + description)
    
    



