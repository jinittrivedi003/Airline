from django.urls import path
from ..views.feedback import *
FeedbackURL=[
    path('viewFeedback/',viewFeedback,name="viewFeedback"),
    path('addFeedback/',addFeedback,name="addFeedback"),  
    path('updateFeedback/<id>',updateFeedback,name="updateFeedback"), 
    path('deleteFeedback/<id>',deleteFeedback,name="deleteFeedback"), 
]