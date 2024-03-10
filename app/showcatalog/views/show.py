from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from showcatalog.serializers import ShowSerializer
from showcatalog.models import Show
import requests


def log_to_mongodb(show_id: int, msg: str, method: str):
    """ Log the status of the request to MongoDB """
    url = 'http://127.0.0.1:3000/api/add-log'
    request_body = {'show_id': show_id, 'msg': msg, 'method': method}

    try:
        requests.post(url, json=request_body)
    except requests.exceptions.ConnectionError:
        print("Connection to logger service failed!")


# Create your views here.
@csrf_exempt
@api_view(['POST'])
def add_show(request):
    """
    Add a showcatalog
    Request Parameters:
    - name: string
    - start_year: integer
    - end_year: integer
    - rating: integer
    - age_rating: string
    """

    serializer = ShowSerializer(data=request.data)
    if serializer.is_valid():
        show = Show(
            name=request.data.get('name'),
            start_year=request.data.get('start_year'),
            end_year=request.data.get('end_year'),
            rating=request.data.get('rating'),
            age_rating=request.data.get('age_rating'),
        )
        show.save()

        log_to_mongodb(show.id, 'Added a show', 'POST')

        return HttpResponse('Added show')

    return HttpResponse('Data not valid')


@csrf_exempt
@api_view(['PATCH'])
def update_show(request):
    """
    Update a showcatalog by id (Show id)
    Request Parameters:
    - show_id: integer
    - name: string
    - start_year: integer
    - end_year: integer
    - rating: integer
    - age_rating: string
    """
    serializer = ShowSerializer(data=request.data)
    if serializer.is_valid():
        show_id = request.data.get('show_id')
        show = Show.objects.get(id=show_id)
        show.name = request.data.get('name')
        show.start_year = request.data.get('start_year')
        show.end_year = request.data.get('end_year')
        show.rating = request.data.get('rating')
        show.age_rating = request.data.get('age_rating')
        show.save()

        log_to_mongodb(show.id, 'Updated a show', 'PATCH')

        return HttpResponse('Updated show')

    return HttpResponse('Data not valid!')


@csrf_exempt
@api_view(['DELETE'])
def delete_show(request):
    """
    Delete a showcatalog by id (Show id)
    Route: /showcatalog/delete-showcatalog?show_id={number}
    Example Route: /showcatalog/delete-showcatalog?show_id=1
    URL Parameters:
    - show_id: integer
    """

    show_id = request.GET.get('show_id', '')
    if show_id != '':
        show = Show.objects.filter(id=show_id)
        show.delete()

        log_to_mongodb(show_id, 'Deleted a show', 'DELETE')

        return HttpResponse('Deleted show')

    return HttpResponse('The show_id is empty!')


@csrf_exempt
@api_view(['GET'])
def fetch_show(request):
    """
    Fetch a showcatalog by id (Show id)
    Route: /showcatalog/fetch-showcatalog?show_id={number}
    Example Route: /showcatalog/fetch-showcatalog?show_id=1
    URL Parameters:
    - show_id: integer
    """

    show_id = request.GET.get('show_id')

    if show_id != '':
        show = Show.objects.get(id=show_id)
        return JsonResponse(
            {
                'name': show.name, 'start_year': show.start_year,
                'end_year': show.end_year, 'rating': show.rating,
                'age_rating': show.age_rating
            }
        )
    return JsonResponse({'err_msg': 'The show_id is empty!'})
