from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'w-full bg-transparent border border-white/20 rounded-[8px] p-4 text-white'}))
    phone = forms.CharField(label='Телефон', max_length=20, required=True, widget=forms.TextInput(attrs={'class': 'w-full bg-transparent border border-white/20 rounded-[8px] p-4 text-white'}))
    message = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'class': 'w-full bg-transparent border border-white/20 rounded-[8px] p-4 h-32 text-white'}))
    consent = forms.BooleanField(label='Согласен с условиями', required=True, widget=forms.CheckboxInput(attrs={'class': 'accent-[#00D4FF]'}))
