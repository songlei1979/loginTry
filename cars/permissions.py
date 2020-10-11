from rest_framework import permissions

class IsManager(permissions.BasePermission):
    message = 'you are not manager'

    def has_permission(self, request, view):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_manager = bool("manager" in user_groups)
        return is_manager

    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_manager = bool("manager" in user_groups)
        return is_manager

class IsDealerOrManager(permissions.BasePermission):
    message = 'This QIF is not assigned to the Current user'

    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        if "manager" in user_groups:
            return True
        elif "dealer" in user_groups and request.user == obj.dealer.user:
            return True
        else:
            return False

class CarPermission(permissions.BasePermission):
    message = 'This QIF is not assigned to the Current user'



    def has_object_permission(self, request, view, obj):
        user_groups = request.user.groups.values_list('name', flat=True)
        is_manager = bool("manager" in user_groups or "dealer" in user_groups)
        return is_manager