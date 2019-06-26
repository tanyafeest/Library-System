from rest_framework import viewsets
from rest_framework.response import Response
from .models import Profile,Loan
from .serializers import ProfileSerializer,BorrowerLoanSerializer,OwnerLoanSerializer


class ProfileAuthViewMixin(object):
    def get_profile(self):
        if not self.request.user or not self.request.user.is_authenticated:
            return None
        try:
            profile = Profile.objects.get(user=self.request.user)
        except Profile.DoesNotExist:
            return None
        return profile 

class ProfileViewSet(viewsets.GenericViewSet,ProfileAuthViewMixin):
    '''
    API Endpoint to list current logged in user details
    '''
    def list(self,request, format=None):
        profile = self.get_profile()
    
        if profile == None:
            return Response({"user":None},status=404)

        return Response( ProfileSerializer(profile).data )

class BorrowedLoanViewSet(viewsets.GenericViewSet,ProfileAuthViewMixin):
    '''Items that have been borrowed by the requesting user'''

    def get_queryset(self):
        profile = self.get_profile()
        if profile == None:
            return Loan.objects.none() 
        return Loan.objects.filter(borrower=profile,status="on-loan") 

    def list(self,request,format=None):
        borrowed_loans = self.get_queryset()

        return Response( BorrowerLoanSerializer(borrowed_loans, many=True).data ) 

class OwnerLoanViewSet(viewsets.GenericViewSet,ProfileAuthViewMixin):
    '''Items owned by the requesting user that are on loan'''

    def get_queryset(self):
        profile = self.get_profile()
        if profile == None:
            return Loan.objects.none() 
        return Loan.objects.filter(item__owner=profile,status="on-loan") 

    def list(self,request,format=None):
        borrowed_loans = self.get_queryset()
        return Response( OwnerLoanSerializer(borrowed_loans, many=True, context={'request':request}).data )

