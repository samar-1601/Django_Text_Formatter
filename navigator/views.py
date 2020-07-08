from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'index2.html')
    # request to get the index.html


def analyse(request):
    # Get the text the user entered
    djtext = request.POST.get('text', 'defaultText')
    purpose = ""

    punctuations = '''`!@#$^&*(){}[]-_;':",?./'''

    removePunctuation_CheckBox = request.POST.get('removePunctuation', 'off')
    CapitalizeString = request.POST.get('CapitalizeString', 'off')
    removeExtraSpace = request.POST.get('removeExtraSpace', 'off')

    if removePunctuation_CheckBox == 'on':
        formatted_string = ''
        for char in djtext:
            if char not in punctuations:
                formatted_string += char
        purpose += "'RemovePunctuations' "
        params = {"formatted_text": formatted_string, 'purpose': purpose}
        djtext = formatted_string
        # return render(request, 'analyse.html', params)

    if CapitalizeString == 'on':
        formatted_string = ''
        for char in djtext:
            formatted_string += char.upper()
        djtext = formatted_string
        purpose += "'Capitalize' "
        params = {"formatted_text": formatted_string, 'purpose': purpose}
        # return render(request, 'analyse.html', params)

    if removeExtraSpace == 'on':
        formatted_string = ''
        for charIndex in  range(0, len(djtext)-1):
            if not (djtext[charIndex] == ' ' and djtext[charIndex + 1] == ' '):
                formatted_string += djtext[charIndex]
        purpose += "'RemoveExtraSpace' "
        params = {"formatted_text": formatted_string, 'purpose': purpose}
        # return render(request, 'analyse.html', params)

    if removePunctuation_CheckBox != "on" and removeExtraSpace != "on" and CapitalizeString != "on":
        return HttpResponse("please select any operation and try again")

    print(purpose)
    print(len(djtext))
    return render(request, 'analyse.html', params)
