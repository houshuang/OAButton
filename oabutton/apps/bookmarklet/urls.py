from django.conf.urls import patterns, url

from views import form1, form2, form3
from views import add_post
from views import generate_bookmarklet
from views import signin
from views import xref_proxy
from views import xref_proxy_simple
from views import email_confirm
from views import open_document


urlpatterns = patterns('',
                       url(r'^signin/$', signin, name="signin"),

                       url(r'^post/(?P<key>.*)/$', add_post, name="add_post"),
                       url(r'^form/page1/(?P<slug>.*)/$', form1, name="form1"),
                       url(r'^form/page2/(?P<key>.*)/_slug_(?P<slug>.*)/$', form2, name="form2"),
                       url(r'^form/page3/(?P<key>.*)/_slug_(?P<slug>.*)/$', form3, name="form3"),

                       url(r'^confirmation/(?P<slug>.*)_(?P<salt>.*)/$',
                           email_confirm,
                           name='email_confirm'),

                       url(r'^bookmarklet/(?P<slug>.*).js$',
                           generate_bookmarklet,
                           name="generate_bookmarklet"),
                       url(r'^xref_proxy/(?P<doi>.*)',
                           xref_proxy,
                           name="xref_proxy"),
                       url(r'^xref_proxy_simple/(?P<doi>.*)',
                           xref_proxy_simple,
                           name="xref_proxy_simple"),


                       # Submit an open version of a document
                       url(r'^api/v1/open_document/(?P<slug>.*)',
                           open_document,
                           name="open_document"),
                       )
