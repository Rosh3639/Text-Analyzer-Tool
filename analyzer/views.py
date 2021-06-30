
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def analyze(request):
    # Get Text
    global params
    textdj = request.POST.get('text', 'default')
    # Checkbox Values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceemover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # If checkbox is on do this
    if removepunc == "on":
        analyzed = ""
        punctuations = '''/[-\]{}"()+?.,=\^$|#\]/,;:!@#$%^&*'\$&'''
        for char in textdj:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        textdj = analyzed

    # If checkbox is on do this
    if fullcaps == "on":
        analyzed = ""
        for char in textdj:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Capitalized Text', 'analyzed_text': analyzed}
        textdj = analyzed

    # If checkbox is on do this
    if newlineremover == "on":
        analyzed = ""
        for char in textdj:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        textdj = analyzed

    # If checkbox is on do this
    if extraspaceemover == "on":
        analyzed = ""
        for index, char in enumerate(textdj):
            if not (textdj[index] == " " and textdj[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        textdj = analyzed

    # If checkbox is on do this
    if charcount == "on":
        analyzed = len(textdj)
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    if removepunc != "on" and newlineremover != "on" and extraspaceemover != "on" and fullcaps != "on" and charcount != "on":
        return render(request, 'error.html')

    return render(request, 'analyze.html', params)


def about(request):
    return HttpResponse("This is About Page!")

