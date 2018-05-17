from django.conf.urls import url
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles.urls import static, settings


urlpatterns = [
    url(r'^order/$', views.create_order, name='create_order'),
    url(r'^order/step1/$', views.choose_sole, name='choose_sole'),
    url(r'^order/step2/$', views.choose_shape, name='choose_shape'),
    url(r'^order/step3/$', views.choose_fabric, name='choose_fabric'),
    url(r'^order/step4/$', views.choose_other, name='choose_other'),
    url(r'^order/step5/$', views.choose_sizes, name='choose_sizes'),
    url(r'^order/step6/$', views.enter_order_data, name='enter_order_data'),
    url(r'^order/step7/$', views.confirm_order, name='confirm_order'),
    url(r'^$', views.index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

