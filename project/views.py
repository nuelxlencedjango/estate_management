from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'index.html')



def team(request):
    return render(request, 'team.html')




def property(request):
    return render(request, 'property.html')




def management(request):
    return render(request, 'management.html')





def marketing(request):
    return render(request, 'marketing.html')





def testimonial(request):
    return render(request, 'testimonial.html')




def contact_us(request):
    return render(request, 'contactus.html')