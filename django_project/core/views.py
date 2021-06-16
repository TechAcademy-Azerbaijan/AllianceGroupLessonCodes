from django.shortcuts import render

user_list = [
    {
        'id': 1,
        'name': 'Kamal',
    },
    {
        'id': 2,
        'name': 'Nermin',
    },
    {
        'id': 3,
        'name': 'Zakir',
    }
]


def home(request):
    context = {
        'users': user_list
    }
    return render(request, 'index.html', context)


def user_detail(request, user_id):
    select_user = None
    for user in user_list:
        if user['id'] == user_id:
            select_user = user
            break
    context = {
        'select_user': select_user
    }
    return render(request, 'user_profile.html',  context)

