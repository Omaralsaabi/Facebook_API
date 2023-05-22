from .models import * 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import *
# Create your views here.



@api_view(['GET'])
def ids(requests, pk):
    
    try:
        
        facebook = FacebookDB.objects.filter(username = pk).first()
        return Response({'username':pk, 'fid':facebook.fid})
    except:
            if 'id=' in pk:
                fid = id_existed(pk)
                facebook = FacebookDB.objects.create(username = pk, fid = fid)
                return Response({'username':pk, 'fid':fid})
            else:
                facebook = get_id(pk)
                fid = facebook['fid']
                facebook = FacebookDB.objects.create(username = pk, fid = fid)

                if fid == 'Not Found':
                    facebook = get_id_with_proxy(pk)
                    fid = facebook['fid']
                    
                    facebook = FacebookDB.objects.get(username = pk)
                    facebook.fid = fid
                    facebook.save()
                    return Response({'username':pk, 'fid':fid})
                
                else:
                    return Response({'username':pk, 'fid':fid})

