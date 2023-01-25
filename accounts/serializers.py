
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserCreateSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=200)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=15, write_only=True,   style={'input_type': 'password'})
    re_password =serializers.CharField(max_length=15, write_only=True,  style={'input_type': 'password'} )


    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def validate(self, attrs):
        password = attrs['password']
        re_password = attrs.pop('re_password')

        if(password != re_password):
            raise serializers.ValidationError({"detail": "Password do not match"})

        user_exists = User.objects.filter(email=attrs['email']).exists()
        if user_exists:
            raise serializers.ValidationError({"detail" : "User already exists"})

        return super().validate(attrs)
    

