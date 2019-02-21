from django.shortcuts import render
def home(request):
    return render(request, 'home.html')
    # render는 3개 1는 request 객채 2는 template 이름 3는 사전형 객채를 받는다

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    sorted_data={k:v for k,v in sorted(word_dictionary.items(),key=lambda x:x[1], reverse=True)}

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'sorteddata': sorted_data.items()})