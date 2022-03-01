from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PreEventForm
from .models import PreEvent
from django.contrib import messages
from django.http import HttpResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
import xlwt


# Create your views here.


def index(request):
    return render(request, 'pitchers/index.html')


def gallery(request):
    return render(request, 'pitchers/gallery.html')



def pre_event_reg(request):
    # form = PreEventForm()
    # print(form)
    if request.method == 'POST':
        form = PreEventForm(request.POST)
        # print(request.POST.get('Member1_are_you_a_thapar_student'))
        # print(form)
        if form.is_valid():
            print("hello")
            form.save()
            messages.success(request,"You are successfully registered for Flip The Script !") 
        return redirect('pre-event-reg')
    else:
        form=PreEventForm()
        context={
            'form': form,
        }
        return render(request, 'user/pre-event-reg.html',context)

def export_answers_xls(request):
    if request.user.is_superuser:
        response = HttpResponse(content_type='application/ms-excel')
        response['Content-Disposition'] = 'attachment; filename="flipthescript.xls"'

        wb = xlwt.Workbook(encoding='utf-8')
        # this will make a sheet named Users Data
        ws = wb.add_sheet('Flip The script responses')

        # Sheet header, first row
        row_num = 0

        font_style = xlwt.XFStyle()
        font_style.font.bold = True

        columns = ['Team_name', 'Member1_name', 'Member1_email', 'Member1_contact_no', 'Member1_roll_no', 'Member1_are_you_a_thapar_student', 'Member1_year_of_study',
                  'Member2_name', 'Member2_email', 'Member2_contact_no', 'Member2_roll_no', 'Member2_are_you_a_thapar_student', 'Member2_year_of_study']

        for col_num in range(len(columns)):
            # at 0 row 0 column
            ws.write(row_num, col_num, columns[col_num], font_style)

        # Sheet body, remaining rows
        font_style = xlwt.XFStyle()

        rows = PreEvent.objects.order_by('Team_name').values_list('Team_name', 'Member1_name', 'Member1_email', 'Member1_contact_no', 'Member1_roll_no', 'Member1_are_you_a_thapar_student', 'Member1_year_of_study',
                  'Member2_name', 'Member2_email', 'Member2_contact_no', 'Member2_roll_no', 'Member2_are_you_a_thapar_student', 'Member2_year_of_study')
        for row in rows:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], font_style)

        wb.save(response)

        return response
    else:
        return redirect('home')

