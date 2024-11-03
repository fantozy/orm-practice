from django.shortcuts import render

def main(request):
    context = {"name": "12345"}
    return render(request, 'nika.html', context=context)