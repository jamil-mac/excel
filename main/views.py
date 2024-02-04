from django.http import HttpResponse
from django.shortcuts import render, redirect
import openpyxl
from openpyxl.workbook import Workbook

from main.models import UserModel


def import_data(request):
    if request.method == 'POST':
        file = request.FILES.get('excel')
        wb = openpyxl.load_workbook(file)
        sheet = wb.active
        users = UserModel.objects.all()

        for user in users:
            cell1 = sheet.cell(row=1, column=1)
            cell2 = sheet.cell(row=2, column=2)

            cell1.value = user.full_name
            cell2.value = user.event_name

            print(
                cell1.value,
                cell2.value,
            )
        wb.save(file)
        return redirect('/import/')
    return render(request, 'excel.html')


def export_data(request):
    wb = Workbook()
    sheet = wb.active
    users = UserModel.objects.all()

    for user in users:
        sheet.append([user.full_name, user.event_name])
    name = UserModel.objects.last()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = f'attachment; filename={name.event_name}.xlsx'

    wb.save(response)

    return response


