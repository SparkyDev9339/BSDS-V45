import json
import random
import string
from Classes.Files.Classes.Cards import Cards
from Classes.Files.Classes.Characters import Characters

class Player:
    ClientVersion = "0.0.0"

    ID = [0, 1]
    AllianceID = [0, 0]
    RoomID = [0, 0]
    Token = ""
    Name = "Brawler"
    Registered = False

    Vip = 0
    Thumbnail = 0
    Namecolor = 0
    Region = "RU"
    ContentCreator = ""

    Coins = 0
    CoinsGained = 0
    Gems = 0
    StarPoints = 0

    ChromaticTokens = 0
    RareTokens = 0
    Blings = 0

    ClubCoins = 0
    
    Trophies = 0
    HighestTrophies = 0
    TrophiesGained = 0
    TrophyRoadTier = 1
    Experience = 0
    Level = 0
    Tokens = 0
    TokensGained = 0
    TokensDoubler = 0

    PushasedOffers = []
    
    delivery_items = {}
    
    BattleLogs = {}
    
    banned = False
    
    BPTokens = 5000

    pl_rank = 1

    club_trophies = 0

    club_rank = 1

    club_tickets = 0

    vs = 0

    # Brawl Pass
    BrawlPassLVL32 = 0
    BrawlPassLVL64 = 0
    BrawlPassLVL96 = 0
    
    BrawlPass1LVL32 = 0
    BrawlPass1LVL64 = 0
    BrawlPass1LVL96 = 0

    RewardTrackType = 0
    RewardForRank = 0

    BrawlPassSeason = 0
    BrawlPassBuy = 0
    # Brawl Pass

    # Teams
    roomID = 0
    roomType = 0
    playerData = []

    # CsvReader
    brawlersID = Characters.getBrawlersID()
    # CsvReader End

    # Profiles
    favoriteBrawler = 0
    battleIcon = 0
    battleIcon1 = 0
    battlePin = 0
    battleTitle = 0

    threeXthreeWins = 0
    solowWins = 0
    duoWins = 0

    battleIconBrawler = {}
    for id in brawlersID:
        battleIconBrawler.update({f'{id}': 0})

    battleIcon1Brawler = {}
    for id in brawlersID:
        battleIcon1Brawler.update({f'{id}': 0})

    battlePinBrawler = {}
    for id in brawlersID:
        battlePinBrawler.update({f'{id}': 0})

    battleTitleBrawler = {}
    for id in brawlersID:
        battleTitleBrawler.update({f'{id}': 0})

    PowerPoints = 0
    
    NotificationFactory = {}

    SelectedSkins = {}
    for id in brawlersID:
        SelectedSkins.update({f'{id}': 0})

    SelectedBrawlers = [0, 1, 8]
    RandomizerSelectedSkins = []
    OwnedPins = []
    OwnedThumbnails = []
    SelectedBrawlersSkins = {
        0: 0,
	1: 0,
	8: 0,
    }
    OwnedBrawlers = {
        0: {'CardID': 0, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
        1: {'CardID': 4, 'Skins': [], 'Trophies': 0, 'HighestTrophies': 0, 'MasteryPoints': 0, 'MasteryClaimed': 0, 'PowerLevel': 1, 'PowerPoints': 0, 'State': 2},
    }

    def __init__(self):
        pass

    def getDataTemplate(self, highid, lowid, token):
        if highid == 0 and lowid == 0:
            self.ID[0] = int(''.join([str(random.randint(0, 9)) for _ in range(1)]))
            self.ID[1] = int(''.join([str(random.randint(0, 9)) for _ in range(8)]))
            self.Token = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(40))
        else:
            self.ID[0] = highid
            self.ID[1] = lowid
            self.Token = token

        DBData = {
            'ID': self.ID,
            'Token': self.Token,
            'Name': self.Name,
            'AllianceID': self.AllianceID,
            'RoomID': self.RoomID,
            'Registered': self.Registered,
            'Vip': self.Vip,
            'Thumbnail': self.Thumbnail,
            'Namecolor': self.Namecolor,
            'Region': self.Region,
            'ContentCreator': self.ContentCreator,
            'Coins': self.Coins,
            'CoinsGained': self.CoinsGained,
            'Gems': self.Gems,
            'StarPoints': self.StarPoints,

            'ChromaticTokens': self.ChromaticTokens,
            'RareTokens': self.RareTokens,
            'Blings': self.Blings,

            'ClubCoins': self.ClubCoins,
            'Trophies': self.Trophies,
            'HighestTrophies': self.HighestTrophies,
            'TrophiesGained': self.TrophiesGained,
            'TrophyRoadTier': self.TrophyRoadTier,
            'Experience': self.Experience,
            'Level': self.Level,
            'Tokens': self.Tokens,
            'TokensGained': self.TokensGained,
            'TokensDoubler': self.TokensDoubler,
            'PushasedOffers': self.PushasedOffers,
            'delivery_items': self.delivery_items,
            'BattleLogs': self.BattleLogs,
            'banned': self.banned,
            'BPTokens': self.BPTokens,
            'pl_rank': self.pl_rank,
            'club_trophies': self.club_trophies,
            'club_rank': self.club_rank,
            'club_tickets': self.club_tickets,
            # Profiles
            'favoriteBrawler': self.favoriteBrawler,
            'battleIcon': self.battleIcon,
            'battleIcon1': self.battleIcon1,
            'battlePin': self.battlePin,
            'battleTitle': self.battleTitle,
            'battleIconBrawler': self.battleIconBrawler,
            'battleIcon1Brawler': self.battleIcon1Brawler,
            'battlePinBrawler': self.battlePinBrawler,
            'battleTitleBrawler': self.battleTitleBrawler,
            'threeXthreeWins': self.threeXthreeWins,
            'soloWins': self.solowWins,
            'duoWins': self.duoWins,
            # Profiles End
            # BrawlPass
            'BrawlPassLVL32': self.BrawlPassLVL32,
            'BrawlPassLVL64': self.BrawlPassLVL64,
            'BrawlPassLVL96': self.BrawlPassLVL96,
            'BrawlPass1LVL32': self.BrawlPass1LVL32,
            'BrawlPass1LVL64': self.BrawlPass1LVL64,
            'BrawlPass1LVL96': self.BrawlPass1LVL96,
            'RewardTrackType': self.RewardTrackType,
            'RewardForRank': self.RewardForRank,
            'BrawlPassSeason': self.BrawlPassSeason,
            'BrawlPassBuy': self.BrawlPassBuy,
            # BrawlPass End
            'roomID': self.roomID,
            'roomType': self.roomType,
            'playerData': self.playerData,
            'brawlersID': self.brawlersID,
            'vs': self.vs,
            'PowerPoints': self.PowerPoints,
            'NotificationFactory': self.NotificationFactory,
            'SelectedSkins': self.SelectedSkins,
            'SelectedBrawlers': self.SelectedBrawlers,
            'OwnedPins': self.OwnedPins,
            'OwnedThumbnails': self.OwnedThumbnails,
            'OwnedBrawlers': self.OwnedBrawlers
        }
        return DBData

    def toJSON(self):
        return json.loads(json.dumps(self, default=lambda o: o.__dict__,
            sort_keys=True, indent=4))
