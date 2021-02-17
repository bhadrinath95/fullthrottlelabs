from main.models import Member, Activity_Period
from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
import string
import names
import random
from random import randrange
from datetime import timedelta, datetime
import pytz


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

class Command(BaseCommand):
    help = 'To populate the database with some dummy data'
    
    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of members to be created')
        
    def handle(self, *args, **kwargs):
        total = kwargs['total']
        try:
            for i in range(total):
                mem = Member.objects.create(
                    member_id=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8)),
                    real_name= names.get_full_name(),
                    tz= random.choice(pytz.all_timezones))
                list = []
                for i in range(random.randint(1,5)):
                    d1 = datetime.strptime("1/1/2020 1:00 AM", '%m/%d/%Y %I:%M %p')
                    d2 = datetime.strptime("1/1/2021 1:00 PM", '%m/%d/%Y %I:%M %p')
                    now = random_date(d1, d2)
                    st = now - timedelta(seconds=random.randint(0, 86400))
                    et = st + timedelta(seconds=random.randint(0, 86400)) 
                    ap = Activity_Period.objects.create(start_time=st.replace(tzinfo=pytz.UTC), end_time=et.replace(tzinfo=pytz.UTC))
                    list.append(ap)
                mem.activity_periods.set(list)
            self.stdout.write(f'Members are created successfully!')
        except Exception as err:
            self.stdout.write('Error in creating member. ' % err)
            
    