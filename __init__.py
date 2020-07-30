from mycroft import MycroftSkill, intent_file_handler
from datetime import datetime
import pytz
import random

class SkillRecappTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('time.start.intent')
    def handle_time_recapp_skill(self, message):
        swiss_timezone = pytz.timezone('Europe/Zurich')
        now = datetime.now(swiss_timezone)

        self.hours = int(now.strftime("%I")) # %I is same as %H: gives hours, but in 12h format
        self.minutes = int(self.round_time(now.strftime("%M")))
        self.log.info("time rounded: {}:{}".format(self.hours, self.minutes))

        if (self.minutes % 60 == 0):
            self.output_full_hour()
        elif (self.minutes % 30 == 0):
            self.output_half_hour()
        elif (self.minutes == 15):
            self.output_15()
        elif (self.minutes == 45):
            self.output_45()
        elif (self.minutes < 30):
            self.output_ab()
        else:
            self.output_vor()


    def round_time(self, curr_minutes):
        minutes = int(curr_minutes)
        rest = minutes % 5
        if (rest >= 3): # round up
            new_minutes = minutes + 5 - rest
            if (new_minutes % 60 == 0): #full hour, need to change hour as well
                self.hours += 1
        else:
            return minutes - rest

    def output_full_hour(self):
        files = ["time.full.hour"]
        dialog_file = random.choice(files)
        self.speak_dialog(dialog_file, data={
            'hours': self.hours
        })

    def output_half_hour(self):
        files = ["time.base", "time.half.hour"]
        dialog_file = random.choice(files)
        if (dialog_file == "time.half.hour"):
            self.speak_dialog(dialog_file, data={
                'hours': (self.hours + 1)
            })
        else:
            self.speak_dialog(dialog_file, data={
                'hours': self.hours
            })

    def output_15(self):
        files = ["time.base", "time.15", "time.ab"]
        dialog_file = random.choice(files)
        self.speak_dialog(dialog_file, data={
            'hours': self.hours,
            'minutes': self.minutes
        })

    def output_45(self):
        files = ["time.base", "time.45", "time.vor"]
        dialog_file = random.choice(files)
        if (dialog_file == "time.vor"):
            self.speak_dialog(dialog_file, data={
                'hours': (self.hours + 1),
                'minutes': (60 - self.minutes)
            })
        elif (dialog_file == "time.45"):
            self.speak_dialog(dialog_file, data={
                'hours': (self.hours + 1),
                'minutes': self.minutes
             })

    def output_ab(self):
        files = ["time.base", "time.ab"]
        dialog_file = random.choice(files)
        self.speak_dialog(dialog_file, data={
            'hours': self.hours,
            'minutes': self.minutes
        })

    def output_vor(self):
        files = ["time.base", "time.vor"]
        dialog_file = random.choice(files)
        if (dialog_file == "time.base"):
            self.speak_dialog(dialog_file, data={
                'hours': self.hours,
                'minutes': self.minutes
            })
        else:
            self.speak_dialog(dialog_file, data={
                'hours': (self.hours + 1),
                'minutes': (60 - self.minutes)
            })


def create_skill():
    return SkillRecappTime()

