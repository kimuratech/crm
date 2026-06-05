from django.shortcuts import render, get_object_or_404, redirect
from .models import Account
from .forms import AccountForm


def account_list(request):
    accounts = Account.objects.all()
    return render(request, 'crm_core/list.html', {'accounts': accounts})


def account_detail(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'crm_core/detail.html', {'account': account})


def account_create(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('account-list')
    else:
        form = AccountForm()
    return render(request, 'crm_core/create.html', {'form': form})
