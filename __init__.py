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

        hours = now.strftime("%H")
        minutes = self.round_time(now.strftime("%M"))
        self.log.info("rounding minutes done")

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



def create_skill():
    return SkillRecappTime()

