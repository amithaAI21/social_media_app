from rest_framework import serializers
from .models import FriendRequest
from user_management.serializers import CustomUserSerializer

class FriendRequestSerializer(serializers.ModelSerializer):
    from_user = CustomUserSerializer(read_only=True)
    to_user = CustomUserSerializer()

    class Meta:
        model = FriendRequest
        fields = '__all__'

    def validate(self, attrs):
        if attrs['to_user'] == self.context['request'].user:
            raise serializers.ValidationError("You cannot send a friend request to yourself.")
        return attrs

class FriendRequestActionSerializer(serializers.Serializer):
    request_id = serializers.IntegerField()
    action = serializers.ChoiceField(choices=['accept', 'reject'])
