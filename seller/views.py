from django.shortcuts import render, redirect
from .models import Food
from django.contrib.auth.decorators import login_required
#자신이 판매하는 상품 리스트를 보여주기
# Create your views here.

@login_required
def seller_index(request):
    foods = Food.objects.all().filter(user__id = request.user.id)
    context =  {
        'object_list': foods
    }
    return render(request, 'seller/seller_index.html')


def add_food(request):
    #get :  처음에 타고 들어올 때는 get 방식
    if request.method =="GET":
        return render(request, 'seller/seller_add_food.html')
    

    #post : form에 내용이 잇는데 들어오는 건 post 방식
    elif request.method =="POST":
        # form에서 전달되는 값을 뽑아와서 DB에 저장

        # food_name, price, description
        return redirect('seller:seller_index')