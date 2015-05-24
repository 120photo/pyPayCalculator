#!	/usr/bin/env python
#  main.py
#  python-hours
#
#  Created by Jose Juarez on 3/13/09.
#  Copyright (c) 2009 Jose Juarez. All rights reserved.
#

hours = float(raw_input('how many hour did you work this pay period?\n'))
rate = float(raw_input('what is your pay rate?\n'))
ot = hours - 80
payment = hours * rate
ot_payment = ot * (rate * 1.5)

if hours > 80:
	hours = 80
	payment = hours * rate

print 'before taxes and no OT you should have made $', payment, 'this pay period.'

print 'on average you are making $', payment * 26, "a year."
print '(assuming you work this may hour per pay period\n and you had the same rate all year long.)'

if hours > 80:
	print 'you worked', ot, 'hour of over time this pay period'
	print 'you should have made $', ot_payment, 'of over time this pay period'

