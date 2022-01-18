import os
import random
import sys

import django

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'rocketdata.settings'
django.setup()

from django_seed import Seed
from employees.models import Employee, User

seeder = Seed.seeder()
for i in range(100):
    seeder.add_entity(Employee, 1, {
        'name': seeder.faker.name(),
        'position': random.choice(Employee.EMPLOYEE_TYPE)[0]
    })


inserted_pks = seeder.execute()
