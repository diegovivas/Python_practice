#django
from django.http import HttpResponse
#utilites
from datetime import datetime
import json

def hello_world(request):
    """ hi """
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('la hora es {}'.format(now))

def sorted_(request):
    """ hi """
    try:
        numbers = request.GET['numbers']
        numbers = sorted([int(i) for i in numbers.split(",")])
        data = {
            'status': 'ok',
            'numbers': numbers,
            'message': 'Integers sorted successfully.'
        }
        json_l = json.dumps(data, indent=4)
        return HttpResponse(json_l, content_type='application/json')
    except:
        return HttpResponse('Error with Get')

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}!, welcome to platzigram'.format(name)
    return HttpResponse(message)
