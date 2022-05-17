from django.urls import path

from measurement.views import SensorView, SensorUpdateView, MeasurementView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorView.as_view(), name='api'),
    path('sensors/<pk>/', SensorUpdateView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
