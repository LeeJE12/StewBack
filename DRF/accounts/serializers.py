from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 
                  'nickname', 'phonenum', 'profile']
    
    def create(self, validated_data):
        #create 함수를 작성하여 입력받은 유저 데이터 저장 처리
        user = User.objects.create(
            phonenum=validated_data['phonenum'], #w전달받은 데이터 그대로 저장
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            profile=validated_data.get('profile', None),
        )
        user.set_password(validated_data['password']) #암호화한 후 저장
        user.save()
        
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=128, write_only=True)

    def validate(self, data): #입력받은 데이터의 유효성을 검증
        username=data.get('username', None)
        password=data.get('password', None)

        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)

            if not user.check_password(password):
                raise serializers.ValidationError('잘못된 비밀번호입니다.')
            else:
                token = RefreshToken.for_user(user)
                refresh = str(token)
                access = str(token.access_token)

                data = {
                    'id': user.id,
                    'username': user.username,
                    'access_token': access
                }
                return data       