from django.urls import path
from book_giveaway import views

urlpatterns = [
	path("request-book/", views.RequestBookView.as_view(), name='request-book'),
	path("books-requests/", views.GetBookRequestListView.as_view(), name='list-requests'),
	path("confirm-request/<int:pk>", views.ConfirmBookRequestView.as_view(), name='confirm-request'),
	path('decline-request/<int:pk>', views.DeclineBookRequestView.as_view(), name='decline-book-request'),
	path('sent-requests/', views.UserSentRequestsListView.as_view(), name='user-sent-requests'),

]