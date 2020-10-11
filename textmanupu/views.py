from django.http import HttpResponse
from django.shortcuts import render

def site(request):
    return HttpResponse("<a href='https://www.google.co.in/'>modi ji</a><br>"
                        "<a href='https://www.google.co.in/'>ram</a><br>"
                        "<a href='https://www.google.co.in/'>shyam</a><br>"
                        "<a href='https://www.google.co.in/'>bxi</a><br>")


def index(request):
    return render(request,'index1.html')

def removepunc(request):
    ruftext=request.POST.get('text','default')
    puncremove=request.POST.get('removepunk','off')
    captal = request.POST.get('upper', 'off')
    line_remove = request.POST.get('newline', 'off')
    extra_space_remove=request.POST.get('extraspace','off')
    purpose =""
    if puncremove=='on':
        panctuations=''',./;'[]\<>?:"{}|!@#$^&*'''
        analysed=""
        for char in ruftext:
            if char not in panctuations:
                analysed=analysed+char
        params={'purpose':'puncremove_Text','anlysed_text':analysed}
        ruftext=analysed
        purpose += 'puncremove_text'
        #return render(request,'analysies.html',params)
    if captal=='on':
        analysed=ruftext.upper()
        params = {'purpose': 'captalize_Text', 'anlysed_text': analysed}
        ruftext = analysed

       # return render(request, 'analysies.html', params)
    if line_remove=='on':
        analysed = ""
        for char in ruftext:
            if char != "\n" and char!="\r":
                analysed += char
        params = {'purpose': 'lineremove', 'anlysed_text': analysed}
        ruftext = analysed
        purpose +='lineremove'
        #return render(request, 'analysies.html', params)
    if extra_space_remove=='on':
        analysed=''
        for index, char in enumerate(ruftext):
            if not(ruftext[index]==" " and ruftext[index+1]==" "):
                analysed+=char
        params = {'purpose': 'extraspace', 'anlysed_text': analysed}
        ruftext = analysed
        purpose += 'extraspace'
    # if count_char=='on':
    #     ccount=0
    #     for c in ruftext:
    #         if c.isspace() != True:
    #             ccount=ccount+1
    #     params = {'purpose': 'count_char', 'countcahr': ccount, 'anlysed_text': analysed}
    #     #return render(request, 'analysies.html', params)


    return render(request,'analysies.html',params)
