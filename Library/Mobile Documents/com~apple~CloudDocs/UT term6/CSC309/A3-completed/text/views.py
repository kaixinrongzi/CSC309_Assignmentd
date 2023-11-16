from django.views.decorators.http import require_http_methods
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Paragraph
import traceback, json

NUM_PARAGRAPH_PER_REQUEST = 5

@require_http_methods(["GET"])
def data(request):
    start = int(request.GET.get("paragraph", 1))
    end = start + NUM_PARAGRAPH_PER_REQUEST
    query = Paragraph.objects.filter(id__gte=start, id__lt=end).order_by('id')
    data = [ {
        'paragraph' : paragraph.id,
        'likes' : paragraph.likes,
        'content' : paragraph. content,
    } for paragraph in query ]
    if Paragraph.objects.filter(id=end).exists():
        response = { 'data' : data, 'next' : True }
    else:
        response = { 'data' : data, 'next' : False }
    return JsonResponse(response)

@require_http_methods(["POST"])
def like(request):
    try:
        data = json.loads(request.body)

        para = get_object_or_404(Paragraph, id=data['paragraph'])
        para.likes += 1
        para.save()
        return JsonResponse({'data' : {'likes' : para.likes }})
    except:
        traceback.print_exc()
    return JsonResponse({'message' : "Unknown error."}, status=400)
