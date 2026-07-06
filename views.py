"""
or=|
and=&
not=~
 """
from django.shortcuts import render
from django.http import HttpResponse
from .models import Countries, Employees, Locations, Jobs, Dependents
from django.db.models import Q, Count

def index_page(request):
    return render(request,'index.html')

# def get_max_salary_employees(request,top):
#     queryset=Employees.objects.all().order_by('-salary')[:top]
#     return render(request,'max_salary.html',{'max_salary':queryset})
#
# def get_dependents(request,employee_id):
#     queryset=Dependents.objects.all().filter(employee=employee_id)
#     employee=Employees.objects.get(employee_id=employee_id)
#     context={'deps':queryset,'employee':employee}
#     return render(request,'dependents.html',context)

# def get_max_salary_jobs(request,top):
#     queryset=Jobs.objects.all().order_by('-max_salary')[:top]
#     return render(request,'max_salary.html',{'max_salary':queryset})

def get_salary_jobs(request,status='all',top=None):
    if status == 'max':
        queryset = Jobs.objects.all().order_by('-max_salary')[:top]
        page_title = f"Top {top} Maksimal maoshlar"
        if top: queryset = queryset[:top]

    elif status == 'min':
        queryset = Jobs.objects.all().order_by('min_salary')[:top]
        page_title = f"Top {top} Minimal maoshlar"
        if top: queryset = queryset[:top]

    else:
        queryset = Jobs.objects.all().order_by('job_title')
        page_title = "Barcha ishchilar ruyxati"
        if top: queryset = queryset[:top]

    context = {
        'jobs_list': queryset,
        'title': page_title
    }
    return render(request, 'salary.html', context)
# def get_min_salary_jobs(request,top):
#     queryset=Jobs.objects.all().order_by('min_salary')[:top]
#     return render(request,'min_salary.html',{'min_salary':queryset})
# def get_all_jobs(request):
#     all_jobs = Jobs.objects.all()
#
#     context = {
#         'jobs': all_jobs
#     }
#     return render(request, 'jobs.html', context)

def get_jobs(request,job_id):
    queryset=Jobs.objects.all().get(job_id=job_id)
    context={'jobs':queryset}
    return render(request,'jobs.html',context)


















# queryset = Countries.objects.only("country_name")
# queryset = Countries.objects.filter(region_id=2)
# queryset = Countries.objects.filter(region_id__in=[1,3])
# queryset = Countries.objects.filter(region__region_name="Europe")
# queryset = Countries.objects.filter(country_name__startswith='A')
# queryset = Countries.objects.filter(country_name__endswith='A')
# queryset = Employees.objects.filter((Q(first_name__startswith="D") | Q(last_name__startswith="J")))
# queryset = Employees.objects.filter((Q(first_name__startswith="k") & Q(last_name__startswith="c")))
# def my_list(request):
#     # queryset = Jobs.objects.prefetch_related('employees_set').get(job_id=9)
#     # r=list(queryset.employees_set.all())
#     # for i in r:
#     #     print(i.first_name)
#     queryset = Employees.objects.values('job_id').annotate(xodim_soni=Count('*'))
#     for i in queryset:
#         print(i)
#     return HttpResponse("ok")
#     # queryset = Locations.objects.select_related('country').first()
#     # print(queryset.street_address)
#     # return HttpResponse(queryset.country.count
#     # emp_list = ""
#     # for c in queryset:
#     #     emp_list += f"<li>{c.first_name} {c.last_name} </li>"
#     # return HttpResponse(f"<ol>{emp_list}</ol>")
