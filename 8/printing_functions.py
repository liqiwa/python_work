import print_models

from build_profile import build_profiles
print(build_profiles)
from build_profile import build_profiles as pp
print(pp('he','aa',location='dd'))

import build_profile as bu 
print(bu.build_profiles('bu','shi',location='japan'))
from build_profile import *
print(build_profiles('all *','***',location='super'))
