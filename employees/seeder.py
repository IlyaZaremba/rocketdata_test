import os
import sys

import django

sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), ".."))
os.environ['DJANGO_SETTINGS_MODULE'] = 'rocketdata.settings'
django.setup()

from django_seed import Seed
from employees.models import Employee, User

seeder = Seed.seeder()
seeder.add_entity(Employee, 5, {
    'name': seeder.faker.name(),

})

inserted_pks = seeder.execute()
