from Classes.Messaging import Messaging

from Classes.Packets.PiranhaMessage import PiranhaMessage


class StartGameMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields):
        pass

    def decode(self):
        fields = {}
        super().decode(fields)
        return fields

    def execute(message, calling_instance, fields):
        fields["Socket"] = calling_instance.client
        fields['BattleTick'] = calling_instance.player.battleTick + 1
        Messaging.sendMessage(24112, fields, calling_instance.player)
        Messaging.sendMessage(20559, fields, calling_instance.player)
        #Messaging.sendMessage(24109, fields, calling_instance.player)

    def getMessageType(self):
        return 14103

    def getMessageVersion(self):
        return self.messageVersion