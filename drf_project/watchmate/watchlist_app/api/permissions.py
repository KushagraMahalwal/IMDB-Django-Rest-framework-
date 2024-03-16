from rest_framework import permissions

# Only admin can do edit, update and delete and others can only see(get)
# because the permission is only for IsAdmin

class IsAdminOrReadOnly(permissions.IsAdminUser):
   
   def has_permission(self, request, view):

    if request.method in permissions.SAFE_METHODS:
        return True
    else:
        return bool(request.user and request.user.is_staff)

# Only a specified user can edit, update, delete and others can read only
class IsReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user==request.user or request.user.is_staff
            
