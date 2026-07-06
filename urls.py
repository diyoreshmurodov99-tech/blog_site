from django.urls import path
from .views import index_page,get_jobs,get_salary_jobs
urlpatterns = [
    path('',index_page,name='my_app'),
    path("salary/<str:status>/<int:top>", get_salary_jobs, name='job-salary'),
    path("salary/list/", get_salary_jobs, {'status' : 'all', 'top':None} , name='job-salary-all'),
    path("jobs/<int:job_id>", get_jobs, name='job-detail'),
    # path("salary/<int:top>",get_max_salary_employees,name='employee-list'),
    #path("deps/<int:employee_id>",get_dependents,name='deps-list'),
    # path("max_salary/max/<int:top>",get_max_salary_jobs,name='job-max-salary'),
    # path("min_salary/min/<int:top>",get_min_salary_jobs,name='job-min-salary'),

]

