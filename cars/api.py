from cars.models import Car
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import CarSerializer
# from .permissions import ManagerPermission, DealerAndManager

# Car Viewset
class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CarSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        current_user = self.request.user
        user_groups = current_user.groups.values_list('name', flat=True)
        if "dealer" in user_groups:
            queryset = queryset.filter(dealer__user=current_user)
        elif "seller" in user_groups:
            queryset = queryset.filter()
        return queryset

    # def get_permissions(self):
    #     permission = self.get_permissions()
    #     if self.action == 'list':
    #         permission = permission
    #     elif self.action == 'retrieve':
    #         permission = permission
    #     elif self.action == 'update':
    #         permission = DealerAndManager
    #     elif self.action == 'update':
    #         permission = DealerAndManager
    #     return permission

    def destroy(self, request, *args, **kwargs):
        current_user = request.user
        user_groups = current_user.groups.values_list('name', flat=True)
        if "manager" not in user_groups :
            result = {'error': "can't"}
            return Response(result)

        return super().destroy(request, *args, **kwargs)
