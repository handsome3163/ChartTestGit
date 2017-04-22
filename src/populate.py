print "Populating Earth..."

import datetime

from django.db import models
from django.utils import timezone
import os
import sys
import django
import time

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charts.settings')
django.setup()

from charts.models import ECoG
from django.utils import timezone
x = 0

while True:
    time.sleep(2)

    q = ECoG(Value=x, Time=timezone.now())
    q.save()
    #print q.id
    x = x+1;
    print ECoG.objects.latest('id').id
    queryset = ECoG.objects.all()
    print([p.Time.strftime('%m/%d/%Y') for p in queryset])
    print([str(p.Value) for p in queryset])





print "Never Reach me"
