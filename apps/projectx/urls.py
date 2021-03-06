from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('apps.projectx.views',
    url(r'^get-vector-functions/$', 'get_vector_functions_view', name='vector-functions'),
    url(r'^exec-json/(?P<name>\w+)/$', 'exec_json_view', name='exec-json'),
    url(r'^get-new-dataset/$', 'get_new_dataset_view', name='get-new-dataset'),
    url(r'^op/(?P<key>\w+)/(?P<name>\w+)/$', 'dataset_operation_view', name='operate-on-dataset'),
    url(r'^create/(?P<name>\w+)/$', 'dataset_creation_view', name='dataset-creation'),
    url(r'^get/(?P<data>[^/]+)/$$', 'get_datasets_view', name='get-datasets'),
)

