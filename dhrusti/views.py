from django.shortcuts import render, get_object_or_404
from .models import Test


# Create your views here.


def index(request):
    return render(request, 'dhrusti/index.html')


def patient_info(request):

    message = ""
    # import pdb
    # pdb.set_trace()
    if request.method == "POST":
        name = request.POST['name']
        date_of_appointment =  request.POST['date']
        fname = request.POST['fname']
        age = request.POST['age']
        gender = request.POST['gender']
        occupation = request.POST['occupation']
        mobile = request.POST['mobile']
        address = request.POST['address']
        email = request.POST['email']
        address = request.POST['address']
        email = request.POST['email']
        samithi = request.POST['samithi']
        bvguru = request.POST['bvguru']
        sai_connect_number = request.POST['sai_connect_number']
        city = request.POST['city']
        state = request.POST['state']

        gradual_decrease_in_vision = request.POST.get('gradual_decrease_in_vision', None)

        if 'gradual_decrease_in_vision' in request.POST:
            gradual_decrease_in_vision = request.POST['gradual_decrease_in_vision']
        else:
            gradual_decrease_in_vision = ''
        gradual_decrease_in_vision1 = request.POST.get('gradual_decrease_in_vision1', None)

        if 'gradual_decrease_in_vision1' in request.POST:
            gradual_decrease_in_vision1 = request.POST['gradual_decrease_in_vision1']
        else:
            gradual_decrease_in_vision1 = ''
        all_gradual_decrease_in_vision = gradual_decrease_in_vision + " , " + gradual_decrease_in_vision1

        sudden_decrease_in_vision = request.POST.get('sudden_decrease_in_vision', None)
        if 'sudden_decrease_in_vision' in request.POST:
            sudden_decrease_in_vision = request.POST['sudden_decrease_in_vision']
        else:
            sudden_decrease_in_vision = ''
        sudden_decrease_in_vision1 = request.POST.get('sudden_decrease_in_vision1', None)
        if 'sudden_decrease_in_vision1' in request.POST:
            sudden_decrease_in_vision1 = request.POST['sudden_decrease_in_vision1']
        else:
            sudden_decrease_in_vision1 = ''
        all_sudden_decrease_in_vision = sudden_decrease_in_vision + " , " + sudden_decrease_in_vision1

        blurred_distant_vision = request.POST.get('blurred_distant_vision', None)

        if 'blurred_distant_vision' in request.POST:
            blurred_distant_vision = request.POST['blurred_distant_vision']
        else:
            blurred_distant_vision = ''
        blurred_distant_vision1 = request.POST.get('blurred_distant_vision1', None)

        if 'blurred_distant_vision1' in request.POST:
            blurred_distant_vision1 = request.POST['blurred_distant_vision1']
        else:
            blurred_distant_vision1 = ''
        all_blurred_distant_vision = blurred_distant_vision + " , " + blurred_distant_vision1

        blurred_near_vision = request.POST.get('blurred_near_vision', None)

        if 'blurred_near_vision' in request.POST:
            blurred_near_vision = request.POST['blurred_near_vision']
        else:
            blurred_near_vision = ''
        blurred_near_vision1 = request.POST.get('blurred_near_vision1', None)

        if 'blurred_near_vision1' in request.POST:
            blurred_near_vision1 = request.POST['blurred_near_vision1']
        else:
            blurred_near_vision1 = ''
        all_blurred_near_vision = blurred_near_vision + " , " + blurred_near_vision1

        if 'pain' in request.POST:
            pain = request.POST['pain']
        else:
            pain = ''
        pain1 = request.POST.get('pain1', None)

        if 'pain1' in request.POST:
            pain1 = request.POST['pain1']
        else:
            pain1 = ''
        all_pain = pain + " , " + pain1

        if 'redness' in request.POST:
            redness = request.POST['redness']
        else:
            redness = ''
        redness1 = request.POST.get('redness1', None)

        if 'redness1' in request.POST:
            redness1 = request.POST['redness1']
        else:
            redness1 = ''
        all_redness = redness + " , " + redness1

        others = request.POST['others']

        if 'past_history' in request.POST:
            past_history = request.POST['past_history']
        else:
            past_history = ''

        if 'past_history1' in request.POST:
            past_history1 = request.POST['past_history1']
        else:
            past_history1 = ''

        if 'past_history2' in request.POST:
            past_history2 = request.POST['past_history2']
        else:
            past_history2 = ''

        if 'past_history3' in request.POST:
            past_history2 = request.POST['past_history3']
        else:
            past_history3 = ''

        allpasthistory = past_history + " , " + past_history1 + " , " + past_history2

        if 'family_history' in request.POST:
            family_history = request.POST['family_history']
        else:
            family_history = ''

        if 'family_history1' in request.POST:
            family_history1 = request.POST['family_history1']
        else:
            family_history1 = ''

        allfamilyhistory = family_history + " , " + family_history1

        Others2 = request.POST['Others2']

        if 'systemic_disease' in request.POST:
            systemic_disease = request.POST['systemic_disease']
        else:
            systemic_disease = ''

        if 'systemic_disease1' in request.POST:
            systemic_disease1 = request.POST['systemic_disease1']
        else:
            systemic_disease1 = ''

        if 'systemic_disease2' in request.POST:
            systemic_disease2 = request.POST['systemic_disease2']
        else:
            systemic_disease2 = ''

        if 'systemic_disease3' in request.POST:
            systemic_disease3 = request.POST['systemic_disease3']
        else:
            systemic_disease3 = ''

        if 'systemic_disease4' in request.POST:
            systemic_disease4 = request.POST['systemic_disease4']
        else:
            systemic_disease4 = ''

        all_systemic_disease = systemic_disease + " , " +    systemic_disease1 + " , " +    systemic_disease2\
                               + " , " +  systemic_disease3 + " , " +    systemic_disease4



        if 'medication' in request.POST:
            medication = request.POST['medication']
        else:
            medication = ''

        if 'medication1' in request.POST:
            medication1 = request.POST['medication1']
        else:
            medication1 = ''

        if 'medication2' in request.POST:
            medication2 = request.POST['medication2']
        else:
            medication2 = ''

        all_medication = medication + " , " + medication1 + " , " + medication2

        others3 = request.POST['others3']

        others4 = request.POST['others4']

        allergy = request.POST['allergy']

        try:
            pd = Test.objects.create(name=name, fname=fname, age=age, gender=gender, occupation=occupation,date_of_appointment= date_of_appointment,
                                mobile=mobile, address=address, email=email, samithi=samithi,
                                bvguru=bvguru, sai_connect_number=sai_connect_number, city=city, state=state,
                                gradual_decrease_in_vision=all_gradual_decrease_in_vision,
                                sudden_decrease_in_vision=all_sudden_decrease_in_vision,
                                blurred_distant_vision=all_blurred_distant_vision,
                                blurred_near_vision=all_blurred_near_vision,
                                pain=all_pain, redness=all_redness, others=others,
                                past_history=allpasthistory, family_history=allfamilyhistory,
                                Others2=Others2, others3=others3, medication=all_medication,
                                others4=others4, allergy=allergy, systemic_disease=all_systemic_disease)

            message = "Data submitted successfully"
        except Exception as e:
            print(e)
            message = " Something went wrong "
        pd = Test.objects.filter(pk=pd.id)
        data = {'message': message, 'pd':pd}
        return render(request, 'dhrusti/user/pdf.html', data)


# def pdf(request):
#     return render(request, 'dhrusti/user/pdf.html')

# def  patient_detail(request,id):
#      pd = get_object_or_404(Test,pk= id)
#      data = {'pd': pd, }
#      return render (request, 'dhrusti/pdf.html',data)

def patient_info_form(request):
    return render(request, 'dhrusti/user/patient_info.html')


