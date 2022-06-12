import requests
import typing
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the games index.")


def deals(request):
    data = {}
    req = requests.get(
        "https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice=15"
    )

    if req.status_code == 200:
        data: typing.List[typing.Dict[str, str]] = json.loads(req.text)
    else:
        raise HttpResponseBadRequest("Could not fetch data from source")

    return render(request, "games/deals.html", {"games": data})
