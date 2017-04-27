print "Populating Earth with BLE..."

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


# BLE part
import pexpect as px

i=0
mom = ""
word_count = 2
index = (word_count-1)*6

gatt = px.spawn('gatttool -b AA:BB:CC:DD:EE:FF -I')


gatt.sendline('connect ')
gatt.expect('CON')
gatt.sendline('mtu 247')



x = 0

while True:
    gatt.expect("Notification handle = 0x001e value: ")    #If there is no responds resent mtu 247
    mom = gatt.readline()

    x = int(mom[index :index +5].replace(" ",""),16)
    print mom
    print x
    q = ECoG(Value=x, Time=timezone.now())
    q.save()
    queryset = ECoG.objects.all()
    #print([p.Time.strftime('%m/%d/%Y') for p in queryset])
    #print([str(p.Value) for p in queryset])



print "Never Reach me"
