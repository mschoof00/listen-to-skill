from mycroft import MycroftSkill, intent_file_handler


class ListenTo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('to.listen.intent')
    def handle_to_listen(self, message):
        artist = message.data.get('artist')

        self.speak_dialog('to.listen', data={
            'artist': artist
        })


def create_skill():
    return ListenTo()

