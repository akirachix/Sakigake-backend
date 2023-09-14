# from rest_framework import permissions
# class IsAdminOrReadOnly(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if request.method in permissions.SAFE_METHODS:
#             return True
#         return request.user and request.user.is_staff
    


# class IsOwnerOrAdmin(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request.user and request.user.is_staff:
#             return True
#         if hasattr(obj, 'created_by'):
#             return obj.created_by == request.user
#         return False
    


from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission to allow administrators full access,
    but read-only access for others (including Teachers and schools).
    """
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Permission to allow administrators full access,
    object owners access, and read-only access for others.
    """
    def has_object_permission(self, request, view, obj):
        if request.user and (request.user.is_staff or obj.created_by == request.user):
            return True
        return False

class IsAdminOrNGO(permissions.BasePermission):
    """
    Custom permission for administrators and Schools (CustomUsers).
    """
    def has_object_permission(self, request, view, obj):
        print(f"::::::::::::::::::::::::::::::::::::{request.user}=============")
        if request.user and (request.user.is_staff or obj.created_by == request.user):
            return True
        return False

class IsHealthworker(permissions.BasePermission):
    """
    Custom permission for Schools.
    """
    def has_permission(self, request, view):
        return getattr(request.user, 'is_teacher',True)
