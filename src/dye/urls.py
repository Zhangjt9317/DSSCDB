from django.conf.urls import url

from dye import views

urlpatterns = [
    url(r'^upload_file/$', views.file_upload, name='file-upload'),
    url(r'^upload/$', views.single_upload, name='single-upload'),
    url(r'^performance-list/$', views.performance_list, name='performance-list'),
    url(r'^performance-list/search/$', views.performance_search, name='performance-search'),
    url(r'^performance-detail/(?P<short_id>[0-9a-f]{10})/$', views.performance_details, name='performance-detail'),
    url(r'^contributions/(?P<short_id>[0-9a-f]{10})/$', views.contribution_performances, name='single-evaluation'),
    url(r'^contributions/$', views.contributions_evaluation_overview, name='evaluate-contributions'),
    url(r'^my-contributions/$', views.my_contributions, name='my-contributions'),
    url(r'^batch-download/$', views.batch_download_info, name='batch-download'),
    url(r'^batch-download/perform$', views.download_all_performances_csv, name='perform-batch-download')
]
