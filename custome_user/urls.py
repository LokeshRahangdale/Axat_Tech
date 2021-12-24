from django.contrib import admin
from django.urls import path
from custome_user import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("index/",views.Index_page,name="index"),
    path("register_student/",views.Register_Stuent_view,name="register_student"),
    path("register_teacher/",views.Register_Teacher_view,name="register_teacher"),
    path("logout/",views.Logout_View,name="logout"),
    path('user_login/',views.Login_View,name="user_login"),
    path("student_img/",views.Student_img_view,name="student_img"),
    path('student_dashboard/',views.student_dashboard,name="student_dashboard"),
    path('teacher_dashboard/',views.teacher_dashboard,name="teacher_dashboard"),
    path("add_teacher_img/",views.add_teacher_img,name="add_teacher_img"),
    #super admin login url

    path("admin_login/",views.Admin_Login,name="admin_login"),
    path("admin_dashboard",views.Admin_dashboard,name="admin_dashboard"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)