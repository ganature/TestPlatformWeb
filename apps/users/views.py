from django.shortcuts import render, HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispatch(self,request,*args,**kwargs):
        return super(LoginRequiredMixin,self).dispatch(request,*args,**kwargs)

@method_decorator(login_required,name='dispatch')
class IndexView(LoginRequiredMixin,View):
    """
    首页
    """

    @staticmethod
    def get(request):
        return render(request, 'index.html')


class LoginView(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        name = request.COOKIES.get('name')
        if name:
            return render(request, 'index.html')
        user_name = request.POST.get('username')
        pass_word = request.POST.get('password')
        auth_login = authenticate(username=user_name, password=pass_word)
        print(auth_login)
        if auth_login:
            login(request, auth_login)
            response = HttpResponseRedirect('/project/list')
            response.set_cookie('name', user_name, 60 * 60 * 24 * 1)
            return response
        else:
            return render(request, 'login.html', {'msg': '登录失败', 'status_code': 101})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
