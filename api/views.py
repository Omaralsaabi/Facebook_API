from django.shortcuts import render
from .models import * 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import *
# Create your views here.



@api_view(['GET'])
def ids(requests, pk):

    try:
        
        facebook = FacebookDB.objects.filter(username = pk).first()
        print (facebook)
        return Response({'username':pk, 'fid':facebook.fid})
    except:
            facebook = get_id(pk)
            fid = facebook['fid']

            facebook = FacebookDB.objects.create(username = pk, fid = fid)

            if fid == 'Not Found':
                facebook = get_id_with_proxy(pk)
                fid = facebook['fid']

                facebook = FacebookDB.objects.create(username = pk, fid = fid)
                
            else:
                return Response({'username':pk, 'fid':fid})

