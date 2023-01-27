from django.shortcuts import render


def view_index(request):
    return render(request, 'school/index.html')

def view_sign_in(request):
    return render(request, 'school/sign-in.html')