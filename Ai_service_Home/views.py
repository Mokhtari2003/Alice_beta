from django.shortcuts import render
def Home(request):
    if request.user.is_authenticated :
        return render(request ,"Home_page/Home.html")
    else :
        return render(request ,"Home_page/NotRegisterPage.html")
