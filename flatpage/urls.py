from django.conf.urls.defaults import *

urlpatterns = patterns('flatpage.views',
    # url(r'^(?P<url>.*)$',
    #     view='flatpage',
    #     name='flatpage'
    # ),
    (r'^list/', 'list'),
    (r'^(?P<url>.*)$', 'flatpage'),
    (r'^update/(?P<num>\d+)/$', 'update'),
)
