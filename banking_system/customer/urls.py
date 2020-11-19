from django.urls import path
from .views import (
              CustomerListView,
              Profile,
              Debtor,
              Transfer
	             )

urlpatterns = [
  path('',CustomerListView.as_view(),name = 'customer-home'),
  path('<uuid:id>/',Profile,name = 'customer-detail'),
  path('<uuid:id>/select-to-transfer/',Debtor.as_view(),name = 'debtor-selection'),
  path('<uuid:creditor>/transfer/<uuid:debtor>/',Transfer,name = 'money-transfer')
]