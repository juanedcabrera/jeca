from rest_framework import serializers
from django.contrib.auth.models import User, Group
from jeca_backend.models import Job,Company,Cover_Letter, Resume

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id','mame')

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ('title', 'company', 'status', 'application_date', 'post_date', 'job_description', 'job_url', 'feedback_tracker')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'website', 'description')

class CoverLetterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover_Letter
        fields = ('job', 'content')

class ResumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = ('job', 'content')