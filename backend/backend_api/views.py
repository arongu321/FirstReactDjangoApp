from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note

# Create your views here.
class NoteListCreate(generics.ListCreateAPIView):
    """
    API view to retrieve and create notes for the authenticated user.
    This view allows authenticated users to:
        - List all their notes.
        - Create a new note.
    Attributes:
        serializer_class (NoteSerializer): The serializer class used to validate and serialize the data.
        permission_classes (list): A list of permission classes that the user must pass to access this view.
    Methods:
        get_queryset(self):
            Returns the queryset of notes filtered by the authenticated user.
    """
    serializer_class = NoteSerializer

    # Cannot access this view unless you're an authenticated user
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns a queryset of Note objects filtered by the current user.
        This method retrieves the current user from the request and filters
        the Note objects to include only those authored by the user.

        Returns:
            QuerySet: A Django QuerySet containing Note objects authored by the current user.
        """
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        """
        Saves the new note with the current user as the author.

        Args:
            serializer (NoteSerializer): The serializer instance used to validate and save the note data.
        
        Returns:
            None
        """
        # Save the note with the current user as the author
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)

class NoteDelete(generics.DestroyAPIView):
    """
    API view to delete a note.
    This view allows authenticated users to delete a note by its ID.
    Attributes:
        queryset (QuerySet): A queryset of all Note objects.
        permission_classes (list): A list of permission classes that the user must pass to access this view.
    """
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Returns a queryset of Note objects filtered by the current user.
        This method retrieves the current user from the request and filters
        the Note objects to include only those authored by the user.

        Returns:
            QuerySet: A Django QuerySet containing Note objects authored by the current user.
        """

        user = self.request.user
        return Note.objects.filter(author=user)
        


class CreateUserView(generics.CreateAPIView):
    """
    API view to create a new user.
    This view allows for the creation of a new user in the system. It uses
    Django REST framework's `CreateAPIView` to handle the creation process.
    Attributes:
        queryset (QuerySet): A queryset of all User objects.
        serializer_class (Serializer): The serializer class used to validate and
            save the user data.
        permission_classes (tuple): The permission classes that determine who
            can access this view. In this case, it allows any user to access it.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
