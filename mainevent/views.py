from django.contrib.auth.decorators import login_required
import xlwt
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm, UserUpdate
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from django.http import HttpResponse
User = get_user_model()


def register(request):
    # print('#########BeforeBefore############')
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        
        # print('#########Before############')
        # print(form)
        if form.is_valid():
            # print('#########After############')
            user=form.save()

            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            user.save()
            send_mail(
                    'PitchVerse Registration',
                    f"""
Dear {user.name},

Greetings from Entrepreneurship Development Cell, TIET!

We hope this email finds you in the best of your health. 
We would like to thank you for filling out our registration form and we are delighted to announce the start of our flagship event Pitch Verse from 5-6 March, 2022.

Kindly join our official discord channel for further updates and news.
Discord link-  https://discord.gg/VwfGFMqJuZ
Psych yourself up as it’s time to research, ideate and explore the arena of emerging
startups.
Good Luck.

Regards, 
Team EDC
                        """,
                    'pitchverse@gmail.com',
                    [email],
                )
            messages.success(request,f"Hello {name} You are successfully registered for PitchVerse")
        return render(request, 'user/register.html')    
    else:
        form = UserRegistrationForm()
        context={
            'form': form,
        }
    return render(request, 'user/register.html',context)


# def activate(request, uidb64, token):
#     try:
#         uid = urlsafe_base64_decode(uidb64).decode()
#         user = User._default_manager.get(pk=uid)
#     except(TypeError, ValueError, OverflowError, User.DoesNotExist):
#         user = None
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         messages.success(
#             request, f'Your account has been created! You can login now.')
#         return redirect('login')
#     else:
#         return HttpResponse('Activation link is invalid!')


def export_answers_xls(request):
    if request.user.is_superuser:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="Pitchverse.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        # this will make a sheet named Users Data
        ws = wb.add_sheet('Pitch verse Responses')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Email', 'Name', 'Contact No', 'Roll No/Application No',
                   'Position','Team Name', 'Company Name', 'Year of Study']

        for col_num in range(len(columns)):
            # at 0 row 0 column
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = User.objects.filter(is_active=True).order_by('team').values_list('email', 'name', 'contact_no', 'roll_no',
                                                                                'position', 'team__team_name', 'team__case_study_name', 'year_of_study')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)

        return response
    else:
        return redirect('home')





def send_emails(request):
    if request.user.is_superuser:
        t_users = User.objects.filter(are_you_a_thapar_student=True)
        if t_users:
            for user in t_users:
                send_mail(
                    'PitchVerse Registration',
                    f"""
Dear {user.name},

Greetings from Entrepreneurship Development Cell, TIET!

We hope this email finds you in the best of your health. 
We would like to thank you for filling out our registration form and we are delighted to announce the start of our flagship event Pitchers 6.0 from 26th February, 2022.

Kindly join our official discord channel for further updates and news.
Discord link-  https://discord.gg/5qeZp9N2SK
Psych yourself up as it’s time to research, ideate and explore the arena of emerging
startups.
Good Luck.

Regards, 
Team EDC
                        """,
                    'pitchers@edctiet.com',
                    [user.email],
                )
            return render(request, 'user/mail.html')
    else:
        return redirect('login')


def mail(request):
    if request.user.is_superuser:
        return render(request, 'user/mail.html')
    else:
        return render(request, 'user/login.html')



