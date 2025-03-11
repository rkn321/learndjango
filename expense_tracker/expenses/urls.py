from django.urls import path
from .views import dashboard, add_expense, delete_expense, signup, user_login, user_logout

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('add/', add_expense, name='add_expense'),
    path('delete/<int:expense_id>/', delete_expense, name='delete_expense'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
