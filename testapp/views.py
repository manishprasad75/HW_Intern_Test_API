from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def UserDetailAPI(request):
    if request.method == 'GET':
        data = request.body
        try:
            data = json.loads(data)
        except ValueError:
            return JsonResponse({'msg': 'Please provide valid data'})
        email = data.get('email', None)
        user_id = data.get('user_id', None)
        password = data.get('password', None)

        if email:
            user = User.objects.filter(email=email).first()
            if user:
                p_data = {
                    "user_id": user.id,
                    "login_type": "signin"
                }
                return JsonResponse(p_data)
            else:
                p_data = {
                    "user_id": "not registered",
                    "login_type": "signup"
                }
                return JsonResponse(p_data)

        if user_id and password:
            user = User.objects.filter(id=user_id).first()
            if user:
                if user.username is None:
                    user.username = user.email
                    user.save()
                user = authenticate(request, username=user.username, password=password)
                if user:
                    p_data = {"message": "login Successful"}
                else:
                    p_data = {"message": "failed"}
            else:
                p_data = {"message": "failed"}
            return JsonResponse(p_data)
        return JsonResponse({'msg': 'Please provide valid data'})
    
    if request.method == 'POST':
        data = request.body
        data = json.loads(data)

        try:
            user = User(email=data['email'], password=data['password'], first_name=data['first_name'], last_name=data['last_name'], username=data['email'])
            user.save()
            p_data = {"message": "Resource stored successfully"}
            return JsonResponse(p_data)
        except :
            p_data = {"message": "Something Goes Wrong"}
            return JsonResponse(p_data)
            
        


        

        
        

# def one(request):
#     email = request.body
#     user = User.objects.filter(email=email).first()
#     if user:
#         response = {}
#     else:
#         response = {}

#     return Response(response)


# def two(request):
#     user_id = request.body.get("user_id")
#     password = request.body.get("password")
    
#     user = User.objects.filter(id=user_id).first()
#     if user:
#         login(request, user)
#         pass
#     else:
#         pass


# def three(request):
#     first_name = request.body.get("first_name")
#     last_name = request.body.get("last_name")
#     email = request.body.get("email")
#     password = request.body.get("password")

#     User(first_name=).save()
