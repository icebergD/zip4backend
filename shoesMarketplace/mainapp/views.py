import numpy
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response

from .models import *
from .algorithm import *

import cv2 as cv
from PIL import Image as Im


def hello(request):
    return HttpResponse("Hello world")


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def search_photo(request):
    if request.method == 'POST':
        if request.method == 'POST':
            # загрузка фото из запроса
            upload = request.FILES['photo']
            img = Im.open(upload)
            open_cv_image = numpy.array(img)
            open_cv_image = open_cv_image[:, :, ::-1].copy()

            # выгружаем фото из базы
            images = ImageShoe.objects.all().values()
            ids = []
            rates = []
            hist1 = hist_generate(open_cv_image)
            for hist in images:
                hist_str2 = hist['histogram']
                hist2 = np.fromstring(hist_str2, dtype=np.float)
                # rate = hist_compare(hist1, hist2)
                # ids.append(hist['id'])
                # rates.append(rate)

            result = zip(rates, ids)
            print(result)
            # desc1 = descriptor_generate(img)
            # for descr in images:
            #     desc2 = descr['descriptor']
            #     rate = descriptor_compare(desc1, desc2)


        result = Shoe.objects.all().values()

        return Response({'result': result})
