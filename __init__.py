from mycroft import MycroftSkill, intent_file_handler
from datetime import datetime
import pytz

class SkillRecappTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('time.start.intent')
    def handle_time_recapp_skill(self, message):
        swiss_timezone = pytz.timezone('Europe/Zurich')
        now = datetime.now(swiss_timezone)

        self.hours = now.strftime("%H")
        self.minutes = self.round_time(now.strftime("%M"))
        self.log.info("rounding minutes done")

        if (minutes == 0):
            self.output_full_hour()
        elif (minutes % 30 == 0):
            self.output_half_hour()
        elif (minutes % 15 == 0):
            self.output15()
        elif (minutes < 30):
            self.output_ab()
        else:
            self.output_vor()
        self.speak_dialog('time.start', data={
            'hours': hours,
            "minutes": minutes
        })

    def round_time(self, curr_minutes):
        minutes = int(curr_minutes)
        rest = minutes % 5
        if (rest > 3): # round up
            return minutes + 5 - rest
        else:
            return minutes - rest

    def output_full_hour():
        pass


def create_skill():
    return SkillRecappTime()

