from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def reverse(request):
    usertext = request.GET['usertext']
    wordlist = usertext.split(' ')
    return render(request, 'reverse.html', {'usertext':usertext, 'reversetext':usertext[::-1], 'wordnum':len(wordlist)})    