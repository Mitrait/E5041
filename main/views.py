import requests
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import ContactForm

def send_to_telegram(text):
    token = settings.TELEGRAM_BOT_TOKEN
    chat_id = settings.TELEGRAM_CHAT_ID
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
    requests.post(url, data=payload)

def index(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            text = f"<b>Новая заявка с E5041.pro</b>\nИмя: {form.cleaned_data['name']}\nТелефон: {form.cleaned_data['phone']}\nСообщение: {form.cleaned_data['message']}"
            send_to_telegram(text)
            return redirect('index')
    return render(request, 'index.html', {'form': form})

def contacts(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            text = f"<b>Новая заявка с контактов E5041.pro</b>\nИмя: {form.cleaned_data['name']}\nТелефон: {form.cleaned_data['phone']}\nСообщение: {form.cleaned_data['message']}"
            send_to_telegram(text)
            return redirect('contacts')
    return render(request, 'contacts.html', {'form': form})

def services(request): return render(request, 'services.html')
def docshel(request): return render(request, 'docshel.html')
def about(request): return render(request, 'about.html')
