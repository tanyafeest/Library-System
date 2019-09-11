from django.core.management.base import BaseCommand, CommandError
from lending.factories import TitleFactory
from lending.factories import LocationFactory
from lending.factories import LoanFactory
from lending.factories import ItemFactory
from lending.factories import ProfileFactory
from lending.factories import TitleRequestFactory
from lending.models import Title,LOAN_STATUS
from django.conf import settings
import requests
import factory
import random

class Command(BaseCommand):
    help = 'Generates test data for lending database. WARNING this will ADD data'

    def add_arguments(self, parser):
        parser.add_argument('num-titles', nargs = 1, type = int, default = 100)
        parser.add_argument('--loans-and-requests',
                action = "store_true",
                help = "flag to indicate to generate active loans and requests",
        )
        parser.add_argument('--multi-item-lender',
                action = "store_true",
                help = "flag to indicate to generate multiple items per profile instead of spreading them out over all",
        )
    def handle(self, *args, **options):
        if not settings.DEBUG:
            print("WARNING: you are not in DEBUG mode, are you sure you want to continue? Y/N")
            if input().lower() != "y":
                print("aborting")
                return
   
        if Title.objects.all().exists():
            print("WARNING: you have titles in your database. Do you want to generate more? Y/N")
            if input().lower() != "y":
                print("aborting")
                return

        LocationFactory(name="Branch Library")
        n = options['num-titles'][0]
        x = TitleFactory.create_batch(n,item='')
        if n<3:
            num_of_locations = n
        else:
            num_of_locations = 3
        e = LocationFactory.create_batch(num_of_locations)
        profile_list = []
        for o in range(n):
            temp_o = o%3  
            location = e[temp_o]
            q = profile_list.append(ProfileFactory(primary_location=location))
        loan_list = []
        if options.get("loans_and_requests"):
            for y in range(n):
                title = x[y]
                owner = profile_list[y//3 if options.get("multi_item_lender", False) else y]
                loan_list.append(LoanFactory(item=factory.SubFactory(ItemFactory, title=title,owner=owner),borrower=owner))
            for t in range(n):
                requester = profile_list[t]
                title = x[t]
                loan = loan_list[t]
                TitleRequestFactory.create_batch(1,requester=requester,title = title,loan=loan)
        else:
            for z in range(n):
                title = x[z]
                owner = profile_list[z//3 if options.get("multi_item_lender", False) else z]
                ItemFactory.create_batch(1, title=title,owner=owner)