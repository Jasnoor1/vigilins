from django.shortcuts import render,redirect
from django.http import HttpResponse
from . models import Document,CreateCSVList
from . forms import DocumentForm
from django.core.files.storage import FileSystemStorage
from django.template import Context, loader
from django.template.loader import render_to_string
import csv
from mimetypes import MimeTypes
import urllib
# Create your views here.

def home(request):
    documents = Document.objects.all()
    return render(request, 'core/home.html', {'documents': documents})

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('model_form_upload')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })

def simple_upload(request):
    print('In simple form')
    # file = request.FILES['myfile']
    # print(file)
    print(request.FILES['myfile'])
    if request.method == 'GET' and request.FILES['myfile']:
        print('In Post')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'core/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'core/simple_upload.html')

def DownloadCSV(self):
    print('i am in function')
    # object_list = CreateCSVList.objects.all()
    # for i in CreateCSVList.objects.all():
    #     val = i.ColumnName
    #     print(val)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="CSVFile.csv"'
    writer = csv.writer(response)
    writer.writerow(['ColumnName'])
    col_name = CreateCSVList.objects.all().values_list('ColumnName')
    for i in col_name:
        writer.writerow(i)
    return response

    # template = loader.get_template('core/export.html')
    # response.write(template.render(Context({'csv_data':CreateCSVList.objects.all()})))
    # return response

    # writer = csv.writer(response)
    # writer.writerow(CreateCSVList().ColumnName())
    # for x in CreateCSVList:
    #     writer.writerow(x.line())
    # return response
    # writer.writerow(['First row', 'Foo', 'Bar', 'Baz'])
    # writer.writerow(['Second row', 'A', 'B', 'C', '"Testing"', "Here's a quote"])
    # csv_data = CreateCSVList.objects.all()
    # return render_to_string('core/export.html',{'csv_data':csv_data})
    # return response
    # context={
    #     'column_name': ColumnName
    # }

    # t = render_to_string('core/export.html')
    # # # # c = Context({
    # # # #     'data':val
    # # # # })
    # response.write(t)
    # response return response
    # word =[]
    # print('helloo',type(word))
    #
    #     # input()
    # val2 = word.append(val)
    #     # print('hfsd0',val2)
    # print('List',val2)
    # print('Model Field',type(i))
    # # print(test)
    # # ChkBoxID = request.GET['id']
    # # print(ChkBoxID)
    # # pass
    # return render(request,'core/export.html',{'object_list':object_list})