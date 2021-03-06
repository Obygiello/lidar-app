"""lidarproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import views
from django.urls import path, include

app_name = "main"

urlpatterns = [
    path("", views.homepage, name='homepage'),
    path("register/", views.register, name='register'),
    path("logout/", views.logout_request, name='logout'),
    path("login/", views.login_request, name='login'),
    path("boards/", views.boards, name="boards"),
    path("boards/create_board", views.create_board, name="create_board"),
    path("boards/<board_id>", views.edit_board, name="edit_board"),
    path("tests/", views.tests, name="tests"),
    path("tests/create_single_test", views.create_single_test, name="create_single_test"),
    path("tests/<test_id>", views.execute_test, name="execute_test"),
    path("scenarios/", views.scenarios, name="scenarios"),
    path("scenarios/create_scenario", views.create_scenario, name="create_scenario"),
    path("scenarios/<id>", views.execute_scenario, name="execute_scenario"),
    path("results/", views.results, name="results"),
    path("results/<pk>", views.display_result, name="display_result"),
    path("create_pdf/<filename>", views.create_pdf),
]
