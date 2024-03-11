from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated

from cride.circles.models import Circle
from cride.circles.models import Membership
from cride.circles.permissions.circles import IsCircleAdmin 
from cride.circles.serializers.circles import CircleModelSerializer

class CircleViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Circle.objects.all()
    serializer_class = CircleModelSerializer 
    
    def get_permissions(self):
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial_update']:
            permissions.append(IsCircleAdmin)
        return [permission() for permission in permissions]


    def perform_create(self, serializer):
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user = user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10
        )
        