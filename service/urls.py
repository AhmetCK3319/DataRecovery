from django.urls import path
from .views import (
    portfolio_services,
    commercial_services,
    backend_services,
    phone_data_services,
    hdd_services,
    ssd_services,
    pc_services,
    usb_services,
    phone_password_services,
    phone_technical_services,
    services_detail,
)

urlpatterns = [
    path("portfolio_services/", portfolio_services, name="portfolio_services"),
    path("commercial_services/", commercial_services, name="commercial_services"),
    path("backend_sevices/", backend_services, name="backend_services"),
    path("phone_data_services/", phone_data_services, name="phone_data_services"),
    path("hdd_services/", hdd_services, name="hdd_services"),
    path("ssd_services/", ssd_services, name="ssd_services"),
    path("pc_services/", pc_services, name="pc_services"),
    path("usb_services/", usb_services, name="usb_services"),
    path("phone_password_services/", phone_password_services, name="phone_password_services"),
    path("phone_technical_services/", phone_technical_services, name="phone_technical_services"),
    path("services_detail/<int:id>/", services_detail, name="services_detail"),
]