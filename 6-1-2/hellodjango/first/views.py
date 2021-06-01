from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from random import sample
from django.shortcuts import render


def show_index(request):
    # return HttpResponse('<h1>Hello,Django!<h1>')
    fruits = [
        'Apple', 'Orange', 'Pitaya', 'Durian', 'Waxberry', 'Buleberry', 'Gtape', 'Peach', 'Pear', 'Banana', 'Watermelon', 'Mango'
    ]
    select_fruits = sample(fruits, 3)
    # content = '<h3>今天推荐的水果是：</h3>'
    # content += '<hr>'
    # content += '<ul>'
    # for fruit in select_fruit:
    #     content += f'<li>{fruit}</li>'
    # content += '</ul>'
    # return HttpResponse(content)
    return  render(request, 'index.html', {'fruits': select_fruits})