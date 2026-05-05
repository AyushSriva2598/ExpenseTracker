from django.shortcuts import render , redirect
from .models import currentBalance, trackHistory
# from django.http import HttpResponse

# def home(request):
#     return HttpResponse("OK")

# Create your views here.

def index(request):
    if request.method=="POST":
        description= request.POST.get('description')
        amount=request.POST.get('amount')

        current_balance, _ =currentBalance.objects.get_or_create(id=1)
        expense_type="CREDIT"
        if float(amount) < 0:
            expense_type="DEBIT"
        tracking_History=trackHistory.objects.create(amount=amount,
            expense_type=expense_type,
            current_balance=current_balance,
            description=description)
        current_balance.current_balance+= float(tracking_History.amount)
        current_balance.save()

        return redirect('/')
        

    current_balance, _ =currentBalance.objects.get_or_create(id=1)
    income=0
    expense=0
    for tracking_history in trackHistory.objects.all():
        if tracking_history.expense_type=="CREDIT":
            income+=tracking_history.amount
        else:
            expense+=tracking_history.amount
    context={'income':income,
             'expense':expense,'transactions':trackHistory.objects.all(),'current_balance':current_balance}
    return render(request,'index.html',context)