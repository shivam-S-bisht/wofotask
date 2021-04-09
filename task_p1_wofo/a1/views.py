from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

# import models for use
from a1.models import Person



# views .....

@csrf_exempt
# @api_view(["POST"])
def create(request):

    json_body = json.loads(request.body)  # string -> json

    if "name" in json_body:
        p = Person(name=json_body["name"], plan=json_body["plan"],
                signalString=json_body["signal_string"])
        p.save()
        # print(p.id)

        return HttpResponse("Created with form id:", p.id)
    
    else: return HttpResponseBadRequest("A key parameter is missing")


@csrf_exempt
def update(request):

    json_body = json.loads(request.body)  # string -> json

    if "formid" in json_body:
        if Person.objects.filter(id=json_body["formid"]).exists():
            p = Person.objects.get(id=json_body["formid"])
            p.name = json_body["name"]
            p.manualbooleanfield = json_body["manualbooleanfield"]
            p.plan = json_body["plan"]
            p.save()

            return HttpResponse("Updated")

        else: return HttpResponseBadRequest("No object fouund with id")

    else: return HttpResponseBadRequest("A key parameter is missing")





@csrf_exempt
def add_ratings(request):

    json_body = json.loads(request.body)  # string -> json

    if "formid" in json_body:

        if Person.objects.filter(id=json_body["formid"]).exists():
            p = Person.objects.get(id=json_body["formid"])
            p.rating = json_body["rating"]
            p.save()

            return HttpResponse("Rating added")

        else: return HttpResponseBadRequest("No object found with id", json_body["formid"])

    else: return HttpResponseBadRequest("A key parameter is missing")



# def getallpersons(request):
#     all_persons_data = Person.objects.all()
#     print(all_persons_data)
#     return "ok"
