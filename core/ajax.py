# coding=utf-8
from annoying.decorators import ajax_request
from django.shortcuts import get_object_or_404

__author__ = 'alexy'


@ajax_request
def ajax_remove_item(request):
    if request.method == 'GET':
        if request.GET.get('item_id') and request.GET.get('item_model'):
            model = request.GET.get('item_model')
            item_id = request.GET.get('item_id')
            item = get_object_or_404(eval(model), pk=int(item_id))
            item.delete()
            return {
                'id': int(request.GET.get('item_id')),
                'model': request.GET.get('item_model'),
            }
        else:
            return {
                'error': True
            }
    else:
        return {
            'error': True
        }
