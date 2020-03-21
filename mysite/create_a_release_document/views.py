from docx import Document
from django.shortcuts import HttpResponse, render


def index(request):
    return render(request, 'create_a_release_document/index.html', {})


def test(request, data):
    document = Document()
    document.add_heading(data, 0)

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    response['Content-Disposition'] = 'attachment; filename=download.docx'
    document.save(response)

    return response
