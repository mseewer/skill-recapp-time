from mycroft import MycroftSkill, intent_file_handler


class SkillRecappTime(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('time.recapp.skill.intent')
    def handle_time_recapp_skill(self, message):
        time = ''

        self.speak_dialog('time.recapp.skill', data={
            'time': time
        })


def create_skill():
    return SkillRecappTime()

