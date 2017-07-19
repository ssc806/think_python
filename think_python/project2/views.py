import json
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Q

from models import CameraLocaiton

# Home page
def home_page(request):
    location_list = CameraLocaiton.objects.all().values_list('camera_id', 'address', 'latitude', 'longitude')
    location_list_json = json.dumps(list(location_list), cls=DjangoJSONEncoder)

    context = {
        'location_list_json' : location_list_json,
    }

    template = loader.get_template('project2/home_page.html')

    return HttpResponse(template.render(context, request))

# Return the json response to the ajax request
def search(request):
    results_json = {}
    if request.method == 'GET': # If the form is submitted
        search_query = request.GET.get('search_box', None)
        if search_query is not None:
            results_list = CameraLocaiton.objects.filter(Q(address__icontains = search_query)).values_list('camera_id', 'address', 'latitude', 'longitude')
            if results_list:
                results_json = json.dumps(list(results_list), cls=DjangoJSONEncoder)

    return JsonResponse(results_json, safe=False)
