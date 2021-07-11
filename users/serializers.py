from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()



class RegisterUserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'email','password')
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['password'])
        user.email = validated_data['email']
        user.save()
        return user


class CustomAuthTokenSerializer(serializers.Serializer):
    username_email = serializers.CharField(
        label="Username_or_email",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label="Token",
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username_email')
        password = attrs.get('password')

        if username and password:
            try:
                user = User.objects.get(email=username)
                username= user.username
            except:            
                pass
            
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "username" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs