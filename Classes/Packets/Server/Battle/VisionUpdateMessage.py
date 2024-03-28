from Classes.Packets.PiranhaMessage import PiranhaMessage
import random
from Classes.BitStream import BitStream

class VisionUpdateMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0

    def encode(self, fields, player):
        self.writeVInt(fields["BattleTick"]) # Battle Tick
        self.writeVInt(0) # wifi posral jidko
        self.writeVInt(0) # Commands Count
        self.writeVInt(fields["BattleTick"]) # spectators
        self.writeBoolean(True) # Live Boolean
        
        #self.writeBoolean(False)
        
        stream = BitStream()
        b = BitStream()
        
        self.writeBytes(stream.getBuff(), len(stream.getBuff()))
        
    def decode(self):
        return {}

    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 24109

    def getMessageVersion(self):
        return self.messageVersion