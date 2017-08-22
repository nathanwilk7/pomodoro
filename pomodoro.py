#!/usr/bin/env python

import datetime
import time

from subprocess import call

focus_time = 25
diffuse_time = 5
long_break_time = 20
iterations = 4
seconds_in_minute = 60
notification_cmd = 'notify-send "{msg}"'
notification_msg = '{action} for {time_min} minutes'
focus_msg = 'FOCUS'
diffuse_msg = 'DIFFUSE'
long_break_msg = 'LONG BREAK'

def get_time():
    now = datetime.datetime.now()
    return '{hour: <2}:{min: <2} '.format(hour=now.hour, min=now.minute)

def start_focus(iteration):
    print(get_time() + 'focus {iteration} of {iterations}'.format(iteration=iteration, iterations=iterations))
    call(notification_cmd.format(msg=notification_msg.format(action=focus_msg, time_min=focus_time)), shell=True)
    time.sleep(focus_time * seconds_in_minute)
    if iteration >= iterations:
        start_long_break(iteration)
    else:
        start_diffuse(iteration)

def start_diffuse(iteration):
    print(str(get_time() + 'diffuse'))
    call(notification_cmd.format(msg=notification_msg.format(action=diffuse_msg, time_min=diffuse_time)), shell=True)
    time.sleep(diffuse_time * seconds_in_minute)
    start_focus(iteration + 1)

def start_long_break(iteration):
    print(get_time() + 'long break')
    call(notification_cmd.format(msg=notification_msg.format(action=long_break_msg, time_min=long_break_time)), shell=True)
    time.sleep(long_break_time * seconds_in_minute)
    start_focus(1)
    
def main():
    print('Press ^-C or CTRL-C to close: ')
    iteration = 1
    start_focus(iteration)

main()
