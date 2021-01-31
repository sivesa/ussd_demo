from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def ussd_demo(request):
    response = ""

    #if request.method == 'POST':
    session_id = request.POST.get('sessionId')
    service_code = request.POST.get('serviceCode')
    phone_number = request.POST.get('phoneNumber')
    text = request.POST.get('text')

    water_usage = 39

    if text == "":
        response = "CON What would you want to check \n"
        response += "1. Water usage \n"
        response += "2. Throtle water usage \n"
        response += "3. Leakages \n"
        response += "4. Request assistant \n"

    elif text == "1":
        response = f"END Water usage is {water_usage} \n"
    elif text == "2":
        response = "END Throtle usage feature coming soon! \n"
    elif text == "3":
        response = "CON Potential leakages \n"
        #response += ""
    # else:
    #     response = "Something went wrong \n"
    return HttpResponse(response) 