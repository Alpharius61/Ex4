from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': "Home",
    }
    return render(request, 'main/index.html', context)


def about(request):
    isAdmin = True
    first_name = "John"
    last_name = "Doe"
    context = {
        'isAdmin': isAdmin,
        'first_name': first_name,
        'last_name': last_name,
    }
    return render(request, 'main/about.html', context)


def about2(request):
    isAdmin = True
    first_name = "John"
    last_name = "Doe"
    if isAdmin:
        content = f"""
        <h1> {first_name} - {last_name} </h1>
        <p> Lorem ipsum dolor, sit amet consectetur adipisicing elit. Labore iste voluptas animi id, cupiditate quisquam
        nulla qui laborum harum impedit. </p>
        """
    else:
        content = "<p>C'est toi. Tu ne sais pas qui tu es ?</p>"
    context = {
        'content': content,
    }
    return render(request, 'main/about2.html', context)
