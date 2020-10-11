from cars.models import Car
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .serializers import CarSerializer
from .permissions import IsManager, IsDealerOrManager

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

    def get_permissions(self):
        permission = super().get_permissions()
        print(permission)
        print(self.action)
        if self.action == 'create':
            permission = [IsManager()]
        elif self.action == 'update':
            permission = [IsDealerOrManager()]
        elif self.action == 'destory':
            permission = [IsManager()]
        return permission

    # def destroy(self, request, *args, **kwargs):
    #     current_user = request.user
    #     user_groups = current_user.groups.values_list('name', flat=True)
    #     if "manager" not in user_groups :
    #         result = {'error': "can't"}
    #         return Response(result)
    #
    #     return super().destroy(request, *args, **kwargs)
