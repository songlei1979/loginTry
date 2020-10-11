from rest_framework import serializers
from cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

    # def update(self, instance, validated_data):
    #     current_user = self.context['request'].user
    #     user_groups = current_user.groups.values_list('name', flat=True)
    #
    #     if "dealer" in user_groups and not instance.dealer.user == current_user:
    #         return serializers.ValidationError("dealer can only update its car")
    #     elif not ("dealer" in user_groups or "manager" in user_groups):
    #         return serializers.ValidationError("normal user can't")
    #
    #     instance.make = validated_data.get('make', instance.make)
    #     instance.save()
    #     return instance

