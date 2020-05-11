from django.shortcuts import render, redirect


def favorites_list(request):
    context = {}
    return False


def add_to_favorites(request, id):
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = []
        else:
            request.session['favorites'] = request.session['favorites']

        # если не нужен список со словарями, а нужен список с просто ids
        # например, если избранное нужно только для одного типа объектов
        # get ids list
        # favorites_ids_list = []
        # for item in request.session['favorites']:
        #     favorites_ids_list.append(item['id'])

        # check if item exist in list of dicts
        item_exist = next((item for item in request.session['favorites'] if
                           item['type'] == request.POST.get('type') and item['id'] == id), False)

        # get item request data
        add_data = {
            'type': request.POST.get('type'),
            'id': id,
        }

        # if id not in favorits_ids_list
        if not item_exist:
            request.session['favorites'].append(add_data)
            request.session.modified = True

    return redirect(request.POST.get('url_from'))


def remove_from_favorites(request, id):
    if request.method == 'POST':

        # delete an item from favorites
        for item in request.session['favorites']:
            if item['id'] == id and item['type'] == request.POST.get('type'):
                item.clear()

        # remove empty {} from favorites list
        while {} in request.session['favorites']:
            request.session['favorites'].remove({})

        # remove favorites if favorites list is empty
        if not request.session['favorites']:
            del request.session['favorites']

        request.session.modified = True

    return redirect(request.POST.get('url_from'))


def delete_favorites(request):
    if request.session.get('favorites'):
        del request.session['favorites']
    return redirect(request.POST.get('url_from'))
