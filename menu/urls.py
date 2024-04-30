from django.urls import path
from menu import views
urlpatterns = [
    path('menuitems/',views.Menu , name='menuitems' ),
    path('add_category/',views.Add_Category , name='add_category' ),
    path('edit_category/<int:pk>',views.Edit_Category , name='edit_category' ),
    path('delete_category/<int:pk>',views.del_Category , name='delete_category' ),
    path('add_fooditem/',views.Add_Category_Wise_Item , name='add_fooditem' ),
    path('fooditems/category/<int:pk>',views.FoodItem_by_category , name='fooditem' ),
]