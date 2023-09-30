from django.shortcuts import render

def users(request):
    context = {'id': 'all users'}
    return render(request, 'user/user.html', context)

def user_id(request, id):
    context = {'id': id}
    return render(request, 'user/user.html', context)
