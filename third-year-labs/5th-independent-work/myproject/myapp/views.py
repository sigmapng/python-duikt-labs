from django.shortcuts import render


def my_info_view(request):
    return render(request, 'base.html')
