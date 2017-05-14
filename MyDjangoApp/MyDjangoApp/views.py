from django.http import HttpResponse

# importing loading from django template
from django.template import loader


# our view which is a function named index
def index(request):
    # getting our template
    template = loader.get_template('index.html')
    context = {
        'name' : 'Eric Xie',
        'fname': 'Beida Xie',
        'course': 'CS3240',
        'address': '2111 JPA Apt 16',
    }
    # rendering the template in HttpResponse
    return HttpResponse(template.render(context, request))