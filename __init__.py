from mycroft import MycroftSkill, intent_file_handler
from datetime import datetime

class SkillRecappTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('time.recapp.skill.intent')
    def handle_time_recapp_skill(self, message):
        now = datetime.now()

        hours = now.strftime("%H")
        curr_minutes = round_time(now.strftime("%M"))

        minutes = round_time(curr_minutes)
        self.speak_dialog('time.recapp.skill', data={
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

