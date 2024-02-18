from django.http import HttpResponse
from django.shortcuts import render
# def index(rquest):
#     return HttpResponse("Hello world")
#
# def hello(request):
#     return HttpResponse("Hiha")
#
# def jo(request):
#     return HttpResponse("<h1>HI kaise Ho bhai</h1>")
#
# def linksV(rquest):
#     return HttpResponse('''<h1>Get Some ideas from thsese amazing v <br><br>
#     <h2>Python Tutorail</h2><a href="https://www.w3schools.com/django/django_templates.php" target="_blank"/>PT</a>
#     <br><br>
#     <h2>Mera Hii</h2><a href="http://127.0.0.1:8000/jojo/" target="_blank"/>HOHO''')

def index(request):
    p={'name':'Rahul'}
    return render(request,'index.html',p)



# def index(request):
#     return HttpResponse("Home")

# def removepunc(request):
#     return HttpResponse('''remove punc <a href="http://127.0.0.1:8000/">GO BACK TO HOME</a>''')
#

# def capfirst(request):
#     text=request.GET.get('txt','kuch aur')
#     print(text)
#     return HttpResponse('''new line remove <a href="http://127.0.0.1:8000/">GO BACK TO HOME</a>''')
#
#
# def ineerlineremover(request):
#     return HttpResponse('''new line remove <a href="http://127.0.0.1:8000/">GO BACK TO HOME</a>''')
#
# def spaceremover(request):
#     return HttpResponse("Space remover")
#
# def charcount(request):
#     return HttpResponse("Count Character")
#
#


def analyze(request):
    text=request.GET.get('txt','default')
    punctuation=request.GET.get('punc','off')
    capital=request.GET.get('caps','off')
    extraspaceremover=request.GET.get('space','off')
    count=request.GET.get('count','off')
    # print(text)
    # print(punctuation)

    analyzes = ""
    if punctuation=="on":
        punctuations = "~  !  @  %  ^  &  *  -  +  =  |  /  :  ?  <  > , . } {"
        for char in text:
            if char not in punctuations:
                analyzes=analyzes+char
        params = {'punchated': 'punctuation', 'Analysed_text': analyzes}

    elif (extraspaceremover=="on"):
        analyzes=""
        for index,char in enumerate(text):
            if not(text[index] ==" " and text[index+1]==" "):
                analyzes=analyzes+char
        params = {'punchated': 'Remove Extra Space', 'Analysed_text': analyzes}


    elif(capital == "on"):
        analyzes = ""
        for char in text:
            analyzes = analyzes + char.upper()
        params = {'punchated': 'Changed to upper case', 'Analysed_text': analyzes}


    elif (count == "on"):
        count=0
        for char in text:
            if char !=' ':
                count+=1
        params = {'punchated': 'Character Count is :', 'Analysed_text': analyzes,'count':count}



    else:
        return  HttpResponse("Error cant parse")
    return render(request, "Analsye.html", params)

def Aboutus(request):
    return render(request,"Aboutus.html")

def Contactus(request):
    return render(request,"Contact.html")