from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jeca_backend.models import Job, Company, Cover_Letter, Resume
from jeca_backend.serializers import (
    JobSerializer,
    CompanySerializer,
    CoverLetterSerializer,
    ResumeSerializer,
)

class JobViewSet (viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    @api_view(['GET', 'POST'])
    def job_list(request):
        if request.method == 'GET':
            jobs = Job.objects.all()
            serializer = JobSerializer(jobs, many=True)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = JobSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def cover_letter_list(request):
    if request.method == 'GET':
        cover_letters = Cover_Letter.objects.all()
        serializer = CoverLetterSerializer(cover_letters, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CoverLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def resume_list(request):
    if request.method == 'GET':
        resumes = Resume.objects.all()
        serializer = ResumeSerializer(resumes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ResumeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
