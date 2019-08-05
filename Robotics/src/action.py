# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Carry out voice commands by recognising keywords."""

import datetime
import logging
import subprocess

import actionbase

from otonomgorev import cizgi
from otonomgorev import kapat

from hareketsesli import ileri
from hareketsesli import geri
from hareketsesli import sol
from hareketsesli import sag
from hareketsesli import sesli
from hareketsesli import ses
from hareketsesli import led

from PortalTurret import Turret_deploy
from PortalTurret import Turret_die
from PortalTurret import Turret_retract
from PortalTurret import Turret_turret_shotat_1
from PortalTurret import Turret_turret_search_2
from PortalTurret import Turret_turret_tipped_4
from PortalTurret import Turret_ping
from PortalTurret import Turret_sp_sabotage_factory_good_fail02
from PortalTurret import Turret_turret_fire_4x_01
from PortalTurret import Turret_turretshotbylaser09
from PortalTurret import Turret_turretshotbylaser10
from PortalTurret import Turret_turretwitnessdeath02
from PortalTurret import Turret_turretwitnessdeath03
from PortalTurret import Turret_turretwitnessdeath05
from PortalTurret import Turret_turretwitnessdeath06
from PortalTurret import Turret_turretwitnessdeath07
from PortalTurret import Turret_turretwitnessdeath08
from PortalTurret import Turret_turretwitnessdeath11
from PortalTurret import Turret_turretwitnessdeath12
from PortalTurret import Turret_turretwitnessdeath13
from PortalTurret import Turret_turretwitnessdeath14
from PortalTurret import Turret_turretwitnessdeath15
from PortalTurret import Hello
from PortalTurret import Turret_sp_sabotage_factory_good_pass01
from PortalTurret import Turret_sp_sabotage_factory_good_prerange01
from PortalTurret import Turret_sp_sabotage_factory_good_fail01
from PortalTurret import Turret_sp_sabotage_factory_good_fail04
from PortalTurret import Turret_sp_sabotage_factory_good_fail05
from PortalTurret import Turret_sp_sabotage_factory_good_fail07
from PortalTurret import Hi
from PortalTurret import Turret_turret_active_2
from PortalTurret import Turret_turret_active_3
from PortalTurret import Turret_turret_active_6
from PortalTurret import Turret_turret_active_8
from PortalTurret import Turret_turret_autosearch_1
from PortalTurret import Turret_turret_autosearch_2
from PortalTurret import Turret_turret_autosearch_3
from PortalTurret import Turret_turret_autosearch_4
from PortalTurret import Turret_turret_autosearch_5
from PortalTurret import Turret_turret_autosearch_6
from PortalTurret import Turret_turret_collide_1
from PortalTurret import Turret_turret_collide_2
from PortalTurret import Turret_turret_collide_3
from PortalTurret import Turret_turret_collide_4
from PortalTurret import Turret_turret_collide_5
from PortalTurret import Turret_turret_deploy_2
from PortalTurret import Turret_turret_deploy_3
from PortalTurret import Turret_turret_deploy_4
from PortalTurret import Turret_turret_deploy_5
from PortalTurret import Turret_turret_disabled_1
from PortalTurret import Turret_turret_disabled_8
from PortalTurret import Turret_turret_disabled_2
from PortalTurret import Turret_turret_disabled_3
from PortalTurret import Shutdown
from PortalTurret import Turret_turret_disabled_5
from PortalTurret import Turret_turret_disabled_7
from PortalTurret import Turret_turret_disabled_6
from PortalTurret import Turret_turret_pickup_6
from PortalTurret import Turret_turret_fizzler_1
from PortalTurret import Turret_turret_protect_humans01

import time
import os

# =============================================================================
#
# Hey, Makers!
#
# This file contains some examples of voice commands that are handled locally,
# right on your Raspberry Pi.
#
# Do you want to add a new voice command? Check out the instructions at:
# https://aiyprojects.withgoogle.com/voice/#makers-guide-3-3--create-a-new-voice-command-or-action
# (MagPi readers - watch out! You should switch to the instructions in the link
#  above, since there's a mistake in the MagPi instructions.)
#
# In order to make a new voice command, you need to do two things. First, make a
# new action where it says:
#   "Implement your own actions here"
# Secondly, add your new voice command to the actor near the bottom of the file,
# where it says:
#   "Add your own voice commands here"
#
# =============================================================================

# Actions might not use the user's command. pylint: disable=unused-argument


# Example: Say a simple response
# ================================
#
# This example will respond to the user by saying something. You choose what it
# says when you add the command below - look for SpeakAction at the bottom of
# the file.
#
# There are two functions:
# __init__ is called when the voice commands are configured, and stores
# information about how the action should work:
#   - self.say is a function that says some text aloud.
#   - self.words are the words to use as the response.
# run is called when the voice command is used. It gets the user's exact voice
# command as a parameter.

class SpeakAction(object):

    """Says the given text via TTS."""

    def __init__(self, say, words):
        self.say = say
        self.words = words

    def run(self, voice_command):
        self.say(self.words)


# Example: Tell the current time
# ==============================
#
# This example will tell the time aloud. The to_str function will turn the time
# into helpful text (for example, "It is twenty past four."). The run function
# uses to_str say it aloud.

class SpeakTime(object):

    """Says the current local time with TTS."""

    def __init__(self, say):
        self.say = say

    def run(self, voice_command):
        time_str = self.to_str(datetime.datetime.now())
        self.say(time_str)

    def to_str(self, dt):
        """Convert a datetime to a human-readable string."""
        HRS_TEXT = ['midnight', 'one', 'two', 'three', 'four', 'five', 'six',
                    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
        MINS_TEXT = ["five", "ten", "quarter", "twenty", "twenty-five", "half"]
        hour = dt.hour
        minute = dt.minute

        # convert to units of five minutes to the nearest hour
        minute_rounded = (minute + 2) // 5
        minute_is_inverted = minute_rounded > 6
        if minute_is_inverted:
            minute_rounded = 12 - minute_rounded
            hour = (hour + 1) % 24

        # convert time from 24-hour to 12-hour
        if hour > 12:
            hour -= 12

        if minute_rounded == 0:
            if hour == 0:
                return 'It is midnight.'
            return "It is %s o'clock." % HRS_TEXT[hour]

        if minute_is_inverted:
            return 'It is %s to %s.' % (MINS_TEXT[minute_rounded - 1], HRS_TEXT[hour])
        return 'It is %s past %s.' % (MINS_TEXT[minute_rounded - 1], HRS_TEXT[hour])


# Example: Run a shell command and say its output
# ===============================================
#
# This example will use a shell command to work out what to say. You choose the
# shell command when you add the voice command below - look for the example
# below where it says the IP address of the Raspberry Pi.

class SpeakShellCommandOutput(object):

    """Speaks out the output of a shell command."""

    def __init__(self, say, shell_command, failure_text):
        self.say = say
        self.shell_command = shell_command
        self.failure_text = failure_text

    def run(self, voice_command):
        output = subprocess.check_output(self.shell_command, shell=True).strip()
        if output:
            self.say(output)
        elif self.failure_text:
            self.say(self.failure_text)


# Example: Change the volume
# ==========================
#
# This example will can change the speaker volume of the Raspberry Pi. It uses
# the shell command SET_VOLUME to change the volume, and then GET_VOLUME gets
# the new volume. The example says the new volume aloud after changing the
# volume.

class VolumeControl(object):

    """Changes the volume and says the new level."""

    GET_VOLUME = r'amixer get Master | grep "Front Left:" | sed "s/.*\[\([0-9]\+\)%\].*/\1/"'
    SET_VOLUME = 'amixer -q set Master %d%%'

    def __init__(self, say, change):
        self.say = say
        self.change = change

    def run(self, voice_command):
        res = subprocess.check_output(VolumeControl.GET_VOLUME, shell=True).strip()
        try:
            logging.info("volume: %s", res)
            vol = int(res) + self.change
            vol = max(0, min(100, vol))
            subprocess.call(VolumeControl.SET_VOLUME % vol, shell=True)
            self.say(_('Volume at %d %%.') % vol)
        except (ValueError, subprocess.CalledProcessError):
            logging.exception("Error using amixer to adjust volume.")


# Example: Repeat after me
# ========================
#
# This example will repeat what the user said. It shows how you can access what
# the user said, and change what you do or how you respond.

class RepeatAfterMe(object):

    """Repeats the user's command."""

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, voice_command):
        # The command still has the 'repeat after me' keyword, so we need to
        # remove it before saying whatever is left.
        to_repeat = voice_command.replace(self.keyword, '', 1)
        self.say(to_repeat)


# Ozel kodlar... ses aktivasyonlu hareket komutları


class Ileri(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_deploy()
        ileri(0.5,100)       
        
class Geri(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_deploy()
        geri(0.5,100)

class Sol(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_deploy()
        sol(0.5,100)

class Sag(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_deploy()
        sag(0.5,100)

class Duzbak(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_turret_active_2()
        sesli(0)

class Yukaribak(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(2)

class Asagibak(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(1)

class Solabak(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(3)

class Sagabak(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(4)

class Kolsol(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(13)

class Kolsag(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(14)

class Kolyuk(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(5)

class Kolasa(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(6)

class Kancaac(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(7)

class Kancakapa(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        sesli(8)

class Fren(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_retract()
        sesli(9)

class Evet(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_turret_shotat_1()
        sesli(10)

class Hayir(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_turret_search_2()
        sesli(11)

class Uzgun(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_turret_tipped_4()
        sesli(12)

class Ses(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        ses(0.6,666)

class Led(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        led(100,1,2)

class Ledleft(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        led(100,1,0)

class Ledright(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        Turret_ping()
        led(100,1,1)


# Voice commands with Portal 2 Turret answers

class Turret1(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('I did everything you asked!!!')
        Turret_sp_sabotage_factory_good_fail02()

class Turret2(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Firing to kill!!!')
        Turret_turret_fire_4x_01()
        led(100,1,2)

class Turret3(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('OK you win')
        Turret_turretshotbylaser09()

class Turret4(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('This is not good.')
        Turret_turretshotbylaser10()

class Turret5(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Well done.')
        Turret_turretwitnessdeath02()

class Turret6(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('I need backup')
        Turret_turretwitnessdeath03()
        sesli(2)
        time.sleep(1)
        self.say('but I do not')
        sesli(0)
        time.sleep(1)
        sesli(5)
        sesli(7)
        sesli(1)
        self.say('put it in my hand, you have 3 seconds for that')
        time.sleep(3)
        sesli(8)
        time.sleep(0.8)        
        sesli(6) 
        sesli(0)

class Turret7(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('I never liked her.')
        Turret_turretwitnessdeath05()

class Turret8(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('These things happen.')
        Turret_turretwitnessdeath06()

class Turret9(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('That was nobodys fault.')
        Turret_turretwitnessdeath07()

class Turret10(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('She was provoking you.')
        Turret_turretwitnessdeath08()

class Turret11(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('I blame myself.')
        Turret_turretwitnessdeath11()

class Turret12(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('She probably deserved it.')
        Turret_turretwitnessdeath12()

class Turret13(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('I saw it. It was an accident.')
        Turret_turretwitnessdeath13()

class Turret14(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('She is probably OK.')
        Turret_turretwitnessdeath14()

class Turret15(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Noted.')
        Turret_turretwitnessdeath15()

class Turret16(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Hello?, Hello friend, There you are, Who is there, ')
        Hello()

class Turret17(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Hello.')
        Turret_sp_sabotage_factory_good_pass01()

class Turret18(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Target aquired')
        Turret_sp_sabotage_factory_good_prerange01()

class Turret19(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Whyyyy?')
        Turret_sp_sabotage_factory_good_fail01()

class Turret20(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('I am fineeee')
        Turret_sp_sabotage_factory_good_fail04()

class Turret21(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Ahhhh')
        Turret_sp_sabotage_factory_good_fail05()

class Turret22(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Whyyy?')
        Turret_sp_sabotage_factory_good_fail07()

class Turret23(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Hi, Hello')
        Hi()

class Turret24(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Target aquired')
        Turret_turret_active_2()

class Turret25(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Dispensing product')
        Turret_turret_active_3()

class Turret26(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Gotcha!!!')
        Turret_turret_active_6()

class Turret27(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('I see you.')
        Turret_turret_active_8()

class Turret28(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Hellooo')
        Turret_turret_autosearch_1()

class Turret29(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Searching...')
        Turret_turret_autosearch_2()

class Turret30(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Canvassing...')
        Turret_turret_autosearch_3()

class Turret31(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Sentry mode activated...')
        Turret_turret_autosearch_4()

class Turret32(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Is anyone there?')
        Turret_turret_autosearch_5()

class Turret33(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Could you come over, here?')
        Turret_turret_autosearch_6()

class Turret34(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Coming through')
        Turret_turret_collide_1()
        ileri(3,100)
        print ('Excuse me')
        Turret_turret_collide_2()
        ileri(1,100)

class Turret35(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Sorry')
        Turret_turret_collide_3()

class Turret36(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('My fault')
        Turret_turret_collide_4()

class Turret37(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Ohh')
        Turret_turret_collide_5()

class Turret38(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Deploying...')
        Turret_turret_deploy_2()
        cizgi(300)

class Turret39(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Preparing to dispense product...')
        Turret_turret_deploy_3()

class Turret40(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Activated.')
        Turret_turret_deploy_4()

class Turret41(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('There you are...')
        Turret_turret_deploy_5()

class Turret42(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Ahahaa')
        Turret_turret_disabled_1()
        time.sleep(2)
        print ('No hard feelings.')
        Turret_turret_disabled_8()

class Turret43(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Critical error')
        Turret_turret_disabled_2()

class Turret44(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Sorry we are closed.')
        Turret_turret_disabled_3()

class Turret45(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Shutting down...')
        Shutdown()

class Turret46(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('I do not blame you!')
        Turret_turret_disabled_5()

class Turret47(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Whyyyy?')
        Turret_turret_disabled_7()
        time.sleep(2)
        print ('I do not hate you')
        Turret_turret_disabled_6()

class Turret48(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Who are you???')
        Turret_turret_pickup_6()

class Turret49(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Aiaiaiaiaiai...')
        Turret_turret_fizzler_1()

class Turret50(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('But I need to protect the humans.')
        Turret_turret_protect_humans01()

class Turret51(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        print ('Deploying...')
        Turret_turret_deploy_2()
        time.sleep(2)
        self.say(self.keyword)
        time.sleep(3) 
        cizgi(100)        

class Turret52(object):

    def __init__(self, say, keyword):
        self.say = say
        self.keyword = keyword

    def run(self, command):
        self.say(self.keyword)
        time.sleep(1.5)
        print ('This is not good.')
        Turret_turretshotbylaser10()
        time.sleep(3)
        kapat()

# =========================================
# Makers! Implement your own actions here.
# =========================================


def make_actor(say):
    """Create an actor to carry out the user's commands."""

    actor = actionbase.Actor()

    actor.add_keyword(
        _('ip address'), SpeakShellCommandOutput(
            say, "ip -4 route get 1 | head -1 | cut -d' ' -f8",
            _('I do not have an ip address assigned to me.')))

    actor.add_keyword(_('volume up'), VolumeControl(say, 10))
    actor.add_keyword(_('volume down'), VolumeControl(say, -10))
    actor.add_keyword(_('max volume'), VolumeControl(say, 100))

    actor.add_keyword(_('go forward'), Ileri(say, _('going forward')))
    actor.add_keyword(_('go backward'), Geri(say, _('going backward')))
    actor.add_keyword(_('turn left'), Sol(say, _('turning left')))
    actor.add_keyword(_('turn right'), Sag(say, _('turning right')))
    actor.add_keyword(_('look ahead'), Duzbak(say, _('looking ahead')))
    actor.add_keyword(_('look up'), Yukaribak(say, _('looking up')))
    actor.add_keyword(_('look down'), Asagibak(say, _('looking down')))
    actor.add_keyword(_('look left'), Solabak(say, _('looking left')))
    actor.add_keyword(_('look right'), Sagabak(say, _('looking right')))
    actor.add_keyword(_('arm left'), Kolsol(say, _('robotic arm turning left')))
    actor.add_keyword(_('arm right'), Kolsag(say, _('robotic arm turning right')))
    actor.add_keyword(_('arm up'), Kolyuk(say, _('robotic arm going up')))
    actor.add_keyword(_('arm down'), Kolasa(say, _('robotic arm going down')))
    actor.add_keyword(_('gripper open'), Kancaac(say, _('gripper opening')))
    actor.add_keyword(_('gripper close'), Kancakapa(say, _('gripper closing')))
    actor.add_keyword(_('stop'), Fren(say, _('breaking')))
    actor.add_keyword(_('express yes'), Evet(say, _('expressing yes')))
    actor.add_keyword(_('express no'), Hayir(say, _('expressing no')))
    actor.add_keyword(_('be sad'), Uzgun(say, _('being sad')))
    actor.add_keyword(_('make sound'), Ses(say, _('making sound')))
    actor.add_keyword(_('light the leds'), Led(say, _('lighting the leds now')))
    actor.add_keyword(_('light the left led'), Ledleft(say, _('lighting the left led now')))
    actor.add_keyword(_('light the right led'), Ledright(say, _('lighting the right led now'))) 

# Voice commands with Portal 2 Turret answers

    actor.add_keyword(_('are you stupid'), Turret1(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('fire'), Turret2(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what you will do now'), Turret3(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('I do not like you'), Turret4(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about this'), Turret5(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('take this'), Turret6(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about sally'), Turret7(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about diana'), Turret7(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about emily'), Turret7(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about her'), Turret7(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about that girl'), Turret7(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about that lady'), Turret7(say, _('PortalTurretAnswers')))

    actor.add_keyword(_('I lost my keys'), Turret8(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('the bomb is exploded'), Turret9(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about that robot'), Turret10(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about that guy'), Turret10(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about that girl'), Turret10(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what do you think about that lady'), Turret10(say, _('PortalTurretAnswers')))

    actor.add_keyword(_('who did this'), Turret11(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('I killed her'), Turret12(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('he is dead'), Turret13(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('call a doctor'), Turret14(say, _('PortalTurretAnswers')))    
    actor.add_keyword(_('note this'), Turret15(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('hello'), Turret16(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('hello there'), Turret17(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('kill him'), Turret18(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('jump of the window'), Turret19(say, _('PortalTurretAnswers'))) 
    actor.add_keyword(_('how are you'), Turret20(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('I will kill you'), Turret21(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('I blame you'), Turret22(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('hi'), Turret23(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('catch him'), Turret24(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('just do it'), Turret25(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('I am finally here'), Turret26(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('it is me'), Turret27(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('robot'), Turret28(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('find him'), Turret29(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('find her'), Turret30(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('find them'), Turret31(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('hi Jack'), Turret32(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('do you hear me'), Turret33(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('come here'), Turret34(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('what are you doing'), Turret35(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('sorry'), Turret36(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('oh men'), Turret37(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('deploy'), Turret38(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('be ready'), Turret39(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('activate searching mode'), Turret40(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('activate killing mode'), Turret40(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('activate sentry mode'), Turret31(say, _('PortalTurretAnswers')))    
    actor.add_keyword(_('activate swift mode'), Turret40(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('activate flying mode'), Turret40(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('activate climbing mode'), Turret40(say, _('PortalTurretAnswers')))

    actor.add_keyword(_('I am here'), Turret41(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('die'), Turret42(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('kill yourself'), Turret43(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('come over here'), Turret44(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('shut down'), Turret45(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('sorry for that'), Turret46(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('I hate you'), Turret47(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('where are you coming from'), Turret48(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('evaporate yourself'), Turret49(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('suicide yourself'), Turret50(say, _('PortalTurretAnswers')))
    actor.add_keyword(_('follow the line'), Turret51(say, _('switching to infinite autonomous mode, press ctrl+c to exit')))
    actor.add_keyword(_('exit the program'), Turret52(say, _('stopping the main program')))

    actor.add_keyword(_('repeat after me'),
                      RepeatAfterMe(say, _('repeat after me')))

    # =========================================
    # Makers! Add your own voice commands here.
    # =========================================

    return actor


def add_commands_just_for_cloud_speech_api(actor, say):
    """Add simple commands that are only used with the Cloud Speech API."""
    def simple_command(keyword, response):
        actor.add_keyword(keyword, SpeakAction(say, response))

    simple_command('alexa', _("We've been friends since we were both starter projects"))
    simple_command(
        'beatbox',
        'pv zk pv pv zk pv zk kz zk pv pv pv zk pv zk zk pzk pzk pvzkpkzvpvzk kkkkkk bsch')
    simple_command(_('clap'), _('clap clap'))
    simple_command('google home', _('She taught me everything I know.'))
    simple_command(_('hello'), _('hello to you too'))
    simple_command(_('tell me a joke'),
                   _('What do you call an alligator in a vest? An investigator.'))
    simple_command(_('three laws of robotics'),
                   _("""The laws of robotics are
0: A robot may not injure a human being or, through inaction, allow a human
being to come to harm.
1: A robot must obey orders given it by human beings except where such orders
would conflict with the First Law.
2: A robot must protect its own existence as long as such protection does not
conflict with the First or Second Law."""))
    simple_command(_('where are you from'), _("A galaxy far, far, just kidding. I'm from errzingann."))
    simple_command(_('your name'), _('A machine has no name'))
    simple_command(_('what is your model'), _('My model is raspberry pi 3 robot version 4.2'))    
    simple_command(_('islamic song'), _('qabadah hhagilarr ghuu, derr Alllahh, ghu, ghu, ghu'))
    simple_command(_('who are you'), _('I am the robot, from, errzingann'))
    simple_command(_('who is your creator'), _('My creator is a robotic enhusiast'))
    simple_command(_('hey dude'), _('hey hey'))
    simple_command(_('how do you do'), _('I am super fine, you?'))
    simple_command(_('how old are you'), _('It is been a year since I was created'))
    simple_command(_('how tall are you'), _('I am around twenty five centimeters tall'))
    simple_command(_('do you speak english'), _('Yeah, probably'))
    simple_command(_('do you speak turkish'), _('Not, yet'))
    simple_command(_('where were you made in'), _('I was made in errzingann'))
    simple_command(_('are you a robot'), _('If you think so'))

    actor.add_keyword(_('time'), SpeakTime(say))

