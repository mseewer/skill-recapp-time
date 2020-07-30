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

        self.hours = now.strftime("%H")
        self.minutes = self.round_time(now.strftime("%M"))
        self.log.info("rounding minutes done. Start with output:")

        if (minutes == 0):
            self.output_full_hour()
        elif (minutes % 30 == 0):
            self.output_half_hour()
        elif (minutes == 15):
            self.output_15()
        elif (minutes == 45):
            self.output_45()
        elif (minutes < 30):
            self.output_ab()
        else:
            self.output_vor()


    def round_time(self, curr_minutes):
        minutes = int(curr_minutes)
        rest = minutes % 5
        if (rest > 3): # round up
            return minutes + 5 - rest
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
        files = ["time.base", "time.45", "time.ab"]
        dialog_file = random.choice(files)
        self.speak_dialog(dialog_file, data={
            'hours': self.hours, 
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
                'hours': self.hours, 
                'minutes': (60 - self.minutes)
            })


def create_skill():
    return SkillRecappTime()

