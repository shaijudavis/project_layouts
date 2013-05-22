from django.conf.urls.defaults import *

urlpatterns = patterns('flatpage.views',
    # url(r'^(?P<url>.*)$',
    #     view='flatpage',
    #     name='flatpage'
    # ),
    (r'^list/', 'list'),
    (r'^pages/update/(?P<id>\d+)/$', 'update'),
    (r'^pages/(?P<url>.*)$', 'flatpage'),
    (r'(?P<url>.*)$', 'showpage'),
)
