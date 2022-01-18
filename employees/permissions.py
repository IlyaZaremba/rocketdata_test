from rest_framework.permissions import BasePermission
from rest_framework_api_key.permissions import BaseHasAPIKey
#from .models import EmployeeAPIKey

#class HasEmployeeAPIKey(BaseHasAPIKey):
    #model = EmployeeAPIKey

#class IsAdminUser(BasePermission):

class IsEnrolled(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner.filter(id=request.user.id).exists()