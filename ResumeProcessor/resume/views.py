from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Candidate
from .serializers import CandidateSerializer
from pyresparser import ResumeParser
import os

class ResumeExtractionView(APIView):
    """
    This class represents a view for extracting candidate information from a resume.

    Methods:
    - post: Handles POST requests to extract candidate information from a resume.

    """

    def post(self, request):
        """
        Handles POST requests to extract candidate information from a resume.

        Parameters:
        - request: The incoming request object.

        Returns:
        - A Response object with the serialized candidate data if successful.
        - A Response object with an error message if no file is uploaded.

        """

        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Save the uploaded file temporarily
        file_path = os.path.join("temp", file.name)
        with open(file_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)

        # Parse the resume
        data = ResumeParser(file_path).get_extracted_data()

        # Extract relevant information
        first_name = data.get('name').split()[0] if data.get('name') else None
        email = data.get('email')
        mobile_number = data.get('mobile_number')

        # Clean up the file
        os.remove(file_path)

        # Save candidate data to the database
        candidate = Candidate.objects.create(
            first_name=first_name,
            email=email,
            mobile_number=mobile_number
        )

        # Serialize the candidate data
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data, status=status.HTTP_201_CREATED)




