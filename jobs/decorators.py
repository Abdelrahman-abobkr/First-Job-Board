from django.shortcuts import redirect
from django.http import HttpResponse




def user_authenticate(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func



def allowed_users(allowed_rolles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

                if group in allowed_rolles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponse("<h1>You Are Not Autharized To View This Please Back To<a href='/'>Home Page</a></h1>")
        return wrapper_func
    return decorator



def for_admin(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

            if group == 'admin':
                return view_func(request, *args, **kwargs)
            
            if group == 'customer':
                return redirect('profile')
    return wrapper_func