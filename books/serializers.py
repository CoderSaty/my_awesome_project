# from msilib.schema import Class
from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    mobile = serializers.CharField()

    class Meta:
        model = Author
        fields = [
            "id",
            "name",
            "email",
            "mobile",
        ]

    # def validate_email(self, email):
    #     if Author.objects.filter(email=email).exists():
    #         raise serializers.ValidationError("Email_already_exists")

    #     return email

    # def validate_mobile(self, mobile):
    #     if Author.objects.filter(mobile=mobile).exists():
    #         raise serializers.ValidationError("Mobile_already_exists")

    #     return mobile

    def validate(self, data: dict):
        email = data.get("email")
        mobile = data.get("mobile")

        if Author.objects.filter(email=email, mobile=mobile).exists():
            raise serializers.ValidationError("Email_and_mobile_combination_exists")

        return data

    def create(self, data):

        author = Author.objects.create(**data)
        # call send_email_method
        return author

    def update(self, instance, data):
        instance.name = data.get("name", instance.name)
        instance.email = data.get("email", instance.email)
        instance.mobile = data.get("mobile", instance.mobile)
        instance.save()

        return instance


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "address",
            "authors",
        ]
