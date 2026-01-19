from .base import CardShapedThing, Cost, Pile

ADVENTURER = CardShapedThing("Adventurer", {"Action"}, Cost(coins=6), "Reveal cards from your deck until you reveal 2 Treasure cards. Put those Treasure cards into your hand and discard the other revealed cards.", "https://wiki.dominionstrategy.com/index.php/Adventurer", "./list_of_cards_files/200px-Adventurer.jpg")
ARTISAN = CardShapedThing("Artisan", {"Action"}, Cost(coins=6), "Gain a card to your hand costing up to $5.Put a card from your hand onto your deck.", "https://wiki.dominionstrategy.com/index.php/Artisan", "./list_of_cards_files/200px-Artisan.jpg")
BANDIT = CardShapedThing("Bandit", {"Action", "Attack"}, Cost(coins=5), "Gain a Gold. Each other player reveals the top 2 cards of their deck, trashes a revealed Treasure other than Copper, and discards the rest.", "https://wiki.dominionstrategy.com/index.php/Bandit", "./list_of_cards_files/200px-Bandit.jpg")
BUREAUCRAT = CardShapedThing("Bureaucrat", {"Action", "Attack"}, Cost(coins=4), "Gain a Silver onto your deck. Each other player reveals a Victory card from their hand and puts it onto their deck (or reveals a hand with no Victory cards).", "https://wiki.dominionstrategy.com/index.php/Bureaucrat", "./list_of_cards_files/200px-Bureaucrat.jpg")
CELLAR = CardShapedThing("Cellar", {"Action"}, Cost(coins=2), "+1 ActionDiscard any number of cards. +1 Card per card discarded.", "https://wiki.dominionstrategy.com/index.php/Cellar", "./list_of_cards_files/200px-Cellar.jpg")
CHANCELLOR = CardShapedThing("Chancellor", {"Action"}, Cost(coins=3), "+$2You may immediately put your deck into your discard pile.", "https://wiki.dominionstrategy.com/index.php/Chancellor", "./list_of_cards_files/200px-Chancellor.jpg")
CHAPEL = CardShapedThing("Chapel", {"Action"}, Cost(coins=2), "Trash up to 4 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Chapel", "./list_of_cards_files/200px-Chapel.jpg")
COUNCIL_ROOM = CardShapedThing("Council Room", {"Action"}, Cost(coins=5), "+4 Cards+1 BuyEach other player draws a card.", "https://wiki.dominionstrategy.com/index.php/Council_Room", "./list_of_cards_files/200px-Council_Room.jpg")
FEAST = CardShapedThing("Feast", {"Action"}, Cost(coins=4), "Trash this card. Gain a card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Feast", "./list_of_cards_files/200px-Feast.jpg")
FESTIVAL = CardShapedThing("Festival", {"Action"}, Cost(coins=5), "+2 Actions+1 Buy+$2", "https://wiki.dominionstrategy.com/index.php/Festival", "./list_of_cards_files/200px-Festival.jpg")
GARDENS = CardShapedThing("Gardens", {"Victory"}, Cost(coins=4), "Worth 1VP per 10 cards you have (round down).", "https://wiki.dominionstrategy.com/index.php/Gardens", "./list_of_cards_files/200px-Gardens.jpg")
HARBINGER = CardShapedThing("Harbinger", {"Action"}, Cost(coins=3), "+1 Card+1 ActionLook through your discard pile. You may put a card from it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Harbinger", "./list_of_cards_files/200px-Harbinger.jpg")
LABORATORY = CardShapedThing("Laboratory", {"Action"}, Cost(coins=5), "+2 Cards+1 Action", "https://wiki.dominionstrategy.com/index.php/Laboratory", "./list_of_cards_files/200px-Laboratory.jpg")
LIBRARY = CardShapedThing("Library", {"Action"}, Cost(coins=5), "Draw until you have 7 cards in hand, skipping any Action cards you choose to; set those aside, discarding them afterwards.", "https://wiki.dominionstrategy.com/index.php/Library", "./list_of_cards_files/200px-Library.jpg")
MARKET = CardShapedThing("Market", {"Action"}, Cost(coins=5), "+1 Card+1 Action+1 Buy+$1", "https://wiki.dominionstrategy.com/index.php/Market", "./list_of_cards_files/200px-Market.jpg")
MERCHANT = CardShapedThing("Merchant", {"Action"}, Cost(coins=3), "+1 Card+1 ActionThe first time you play a Silver this turn, +$1.", "https://wiki.dominionstrategy.com/index.php/Merchant", "./list_of_cards_files/200px-Merchant.jpg")
MILITIA = CardShapedThing("Militia", {"Action", "Attack"}, Cost(coins=4), "+$2Each other player discards down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Militia", "./list_of_cards_files/200px-Militia.jpg")
MINE = CardShapedThing("Mine", {"Action"}, Cost(coins=5), "You may trash a Treasure from your hand. Gain a Treasure to your hand costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Mine", "./list_of_cards_files/200px-Mine.jpg")
MOAT = CardShapedThing("Moat", {"Action", "Reaction"}, Cost(coins=2), "+2 CardsWhen another player plays an Attack card, you may first reveal this from your hand, to be unaffected by it.", "https://wiki.dominionstrategy.com/index.php/Moat", "./list_of_cards_files/200px-Moat.jpg")
MONEYLENDER = CardShapedThing("Moneylender", {"Action"}, Cost(coins=4), "You may trash a Copper from your hand for +$3.", "https://wiki.dominionstrategy.com/index.php/Moneylender", "./list_of_cards_files/200px-Moneylender.jpg")
POACHER = CardShapedThing("Poacher", {"Action"}, Cost(coins=4), "+1 Card+1 Action+$1Discard a card per empty Supply pile.", "https://wiki.dominionstrategy.com/index.php/Poacher", "./list_of_cards_files/200px-Poacher.jpg")
REMODEL = CardShapedThing("Remodel", {"Action"}, Cost(coins=4), "Trash a card from your hand. Gain a card costing up to $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Remodel", "./list_of_cards_files/200px-Remodel.jpg")
SENTRY = CardShapedThing("Sentry", {"Action"}, Cost(coins=5), "+1 Card+1 ActionLook at the top 2 cards of your deck. Trash and/or discard any number of them. Put the rest back on top in any order.", "https://wiki.dominionstrategy.com/index.php/Sentry", "./list_of_cards_files/200px-Sentry.jpg")
SMITHY = CardShapedThing("Smithy", {"Action"}, Cost(coins=4), "+3 Cards", "https://wiki.dominionstrategy.com/index.php/Smithy", "./list_of_cards_files/200px-Smithy.jpg")
SPY = CardShapedThing("Spy", {"Action", "Attack"}, Cost(coins=4), "+1 Card+1 ActionEach player (including you) reveals the top card of their deck and either discards it or puts it back, your choice.", "https://wiki.dominionstrategy.com/index.php/Spy", "./list_of_cards_files/200px-Spy.jpg")
THIEF = CardShapedThing("Thief", {"Action", "Attack"}, Cost(coins=4), "Each other player reveals the top 2 cards of their deck. If they revealed any Treasure cards, they trash one of them that you choose. You may gain any or all of these trashed cards. They discard the other revealed cards.", "https://wiki.dominionstrategy.com/index.php/Thief", "./list_of_cards_files/200px-Thief.jpg")
THRONE_ROOM = CardShapedThing("Throne Room", {"Action"}, Cost(coins=4), "You may play an Action card from your hand twice.", "https://wiki.dominionstrategy.com/index.php/Throne_Room", "./list_of_cards_files/200px-Throne_Room.jpg")
VASSAL = CardShapedThing("Vassal", {"Action"}, Cost(coins=3), "+$2Discard the top card of your deck. If it's an Action card, you may play it.", "https://wiki.dominionstrategy.com/index.php/Vassal", "./list_of_cards_files/200px-Vassal.jpg")
VILLAGE = CardShapedThing("Village", {"Action"}, Cost(coins=3), "+1 Card+2 Actions", "https://wiki.dominionstrategy.com/index.php/Village", "./list_of_cards_files/200px-Village.jpg")
WITCH = CardShapedThing("Witch", {"Action", "Attack"}, Cost(coins=5), "+2 CardsEach other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Witch", "./list_of_cards_files/200px-Witch.jpg")
WOODCUTTER = CardShapedThing("Woodcutter", {"Action"}, Cost(coins=3), "+1 Buy+$2", "https://wiki.dominionstrategy.com/index.php/Woodcutter", "./list_of_cards_files/200px-Woodcutter.jpg")
WORKSHOP = CardShapedThing("Workshop", {"Action"}, Cost(coins=3), "Gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Workshop", "./list_of_cards_files/200px-Workshop.jpg")
COPPER = CardShapedThing("Copper", {"Treasure"}, Cost(coins=0), "$1", "https://wiki.dominionstrategy.com/index.php/Copper", "./list_of_cards_files/200px-Copper.jpg")
SILVER = CardShapedThing("Silver", {"Treasure"}, Cost(coins=3), "$2", "https://wiki.dominionstrategy.com/index.php/Silver", "./list_of_cards_files/200px-Silver.jpg")
GOLD = CardShapedThing("Gold", {"Treasure"}, Cost(coins=6), "$3", "https://wiki.dominionstrategy.com/index.php/Gold", "./list_of_cards_files/200px-Gold.jpg")
ESTATE = CardShapedThing("Estate", {"Victory"}, Cost(coins=2), "1VP", "https://wiki.dominionstrategy.com/index.php/Estate", "./list_of_cards_files/200px-Estate.jpg")
DUCHY = CardShapedThing("Duchy", {"Victory"}, Cost(coins=5), "3VP", "https://wiki.dominionstrategy.com/index.php/Duchy", "./list_of_cards_files/200px-Duchy.jpg")
PROVINCE = CardShapedThing("Province", {"Victory"}, Cost(coins=8), "6VP", "https://wiki.dominionstrategy.com/index.php/Province", "./list_of_cards_files/200px-Province.jpg")
CURSE = CardShapedThing("Curse", {"Curse"}, Cost(coins=0), "-1VP", "https://wiki.dominionstrategy.com/index.php/Curse", "./list_of_cards_files/200px-Curse.jpg")
BARON = CardShapedThing("Baron", {"Action"}, Cost(coins=4), "+1 BuyYou may discard an Estate for +$4. If you don't, gain an Estate.", "https://wiki.dominionstrategy.com/index.php/Baron", "./list_of_cards_files/200px-Baron.jpg")
BRIDGE = CardShapedThing("Bridge", {"Action"}, Cost(coins=4), "+1 Buy+$1This turn, cards (everywhere) cost $1 less.", "https://wiki.dominionstrategy.com/index.php/Bridge", "./list_of_cards_files/200px-Bridge.jpg")
CONSPIRATOR = CardShapedThing("Conspirator", {"Action"}, Cost(coins=4), "+$2If you've played 3 or more Actions this turn (counting this), +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Conspirator", "./list_of_cards_files/200px-Conspirator.jpg")
COPPERSMITH = CardShapedThing("Coppersmith", {"Action"}, Cost(coins=4), "Copper produces an extra $1 this turn.", "https://wiki.dominionstrategy.com/index.php/Coppersmith", "./list_of_cards_files/200px-Coppersmith.jpg")
COURTIER = CardShapedThing("Courtier", {"Action"}, Cost(coins=5), "Reveal a card from your hand. For each type it has (Action, Attack, etc.), choose one: +1 Action; or +1 Buy; or +$3; or gain a Gold. The choices must be different.", "https://wiki.dominionstrategy.com/index.php/Courtier", "./list_of_cards_files/200px-Courtier.jpg")
COURTYARD = CardShapedThing("Courtyard", {"Action"}, Cost(coins=2), "+3 CardsPut a card from your hand onto your deck.", "https://wiki.dominionstrategy.com/index.php/Courtyard", "./list_of_cards_files/200px-Courtyard.jpg")
DIPLOMAT = CardShapedThing("Diplomat", {"Action", "Reaction"}, Cost(coins=4), "+2 CardsIf you have 5 or fewer cards in hand (after drawing), +2 Actions.When another player plays an Attack card, you may first reveal this from a hand of 5 or more cards, to draw 2 cards then discard 3.", "https://wiki.dominionstrategy.com/index.php/Diplomat", "./list_of_cards_files/200px-Diplomat.jpg")
DUKE = CardShapedThing("Duke", {"Victory"}, Cost(coins=5), "Worth 1VP per Duchy you have.", "https://wiki.dominionstrategy.com/index.php/Duke", "./list_of_cards_files/200px-Duke.jpg")
GREAT_HALL = CardShapedThing("Great Hall", {"Action", "Victory"}, Cost(coins=3), "+1 Card+1 Action1VP", "https://wiki.dominionstrategy.com/index.php/Great_Hall", "./list_of_cards_files/200px-Great_Hall.jpg")
FARM = CardShapedThing("Farm", {"Treasure", "Victory"}, Cost(coins=6), "$22VP", "https://wiki.dominionstrategy.com/index.php/Farm", "./list_of_cards_files/200px-Farm.jpg")
IRONWORKS = CardShapedThing("Ironworks", {"Action"}, Cost(coins=4), "Gain a card costing up to $4.If the gained card is an…Action card, +1 ActionTreasure card, +$1Victory card, +1 Card", "https://wiki.dominionstrategy.com/index.php/Ironworks", "./list_of_cards_files/200px-Ironworks.jpg")
LURKER = CardShapedThing("Lurker", {"Action"}, Cost(coins=2), "+1 ActionChoose one: Trash an Action card from the Supply; or gain an Action card from the trash.", "https://wiki.dominionstrategy.com/index.php/Lurker", "./list_of_cards_files/200px-Lurker.jpg")
MASQUERADE = CardShapedThing("Masquerade", {"Action"}, Cost(coins=3), "+2 CardsEach player with any cards in hand passes one to the next such player to their left, at once. Then you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Masquerade", "./list_of_cards_files/200px-Masquerade.jpg")
MILL = CardShapedThing("Mill", {"Action", "Victory"}, Cost(coins=4), "+1 Card+1 ActionYou may discard 2 cards. If you do, +$2.1VP", "https://wiki.dominionstrategy.com/index.php/Mill", "./list_of_cards_files/200px-Mill.jpg")
MINING_VILLAGE = CardShapedThing("Mining Village", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsYou may trash this for +$2.", "https://wiki.dominionstrategy.com/index.php/Mining_Village", "./list_of_cards_files/200px-Mining_Village.jpg")
MINION = CardShapedThing("Minion", {"Action", "Attack"}, Cost(coins=5), "+1 ActionChoose one: +$2; or discard your hand, +4 Cards, and each other player with at least 5 cards in hand discards their hand and draws 4 cards.", "https://wiki.dominionstrategy.com/index.php/Minion", "./list_of_cards_files/200px-Minion.jpg")
NOBLES = CardShapedThing("Nobles", {"Action", "Victory"}, Cost(coins=6), "Choose one: +3 Cards; or +2 Actions.2VP", "https://wiki.dominionstrategy.com/index.php/Nobles", "./list_of_cards_files/200px-Nobles.jpg")
PATROL = CardShapedThing("Patrol", {"Action"}, Cost(coins=5), "+3 CardsReveal the top 4 cards of your deck. Put the Victory cards and Curses into your hand. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Patrol", "./list_of_cards_files/200px-Patrol.jpg")
PAWN = CardShapedThing("Pawn", {"Action"}, Cost(coins=2), "Choose two: +1 Card; +1 Action; +1 Buy; +$1. The choices must be different.", "https://wiki.dominionstrategy.com/index.php/Pawn", "./list_of_cards_files/200px-Pawn.jpg")
REPLACE = CardShapedThing("Replace", {"Action", "Attack"}, Cost(coins=5), "Trash a card from your hand. Gain a card costing up to $2 more than it. If the gained card is an Action or Treasure, put it onto your deck; if it's a Victory card, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Replace", "./list_of_cards_files/200px-Replace.jpg")
SABOTEUR = CardShapedThing("Saboteur", {"Action", "Attack"}, Cost(coins=5), "Each other player reveals cards from the top of their deck until revealing one costing $3 or more. They trash that card and may gain a card costing at most $2 less than it. They discard the other revealed cards.", "https://wiki.dominionstrategy.com/index.php/Saboteur", "./list_of_cards_files/200px-Saboteur.jpg")
SCOUT = CardShapedThing("Scout", {"Action"}, Cost(coins=4), "+1 ActionReveal the top 4 cards of your deck. Put the revealed Victory cards into your hand. Put the other cards on top of your deck in any order.", "https://wiki.dominionstrategy.com/index.php/Scout", "./list_of_cards_files/200px-Scout.jpg")
SECRET_CHAMBER = CardShapedThing("Secret Chamber", {"Action", "Reaction"}, Cost(coins=2), "Discard any number of cards. +$1 per card discarded.When another player plays an Attack card, you may reveal this from your hand. If you do, +2 Cards, then put 2 cards from your hand on top of your deck.", "https://wiki.dominionstrategy.com/index.php/Secret_Chamber", "./list_of_cards_files/200px-Secret_Chamber.jpg")
SECRET_PASSAGE = CardShapedThing("Secret Passage", {"Action"}, Cost(coins=4), "+2 Cards+1 ActionTake a card from your hand and put it anywhere in your deck.", "https://wiki.dominionstrategy.com/index.php/Secret_Passage", "./list_of_cards_files/200px-Secret_Passage.jpg")
SHANTY_TOWN = CardShapedThing("Shanty Town", {"Action"}, Cost(coins=3), "+2 ActionsReveal your hand. If you have no Action cards in hand, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Shanty_Town", "./list_of_cards_files/200px-Shanty_Town.jpg")
STEWARD = CardShapedThing("Steward", {"Action"}, Cost(coins=3), "Choose one: +2 Cards; or +$2; or trash 2 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Steward", "./list_of_cards_files/200px-Steward.jpg")
SWINDLER = CardShapedThing("Swindler", {"Action", "Attack"}, Cost(coins=3), "+$2Each other player trashes the top card of their deck and gains a card with the same cost that you choose.", "https://wiki.dominionstrategy.com/index.php/Swindler", "./list_of_cards_files/200px-Swindler.jpg")
TORTURER = CardShapedThing("Torturer", {"Action", "Attack"}, Cost(coins=5), "+3 CardsEach other player either discards 2 cards or gains a Curse to their hand, their choice. (They may pick an option they can't do.)", "https://wiki.dominionstrategy.com/index.php/Torturer", "./list_of_cards_files/200px-Torturer.jpg")
TRADING_POST = CardShapedThing("Trading Post", {"Action"}, Cost(coins=5), "Trash 2 cards from your hand. If you did, gain a Silver to your hand.", "https://wiki.dominionstrategy.com/index.php/Trading_Post", "./list_of_cards_files/200px-Trading_Post.jpg")
TRIBUTE = CardShapedThing("Tribute", {"Action"}, Cost(coins=5), "The player to your left reveals then discards the top 2 cards of their deck. For each differently named card revealed, if it is an…Action Card, +2 ActionsTreasure Card, +$2Victory Card, +2 Cards", "https://wiki.dominionstrategy.com/index.php/Tribute", "./list_of_cards_files/200px-Tribute.jpg")
UPGRADE = CardShapedThing("Upgrade", {"Action"}, Cost(coins=5), "+1 Card+1 ActionTrash a card from your hand. Gain a card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Upgrade", "./list_of_cards_files/200px-Upgrade.jpg")
WISHING_WELL = CardShapedThing("Wishing Well", {"Action"}, Cost(coins=3), "+1 Card+1 ActionName a card, then reveal the top card of your deck. If you named it, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Wishing_Well", "./list_of_cards_files/200px-Wishing_Well.jpg")
AMBASSADOR = CardShapedThing("Ambassador", {"Action", "Attack"}, Cost(coins=3), "Reveal a card from your hand. Return up to 2 copies of it from your hand to the Supply. Then each other player gains a copy of it.", "https://wiki.dominionstrategy.com/index.php/Ambassador", "./list_of_cards_files/200px-Ambassador.jpg")
ASTROLABE = CardShapedThing("Astrolabe", {"Treasure", "Duration"}, Cost(coins=3), "Now and at the start of your next turn:$1+1 Buy", "https://wiki.dominionstrategy.com/index.php/Astrolabe", "./list_of_cards_files/200px-Astrolabe.jpg")
BAZAAR = CardShapedThing("Bazaar", {"Action"}, Cost(coins=5), "+1 Card+2 Actions+$1", "https://wiki.dominionstrategy.com/index.php/Bazaar", "./list_of_cards_files/200px-Bazaar.jpg")
BLOCKADE = CardShapedThing("Blockade", {"Action", "Duration", "Attack"}, Cost(coins=4), "Gain a card costing up to $4, setting it aside.At the start of your next turn, put it into your hand. While it's set aside, when another player gains a copy of it on their turn, they gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Blockade", "./list_of_cards_files/200px-Blockade.jpg")
CARAVAN = CardShapedThing("Caravan", {"Action", "Duration"}, Cost(coins=4), "+1 Card+1 ActionAt the start of your next turn, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Caravan", "./list_of_cards_files/200px-Caravan.jpg")
CORSAIR = CardShapedThing("Corsair", {"Action", "Duration", "Attack"}, Cost(coins=5), "+$2At the start of your next turn, +1 Card. Until then, each other player trashes the first Silver or Gold they play each turn.", "https://wiki.dominionstrategy.com/index.php/Corsair", "./list_of_cards_files/200px-Corsair.jpg")
CUTPURSE = CardShapedThing("Cutpurse", {"Action", "Attack"}, Cost(coins=4), "+$2Each other player discards a Copper (or reveals a hand with no Copper).", "https://wiki.dominionstrategy.com/index.php/Cutpurse", "./list_of_cards_files/200px-Cutpurse.jpg")
EMBARGO = CardShapedThing("Embargo", {"Action"}, Cost(coins=2), "+$2Trash this to add an Embargo token to a Supply pile. (For the rest of the game, when a player buys a card from that pile, they gain a Curse.)", "https://wiki.dominionstrategy.com/index.php/Embargo", "./list_of_cards_files/200px-Embargo.jpg")
EXPLORER = CardShapedThing("Explorer", {"Action"}, Cost(coins=5), "You may reveal a Province from your hand. If you do, gain a Gold to your hand. If you don't, gain a Silver to your hand.", "https://wiki.dominionstrategy.com/index.php/Explorer", "./list_of_cards_files/200px-Explorer.jpg")
FISHING_VILLAGE = CardShapedThing("Fishing Village", {"Action", "Duration"}, Cost(coins=3), "+2 Actions+$1At the start of your next turn: +1 Action and +$1.", "https://wiki.dominionstrategy.com/index.php/Fishing_Village", "./list_of_cards_files/200px-Fishing_Village.jpg")
GHOST_SHIP = CardShapedThing("Ghost Ship", {"Action", "Attack"}, Cost(coins=5), "+2 CardsEach other player with 4 or more cards in hand puts cards from their hand onto their deck until they have 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Ghost_Ship", "./list_of_cards_files/200px-Ghost_Ship.jpg")
HAVEN = CardShapedThing("Haven", {"Action", "Duration"}, Cost(coins=2), "+1 Card+1 ActionSet aside a card from your hand face down (under this). At the start of your next turn, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Haven", "./list_of_cards_files/200px-Haven.jpg")
ISLAND = CardShapedThing("Island", {"Action", "Victory"}, Cost(coins=4), "Put this and a card from your hand onto your Island mat.2VP", "https://wiki.dominionstrategy.com/index.php/Island", "./list_of_cards_files/200px-Island.jpg")
LIGHTHOUSE = CardShapedThing("Lighthouse", {"Action", "Duration"}, Cost(coins=2), "+1 Action+$1At the start of your next turn, +$1. Until then, when another player plays an Attack card, it doesn't affect you.", "https://wiki.dominionstrategy.com/index.php/Lighthouse", "./list_of_cards_files/200px-Lighthouse.jpg")
LOOKOUT = CardShapedThing("Lookout", {"Action"}, Cost(coins=3), "+1 ActionLook at the top 3 cards of your deck. Trash one of them. Discard one of them. Put the other one back on top of your deck.", "https://wiki.dominionstrategy.com/index.php/Lookout", "./list_of_cards_files/200px-Lookout.jpg")
MERCHANT_SHIP = CardShapedThing("Merchant Ship", {"Action", "Duration"}, Cost(coins=5), "Now and at the start of your next turn: +$2.", "https://wiki.dominionstrategy.com/index.php/Merchant_Ship", "./list_of_cards_files/200px-Merchant_Ship.jpg")
MONKEY = CardShapedThing("Monkey", {"Action", "Duration"}, Cost(coins=3), "Until your next turn, when the player to your right gains a card, +1 Card.At the start of your next turn, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Monkey", "./list_of_cards_files/200px-Monkey.jpg")
NATIVE_VILLAGE = CardShapedThing("Native Village", {"Action"}, Cost(coins=2), "+2 ActionsChoose one: Put the top card of your deck face down on your Native Village mat (you may look at those cards at any time); or put all the cards from your mat into your hand.", "https://wiki.dominionstrategy.com/index.php/Native_Village", "./list_of_cards_files/200px-Native_Village.jpg")
NAVIGATOR = CardShapedThing("Navigator", {"Action"}, Cost(coins=4), "+$2Look at the top 5 cards of your deck. Either discard them all, or put them back in any order.", "https://wiki.dominionstrategy.com/index.php/Navigator", "./list_of_cards_files/200px-Navigator.jpg")
OUTPOST = CardShapedThing("Outpost", {"Action", "Duration"}, Cost(coins=5), "You only draw 3 cards for your next hand. Take an extra turn after this one (but not a 3rd turn in a row).", "https://wiki.dominionstrategy.com/index.php/Outpost", "./list_of_cards_files/200px-Outpost.jpg")
PEARL_DIVER = CardShapedThing("Pearl Diver", {"Action"}, Cost(coins=2), "+1 Card+1 ActionLook at the bottom card of your deck. You may put it on top.", "https://wiki.dominionstrategy.com/index.php/Pearl_Diver", "./list_of_cards_files/200px-Pearl_Diver.jpg")
PIRATE = CardShapedThing("Pirate", {"Action", "Duration", "Reaction"}, Cost(coins=5), "At the start of your next turn, gain a Treasure costing up to $6 to your hand.When any player gains a Treasure, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Pirate", "./list_of_cards_files/200px-Pirate.jpg")
PIRATE_SHIP = CardShapedThing("Pirate Ship", {"Action", "Attack"}, Cost(coins=4), "Choose one: +$1 per Coin token on your Pirate Ship mat; or each other player reveals the top 2 cards of their deck, trashes one of those Treasures that you choose, and discards the rest, and then if anyone trashed a Treasure, you add a Coin token to your Pirate Ship mat.", "https://wiki.dominionstrategy.com/index.php/Pirate_Ship", "./list_of_cards_files/200px-Pirate_Ship.jpg")
SAILOR = CardShapedThing("Sailor", {"Action", "Duration"}, Cost(coins=4), "+1 ActionOnce this turn, when you gain a Duration card, you may play it.At the start of your next turn, +$2 and you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Sailor", "./list_of_cards_files/200px-Sailor.jpg")
SALVAGER = CardShapedThing("Salvager", {"Action"}, Cost(coins=4), "+1 BuyTrash a card from your hand. +$1 per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Salvager", "./list_of_cards_files/200px-Salvager.jpg")
SEA_CHART = CardShapedThing("Sea Chart", {"Action"}, Cost(coins=3), "+1 Card+1 ActionReveal the top card of your deck. If you have a copy of it in play, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Sea_Chart", "./list_of_cards_files/200px-Sea_Chart.jpg")
SEA_HAG = CardShapedThing("Sea Hag", {"Action", "Attack"}, Cost(coins=4), "Each other player discards the top card of their deck, then gains a Curse onto their deck.", "https://wiki.dominionstrategy.com/index.php/Sea_Hag", "./list_of_cards_files/200px-Sea_Hag.jpg")
SEA_WITCH = CardShapedThing("Sea Witch", {"Action", "Duration", "Attack"}, Cost(coins=5), "+2 CardsEach other player gains a Curse.At the start of your next turn, +2 Cards, then discard 2 cards.", "https://wiki.dominionstrategy.com/index.php/Sea_Witch", "./list_of_cards_files/200px-Sea_Witch.jpg")
SMUGGLERS = CardShapedThing("Smugglers", {"Action"}, Cost(coins=3), "Gain a copy of a card costing up to $6 that the player to your right gained on their last turn.", "https://wiki.dominionstrategy.com/index.php/Smugglers", "./list_of_cards_files/200px-Smugglers.jpg")
TACTICIAN = CardShapedThing("Tactician", {"Action", "Duration"}, Cost(coins=5), "If you have at least one card in hand: Discard your hand, and at the start of your next turn, +5 Cards, +1 Action, and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Tactician", "./list_of_cards_files/200px-Tactician.jpg")
TIDE_POOLS = CardShapedThing("Tide Pools", {"Action", "Duration"}, Cost(coins=4), "+3 Cards+1 ActionAt the start of your next turn, discard 2 cards.", "https://wiki.dominionstrategy.com/index.php/Tide_Pools", "./list_of_cards_files/200px-Tide_Pools.jpg")
TREASURE_MAP = CardShapedThing("Treasure Map", {"Action"}, Cost(coins=4), "Trash this and a Treasure Map from your hand. If you trashed two Treasure Maps, gain 4 Golds onto your deck.", "https://wiki.dominionstrategy.com/index.php/Treasure_Map", "./list_of_cards_files/200px-Treasure_Map.jpg")
TREASURY = CardShapedThing("Treasury", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1At the end of your Buy phase this turn, if you didn't gain a Victory card in it, you may put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Treasury", "./list_of_cards_files/200px-Treasury.jpg")
WAREHOUSE = CardShapedThing("Warehouse", {"Action"}, Cost(coins=3), "+3 Cards+1 ActionDiscard 3 cards.", "https://wiki.dominionstrategy.com/index.php/Warehouse", "./list_of_cards_files/200px-Warehouse.jpg")
WHARF = CardShapedThing("Wharf", {"Action", "Duration"}, Cost(coins=5), "Now and at the start of your next turn: +2 Cards and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Wharf", "./list_of_cards_files/200px-Wharf.jpg")
ALCHEMIST = CardShapedThing("Alchemist", {"Action"}, Cost(coins=3, potions=1), "+2 Cards+1 ActionAt the start of Clean-up this turn, if you have a Potion in play, you may put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Alchemist", "./list_of_cards_files/200px-Alchemist.jpg")
APOTHECARY = CardShapedThing("Apothecary", {"Action"}, Cost(coins=2, potions=1), "+1 Card+1 ActionReveal the top 4 cards of your deck. Put the Coppers and Potions into your hand. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Apothecary", "./list_of_cards_files/200px-Apothecary.jpg")
APPRENTICE = CardShapedThing("Apprentice", {"Action"}, Cost(coins=5), "+1 ActionTrash a card from your hand.+1 Card per $1 it costs.+2 Cards if it has P in its cost.", "https://wiki.dominionstrategy.com/index.php/Apprentice", "./list_of_cards_files/200px-Apprentice.jpg")
FAMILIAR = CardShapedThing("Familiar", {"Action", "Attack"}, Cost(coins=3, potions=1), "+1 Card+1 ActionEach other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Familiar", "./list_of_cards_files/200px-Familiar.jpg")
GOLEM = CardShapedThing("Golem", {"Action"}, Cost(coins=4, potions=1), "Reveal cards from your deck until you reveal 2 Action cards other than Golems. Discard the other cards, then play the Action cards in either order.", "https://wiki.dominionstrategy.com/index.php/Golem", "./list_of_cards_files/200px-Golem.jpg")
HERBALIST = CardShapedThing("Herbalist", {"Action"}, Cost(coins=2), "+1 Buy+$1Once this turn, when you discard a Treasure from play, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Herbalist", "./list_of_cards_files/200px-Herbalist.jpg")
PHILOSOPHERS_STONE = CardShapedThing("Philosopher's Stone", {"Treasure"}, Cost(coins=3, potions=1), "Count your deck and discard pile. +$1 per 5 cards total between them (round down).", "https://wiki.dominionstrategy.com/index.php/Philosopher%27s_Stone", "./list_of_cards_files/200px-Philosopher's_Stone.jpg")
POSSESSION = CardShapedThing("Possession", {"Action"}, Cost(coins=6, potions=1), "The player to your left takes an extra turn after this one (but not a 2nd extra turn in a row), in which you can see all cards they can and make all decisions for them. Any cards or D they would gain on that turn, you gain instead; any cards of theirs that are trashed are set aside and put in their discard pile at end of turn.", "https://wiki.dominionstrategy.com/index.php/Possession", "./list_of_cards_files/200px-Possession.jpg")
SCRYING_POOL = CardShapedThing("Scrying Pool", {"Action", "Attack"}, Cost(coins=2, potions=1), "+1 ActionEach player (including you) reveals the top card of their deck and either discards it or puts it back, your choice. Then reveal cards from your deck until revealing one that isn't an Action. Put all of those revealed cards into your hand.", "https://wiki.dominionstrategy.com/index.php/Scrying_Pool", "./list_of_cards_files/200px-Scrying_Pool.jpg")
TRANSMUTE = CardShapedThing("Transmute", {"Action"}, Cost(potions=1), "Trash a card from your hand. If it is an…Action card, gain a DuchyTreasure card, gain a TransmuteVictory card, gain a Gold", "https://wiki.dominionstrategy.com/index.php/Transmute", "./list_of_cards_files/200px-Transmute.jpg")
UNIVERSITY = CardShapedThing("University", {"Action"}, Cost(coins=2, potions=1), "+2 ActionsYou may gain an Action card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/University", "./list_of_cards_files/200px-University.jpg")
VINEYARD = CardShapedThing("Vineyard", {"Victory"}, Cost(potions=1), "Worth 1VP per 3 Action cards you have (rounded down).", "https://wiki.dominionstrategy.com/index.php/Vineyard", "./list_of_cards_files/200px-Vineyard.jpg")
POTION = CardShapedThing("Potion", {"Treasure"}, Cost(coins=4), "P", "https://wiki.dominionstrategy.com/index.php/Potion", "./list_of_cards_files/200px-Potion.jpg")
ANVIL = CardShapedThing("Anvil", {"Treasure"}, Cost(coins=3), "$1You may discard a Treasure to gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Anvil", "./list_of_cards_files/200px-Anvil.jpg")
BANK = CardShapedThing("Bank", {"Treasure"}, Cost(coins=7), "+$1 per Treasure card you have in play (counting this).", "https://wiki.dominionstrategy.com/index.php/Bank", "./list_of_cards_files/200px-Bank.jpg")
BISHOP = CardShapedThing("Bishop", {"Action"}, Cost(coins=4), "+$1+1VPTrash a card from your hand. +1VP per $2 it costs (round down). Each other player may trash a card from their hand.", "https://wiki.dominionstrategy.com/index.php/Bishop", "./list_of_cards_files/200px-Bishop.jpg")
CHARLATAN = CardShapedThing("Charlatan", {"Action", "Attack"}, Cost(coins=5), "+$3Each other player gains a Curse.In games using this, Curse is also a Treasure worth $1.", "https://wiki.dominionstrategy.com/index.php/Charlatan", "./list_of_cards_files/200px-Charlatan.jpg")
CITY = CardShapedThing("City", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsIf there are one or more empty Supply piles, +1 Card. If there are two or more, +1 Buy and +$1.", "https://wiki.dominionstrategy.com/index.php/City", "./list_of_cards_files/200px-City.jpg")
CLERK = CardShapedThing("Clerk", {"Action", "Reaction", "Attack"}, Cost(coins=4), "+$2Each other player with 5 or more cards in hand puts one onto their deck.At the start of your turn, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Clerk", "./list_of_cards_files/200px-Clerk.jpg")
COLLECTION = CardShapedThing("Collection", {"Treasure"}, Cost(coins=5), "$2+1 BuyThis turn, when you gain an Action card, +1VP.", "https://wiki.dominionstrategy.com/index.php/Collection", "./list_of_cards_files/200px-Collection.jpg")
CONTRABAND = CardShapedThing("Contraband", {"Treasure"}, Cost(coins=5), "$3+1 BuyThe player to your left names a card. You can't buy that card this turn.", "https://wiki.dominionstrategy.com/index.php/Contraband", "./list_of_cards_files/200px-Contraband.jpg")
COUNTING_HOUSE = CardShapedThing("Counting House", {"Action"}, Cost(coins=5), "Look through your discard pile, reveal any number of Coppers from it, and put them into your hand.", "https://wiki.dominionstrategy.com/index.php/Counting_House", "./list_of_cards_files/200px-Counting_House.jpg")
CRYSTAL_BALL = CardShapedThing("Crystal Ball", {"Treasure"}, Cost(coins=5), "$1Look at the top card of your deck. You may trash it, discard it, or, if it's an Action or Treasure, play it.", "https://wiki.dominionstrategy.com/index.php/Crystal_Ball", "./list_of_cards_files/200px-Crystal_Ball.jpg")
EXPAND = CardShapedThing("Expand", {"Action"}, Cost(coins=7), "Trash a card from your hand. Gain a card costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Expand", "./list_of_cards_files/200px-Expand.jpg")
FORGE = CardShapedThing("Forge", {"Action"}, Cost(coins=7), "Trash any number of cards from your hand. Gain a card with cost exactly equal to the total cost in $ of the trashed cards.", "https://wiki.dominionstrategy.com/index.php/Forge", "./list_of_cards_files/200px-Forge.jpg")
GOONS = CardShapedThing("Goons", {"Action", "Attack"}, Cost(coins=6), "+1 Buy+$2Each other player discards down to 3 cards in hand.While you have this in play, when you buy a card, +1VP.", "https://wiki.dominionstrategy.com/index.php/Goons", "./list_of_cards_files/200px-Goons.jpg")
GRAND_MARKET = CardShapedThing("Grand Market", {"Action"}, Cost(coins=6), "+1 Card+1 Action+1 Buy+$2You can't buy this if you have any Coppers in play.", "https://wiki.dominionstrategy.com/index.php/Grand_Market", "./list_of_cards_files/200px-Grand_Market.jpg")
HOARD = CardShapedThing("Hoard", {"Treasure"}, Cost(coins=6), "$2This turn, when you gain a Victory card, if you bought it, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Hoard", "./list_of_cards_files/200px-Hoard.jpg")
INVESTMENT = CardShapedThing("Investment", {"Treasure"}, Cost(coins=4), "Trash a card from your hand. Choose one: +$1; or trash this to reveal your hand for +1VP per differently named Treasure there.", "https://wiki.dominionstrategy.com/index.php/Investment", "./list_of_cards_files/200px-Investment.jpg")
KINGS_COURT = CardShapedThing("King's Court", {"Action"}, Cost(coins=7), "You may play an Action card from your hand three times.", "https://wiki.dominionstrategy.com/index.php/King%27s_Court", "./list_of_cards_files/200px-King's_Court.jpg")
LOAN = CardShapedThing("Loan", {"Treasure"}, Cost(coins=3), "$1Reveal cards from your deck until you reveal a Treasure. Discard it or trash it. Discard the other cards.", "https://wiki.dominionstrategy.com/index.php/Loan", "./list_of_cards_files/200px-Loan.jpg")
MAGNATE = CardShapedThing("Magnate", {"Action"}, Cost(coins=5), "Reveal your hand. +1 Card per Treasure in it.", "https://wiki.dominionstrategy.com/index.php/Magnate", "./list_of_cards_files/200px-Magnate.jpg")
MINT = CardShapedThing("Mint", {"Action"}, Cost(coins=5), "You may reveal a Treasure card from your hand. Gain a copy of it.When you gain this, trash all non-Duration Treasures you have in play.", "https://wiki.dominionstrategy.com/index.php/Mint", "./list_of_cards_files/200px-Mint.jpg")
MONUMENT = CardShapedThing("Monument", {"Action"}, Cost(coins=4), "+$2+1VP", "https://wiki.dominionstrategy.com/index.php/Monument", "./list_of_cards_files/200px-Monument.jpg")
MOUNTEBANK = CardShapedThing("Mountebank", {"Action", "Attack"}, Cost(coins=5), "+$2Each other player may discard a Curse. If they don't, they gain a Curse and a Copper.", "https://wiki.dominionstrategy.com/index.php/Mountebank", "./list_of_cards_files/200px-Mountebank.jpg")
PEDDLER = CardShapedThing("Peddler", {"Action"}, Cost(coins=8), "+1 Card+1 Action+$1During a player's Buy phase, this costs $2 less per Action card they have in play.", "https://wiki.dominionstrategy.com/index.php/Peddler", "./list_of_cards_files/200px-Peddler.jpg")
QUARRY = CardShapedThing("Quarry", {"Treasure"}, Cost(coins=4), "$1This turn, Actions cost $2 less.", "https://wiki.dominionstrategy.com/index.php/Quarry", "./list_of_cards_files/200px-Quarry.jpg")
RABBLE = CardShapedThing("Rabble", {"Action", "Attack"}, Cost(coins=5), "+3 CardsEach other player reveals the top 3 cards of their deck, discards the Actions and Treasures, and puts the rest back in any order they choose.", "https://wiki.dominionstrategy.com/index.php/Rabble", "./list_of_cards_files/200px-Rabble.jpg")
ROYAL_SEAL = CardShapedThing("Royal Seal", {"Treasure"}, Cost(coins=5), "$2While you have this in play, when you gain a card, you may put that card onto your deck.", "https://wiki.dominionstrategy.com/index.php/Royal_Seal", "./list_of_cards_files/200px-Royal_Seal.jpg")
TALISMAN = CardShapedThing("Talisman", {"Treasure"}, Cost(coins=4), "$1While you have this in play, when you buy a non-Victory card costing $4 or less, gain a copy of it.", "https://wiki.dominionstrategy.com/index.php/Talisman", "./list_of_cards_files/200px-Talisman.jpg")
TIARA = CardShapedThing("Tiara", {"Treasure"}, Cost(coins=4), "+1 BuyThis turn, when you gain a card, you may put it onto your deck.You may play a Treasure from your hand twice.", "https://wiki.dominionstrategy.com/index.php/Tiara", "./list_of_cards_files/200px-Tiara.jpg")
TRADE_ROUTE = CardShapedThing("Trade Route", {"Action"}, Cost(coins=3), "+1 BuyTrash a card from your hand. +$1 per Coin token on the Trade Route mat.Setup: Add a Coin token to each Victory Supply pile; move that token to the Trade Route mat when a card is gained from the pile.", "https://wiki.dominionstrategy.com/index.php/Trade_Route", "./list_of_cards_files/200px-Trade_Route.jpg")
VAULT = CardShapedThing("Vault", {"Action"}, Cost(coins=5), "+2 CardsDiscard any number of cards for +$1 each.Each other player may discard 2 cards, to draw a card.", "https://wiki.dominionstrategy.com/index.php/Vault", "./list_of_cards_files/200px-Vault.jpg")
VENTURE = CardShapedThing("Venture", {"Treasure"}, Cost(coins=5), "$1Reveal cards from your deck until you reveal a Treasure. Discard the other cards. Play that Treasure.", "https://wiki.dominionstrategy.com/index.php/Venture", "./list_of_cards_files/200px-Venture.jpg")
WAR_CHEST = CardShapedThing("War Chest", {"Treasure"}, Cost(coins=5), "The player to your left names a card. Gain a card costing up to $5 that hasn't been named for War Chests this turn.", "https://wiki.dominionstrategy.com/index.php/War_Chest", "./list_of_cards_files/200px-War_Chest.jpg")
WATCHTOWER = CardShapedThing("Watchtower", {"Action", "Reaction"}, Cost(coins=3), "Draw until you have 6 cards in hand.When you gain a card, you may reveal this from your hand, to either trash that card or put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Watchtower", "./list_of_cards_files/200px-Watchtower.jpg")
WORKERS_VILLAGE = CardShapedThing("Worker's Village", {"Action"}, Cost(coins=4), "+1 Card+2 Actions+1 Buy", "https://wiki.dominionstrategy.com/index.php/Worker%27s_Village", "./list_of_cards_files/200px-Worker's_Village.jpg")
PLATINUM = CardShapedThing("Platinum", {"Treasure"}, Cost(coins=9), "$5", "https://wiki.dominionstrategy.com/index.php/Platinum", "./list_of_cards_files/200px-Platinum.jpg")
COLONY = CardShapedThing("Colony", {"Victory"}, Cost(coins=11), "10VP", "https://wiki.dominionstrategy.com/index.php/Colony", "./list_of_cards_files/200px-Colony.jpg")
ADVISOR = CardShapedThing("Advisor", {"Action"}, Cost(coins=4), "+1 ActionReveal the top 3 cards of your deck. The player to your left chooses one of them. Discard that card and put the rest into your hand.", "https://wiki.dominionstrategy.com/index.php/Advisor", "./list_of_cards_files/200px-Advisor.jpg")
BAKER = CardShapedThing("Baker", {"Action"}, Cost(coins=5), "+1 Card+1 Action+1 CoffersSetup: Each player gets +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Baker", "./list_of_cards_files/200px-Baker.jpg")
BUTCHER = CardShapedThing("Butcher", {"Action"}, Cost(coins=5), "+2 CoffersYou may trash a card from your hand, to gain a card, costing up to $1 more than it per Coffers you spend.", "https://wiki.dominionstrategy.com/index.php/Butcher", "./list_of_cards_files/200px-Butcher.jpg")
CANDLESTICK_MAKER = CardShapedThing("Candlestick Maker", {"Action"}, Cost(coins=2), "+1 Action+1 Buy+1 Coffers", "https://wiki.dominionstrategy.com/index.php/Candlestick_Maker", "./list_of_cards_files/200px-Candlestick_Maker.jpg")
CARNIVAL = CardShapedThing("Carnival", {"Action"}, Cost(coins=5), "Reveal the top 4 cards of your deck. Put one of each differently named card into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Carnival", "./list_of_cards_files/200px-Carnival.jpg")
DOCTOR = CardShapedThing("Doctor", {"Action"}, Cost(coins=3), "Name a card. Reveal the top 3 cards of your deck. Trash the matches. Put the rest back in any order.Overpay: Per $1 overpaid, look at the top card of your deck; trash it, discard it, or put it back.", "https://wiki.dominionstrategy.com/index.php/Doctor", "./list_of_cards_files/200px-DoctorDigital.jpg")
FAIRGROUNDS = CardShapedThing("Fairgrounds", {"Victory"}, Cost(coins=6), "Worth 2VP per 5 differently named cards you have (round down).", "https://wiki.dominionstrategy.com/index.php/Fairgrounds", "./list_of_cards_files/200px-Fairgrounds.jpg")
FARMHANDS = CardShapedThing("Farmhands", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsWhen you gain this, you may set aside an Action or Treasure from your hand, and play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Farmhands", "./list_of_cards_files/200px-Farmhands.jpg")
FARMING_VILLAGE = CardShapedThing("Farming Village", {"Action"}, Cost(coins=4), "+2 ActionsReveal cards from your deck until you reveal a Treasure or Action card. Put that card into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Farming_Village", "./list_of_cards_files/200px-Farming_Village.jpg")
FARRIER = CardShapedThing("Farrier", {"Action"}, Cost(coins=2), "+1 Card+1 Action+1 BuyOverpay: +1 Card at the end of this turn per $1 overpaid.", "https://wiki.dominionstrategy.com/index.php/Farrier", "./list_of_cards_files/200px-Farrier.jpg")
FERRYMAN = CardShapedThing("Ferryman", {"Action"}, Cost(coins=5), "+2 Cards+1 ActionDiscard a card.Setup: Choose an unused Kingdom card pile costing $3 or $4. Gain one when you gain a Ferryman.", "https://wiki.dominionstrategy.com/index.php/Ferryman", "./list_of_cards_files/200px-Ferryman.jpg")
FOOTPAD = CardShapedThing("Footpad", {"Action", "Attack"}, Cost(coins=5), "+2 CoffersEach other player discards down to 3 cards in hand.In games using this, when you gain a card in an Action phase, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Footpad", "./list_of_cards_files/200px-Footpad.jpg")
FORTUNE_TELLER = CardShapedThing("Fortune Teller", {"Action", "Attack"}, Cost(coins=3), "+$2Each other player reveals cards from the top of their deck until they reveal a Victory card or a Curse. They put it on top and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Fortune_Teller", "./list_of_cards_files/200px-Fortune_Teller.jpg")
HAMLET = CardShapedThing("Hamlet", {"Action"}, Cost(coins=2), "+1 Card+1 ActionYou may discard a card for +1 Action.You may discard a card for +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Hamlet", "./list_of_cards_files/200px-Hamlet.jpg")
HARVEST = CardShapedThing("Harvest", {"Action"}, Cost(coins=5), "Reveal the top 4 cards of your deck, then discard them. +$1 per differently named card revealed.", "https://wiki.dominionstrategy.com/index.php/Harvest", "./list_of_cards_files/200px-Harvest.jpg")
HERALD = CardShapedThing("Herald", {"Action"}, Cost(coins=4), "+1 Card+1 ActionReveal the top card of your deck. If it's an Action, play it.Overpay: Per $1 overpaid, put any card from your discard pile onto your deck.", "https://wiki.dominionstrategy.com/index.php/Herald", "./list_of_cards_files/200px-Herald.jpg")
HORN_OF_PLENTY = CardShapedThing("Horn of Plenty", {"Treasure"}, Cost(coins=5), "Gain a card costing up to $1 per differently named card you have in play (counting this). If it's a Victory card, trash this.", "https://wiki.dominionstrategy.com/index.php/Horn_of_Plenty", "./list_of_cards_files/200px-Horn_of_Plenty.jpg")
HORSE_TRADERS = CardShapedThing("Horse Traders", {"Action", "Reaction"}, Cost(coins=4), "+1 Buy+$3Discard 2 cards.When another player plays an Attack card, you may first set this aside from your hand. If you do, then at the start of your next turn, +1 Card and return this to your hand.", "https://wiki.dominionstrategy.com/index.php/Horse_Traders", "./list_of_cards_files/200px-Horse_Traders.jpg")
HUNTING_PARTY = CardShapedThing("Hunting Party", {"Action"}, Cost(coins=5), "+1 Card+1 ActionReveal your hand. Reveal cards from your deck until you reveal a card that isn't a copy of one in your hand. Put it into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Hunting_Party", "./list_of_cards_files/200px-Hunting_Party.jpg")
INFIRMARY = CardShapedThing("Infirmary", {"Action"}, Cost(coins=3), "+1 CardYou may trash a card from your hand.Overpay: Play this once per $1 overpaid.", "https://wiki.dominionstrategy.com/index.php/Infirmary", "./list_of_cards_files/200px-Infirmary.jpg")
JESTER = CardShapedThing("Jester", {"Action", "Attack"}, Cost(coins=5), "+$2Each other player discards the top card of their deck. If it's a Victory card they gain a Curse; otherwise they gain a copy of the discarded card or you do, your choice.", "https://wiki.dominionstrategy.com/index.php/Jester", "./list_of_cards_files/200px-Jester.jpg")
JOURNEYMAN = CardShapedThing("Journeyman", {"Action"}, Cost(coins=5), "Name a card. Reveal cards from your deck until you reveal 3 cards without that name. Put those cards into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Journeyman", "./list_of_cards_files/200px-Journeyman.jpg")
JOUST = CardShapedThing("Joust", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1You may set aside a Province from your hand to gain any Reward to your hand. Discard the Province in Clean-up.", "https://wiki.dominionstrategy.com/index.php/Joust", "./list_of_cards_files/200px-Joust.jpg")
MASTERPIECE = CardShapedThing("Masterpiece", {"Treasure"}, Cost(coins=3), "$1Overpay: Gain a Silver per $1 overpaid.", "https://wiki.dominionstrategy.com/index.php/Masterpiece", "./list_of_cards_files/200px-MasterpieceDigital.jpg")
MENAGERIE = CardShapedThing("Menagerie", {"Action"}, Cost(coins=3), "+1 ActionReveal your hand. If the revealed cards all have different names, +3 Cards. Otherwise, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Menagerie", "./list_of_cards_files/200px-Menagerie.jpg")
MERCHANT_GUILD = CardShapedThing("Merchant Guild", {"Action"}, Cost(coins=5), "+1 Buy+$1At the end of your Buy phase this turn, +1 Coffers per card you gained in it.", "https://wiki.dominionstrategy.com/index.php/Merchant_Guild", "./list_of_cards_files/200px-Merchant_Guild.jpg")
PLAZA = CardShapedThing("Plaza", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsYou may discard a Treasure for +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Plaza", "./list_of_cards_files/200px-Plaza.jpg")
REMAKE = CardShapedThing("Remake", {"Action"}, Cost(coins=4), "Do this twice: Trash a card from your hand, then gain a card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Remake", "./list_of_cards_files/200px-Remake.jpg")
SHOP = CardShapedThing("Shop", {"Action"}, Cost(coins=3), "+1 Card+$1You may play an Action card from your hand that you don't have a copy of in play.", "https://wiki.dominionstrategy.com/index.php/Shop", "./list_of_cards_files/200px-Shop.jpg")
SOOTHSAYER = CardShapedThing("Soothsayer", {"Action", "Attack"}, Cost(coins=5), "Gain a Gold. Each other player gains a Curse, and if they did, draws a card.", "https://wiki.dominionstrategy.com/index.php/Soothsayer", "./list_of_cards_files/200px-Soothsayer.jpg")
STONEMASON = CardShapedThing("Stonemason", {"Action"}, Cost(coins=2), "Trash a card from your hand. Gain 2 cards each costing less than it.Overpay: Gain 2 Action cards each costing the amount overpaid.", "https://wiki.dominionstrategy.com/index.php/Stonemason", "./list_of_cards_files/200px-Stonemason.jpg")
TAXMAN = CardShapedThing("Taxman", {"Action", "Attack"}, Cost(coins=4), "You may trash a Treasure from your hand. Each other player with 5 or more cards in hand discards a copy of it (or reveals they can't). Gain a Treasure onto your deck costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Taxman", "./list_of_cards_files/200px-Taxman.jpg")
TOURNAMENT = CardShapedThing("Tournament", {"Action"}, Cost(coins=4), "+1 ActionEach player may reveal a Province from their hand. If you do, discard it and gain any Prize (from the Prize pile) or a Duchy, onto your deck. If no-one else does, +1 Card and +$1.", "https://wiki.dominionstrategy.com/index.php/Tournament", "./list_of_cards_files/200px-Tournament.jpg")
YOUNG_WITCH = CardShapedThing("Young Witch", {"Action", "Attack"}, Cost(coins=4), "+2 CardsDiscard 2 cards. Each other player gains a Curse unless they reveal a Bane from their hand.Setup: Add an extra Kingdom card pile costing $2 or $3 to the Supply. Its cards are Banes.", "https://wiki.dominionstrategy.com/index.php/Young_Witch", "./list_of_cards_files/200px-Young_Witch.jpg")
BAG_OF_GOLD = CardShapedThing("Bag of Gold", {"Action", "Prize"}, Cost(coins=0), "+1 ActionGain a Gold onto your deck.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Bag_of_Gold", "./list_of_cards_files/200px-Bag_of_Gold.jpg")
CORONET = CardShapedThing("Coronet", {"Action", "Treasure", "Reward"}, Cost(coins=0), "You may play a non-Reward Action from your hand twice.You may play a non-Reward Treasure from your hand twice.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Coronet", "./list_of_cards_files/200px-Coronet.jpg")
COURSER = CardShapedThing("Courser", {"Action", "Reward"}, Cost(coins=0), "Choose two different options: +2 Cards; +2 Actions; +$2; gain 4 Silvers.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Courser", "./list_of_cards_files/200px-Courser.jpg")
DEMESNE = CardShapedThing("Demesne", {"Action", "Victory", "Reward"}, Cost(coins=0), "+2 Actions+2 BuysGain a Gold.Worth 1VP per Gold you have.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Demesne", "./list_of_cards_files/200px-Demesne.jpg")
DIADEM = CardShapedThing("Diadem", {"Treasure", "Prize"}, Cost(coins=0), "$2+$1 per unused Action you have (Action, not Action card).(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Diadem", "./list_of_cards_files/200px-Diadem.jpg")
FOLLOWERS = CardShapedThing("Followers", {"Action", "Attack", "Prize"}, Cost(coins=0), "+2 CardsGain an Estate. Each other player gains a Curse and discards down to 3 cards in hand.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Followers", "./list_of_cards_files/200px-Followers.jpg")
HOUSECARL = CardShapedThing("Housecarl", {"Action", "Reward"}, Cost(coins=0), "+1 Card per differently named Action card you have in play.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Housecarl", "./list_of_cards_files/200px-Housecarl.jpg")
HUGE_TURNIP = CardShapedThing("Huge Turnip", {"Treasure", "Reward"}, Cost(coins=0), "+2 Coffers+$1 per Coffers you have.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Huge_Turnip", "./list_of_cards_files/200px-Huge_Turnip.jpg")
PRINCESS = CardShapedThing("Princess", {"Action", "Prize"}, Cost(coins=0), "+1 BuyThis turn, cards cost $2 less.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Princess", "./list_of_cards_files/200px-Princess.jpg")
RENOWN = CardShapedThing("Renown", {"Action", "Reward"}, Cost(coins=0), "+1 BuyThis turn, cards cost $2 less.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Renown", "./list_of_cards_files/200px-Renown.jpg")
TRUSTY_STEED = CardShapedThing("Trusty Steed", {"Action", "Prize"}, Cost(coins=0), "Choose two: +2 Cards; or +2 Actions; or +$2; or gain 4 Silvers and put your deck into your discard pile. The choices must be different.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Trusty_Steed", "./list_of_cards_files/200px-Trusty_Steed.jpg")
BERSERKER = CardShapedThing("Berserker", {"Action", "Attack"}, Cost(coins=5), "Gain a card costing less than this. Each other player discards down to 3 cards in hand.When you gain this, if you have an Action in play, play this.", "https://wiki.dominionstrategy.com/index.php/Berserker", "./list_of_cards_files/200px-Berserker.jpg")
BORDER_VILLAGE = CardShapedThing("Border Village", {"Action"}, Cost(coins=6), "+1 Card+2 ActionsWhen you gain this, gain a cheaper card.", "https://wiki.dominionstrategy.com/index.php/Border_Village", "./list_of_cards_files/200px-Border_Village.jpg")
CACHE = CardShapedThing("Cache", {"Treasure"}, Cost(coins=5), "$3When you gain this, gain 2 Coppers.", "https://wiki.dominionstrategy.com/index.php/Cache", "./list_of_cards_files/200px-CacheOld2.jpg")
CARTOGRAPHER = CardShapedThing("Cartographer", {"Action"}, Cost(coins=5), "+1 Card+1 ActionLook at the top 4 cards of your deck. Discard any number of them, then put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Cartographer", "./list_of_cards_files/200px-Cartographer.jpg")
CAULDRON = CardShapedThing("Cauldron", {"Treasure", "Attack"}, Cost(coins=5), "$2+1 BuyThe third time you gain an Action this turn, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Cauldron", "./list_of_cards_files/200px-Cauldron.jpg")
CROSSROADS = CardShapedThing("Crossroads", {"Action"}, Cost(coins=2), "Reveal your hand. +1 Card per Victory card revealed. If this is the first time you played a Crossroads this turn, +3 Actions.", "https://wiki.dominionstrategy.com/index.php/Crossroads", "./list_of_cards_files/200px-Crossroads.jpg")
DEVELOP = CardShapedThing("Develop", {"Action"}, Cost(coins=3), "Trash a card from your hand. Gain two cards onto your deck, with one costing exactly $1 more than it, and one costing exactly $1 less than it, in either order.", "https://wiki.dominionstrategy.com/index.php/Develop", "./list_of_cards_files/200px-Develop.jpg")
DUCHESS = CardShapedThing("Duchess", {"Action"}, Cost(coins=2), "+$2Each player (including you) looks at the top card of their deck and may discard it.In games using this, when you gain a Duchy, you may gain a Duchess.", "https://wiki.dominionstrategy.com/index.php/Duchess", "./list_of_cards_files/200px-Duchess.jpg")
EMBASSY = CardShapedThing("Embassy", {"Action"}, Cost(coins=5), "+5 CardsDiscard 3 cards.When you gain this, each other player gains a Silver.", "https://wiki.dominionstrategy.com/index.php/Embassy", "./list_of_cards_files/200px-EmbassyOld2.jpg")
FARMLAND = CardShapedThing("Farmland", {"Victory"}, Cost(coins=6), "2VPWhen you gain this, trash a card from your hand and gain a non-Farmland card costing exactly $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Farmland", "./list_of_cards_files/200px-Farmland.jpg")
FOOLS_GOLD = CardShapedThing("Fool's Gold", {"Treasure", "Reaction"}, Cost(coins=2), "If this is the first time you played a Fool's Gold this turn, +$1, otherwise +$4.When another player gains a Province, you may trash this from your hand, to gain a Gold onto your deck.", "https://wiki.dominionstrategy.com/index.php/Fool%27s_Gold", "./list_of_cards_files/200px-Fool's_Gold.jpg")
GUARD_DOG = CardShapedThing("Guard Dog", {"Action", "Reaction"}, Cost(coins=3), "+2 CardsIf you have 5 or fewer cards in hand, +2 Cards.When another player plays an Attack, you may first play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Guard_Dog", "./list_of_cards_files/200px-Guard_Dog.jpg")
HAGGLER = CardShapedThing("Haggler", {"Action"}, Cost(coins=5), "+$2This turn, when you gain a card, if you bought it, gain a cheaper non-Victory card.", "https://wiki.dominionstrategy.com/index.php/Haggler", "./list_of_cards_files/200px-Haggler.jpg")
HIGHWAY = CardShapedThing("Highway", {"Action"}, Cost(coins=5), "+1 Card+1 ActionThis turn, cards cost $1 less.", "https://wiki.dominionstrategy.com/index.php/Highway", "./list_of_cards_files/200px-Highway.jpg")
ILL_GOTTEN_GAINS = CardShapedThing("Ill-Gotten Gains", {"Treasure"}, Cost(coins=5), "$1You may gain a Copper to your hand.When you gain this, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Ill-Gotten_Gains", "./list_of_cards_files/200px-Ill-Gotten_Gains.jpg")
INN = CardShapedThing("Inn", {"Action"}, Cost(coins=5), "+2 Cards+2 ActionsDiscard 2 cards.When you gain this, reveal any number of Action cards from your discard pile and shuffle them into your deck.", "https://wiki.dominionstrategy.com/index.php/Inn", "./list_of_cards_files/200px-Inn.jpg")
JACK_OF_ALL_TRADES = CardShapedThing("Jack of All Trades", {"Action"}, Cost(coins=4), "Gain a Silver. Look at the top card of your deck; you may discard it. Draw until you have 5 cards in hand. You may trash a non-Treasure card from your hand.", "https://wiki.dominionstrategy.com/index.php/Jack_of_All_Trades", "./list_of_cards_files/200px-Jack_of_All_Trades.jpg")
MANDARIN = CardShapedThing("Mandarin", {"Action"}, Cost(coins=5), "+$3Put a card from your hand onto your deck.When you gain this, put all Treasures you have in play onto your deck in any order.", "https://wiki.dominionstrategy.com/index.php/Mandarin", "./list_of_cards_files/200px-MandarinOld2.jpg")
MARGRAVE = CardShapedThing("Margrave", {"Action", "Attack"}, Cost(coins=5), "+3 Cards+1 BuyEach other player draws a card, then discards down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Margrave", "./list_of_cards_files/200px-Margrave.jpg")
NOBLE_BRIGAND = CardShapedThing("Noble Brigand", {"Action", "Attack"}, Cost(coins=4), "+$1Each other player reveals the top 2 cards of their deck, trashes a revealed Silver or Gold you choose, discards the rest, and gains a Copper if they didn't reveal a Treasure. You gain the trashed cards.When you buy this, do its attack.", "https://wiki.dominionstrategy.com/index.php/Noble_Brigand", "./list_of_cards_files/200px-Noble_Brigand.jpg")
NOMAD_CAMP = CardShapedThing("Nomad Camp", {"Action"}, Cost(coins=4), "+1 Buy+$2This is gained onto your deck (instead of to your discard pile).", "https://wiki.dominionstrategy.com/index.php/Nomad_Camp", "./list_of_cards_files/200px-Nomad_CampOld2.jpg")
NOMADS = CardShapedThing("Nomads", {"Action"}, Cost(coins=4), "+1 Buy+$2When you gain or trash this, +$2.", "https://wiki.dominionstrategy.com/index.php/Nomads", "./list_of_cards_files/200px-Nomads.jpg")
OASIS = CardShapedThing("Oasis", {"Action"}, Cost(coins=3), "+1 Card+1 Action+$1Discard a card.", "https://wiki.dominionstrategy.com/index.php/Oasis", "./list_of_cards_files/200px-Oasis.jpg")
ORACLE = CardShapedThing("Oracle", {"Action", "Attack"}, Cost(coins=3), "Each player (including you) reveals the top 2 cards of their deck, and discards them or puts them back, your choice (they choose the order). Then, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Oracle", "./list_of_cards_files/200px-Oracle.jpg")
SCHEME = CardShapedThing("Scheme", {"Action"}, Cost(coins=3), "+1 Card+1 ActionThis turn, you may put one of your Action cards onto your deck when you discard it from play.", "https://wiki.dominionstrategy.com/index.php/Scheme", "./list_of_cards_files/200px-Scheme.jpg")
SILK_ROAD = CardShapedThing("Silk Road", {"Victory"}, Cost(coins=4), "Worth 1VP for every 4 Victory cards you have (round down).", "https://wiki.dominionstrategy.com/index.php/Silk_Road", "./list_of_cards_files/200px-Silk_Road.jpg")
SOUK = CardShapedThing("Souk", {"Action"}, Cost(coins=5), "+1 Buy+$7-$1 per card in your hand (you can't go below $0).When you gain this, trash up to 2 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Souk", "./list_of_cards_files/200px-Souk.jpg")
SPICE_MERCHANT = CardShapedThing("Spice Merchant", {"Action"}, Cost(coins=4), "You may trash a Treasure from your hand to choose one: +2 Cards and +1 Action; or +1 Buy and +$2.", "https://wiki.dominionstrategy.com/index.php/Spice_Merchant", "./list_of_cards_files/200px-Spice_Merchant.jpg")
STABLES = CardShapedThing("Stables", {"Action"}, Cost(coins=5), "You may discard a Treasure, for +3 Cards and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Stables", "./list_of_cards_files/200px-Stables.jpg")
TRADER = CardShapedThing("Trader", {"Action", "Reaction"}, Cost(coins=4), "Trash a card from your hand. Gain a Silver per $1 it costs.When you gain a card, you may reveal this from your hand, to exchange the card for a Silver.", "https://wiki.dominionstrategy.com/index.php/Trader", "./list_of_cards_files/200px-Trader.jpg")
TRAIL = CardShapedThing("Trail", {"Action", "Reaction"}, Cost(coins=4), "+1 Card+1 ActionWhen you gain, trash, or discard this, other than in Clean-up, you may play it.", "https://wiki.dominionstrategy.com/index.php/Trail", "./list_of_cards_files/200px-Trail.jpg")
TUNNEL = CardShapedThing("Tunnel", {"Victory", "Reaction"}, Cost(coins=3), "2VPWhen you discard this other than during Clean-up, you may reveal it to gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Tunnel", "./list_of_cards_files/200px-Tunnel.jpg")
WEAVER = CardShapedThing("Weaver", {"Action", "Reaction"}, Cost(coins=4), "Gain two Silvers or a card costing up to $4.When you discard this other than in Clean-up, you may play it.", "https://wiki.dominionstrategy.com/index.php/Weaver", "./list_of_cards_files/200px-Weaver.jpg")
WHEELWRIGHT = CardShapedThing("Wheelwright", {"Action"}, Cost(coins=5), "+1 Card+1 ActionYou may discard a card to gain an Action card costing as much as it or less.", "https://wiki.dominionstrategy.com/index.php/Wheelwright", "./list_of_cards_files/200px-Wheelwright.jpg")
WITCHS_HUT = CardShapedThing("Witch's Hut", {"Action", "Attack"}, Cost(coins=5), "+4 CardsDiscard 2 cards, revealed. If they're both Actions, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Witch%27s_Hut", "./list_of_cards_files/200px-Witch's_Hut.jpg")
ALTAR = CardShapedThing("Altar", {"Action"}, Cost(coins=6), "Trash a card from your hand. Gain a card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Altar", "./list_of_cards_files/200px-Altar.jpg")
ARMORY = CardShapedThing("Armory", {"Action"}, Cost(coins=4), "Gain a card onto your deck costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Armory", "./list_of_cards_files/200px-Armory.jpg")
BAND_OF_MISFITS = CardShapedThing("Band of Misfits", {"Action", "Command"}, Cost(coins=5), "Play a non-Command non-Duration Action card from the Supply that costs less than this, leaving it there.", "https://wiki.dominionstrategy.com/index.php/Band_of_Misfits", "./list_of_cards_files/200px-Band_of_Misfits.jpg")
BANDIT_CAMP = CardShapedThing("Bandit Camp", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsGain a Spoils.", "https://wiki.dominionstrategy.com/index.php/Bandit_Camp", "./list_of_cards_files/200px-Bandit_Camp.jpg")
BEGGAR = CardShapedThing("Beggar", {"Action", "Reaction"}, Cost(coins=2), "Gain 3 Coppers to your hand.When another player plays an Attack card, you may first discard this to gain 2 Silvers, putting one onto your deck.", "https://wiki.dominionstrategy.com/index.php/Beggar", "./list_of_cards_files/200px-Beggar.jpg")
CATACOMBS = CardShapedThing("Catacombs", {"Action"}, Cost(coins=5), "Look at the top 3 cards of your deck. Choose one: Put them into your hand; or discard them and +3 Cards.When you trash this, gain a cheaper card.", "https://wiki.dominionstrategy.com/index.php/Catacombs", "./list_of_cards_files/200px-Catacombs.jpg")
COUNT = CardShapedThing("Count", {"Action"}, Cost(coins=5), "Choose one: Discard 2 cards; or put a card from your hand onto your deck; or gain a Copper.Choose one: +$3; or trash your hand; or gain a Duchy.", "https://wiki.dominionstrategy.com/index.php/Count", "./list_of_cards_files/200px-Count.jpg")
COUNTERFEIT = CardShapedThing("Counterfeit", {"Treasure"}, Cost(coins=5), "$1+1 BuyYou may play a non-Duration Treasure from your hand twice. Trash it.", "https://wiki.dominionstrategy.com/index.php/Counterfeit", "./list_of_cards_files/200px-Counterfeit.jpg")
CULTIST = CardShapedThing("Cultist", {"Action", "Attack", "Looter"}, Cost(coins=5), "+2 CardsEach other player gains a Ruins. You may play a Cultist from your hand.When you trash this, +3 Cards.", "https://wiki.dominionstrategy.com/index.php/Cultist", "./list_of_cards_files/200px-Cultist.jpg")
DAME_ANNA = CardShapedThing("Dame Anna", {"Action", "Attack", "Knight"}, Cost(coins=5), "You may trash up to 2 cards from your hand. Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Dame_Anna", "./list_of_cards_files/200px-Dame_Anna.jpg")
DAME_JOSEPHINE = CardShapedThing("Dame Josephine", {"Action", "Attack", "Knight", "Victory"}, Cost(coins=5), "Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.2VP", "https://wiki.dominionstrategy.com/index.php/Dame_Josephine", "./list_of_cards_files/200px-Dame_Josephine.jpg")
DAME_MOLLY = CardShapedThing("Dame Molly", {"Action", "Attack", "Knight"}, Cost(coins=5), "+2 ActionsEach other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Dame_Molly", "./list_of_cards_files/200px-Dame_Molly.jpg")
DAME_NATALIE = CardShapedThing("Dame Natalie", {"Action", "Attack", "Knight"}, Cost(coins=5), "You may gain a card costing up to $3. Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Dame_Natalie", "./list_of_cards_files/200px-Dame_Natalie.jpg")
DAME_SYLVIA = CardShapedThing("Dame Sylvia", {"Action", "Attack", "Knight"}, Cost(coins=5), "+$2Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Dame_Sylvia", "./list_of_cards_files/200px-Dame_Sylvia.jpg")
DEATH_CART = CardShapedThing("Death Cart", {"Action", "Looter"}, Cost(coins=4), "You may trash this or an Action card from your hand, for +$5.When you gain this, gain 2 Ruins.", "https://wiki.dominionstrategy.com/index.php/Death_Cart", "./list_of_cards_files/200px-Death_Cart.jpg")
FEODUM = CardShapedThing("Feodum", {"Victory"}, Cost(coins=4), "Worth 1VP per 3 Silvers you have (round down).When you trash this, gain 3 Silvers.", "https://wiki.dominionstrategy.com/index.php/Feodum", "./list_of_cards_files/200px-Feodum.jpg")
FORAGER = CardShapedThing("Forager", {"Action"}, Cost(coins=3), "+1 Action+1 BuyTrash a card from your hand, then +$1 per differently named Treasure in the trash.", "https://wiki.dominionstrategy.com/index.php/Forager", "./list_of_cards_files/200px-Forager.jpg")
FORTRESS = CardShapedThing("Fortress", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsWhen you trash this, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Fortress", "./list_of_cards_files/200px-Fortress.jpg")
GRAVEROBBER = CardShapedThing("Graverobber", {"Action"}, Cost(coins=5), "Choose one: Gain a card from the trash costing from $3 to $6, onto your deck; or trash an Action card from your hand and gain a card costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Graverobber", "./list_of_cards_files/200px-Graverobber.jpg")
HERMIT = CardShapedThing("Hermit", {"Action"}, Cost(coins=3), "Look through your discard pile. You may trash a non-Treasure from it or from your hand. Gain a card costing up to $3. At the end of your Buy phase this turn, if you didn't gain any cards in it, exchange this for a Madman.", "https://wiki.dominionstrategy.com/index.php/Hermit", "./list_of_cards_files/200px-Hermit.jpg")
HUNTING_GROUNDS = CardShapedThing("Hunting Grounds", {"Action"}, Cost(coins=6), "+4 CardsWhen you trash this, gain a Duchy or 3 Estates.", "https://wiki.dominionstrategy.com/index.php/Hunting_Grounds", "./list_of_cards_files/200px-Hunting_Grounds.jpg")
IRONMONGER = CardShapedThing("Ironmonger", {"Action"}, Cost(coins=4), "+1 Card+1 ActionReveal the top card of your deck; you may discard it. Either way, if it is an…Action card, +1 ActionTreasure card, +$1Victory card, +1 Card", "https://wiki.dominionstrategy.com/index.php/Ironmonger", "./list_of_cards_files/200px-Ironmonger.jpg")
JUNK_DEALER = CardShapedThing("Junk Dealer", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1Trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Junk_Dealer", "./list_of_cards_files/200px-Junk_Dealer.jpg")
MARAUDER = CardShapedThing("Marauder", {"Action", "Attack", "Looter"}, Cost(coins=4), "Gain a Spoils. Each other player gains a Ruins.", "https://wiki.dominionstrategy.com/index.php/Marauder", "./list_of_cards_files/200px-Marauder.jpg")
MARKET_SQUARE = CardShapedThing("Market Square", {"Action", "Reaction"}, Cost(coins=3), "+1 Card+1 Action+1 BuyWhen one of your cards is trashed, you may discard this from your hand to gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Market_Square", "./list_of_cards_files/200px-Market_Square.jpg")
MYSTIC = CardShapedThing("Mystic", {"Action"}, Cost(coins=5), "+1 Action+$2Name a card, then reveal the top card of your deck. If you named it, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Mystic", "./list_of_cards_files/200px-Mystic.jpg")
PILLAGE = CardShapedThing("Pillage", {"Action", "Attack"}, Cost(coins=5), "Trash this. If you did, gain 2 Spoils, and each other player with 5 or more cards in hand reveals their hand and discards a card that you choose.", "https://wiki.dominionstrategy.com/index.php/Pillage", "./list_of_cards_files/200px-Pillage.jpg")
POOR_HOUSE = CardShapedThing("Poor House", {"Action"}, Cost(coins=1), "+$4Reveal your hand. -$1 per Treasure card in your hand. (You can't go below $0.)", "https://wiki.dominionstrategy.com/index.php/Poor_House", "./list_of_cards_files/200px-Poor_House.jpg")
PROCESSION = CardShapedThing("Procession", {"Action"}, Cost(coins=4), "You may play a non-Duration Action card from your hand twice. Trash it. Gain an Action card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Procession", "./list_of_cards_files/200px-Procession.jpg")
RATS = CardShapedThing("Rats", {"Action"}, Cost(coins=4), "+1 Card+1 ActionGain a Rats. Trash a card from your hand other than a Rats (or reveal a hand of all Rats).When you trash this, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Rats", "./list_of_cards_files/200px-Rats.jpg")
REBUILD = CardShapedThing("Rebuild", {"Action"}, Cost(coins=5), "+1 ActionName a card. Reveal cards from your deck until you reveal a Victory card you did not name. Discard the rest, trash the Victory card, and gain a Victory card costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Rebuild", "./list_of_cards_files/200px-Rebuild.jpg")
ROGUE = CardShapedThing("Rogue", {"Action", "Attack"}, Cost(coins=5), "+$2If there are any cards in the trash costing from $3 to $6, gain one of them. Otherwise, each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest.", "https://wiki.dominionstrategy.com/index.php/Rogue", "./list_of_cards_files/200px-Rogue.jpg")
SAGE = CardShapedThing("Sage", {"Action"}, Cost(coins=3), "+1 ActionReveal cards from the top of your deck until you reveal one costing $3 or more. Put that card into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Sage", "./list_of_cards_files/200px-Sage.jpg")
SCAVENGER = CardShapedThing("Scavenger", {"Action"}, Cost(coins=4), "+$2You may put your deck into your discard pile. Put a card from your discard pile onto your deck.", "https://wiki.dominionstrategy.com/index.php/Scavenger", "./list_of_cards_files/200px-Scavenger.jpg")
SIR_BAILEY = CardShapedThing("Sir Bailey", {"Action", "Attack", "Knight"}, Cost(coins=5), "+1 Card+1 ActionEach other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Sir_Bailey", "./list_of_cards_files/200px-Sir_Bailey.jpg")
SIR_DESTRY = CardShapedThing("Sir Destry", {"Action", "Attack", "Knight"}, Cost(coins=5), "+2 CardsEach other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Sir_Destry", "./list_of_cards_files/200px-Sir_Destry.jpg")
SIR_MARTIN = CardShapedThing("Sir Martin", {"Action", "Attack", "Knight"}, Cost(coins=4), "+2 BuysEach other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Sir_Martin", "./list_of_cards_files/200px-Sir_Martin.jpg")
SIR_MICHAEL = CardShapedThing("Sir Michael", {"Action", "Attack", "Knight"}, Cost(coins=5), "Each other player discards down to 3 cards in hand. Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Sir_Michael", "./list_of_cards_files/200px-Sir_Michael.jpg")
SIR_VANDER = CardShapedThing("Sir Vander", {"Action", "Attack", "Knight"}, Cost(coins=5), "Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.When you trash this, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Sir_Vander", "./list_of_cards_files/200px-Sir_Vander.jpg")
SQUIRE = CardShapedThing("Squire", {"Action"}, Cost(coins=2), "+$1Choose one: +2 Actions; or +2 Buys; or gain a Silver.When you trash this, gain an Attack card.", "https://wiki.dominionstrategy.com/index.php/Squire", "./list_of_cards_files/200px-Squire.jpg")
STOREROOM = CardShapedThing("Storeroom", {"Action"}, Cost(coins=3), "+1 BuyDiscard any number of cards, then draw that many. Then discard any number of cards for +$1 each.", "https://wiki.dominionstrategy.com/index.php/Storeroom", "./list_of_cards_files/200px-Storeroom.jpg")
URCHIN = CardShapedThing("Urchin", {"Action", "Attack"}, Cost(coins=3), "+1 Card+1 ActionEach other player discards down to 4 cards in hand.When you play another Attack card with this in play, you may first trash this, to gain a Mercenary.", "https://wiki.dominionstrategy.com/index.php/Urchin", "./list_of_cards_files/200px-Urchin.jpg")
VAGRANT = CardShapedThing("Vagrant", {"Action"}, Cost(coins=2), "+1 Card+1 ActionReveal the top card of your deck. If it's a Curse, Ruins, Shelter, or Victory card, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Vagrant", "./list_of_cards_files/200px-Vagrant.jpg")
WANDERING_MINSTREL = CardShapedThing("Wandering Minstrel", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsReveal the top 3 cards of your deck. Put the Action cards back in any order and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Wandering_Minstrel", "./list_of_cards_files/200px-Wandering_Minstrel.jpg")
ABANDONED_MINE = CardShapedThing("Abandoned Mine", {"Action", "Ruins"}, Cost(coins=0), "+$1", "https://wiki.dominionstrategy.com/index.php/Abandoned_Mine", "./list_of_cards_files/200px-Abandoned_Mine.jpg")
RUINED_LIBRARY = CardShapedThing("Ruined Library", {"Action", "Ruins"}, Cost(coins=0), "+1 Card", "https://wiki.dominionstrategy.com/index.php/Ruined_Library", "./list_of_cards_files/200px-Ruined_Library.jpg")
RUINED_MARKET = CardShapedThing("Ruined Market", {"Action", "Ruins"}, Cost(coins=0), "+1 Buy", "https://wiki.dominionstrategy.com/index.php/Ruined_Market", "./list_of_cards_files/200px-Ruined_Market.jpg")
RUINED_VILLAGE = CardShapedThing("Ruined Village", {"Action", "Ruins"}, Cost(coins=0), "+1 Action", "https://wiki.dominionstrategy.com/index.php/Ruined_Village", "./list_of_cards_files/200px-Ruined_Village.jpg")
SURVIVORS = CardShapedThing("Survivors", {"Action", "Ruins"}, Cost(coins=0), "Look at the top 2 cards of your deck. Discard them or put them back in any order.", "https://wiki.dominionstrategy.com/index.php/Survivors", "./list_of_cards_files/200px-Survivors.jpg")
HOVEL = CardShapedThing("Hovel", {"Reaction", "Shelter"}, Cost(coins=1), "When you gain a Victory card, you may trash this from your hand.", "https://wiki.dominionstrategy.com/index.php/Hovel", "./list_of_cards_files/200px-Hovel.jpg")
MADMAN = CardShapedThing("Madman", {"Action"}, Cost(coins=0), "+2 ActionsReturn this to the Madman pile. If you do, +1 Card per card in your hand.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Madman", "./list_of_cards_files/200px-Madman.jpg")
MERCENARY = CardShapedThing("Mercenary", {"Action", "Attack"}, Cost(coins=0), "You may trash 2 cards from your hand. If you did, +2 Cards, +$2, and each other player discards down to 3 cards in hand.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Mercenary", "./list_of_cards_files/200px-Mercenary.jpg")
NECROPOLIS = CardShapedThing("Necropolis", {"Action", "Shelter"}, Cost(coins=1), "+2 Actions", "https://wiki.dominionstrategy.com/index.php/Necropolis", "./list_of_cards_files/200px-Necropolis.jpg")
OVERGROWN_ESTATE = CardShapedThing("Overgrown Estate", {"Victory", "Shelter"}, Cost(coins=1), "0VPWhen you trash this, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Overgrown_Estate", "./list_of_cards_files/200px-Overgrown_Estate.jpg")
SPOILS = CardShapedThing("Spoils", {"Treasure"}, Cost(coins=0), "$3When you play this, return it to the Spoils pile.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Spoils", "./list_of_cards_files/200px-Spoils.jpg")
AMULET = CardShapedThing("Amulet", {"Action", "Duration"}, Cost(coins=3), "Now and at the start of your next turn, choose one: +$1; or trash a card from your hand; or gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Amulet", "./list_of_cards_files/200px-Amulet.jpg")
ARTIFICER = CardShapedThing("Artificer", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1Discard any number of cards. You may gain a card onto your deck, costing exactly $1 per card discarded.", "https://wiki.dominionstrategy.com/index.php/Artificer", "./list_of_cards_files/200px-Artificer.jpg")
BRIDGE_TROLL = CardShapedThing("Bridge Troll", {"Action", "Duration", "Attack"}, Cost(coins=5), "Each other player takes their -$1 token. On this turn and your next turn, cards cost $1 less. Now and at the start of your next turn: +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Bridge_Troll", "./list_of_cards_files/200px-Bridge_Troll.jpg")
CARAVAN_GUARD = CardShapedThing("Caravan Guard", {"Action", "Duration", "Reaction"}, Cost(coins=3), "+1 Card+1 ActionAt the start of your next turn, +$1.When another player plays an Attack card, you may first play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Caravan_Guard", "./list_of_cards_files/200px-Caravan_Guard.jpg")
COIN_OF_THE_REALM = CardShapedThing("Coin of the Realm", {"Treasure", "Reserve"}, Cost(coins=2), "$1Put this on your Tavern mat.After you play an Action card, you may call this, for +2 Actions.", "https://wiki.dominionstrategy.com/index.php/Coin_of_the_Realm", "./list_of_cards_files/200px-Coin_of_the_Realm.jpg")
DISTANT_LANDS = CardShapedThing("Distant Lands", {"Action", "Reserve", "Victory"}, Cost(coins=5), "Put this on your Tavern mat.Worth 4VP if on your Tavern mat at the end of the game (otherwise worth 0VP).", "https://wiki.dominionstrategy.com/index.php/Distant_Lands", "./list_of_cards_files/200px-Distant_Lands.jpg")
DUNGEON = CardShapedThing("Dungeon", {"Action", "Duration"}, Cost(coins=3), "+1 ActionNow and at the start of your next turn: +2 Cards, then discard 2 cards.", "https://wiki.dominionstrategy.com/index.php/Dungeon", "./list_of_cards_files/200px-Dungeon.jpg")
DUPLICATE = CardShapedThing("Duplicate", {"Action", "Reserve"}, Cost(coins=4), "Put this on your Tavern mat.When you gain a card costing up to $6, you may call this, to gain a copy of that card.", "https://wiki.dominionstrategy.com/index.php/Duplicate", "./list_of_cards_files/200px-Duplicate.jpg")
GEAR = CardShapedThing("Gear", {"Action", "Duration"}, Cost(coins=3), "+2 CardsSet aside up to 2 cards from your hand face down (under this). At the start of your next turn, put them into your hand.", "https://wiki.dominionstrategy.com/index.php/Gear", "./list_of_cards_files/200px-Gear.jpg")
GIANT = CardShapedThing("Giant", {"Action", "Attack"}, Cost(coins=5), "Turn your Journey token over (it starts face up). Then if it's face down, +$1. If it's face up, +$5, and each other player reveals the top card of their deck, trashes it if it costs from $3 to $6, and otherwise discards it and gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Giant", "./list_of_cards_files/200px-Giant.jpg")
GUIDE = CardShapedThing("Guide", {"Action", "Reserve"}, Cost(coins=3), "+1 Card+1 ActionPut this on your Tavern mat.At the start of your turn, you may call this, to discard your hand and draw 5 cards.", "https://wiki.dominionstrategy.com/index.php/Guide", "./list_of_cards_files/200px-Guide.jpg")
HAUNTED_WOODS = CardShapedThing("Haunted Woods", {"Action", "Duration", "Attack"}, Cost(coins=5), "At the start of your next turn: +3 Cards.Until then, when any other player gains a card they bought, they put their hand onto their deck in any order.", "https://wiki.dominionstrategy.com/index.php/Haunted_Woods", "./list_of_cards_files/200px-Haunted_Woods.jpg")
HIRELING = CardShapedThing("Hireling", {"Action", "Duration"}, Cost(coins=6), "At the start of each of your turns for the rest of the game: +1 Card.", "https://wiki.dominionstrategy.com/index.php/Hireling", "./list_of_cards_files/200px-Hireling.jpg")
LOST_CITY = CardShapedThing("Lost City", {"Action"}, Cost(coins=5), "+2 Cards+2 ActionsWhen you gain this, each other player draws a card.", "https://wiki.dominionstrategy.com/index.php/Lost_City", "./list_of_cards_files/200px-Lost_City.jpg")
MAGPIE = CardShapedThing("Magpie", {"Action"}, Cost(coins=4), "+1 Card+1 ActionReveal the top card of your deck.  If it's a Treasure, put it into your hand. If it's an Action or Victory card, gain a Magpie.", "https://wiki.dominionstrategy.com/index.php/Magpie", "./list_of_cards_files/200px-Magpie.jpg")
MESSENGER = CardShapedThing("Messenger", {"Action"}, Cost(coins=4), "+1 Buy+$2You may put your deck into your discard pile.When this is the first card you gain in your Buy phase, gain a card costing up to $4, and each other player gains a copy of it.", "https://wiki.dominionstrategy.com/index.php/Messenger", "./list_of_cards_files/200px-Messenger.jpg")
MISER = CardShapedThing("Miser", {"Action"}, Cost(coins=4), "Choose one: Put a Copper from your hand onto your Tavern mat; or +$1 per Copper on your Tavern mat.", "https://wiki.dominionstrategy.com/index.php/Miser", "./list_of_cards_files/200px-Miser.jpg")
PAGE = CardShapedThing("Page", {"Action", "Traveller"}, Cost(coins=2), "+1 Card+1 ActionWhen you discard this from play, you may exchange it for a Treasure Hunter.", "https://wiki.dominionstrategy.com/index.php/Page", "./list_of_cards_files/200px-Page.jpg")
PEASANT = CardShapedThing("Peasant", {"Action", "Traveller"}, Cost(coins=2), "+1 Buy+$1When you discard this from play, you may exchange it for a Soldier.", "https://wiki.dominionstrategy.com/index.php/Peasant", "./list_of_cards_files/200px-Peasant.jpg")
PORT = CardShapedThing("Port", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsWhen you gain this, gain another Port (that doesn't come with another).", "https://wiki.dominionstrategy.com/index.php/Port", "./list_of_cards_files/200px-Port.jpg")
RANGER = CardShapedThing("Ranger", {"Action"}, Cost(coins=4), "+1 BuyTurn your Journey token over (it starts face up). Then if it's face up, +5 Cards.", "https://wiki.dominionstrategy.com/index.php/Ranger", "./list_of_cards_files/200px-Ranger.jpg")
RATCATCHER = CardShapedThing("Ratcatcher", {"Action", "Reserve"}, Cost(coins=2), "+1 Card+1 ActionPut this on your Tavern mat.At the start of your turn, you may call this to trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Ratcatcher", "./list_of_cards_files/200px-Ratcatcher.jpg")
RAZE = CardShapedThing("Raze", {"Action"}, Cost(coins=2), "+1 ActionTrash this or a card from your hand. Look at one card from the top of your deck per $1 the trashed card costs. Put one of them into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Raze", "./list_of_cards_files/200px-Raze.jpg")
RELIC = CardShapedThing("Relic", {"Treasure", "Attack"}, Cost(coins=5), "$2Each other player puts their -1 Card token on their deck.", "https://wiki.dominionstrategy.com/index.php/Relic", "./list_of_cards_files/200px-Relic.jpg")
ROYAL_CARRIAGE = CardShapedThing("Royal Carriage", {"Action", "Reserve"}, Cost(coins=5), "+1 ActionPut this on your Tavern mat.After you play an Action card, if it's still in play, you may call this, to replay that Action.", "https://wiki.dominionstrategy.com/index.php/Royal_Carriage", "./list_of_cards_files/200px-Royal_Carriage.jpg")
STORYTELLER = CardShapedThing("Storyteller", {"Action"}, Cost(coins=5), "+1 ActionPlay up to 3 Treasures from your hand. Then +1 Card, and pay all of your $ for +1 Card per $1 you paid.", "https://wiki.dominionstrategy.com/index.php/Storyteller", "./list_of_cards_files/200px-Storyteller.jpg")
SWAMP_HAG = CardShapedThing("Swamp Hag", {"Action", "Duration", "Attack"}, Cost(coins=5), "At the start of your next turn: +$3.Until then, when any other player gains a card they bought, they gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Swamp_Hag", "./list_of_cards_files/200px-Swamp_Hag.jpg")
TRANSMOGRIFY = CardShapedThing("Transmogrify", {"Action", "Reserve"}, Cost(coins=4), "+1 ActionPut this on your Tavern mat.At the start of your turn, you may call this, to trash a card from your hand, and gain a card to your hand costing up to $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Transmogrify", "./list_of_cards_files/200px-Transmogrify.jpg")
TREASURE_TROVE = CardShapedThing("Treasure Trove", {"Treasure"}, Cost(coins=5), "$2Gain a Gold and a Copper.", "https://wiki.dominionstrategy.com/index.php/Treasure_Trove", "./list_of_cards_files/200px-Treasure_Trove.jpg")
WINE_MERCHANT = CardShapedThing("Wine Merchant", {"Action", "Reserve"}, Cost(coins=5), "+1 Buy+$4Put this on your Tavern mat.At the end of your Buy phase, if you have at least $2 unspent, you may discard this from your Tavern mat.", "https://wiki.dominionstrategy.com/index.php/Wine_Merchant", "./list_of_cards_files/200px-Wine_Merchant.jpg")
CHAMPION = CardShapedThing("Champion", {"Action", "Duration"}, Cost(coins=6), "+1 ActionFor the rest of the game, when another player plays an Attack, it doesn't affect you, and when you play an Action card, you first get +1 Action.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Champion", "./list_of_cards_files/200px-Champion.jpg")
DISCIPLE = CardShapedThing("Disciple", {"Action", "Traveller"}, Cost(coins=5), "You may play an Action card from your hand twice. Gain a copy of it.When you discard this from play, you may exchange it for a Teacher.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Disciple", "./list_of_cards_files/200px-Disciple.jpg")
FUGITIVE = CardShapedThing("Fugitive", {"Action", "Traveller"}, Cost(coins=4), "+2 Cards+1 ActionDiscard a card.When you discard this from play, you may exchange it for a Disciple.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Fugitive", "./list_of_cards_files/200px-Fugitive.jpg")
HERO = CardShapedThing("Hero", {"Action", "Traveller"}, Cost(coins=5), "+$2Gain a Treasure.When you discard this from play, you may exchange it for a Champion.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Hero", "./list_of_cards_files/200px-Hero.jpg")
SOLDIER = CardShapedThing("Soldier", {"Action", "Attack", "Traveller"}, Cost(coins=3), "+$2+$1 per other Attack you have in play. Each other player with 4 or more cards in hand discards a card.When you discard this from play, you may exchange it for a Fugitive. (This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Soldier", "./list_of_cards_files/200px-Soldier.jpg")
TEACHER = CardShapedThing("Teacher", {"Action", "Reserve"}, Cost(coins=6), "Put this on your Tavern mat.At the start of your turn, you may call this, to move your +1 Card, +1 Action, +1 Buy, or +$1 token to an Action Supply pile you have no tokens on. (When you play a card from that pile, you first get that bonus.)(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Teacher", "./list_of_cards_files/200px-Teacher.jpg")
TREASURE_HUNTER = CardShapedThing("Treasure Hunter", {"Action", "Traveller"}, Cost(coins=3), "+1 Action+$1Gain a Silver per card the player to your right gained in their last turn.When you discard this from play, you may exchange it for a Warrior.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Treasure_Hunter", "./list_of_cards_files/200px-Treasure_Hunter.jpg")
WARRIOR = CardShapedThing("Warrior", {"Action", "Attack", "Traveller"}, Cost(coins=4), "+2 CardsFor each Traveller you have in play (including this), each other player discards the top card of their deck and trashes it if it costs $3 or $4.When you discard this from play, you may exchange it for a Hero.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Warrior", "./list_of_cards_files/200px-Warrior.jpg")
ALMS = CardShapedThing("Alms", {"Event"}, Cost(coins=0), "Once per turn: If you have no Treasures in play, gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Alms", "./list_of_cards_files/320px-Alms.jpg")
BALL = CardShapedThing("Ball", {"Event"}, Cost(coins=5), "Take your -$1 token. Gain 2 cards each costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Ball", "./list_of_cards_files/320px-Ball.jpg")
BONFIRE = CardShapedThing("Bonfire", {"Event"}, Cost(coins=3), "Trash up to 2 Coppers you have in play.", "https://wiki.dominionstrategy.com/index.php/Bonfire", "./list_of_cards_files/320px-Bonfire.jpg")
BORROW = CardShapedThing("Borrow", {"Event"}, Cost(coins=0), "Once per turn: +1 Buy. If your -1 Card token isn't on your deck, put it there and +$1.", "https://wiki.dominionstrategy.com/index.php/Borrow", "./list_of_cards_files/320px-Borrow.jpg")
EXPEDITION = CardShapedThing("Expedition", {"Event"}, Cost(coins=3), "Draw 2 extra cards for your next hand.", "https://wiki.dominionstrategy.com/index.php/Expedition", "./list_of_cards_files/320px-Expedition.jpg")
FERRY = CardShapedThing("Ferry", {"Event"}, Cost(coins=3), "Move your -$2 token to an Action Supply pile. (Cards from that pile cost $2 less on your turns.)", "https://wiki.dominionstrategy.com/index.php/Ferry", "./list_of_cards_files/320px-Ferry.jpg")
INHERITANCE = CardShapedThing("Inheritance", {"Event"}, Cost(coins=7), "Once per game: Set aside a non-Command non-Duration Action card from the Supply costing up to $4. Move your Estate token to it. (During your turns, Estates are also Command Actions with \"Play the card with your Estate token, leaving it there.\")", "https://wiki.dominionstrategy.com/index.php/Inheritance", "./list_of_cards_files/320px-Inheritance.jpg")
LOST_ARTS = CardShapedThing("Lost Arts", {"Event"}, Cost(coins=6), "Move your +1 Action token to an Action Supply pile. (When you play a card from that pile, you first get +1 Action.)", "https://wiki.dominionstrategy.com/index.php/Lost_Arts", "./list_of_cards_files/320px-Lost_Arts.jpg")
MISSION = CardShapedThing("Mission", {"Event"}, Cost(coins=4), "Take an extra turn after this one (but not a 3rd turn in a row), during which you can't buy cards.(You can still buy Events.)", "https://wiki.dominionstrategy.com/index.php/Mission", "./list_of_cards_files/320px-Mission.jpg")
PATHFINDING = CardShapedThing("Pathfinding", {"Event"}, Cost(coins=8), "Move your +1 Card token to an Action Supply pile. (When you play a card from that pile, you first get +1 Card.)", "https://wiki.dominionstrategy.com/index.php/Pathfinding", "./list_of_cards_files/320px-Pathfinding.jpg")
PILGRIMAGE = CardShapedThing("Pilgrimage", {"Event"}, Cost(coins=4), "Once per turn: Turn your Journey token over (it starts face up); then if it's face up, choose up to 3 differently named cards you have in play and gain a copy of each.", "https://wiki.dominionstrategy.com/index.php/Pilgrimage", "./list_of_cards_files/320px-Pilgrimage.jpg")
PLAN = CardShapedThing("Plan", {"Event"}, Cost(coins=3), "Move your Trashing token to an Action Supply pile. (When you gain a card from that pile, you may trash a card from your hand.)", "https://wiki.dominionstrategy.com/index.php/Plan", "./list_of_cards_files/320px-Plan.jpg")
QUEST = CardShapedThing("Quest", {"Event"}, Cost(coins=0), "You may discard an Attack, two Curses, or six cards. If you do, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Quest", "./list_of_cards_files/320px-Quest.jpg")
RAID = CardShapedThing("Raid", {"Event"}, Cost(coins=5), "Gain a Silver per Silver you have in play. Each other player puts their -1 Card token on their deck.", "https://wiki.dominionstrategy.com/index.php/Raid", "./list_of_cards_files/320px-Raid.jpg")
SAVE = CardShapedThing("Save", {"Event"}, Cost(coins=1), "Once per turn: +1 Buy. Set aside a card from your hand, and put it into your hand at end of turn (after drawing).", "https://wiki.dominionstrategy.com/index.php/Save", "./list_of_cards_files/320px-Save.jpg")
SCOUTING_PARTY = CardShapedThing("Scouting Party", {"Event"}, Cost(coins=2), "+1 BuyLook at the top 5 cards of your deck. Discard 3 and put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Scouting_Party", "./list_of_cards_files/320px-Scouting_Party.jpg")
SEAWAY = CardShapedThing("Seaway", {"Event"}, Cost(coins=5), "Gain an Action card costing up to $4. Move your +1 Buy token to its pile. (When you play a card from that pile, you first get +1 Buy.)", "https://wiki.dominionstrategy.com/index.php/Seaway", "./list_of_cards_files/320px-Seaway.jpg")
TRADE = CardShapedThing("Trade", {"Event"}, Cost(coins=5), "Trash up to 2 cards from your hand. Gain a Silver per card you trashed.", "https://wiki.dominionstrategy.com/index.php/Trade", "./list_of_cards_files/320px-Trade.jpg")
TRAINING = CardShapedThing("Training", {"Event"}, Cost(coins=6), "Move your +$1 token to an Action Supply pile. (When you play a card from that pile, you first get +$1.)", "https://wiki.dominionstrategy.com/index.php/Training", "./list_of_cards_files/320px-Training.jpg")
TRAVELLING_FAIR = CardShapedThing("Travelling Fair", {"Event"}, Cost(coins=2), "+2 BuysWhen you gain a card this turn, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Travelling_Fair", "./list_of_cards_files/320px-Travelling_Fair.jpg")
ARCHIVE = CardShapedThing("Archive", {"Action", "Duration"}, Cost(coins=5), "+1 ActionSet aside the top 3 cards of your deck face down (you may look at them). Now and at the start of your next two turns, put one into your hand.", "https://wiki.dominionstrategy.com/index.php/Archive", "./list_of_cards_files/200px-Archive.jpg")
BUSTLING_VILLAGE = CardShapedThing("Bustling Village", {"Action"}, Cost(coins=5), "+1 Card+3 ActionsYou may reveal a Settlers from your discard pile and put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Bustling_Village", "./list_of_cards_files/200px-Bustling_Village.jpg")
CAPITAL = CardShapedThing("Capital", {"Treasure"}, Cost(coins=5), "$6+1 BuyWhen you discard this from play, +6D.", "https://wiki.dominionstrategy.com/index.php/Capital", "./list_of_cards_files/200px-Capital.jpg")
CATAPULT = CardShapedThing("Catapult", {"Action", "Attack"}, Cost(coins=3), "+$1Trash a card from your hand. If it costs $3 or more, each other player gains a Curse. If it's a Treasure, each other player discards down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Catapult", "./list_of_cards_files/200px-Catapult.jpg")
CHARIOT_RACE = CardShapedThing("Chariot Race", {"Action"}, Cost(coins=3), "+1 Action+1 Card, revealing it. The player to your left reveals the top card of their deck. If your card costs more, +$1 and +1VP.", "https://wiki.dominionstrategy.com/index.php/Chariot_Race", "./list_of_cards_files/200px-Chariot_Race.jpg")
CHARM = CardShapedThing("Charm", {"Treasure"}, Cost(coins=5), "Choose one: +1 Buy and +$2; or the next time you gain a card this turn, you may also gain a differently named card with the same cost.", "https://wiki.dominionstrategy.com/index.php/Charm", "./list_of_cards_files/200px-Charm.jpg")
CITY_QUARTER = CardShapedThing("City Quarter", {"Action"}, Cost(debt=8), "+2 ActionsReveal your hand. +1 Card per Action card revealed.", "https://wiki.dominionstrategy.com/index.php/City_Quarter", "./list_of_cards_files/200px-City_Quarter.jpg")
CROWN = CardShapedThing("Crown", {"Action", "Treasure"}, Cost(coins=5), "If it's your Action phase, you may play an Action from your hand twice.If it's your Buy phase, you may play a Treasure from your hand twice.", "https://wiki.dominionstrategy.com/index.php/Crown", "./list_of_cards_files/200px-Crown.jpg")
CRUMBLING_CASTLE = CardShapedThing("Crumbling Castle", {"Victory", "Castle"}, Cost(coins=4), "1VPWhen you gain or trash this, +1VP and gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Crumbling_Castle", "./list_of_cards_files/200px-Crumbling_Castle.jpg")
EMPORIUM = CardShapedThing("Emporium", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1When you gain this, if you have at least 5 Action cards in play, +2VP.", "https://wiki.dominionstrategy.com/index.php/Emporium", "./list_of_cards_files/200px-Emporium.jpg")
ENCAMPMENT = CardShapedThing("Encampment", {"Action"}, Cost(coins=2), "+2 Cards+2 ActionsYou may reveal a Gold or Plunder from your hand. If you do not, set this aside, and return it to its pile at the start of Clean-up.", "https://wiki.dominionstrategy.com/index.php/Encampment", "./list_of_cards_files/200px-Encampment.jpg")
ENCHANTRESS = CardShapedThing("Enchantress", {"Action", "Attack", "Duration"}, Cost(coins=3), "Until your next turn, the first time each other player plays an Action card on their turn, they get +1 Card and +1 Action instead of following its instructions.At the start of your next turn, +2 Cards", "https://wiki.dominionstrategy.com/index.php/Enchantress", "./list_of_cards_files/200px-Enchantress.jpg")
ENGINEER = CardShapedThing("Engineer", {"Action"}, Cost(debt=4), "Gain a card costing up to $4. You may trash this. If you do, gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Engineer", "./list_of_cards_files/200px-Engineer.jpg")
FARMERS_MARKET = CardShapedThing("Farmers' Market", {"Action", "Gathering"}, Cost(coins=3), "+1 BuyIf there are 4VP or more on the Farmers' Market pile, take them and trash this. Otherwise, add 1VP to the pile and then +$1 per 1VP on the pile.", "https://wiki.dominionstrategy.com/index.php/Farmers%27_Market", "./list_of_cards_files/200px-Farmers'_Market.jpg")
FORTUNE = CardShapedThing("Fortune", {"Treasure"}, Cost(coins=8, debt=8), "+1 BuyDouble your $ if you haven't yet this turn.When you gain this, gain a Gold per Gladiator you have in play.", "https://wiki.dominionstrategy.com/index.php/Fortune", "./list_of_cards_files/200px-Fortune.jpg")
FORUM = CardShapedThing("Forum", {"Action"}, Cost(coins=5), "+3 Cards+1 ActionDiscard 2 cards.When you gain this, +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Forum", "./list_of_cards_files/200px-Forum.jpg")
GLADIATOR = CardShapedThing("Gladiator", {"Action"}, Cost(coins=3), "+$2Reveal a card from your hand. The player to your left may reveal a copy from their hand. If they don't, +$1 and trash a Gladiator from its pile.", "https://wiki.dominionstrategy.com/index.php/Gladiator", "./list_of_cards_files/200px-Gladiator.jpg")
GRAND_CASTLE = CardShapedThing("Grand Castle", {"Victory", "Castle"}, Cost(coins=9), "5VPWhen you gain this, reveal your hand. +1VP per Victory card in your hand and/or in play.", "https://wiki.dominionstrategy.com/index.php/Grand_Castle", "./list_of_cards_files/200px-Grand_Castle.jpg")
GROUNDSKEEPER = CardShapedThing("Groundskeeper", {"Action"}, Cost(coins=5), "+1 Card+1 ActionThis turn, when you gain a Victory card, +1VP.", "https://wiki.dominionstrategy.com/index.php/Groundskeeper", "./list_of_cards_files/200px-Groundskeeper.jpg")
HAUNTED_CASTLE = CardShapedThing("Haunted Castle", {"Victory", "Castle"}, Cost(coins=6), "2VPWhen you gain this during your turn, gain a Gold, and each other player with 5 or more cards in hand puts 2 of them onto their deck.", "https://wiki.dominionstrategy.com/index.php/Haunted_Castle", "./list_of_cards_files/200px-Haunted_Castle.jpg")
HUMBLE_CASTLE = CardShapedThing("Humble Castle", {"Treasure", "Victory", "Castle"}, Cost(coins=3), "$1Worth 1VP per Castle you have.", "https://wiki.dominionstrategy.com/index.php/Humble_Castle", "./list_of_cards_files/200px-Humble_Castle.jpg")
KINGS_CASTLE = CardShapedThing("King's Castle", {"Victory", "Castle"}, Cost(coins=10), "Worth 2VP per Castle you have.", "https://wiki.dominionstrategy.com/index.php/King%27s_Castle", "./list_of_cards_files/200px-King's_Castle.jpg")
LEGIONARY = CardShapedThing("Legionary", {"Action", "Attack"}, Cost(coins=5), "+$3You may reveal a Gold from your hand. If you do, each other player discards down to 2 cards in hand, then draws a card.", "https://wiki.dominionstrategy.com/index.php/Legionary", "./list_of_cards_files/200px-Legionary.jpg")
OPULENT_CASTLE = CardShapedThing("Opulent Castle", {"Action", "Victory", "Castle"}, Cost(coins=7), "Discard any number of Victory cards, revealed. +$2 per card discarded.3VP", "https://wiki.dominionstrategy.com/index.php/Opulent_Castle", "./list_of_cards_files/200px-Opulent_Castle.jpg")
OVERLORD = CardShapedThing("Overlord", {"Action", "Command"}, Cost(debt=8), "Play a non-Command non-Duration Action card from the Supply costing up to $5, leaving it there.", "https://wiki.dominionstrategy.com/index.php/Overlord", "./list_of_cards_files/200px-Overlord.jpg")
PATRICIAN = CardShapedThing("Patrician", {"Action"}, Cost(coins=2), "+1 Card+1 ActionReveal the top card of your deck. If it costs $5 or more, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Patrician", "./list_of_cards_files/200px-Patrician.jpg")
PLUNDER = CardShapedThing("Plunder", {"Treasure"}, Cost(coins=5), "$2+1VP", "https://wiki.dominionstrategy.com/index.php/Plunder", "./list_of_cards_files/200px-Plunder.jpg")
ROCKS = CardShapedThing("Rocks", {"Treasure"}, Cost(coins=4), "$1When you gain or trash this: If it's your Buy phase, gain a Silver onto your deck, otherwise gain a Silver to your hand.", "https://wiki.dominionstrategy.com/index.php/Rocks", "./list_of_cards_files/200px-Rocks.jpg")
ROYAL_BLACKSMITH = CardShapedThing("Royal Blacksmith", {"Action"}, Cost(debt=8), "+5 CardsReveal your hand; discard the Coppers.", "https://wiki.dominionstrategy.com/index.php/Royal_Blacksmith", "./list_of_cards_files/200px-Royal_Blacksmith.jpg")
SACRIFICE = CardShapedThing("Sacrifice", {"Action"}, Cost(coins=4), "Trash a card from your hand.If it's an…Action card, +2 Cards and +2 ActionsTreasure card, +$2Victory card, +2VP", "https://wiki.dominionstrategy.com/index.php/Sacrifice", "./list_of_cards_files/200px-Sacrifice.jpg")
SETTLERS = CardShapedThing("Settlers", {"Action"}, Cost(coins=2), "+1 Card+1 ActionYou may reveal a Copper from your discard pile and put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Settlers", "./list_of_cards_files/200px-Settlers.jpg")
SMALL_CASTLE = CardShapedThing("Small Castle", {"Action", "Victory", "Castle"}, Cost(coins=5), "Trash this or a Castle from your hand. If you do, gain a Castle.2VP", "https://wiki.dominionstrategy.com/index.php/Small_Castle", "./list_of_cards_files/200px-Small_Castle.jpg")
SPRAWLING_CASTLE = CardShapedThing("Sprawling Castle", {"Victory", "Castle"}, Cost(coins=8), "4VPWhen you gain this, gain a Duchy or 3 Estates.", "https://wiki.dominionstrategy.com/index.php/Sprawling_Castle", "./list_of_cards_files/200px-Sprawling_Castle.jpg")
TEMPLE = CardShapedThing("Temple", {"Action", "Gathering"}, Cost(coins=4), "+1VPTrash from 1 to 3 differently named cards from your hand. Add 1VP to the Temple pile.When you gain this, take the VP from the Temple pile.", "https://wiki.dominionstrategy.com/index.php/Temple", "./list_of_cards_files/200px-Temple.jpg")
VILLA = CardShapedThing("Villa", {"Action"}, Cost(coins=4), "+2 Actions+1 Buy+$1When you gain this, put it into your hand, +1 Action, and if it's your Buy phase return to your Action phase.", "https://wiki.dominionstrategy.com/index.php/Villa", "./list_of_cards_files/200px-Villa.jpg")
WILD_HUNT = CardShapedThing("Wild Hunt", {"Action", "Gathering"}, Cost(coins=5), "Choose one: +3 Cards and add 1VP to the Wild Hunt pile; or gain an Estate, and if you do, take the VP from the pile.", "https://wiki.dominionstrategy.com/index.php/Wild_Hunt", "./list_of_cards_files/200px-Wild_Hunt.jpg")
ADVANCE = CardShapedThing("Advance", {"Event"}, Cost(coins=0), "You may trash an Action card from your hand. If you do, gain an Action card costing up to $6.", "https://wiki.dominionstrategy.com/index.php/Advance", "./list_of_cards_files/320px-Advance.jpg")
ANNEX = CardShapedThing("Annex", {"Event"}, Cost(debt=8), "Look through your discard pile. Shuffle all but up to 5 cards from it into your deck. Gain a Duchy.", "https://wiki.dominionstrategy.com/index.php/Annex", "./list_of_cards_files/320px-Annex.jpg")
BANQUET = CardShapedThing("Banquet", {"Event"}, Cost(coins=3), "Gain 2 Coppers and a non-Victory card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Banquet", "./list_of_cards_files/320px-Banquet.jpg")
CONQUEST = CardShapedThing("Conquest", {"Event"}, Cost(coins=6), "Gain 2 Silvers. +1VP per Silver you've gained this turn.", "https://wiki.dominionstrategy.com/index.php/Conquest", "./list_of_cards_files/320px-Conquest.jpg")
DELVE = CardShapedThing("Delve", {"Event"}, Cost(coins=2), "+1 BuyGain a Silver.", "https://wiki.dominionstrategy.com/index.php/Delve", "./list_of_cards_files/320px-Delve.jpg")
DOMINATE = CardShapedThing("Dominate", {"Event"}, Cost(coins=14), "Gain a Province. If you do, +9VP.", "https://wiki.dominionstrategy.com/index.php/Dominate", "./list_of_cards_files/320px-Dominate.jpg")
DONATE = CardShapedThing("Donate", {"Event"}, Cost(debt=8), "At the start of your next turn, first, put your deck and discard pile into your hand, trash any number of cards from it, then shuffle the rest into your deck and draw 5 cards.", "https://wiki.dominionstrategy.com/index.php/Donate", "./list_of_cards_files/320px-Donate.jpg")
RITUAL = CardShapedThing("Ritual", {"Event"}, Cost(coins=4), "Gain a Curse. If you do, trash a card from your hand. +1VP per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Ritual", "./list_of_cards_files/320px-Ritual.jpg")
SALT_THE_EARTH = CardShapedThing("Salt the Earth", {"Event"}, Cost(coins=4), "+1VPTrash a Victory card from the Supply.", "https://wiki.dominionstrategy.com/index.php/Salt_the_Earth", "./list_of_cards_files/320px-Salt_the_Earth.jpg")
TAX = CardShapedThing("Tax", {"Event"}, Cost(coins=2), "Add 2D to a Supply pile.Setup: Add 1D to each Supply pile. When a player gains a card in their Buy phase, they take the D from its pile.", "https://wiki.dominionstrategy.com/index.php/Tax", "./list_of_cards_files/320px-Tax.jpg")
TRIUMPH = CardShapedThing("Triumph", {"Event"}, Cost(debt=5), "Gain an Estate. If you did, +1VP per card you've gained this turn.", "https://wiki.dominionstrategy.com/index.php/Triumph", "./list_of_cards_files/320px-Triumph.jpg")
WEDDING = CardShapedThing("Wedding", {"Event"}, Cost(coins=4, debt=3), "+1VPGain a Gold.", "https://wiki.dominionstrategy.com/index.php/Wedding", "./list_of_cards_files/320px-Wedding.jpg")
WINDFALL = CardShapedThing("Windfall", {"Event"}, Cost(coins=5), "If your deck and discard pile are empty, gain 3 Golds.", "https://wiki.dominionstrategy.com/index.php/Windfall", "./list_of_cards_files/320px-Windfall.jpg")
AQUEDUCT = CardShapedThing("Aqueduct", {"Landmark"}, Cost(), "When you gain a Treasure, move 1VP from its pile to this. When you gain a Victory card, take the VP from this.Setup: Put 8VP on the Silver and Gold piles.", "https://wiki.dominionstrategy.com/index.php/Aqueduct", "./list_of_cards_files/320px-Aqueduct.jpg")
ARENA = CardShapedThing("Arena", {"Landmark"}, Cost(), "At the start of your Buy phase, you may discard an Action card. If you do, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Arena", "./list_of_cards_files/320px-Arena.jpg")
BANDIT_FORT = CardShapedThing("Bandit Fort", {"Landmark"}, Cost(), "When scoring, -2VP for each Silver and each Gold you have.", "https://wiki.dominionstrategy.com/index.php/Bandit_Fort", "./list_of_cards_files/320px-Bandit_Fort.jpg")
BASILICA = CardShapedThing("Basilica", {"Landmark"}, Cost(), "When you gain a card in your Buy phase, if you have $2 or more, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Basilica", "./list_of_cards_files/320px-Basilica.jpg")
BATHS = CardShapedThing("Baths", {"Landmark"}, Cost(), "When you end your turn without having gained a card, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Baths", "./list_of_cards_files/320px-Baths.jpg")
BATTLEFIELD = CardShapedThing("Battlefield", {"Landmark"}, Cost(), "When you gain a Victory card, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Battlefield", "./list_of_cards_files/320px-Battlefield.jpg")
COLONNADE = CardShapedThing("Colonnade", {"Landmark"}, Cost(), "When you gain an Action card in your Buy phase, if you have a copy of it in play, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Colonnade", "./list_of_cards_files/320px-Colonnade.jpg")
DEFILED_SHRINE = CardShapedThing("Defiled Shrine", {"Landmark"}, Cost(), "When you gain an Action, move 1VP from its pile to this. When you gain a Curse in your Buy phase, take the VP from this.Setup: Put 2VP on each non-Gathering Action Supply pile.", "https://wiki.dominionstrategy.com/index.php/Defiled_Shrine", "./list_of_cards_files/320px-Defiled_Shrine.jpg")
FOUNTAIN = CardShapedThing("Fountain", {"Landmark"}, Cost(), "When scoring, 15VP if you have at least 10 Coppers.", "https://wiki.dominionstrategy.com/index.php/Fountain", "./list_of_cards_files/320px-Fountain.jpg")
KEEP = CardShapedThing("Keep", {"Landmark"}, Cost(), "When scoring, 5VP per differently named Treasure you have, that you have more copies of than each other player, or tied for most.", "https://wiki.dominionstrategy.com/index.php/Keep", "./list_of_cards_files/320px-Keep.jpg")
LABYRINTH = CardShapedThing("Labyrinth", {"Landmark"}, Cost(), "When you gain a 2nd card in one of your turns, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Labyrinth", "./list_of_cards_files/320px-Labyrinth.jpg")
MOUNTAIN_PASS = CardShapedThing("Mountain Pass", {"Landmark"}, Cost(), "When you are the first player to gain a Province, each player bids once, up to 40D, ending with you. High bidder gets +8VP and takes the D they bid.", "https://wiki.dominionstrategy.com/index.php/Mountain_Pass", "./list_of_cards_files/320px-Mountain_Pass.jpg")
MUSEUM = CardShapedThing("Museum", {"Landmark"}, Cost(), "When scoring, 2VP per differently named card you have.", "https://wiki.dominionstrategy.com/index.php/Museum", "./list_of_cards_files/320px-Museum.jpg")
OBELISK = CardShapedThing("Obelisk", {"Landmark"}, Cost(), "When scoring, 2VP per card you have from the chosen pile.Setup: Choose a random Action Supply pile.", "https://wiki.dominionstrategy.com/index.php/Obelisk", "./list_of_cards_files/320px-Obelisk.jpg")
ORCHARD = CardShapedThing("Orchard", {"Landmark"}, Cost(), "When scoring, 4VP per differently named Action card you have 3 or more copies of.", "https://wiki.dominionstrategy.com/index.php/Orchard", "./list_of_cards_files/320px-Orchard.jpg")
PALACE = CardShapedThing("Palace", {"Landmark"}, Cost(), "When scoring, 3VP per set you have of Copper - Silver - Gold.", "https://wiki.dominionstrategy.com/index.php/Palace", "./list_of_cards_files/320px-Palace.jpg")
TOMB = CardShapedThing("Tomb", {"Landmark"}, Cost(), "When you trash a card, +1VP.", "https://wiki.dominionstrategy.com/index.php/Tomb", "./list_of_cards_files/320px-Tomb.jpg")
TOWER = CardShapedThing("Tower", {"Landmark"}, Cost(), "When scoring, 1VP per non-Victory card you have from an empty Supply pile.", "https://wiki.dominionstrategy.com/index.php/Tower", "./list_of_cards_files/320px-Tower.jpg")
TRIUMPHAL_ARCH = CardShapedThing("Triumphal Arch", {"Landmark"}, Cost(), "When scoring, 3VP per copy you have of the 2nd most common Action card among your cards (if it's a tie, count either).", "https://wiki.dominionstrategy.com/index.php/Triumphal_Arch", "./list_of_cards_files/320px-Triumphal_Arch.jpg")
WALL = CardShapedThing("Wall", {"Landmark"}, Cost(), "When scoring, -1VP per card you have after the first 15.", "https://wiki.dominionstrategy.com/index.php/Wall", "./list_of_cards_files/320px-Wall.jpg")
WOLF_DEN = CardShapedThing("Wolf Den", {"Landmark"}, Cost(), "When scoring, -3VP per card you have exactly one copy of.", "https://wiki.dominionstrategy.com/index.php/Wolf_Den", "./list_of_cards_files/320px-Wolf_Den.jpg")
BARD = CardShapedThing("Bard", {"Action", "Fate"}, Cost(coins=4), "+$2Receive a Boon.", "https://wiki.dominionstrategy.com/index.php/Bard", "./list_of_cards_files/200px-Bard.jpg")
BLESSED_VILLAGE = CardShapedThing("Blessed Village", {"Action", "Fate"}, Cost(coins=4), "+1 Card+2 ActionsWhen you gain this, take a Boon. Receive it now or at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Blessed_Village", "./list_of_cards_files/200px-Blessed_Village.jpg")
CEMETERY = CardShapedThing("Cemetery", {"Victory"}, Cost(coins=4), "2VPWhen you gain this, trash up to 4 cards from your hand.Heirloom: Haunted Mirror", "https://wiki.dominionstrategy.com/index.php/Cemetery", "./list_of_cards_files/200px-Cemetery.jpg")
CHANGELING = CardShapedThing("Changeling", {"Night"}, Cost(coins=3), "Trash this. Gain a copy of a card you have in play.In games using this, when you gain a card costing $3 or more, you may exchange it for a Changeling.", "https://wiki.dominionstrategy.com/index.php/Changeling", "./list_of_cards_files/200px-Changeling.jpg")
COBBLER = CardShapedThing("Cobbler", {"Night", "Duration"}, Cost(coins=5), "At the start of your next turn, gain a card to your hand costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Cobbler", "./list_of_cards_files/200px-Cobbler.jpg")
CONCLAVE = CardShapedThing("Conclave", {"Action"}, Cost(coins=4), "+$2You may play an Action card from your hand that you don't have a copy of in play. If you do, +1 Action.", "https://wiki.dominionstrategy.com/index.php/Conclave", "./list_of_cards_files/200px-Conclave.jpg")
CRYPT = CardShapedThing("Crypt", {"Night", "Duration"}, Cost(coins=5), "Set aside any number of non-Duration Treasures you have in play, face down (under this). While any remain, at the start of each of your turns, put one of them into your hand.", "https://wiki.dominionstrategy.com/index.php/Crypt", "./list_of_cards_files/200px-Crypt.jpg")
CURSED_VILLAGE = CardShapedThing("Cursed Village", {"Action", "Doom"}, Cost(coins=5), "+2 ActionsDraw until you have 6 cards in hand.When you gain this, receive a Hex.", "https://wiki.dominionstrategy.com/index.php/Cursed_Village", "./list_of_cards_files/200px-Cursed_Village.jpg")
DEN_OF_SIN = CardShapedThing("Den of Sin", {"Night", "Duration"}, Cost(coins=5), "At the start of your next turn, +2 Cards.This is gained to your hand (instead of your discard pile).", "https://wiki.dominionstrategy.com/index.php/Den_of_Sin", "./list_of_cards_files/200px-Den_of_Sin.jpg")
DEVILS_WORKSHOP = CardShapedThing("Devil's Workshop", {"Night"}, Cost(coins=4), "If the number of cards you've gained this turn is:2+, gain an Imp;1, gain a card costing up to $4;0, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Devil%27s_Workshop", "./list_of_cards_files/200px-Devil's_Workshop.jpg")
DRUID = CardShapedThing("Druid", {"Action", "Fate"}, Cost(coins=2), "+1 Buy Receive one of the set-aside Boons (leaving it there).Setup: Set aside the top 3 Boons face up.", "https://wiki.dominionstrategy.com/index.php/Druid", "./list_of_cards_files/200px-Druid.jpg")
EXORCIST = CardShapedThing("Exorcist", {"Night"}, Cost(coins=4), "Trash a card from your hand. Gain a cheaper Spirit from one of the Spirit piles.", "https://wiki.dominionstrategy.com/index.php/Exorcist", "./list_of_cards_files/200px-Exorcist.jpg")
FAITHFUL_HOUND = CardShapedThing("Faithful Hound", {"Action", "Reaction"}, Cost(coins=2), "+2 CardsWhen you discard this other than during Clean-up, you may set it aside, and put it into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Faithful_Hound", "./list_of_cards_files/200px-Faithful_HoundOld.jpg")
FOOL = CardShapedThing("Fool", {"Action", "Fate"}, Cost(coins=3), "If you aren't the player with Lost in the Woods: take it, take 3 Boons, and receive the Boons in any order.Heirloom: Lucky Coin", "https://wiki.dominionstrategy.com/index.php/Fool", "./list_of_cards_files/200px-Fool.jpg")
GHOST_TOWN = CardShapedThing("Ghost Town", {"Night", "Duration"}, Cost(coins=3), "At the start of your next turn, +1 Card and +1 Action.This is gained to your hand (instead of your discard pile).", "https://wiki.dominionstrategy.com/index.php/Ghost_Town", "./list_of_cards_files/200px-Ghost_Town.jpg")
GUARDIAN = CardShapedThing("Guardian", {"Night", "Duration"}, Cost(coins=2), "At the start of your next turn, +$1. Until then, when another player plays an Attack card, it doesn't affect you. This is gained to your hand (instead of your discard pile).", "https://wiki.dominionstrategy.com/index.php/Guardian", "./list_of_cards_files/200px-Guardian.jpg")
IDOL = CardShapedThing("Idol", {"Treasure", "Attack", "Fate"}, Cost(coins=5), "$2If you have an odd number of Idols in play (counting this), receive a Boon; otherwise, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Idol", "./list_of_cards_files/200px-Idol.jpg")
LEPRECHAUN = CardShapedThing("Leprechaun", {"Action", "Doom"}, Cost(coins=3), "Gain a Gold. If you have exactly 7 cards in play, gain a Wish. Otherwise, receive a Hex.", "https://wiki.dominionstrategy.com/index.php/Leprechaun", "./list_of_cards_files/200px-Leprechaun.jpg")
MONASTERY = CardShapedThing("Monastery", {"Night"}, Cost(coins=2), "For each card you've gained this turn, you may trash a card from your hand or a Copper you have in play.", "https://wiki.dominionstrategy.com/index.php/Monastery", "./list_of_cards_files/200px-MonasteryOld.jpg")
NECROMANCER = CardShapedThing("Necromancer", {"Action"}, Cost(coins=4), "Choose a face up, non-Duration Action card in the trash. Turn it face down for the turn, and play it, leaving it there.Setup: Put the 3 Zombies into the trash.", "https://wiki.dominionstrategy.com/index.php/Necromancer", "./list_of_cards_files/200px-Necromancer.jpg")
NIGHT_WATCHMAN = CardShapedThing("Night Watchman", {"Night"}, Cost(coins=3), "Look at the top 5 cards of your deck, discard any number, and put the rest back in any order.This is gained to your hand (instead of your discard pile).", "https://wiki.dominionstrategy.com/index.php/Night_Watchman", "./list_of_cards_files/200px-Night_WatchmanOld.jpg")
PIXIE = CardShapedThing("Pixie", {"Action", "Fate"}, Cost(coins=2), "+1 Card+1 ActionDiscard the top Boon. You may trash this to receive that Boon twice.Heirloom: Goat", "https://wiki.dominionstrategy.com/index.php/Pixie", "./list_of_cards_files/200px-Pixie.jpg")
POOKA = CardShapedThing("Pooka", {"Action"}, Cost(coins=5), "You may trash a Treasure other than Cursed Gold from your hand, for +4 Cards.Heirloom: Cursed Gold", "https://wiki.dominionstrategy.com/index.php/Pooka", "./list_of_cards_files/200px-PookaOld.jpg")
RAIDER = CardShapedThing("Raider", {"Night", "Duration", "Attack"}, Cost(coins=6), "Each other player with 5 or more cards in hand discards a copy of a card you have in play (or reveals they can't).At the start of your next turn, +$3.", "https://wiki.dominionstrategy.com/index.php/Raider", "./list_of_cards_files/200px-RaiderOld.jpg")
SACRED_GROVE = CardShapedThing("Sacred Grove", {"Action", "Fate"}, Cost(coins=5), "+1 Buy+$3Receive a Boon. If it doesn't give +$1, each other player may receive it.", "https://wiki.dominionstrategy.com/index.php/Sacred_Grove", "./list_of_cards_files/200px-Sacred_Grove.jpg")
SECRET_CAVE = CardShapedThing("Secret Cave", {"Action", "Duration"}, Cost(coins=3), "+1 Card+1 ActionYou may discard 3 cards. If you did, then at the start of your next turn, +$3.Heirloom: Magic Lamp", "https://wiki.dominionstrategy.com/index.php/Secret_Cave", "./list_of_cards_files/200px-Secret_Cave.jpg")
SHEPHERD = CardShapedThing("Shepherd", {"Action"}, Cost(coins=4), "+1 ActionDiscard any number of Victory cards, revealing them. +2 Cards per card discarded.Heirloom: Pasture", "https://wiki.dominionstrategy.com/index.php/Shepherd", "./list_of_cards_files/200px-Shepherd.jpg")
SKULK = CardShapedThing("Skulk", {"Action", "Attack", "Doom"}, Cost(coins=4), "+1 BuyEach other player receives the next Hex.When you gain this, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Skulk", "./list_of_cards_files/200px-Skulk.jpg")
TORMENTOR = CardShapedThing("Tormentor", {"Action", "Attack", "Doom"}, Cost(coins=5), "+$2If you have no other cards in play, gain an Imp. Otherwise, each other player receives the next Hex.", "https://wiki.dominionstrategy.com/index.php/Tormentor", "./list_of_cards_files/200px-Tormentor.jpg")
TRACKER = CardShapedThing("Tracker", {"Action", "Fate"}, Cost(coins=2), "+$1This turn, when you gain a card, you may put it onto your deck. Receive a Boon.Heirloom: Pouch", "https://wiki.dominionstrategy.com/index.php/Tracker", "./list_of_cards_files/200px-Tracker.jpg")
TRAGIC_HERO = CardShapedThing("Tragic Hero", {"Action"}, Cost(coins=5), "+3 Cards+1 BuyIf you have 8 or more cards in hand (after drawing), trash this and gain a Treasure.", "https://wiki.dominionstrategy.com/index.php/Tragic_Hero", "./list_of_cards_files/200px-Tragic_HeroOld.jpg")
VAMPIRE = CardShapedThing("Vampire", {"Night", "Attack", "Doom"}, Cost(coins=5), "Each other player receives the next Hex. Gain a card costing up to $5 other than a Vampire.Exchange this for a Bat.", "https://wiki.dominionstrategy.com/index.php/Vampire", "./list_of_cards_files/200px-VampireOld.jpg")
WEREWOLF = CardShapedThing("Werewolf", {"Action", "Night", "Attack", "Doom"}, Cost(coins=5), "If it's your Night phase, each other player receives the next Hex. Otherwise, +3 Cards.", "https://wiki.dominionstrategy.com/index.php/Werewolf", "./list_of_cards_files/200px-Werewolf.jpg")
BAT = CardShapedThing("Bat", {"Night"}, Cost(coins=2), "Trash up to 2 cards from your hand. If you trashed at least one, exchange this for a Vampire.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Bat", "./list_of_cards_files/200px-Bat.jpg")
CURSED_GOLD = CardShapedThing("Cursed Gold", {"Treasure", "Heirloom"}, Cost(coins=4), "$3Gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Cursed_Gold", "./list_of_cards_files/200px-Cursed_Gold.jpg")
GHOST = CardShapedThing("Ghost", {"Night", "Duration", "Spirit"}, Cost(coins=4), "Reveal cards from your deck until you reveal an Action. Discard the other cards and set aside the Action. At the start of your next turn, play it twice.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Ghost", "./list_of_cards_files/200px-Ghost.jpg")
GOAT = CardShapedThing("Goat", {"Treasure", "Heirloom"}, Cost(coins=2), "$1You may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Goat", "./list_of_cards_files/200px-Goat.jpg")
HAUNTED_MIRROR = CardShapedThing("Haunted Mirror", {"Treasure", "Heirloom"}, Cost(coins=0), "$1When you trash this, you may discard an Action card, to gain a Ghost.", "https://wiki.dominionstrategy.com/index.php/Haunted_Mirror", "./list_of_cards_files/200px-Haunted_Mirror.jpg")
IMP = CardShapedThing("Imp", {"Action", "Spirit"}, Cost(coins=2), "+2 CardsYou may play an Action card from your hand that you don't have a copy of in play.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Imp", "./list_of_cards_files/200px-Imp.jpg")
LUCKY_COIN = CardShapedThing("Lucky Coin", {"Treasure", "Heirloom"}, Cost(coins=4), "$1Gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Lucky_Coin", "./list_of_cards_files/200px-Lucky_Coin.jpg")
MAGIC_LAMP = CardShapedThing("Magic Lamp", {"Treasure", "Heirloom"}, Cost(coins=0), "$1If there are at least 6 cards that you have exactly 1 copy of in play (counting this), trash this. If you did, gain 3 Wishes.", "https://wiki.dominionstrategy.com/index.php/Magic_Lamp", "./list_of_cards_files/200px-Magic_Lamp.jpg")
PASTURE = CardShapedThing("Pasture", {"Treasure", "Victory", "Heirloom"}, Cost(coins=2), "$1Worth 1VP per Estate you have.", "https://wiki.dominionstrategy.com/index.php/Pasture", "./list_of_cards_files/200px-Pasture.jpg")
POUCH = CardShapedThing("Pouch", {"Treasure", "Heirloom"}, Cost(coins=2), "$1+1 Buy", "https://wiki.dominionstrategy.com/index.php/Pouch", "./list_of_cards_files/200px-Pouch.jpg")
WILL_O_WISP = CardShapedThing("Will-o'-Wisp", {"Action", "Spirit"}, Cost(coins=0), "+1 Card+1 ActionReveal the top card of your deck. If it costs $2 or less, put it into your hand.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Will-o%27-Wisp", "./list_of_cards_files/200px-Will-o'-Wisp.jpg")
WISH = CardShapedThing("Wish", {"Action"}, Cost(coins=0), "+1 ActionReturn this to its pile. If you did, gain a card to your hand costing up to $6.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Wish", "./list_of_cards_files/200px-Wish.jpg")
ZOMBIE_APPRENTICE = CardShapedThing("Zombie Apprentice", {"Action", "Zombie"}, Cost(coins=3), "You may trash an Action card from your hand for +3 Cards and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Zombie_Apprentice", "./list_of_cards_files/200px-Zombie_Apprentice.jpg")
ZOMBIE_MASON = CardShapedThing("Zombie Mason", {"Action", "Zombie"}, Cost(coins=3), "Trash the top card of your deck. You may gain a card costing up to $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Zombie_Mason", "./list_of_cards_files/200px-Zombie_Mason.jpg")
ZOMBIE_SPY = CardShapedThing("Zombie Spy", {"Action", "Zombie"}, Cost(coins=3), "+1 Card+1 ActionLook at the top card of your deck. Discard it or put it back.", "https://wiki.dominionstrategy.com/index.php/Zombie_Spy", "./list_of_cards_files/200px-Zombie_Spy.jpg")
THE_EARTHS_GIFT = CardShapedThing("The Earth's Gift", {"Boon"}, Cost(), "You may discard a Treasure to gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/The_Earth%27s_Gift", "./list_of_cards_files/320px-The_Earth's_Gift.jpg")
THE_FIELDS_GIFT = CardShapedThing("The Field's Gift", {"Boon"}, Cost(), "+1 Action+$1(Keep this until Clean-up.)", "https://wiki.dominionstrategy.com/index.php/The_Field%27s_Gift", "./list_of_cards_files/320px-The_Field's_Gift.jpg")
THE_FLAMES_GIFT = CardShapedThing("The Flame's Gift", {"Boon"}, Cost(), "You may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/The_Flame%27s_Gift", "./list_of_cards_files/320px-The_Flame's_Gift.jpg")
THE_FORESTS_GIFT = CardShapedThing("The Forest's Gift", {"Boon"}, Cost(), "+1 Buy+$1(Keep this until Clean-up.)", "https://wiki.dominionstrategy.com/index.php/The_Forest%27s_Gift", "./list_of_cards_files/320px-The_Forest's_Gift.jpg")
THE_MOONS_GIFT = CardShapedThing("The Moon's Gift", {"Boon"}, Cost(), "Look through your discard pile. You may put a card from it onto your deck.", "https://wiki.dominionstrategy.com/index.php/The_Moon%27s_Gift", "./list_of_cards_files/320px-The_Moon's_Gift.jpg")
THE_MOUNTAINS_GIFT = CardShapedThing("The Mountain's Gift", {"Boon"}, Cost(), "Gain a Silver.", "https://wiki.dominionstrategy.com/index.php/The_Mountain%27s_Gift", "./list_of_cards_files/320px-The_Mountain's_Gift.jpg")
THE_RIVERS_GIFT = CardShapedThing("The River's Gift", {"Boon"}, Cost(), "+1 Card at the end of this turn.(Keep this until Clean-up.)", "https://wiki.dominionstrategy.com/index.php/The_River%27s_Gift", "./list_of_cards_files/320px-The_River's_Gift.jpg")
THE_SEAS_GIFT = CardShapedThing("The Sea's Gift", {"Boon"}, Cost(), "+1 Card", "https://wiki.dominionstrategy.com/index.php/The_Sea%27s_Gift", "./list_of_cards_files/320px-The_Sea's_Gift.jpg")
THE_SKYS_GIFT = CardShapedThing("The Sky's Gift", {"Boon"}, Cost(), "You may discard 3 cards to gain a Gold.", "https://wiki.dominionstrategy.com/index.php/The_Sky%27s_Gift", "./list_of_cards_files/320px-The_Sky's_Gift.jpg")
THE_SUNS_GIFT = CardShapedThing("The Sun's Gift", {"Boon"}, Cost(), "Look at the top 4 cards of your deck. Discard any number of them and put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/The_Sun%27s_Gift", "./list_of_cards_files/320px-The_Sun's_Gift.jpg")
THE_SWAMPS_GIFT = CardShapedThing("The Swamp's Gift", {"Boon"}, Cost(), "Gain a Will-o'-Wisp.", "https://wiki.dominionstrategy.com/index.php/The_Swamp%27s_Gift", "./list_of_cards_files/320px-The_Swamp's_Gift.jpg")
THE_WINDS_GIFT = CardShapedThing("The Wind's Gift", {"Boon"}, Cost(), "+2 CardsDiscard 2 cards.", "https://wiki.dominionstrategy.com/index.php/The_Wind%27s_Gift", "./list_of_cards_files/320px-The_Wind's_Gift.jpg")
BAD_OMENS = CardShapedThing("Bad Omens", {"Hex"}, Cost(), "Put your deck into your discard pile. Look through it and put 2 Coppers from it onto your deck (or reveal you can't).", "https://wiki.dominionstrategy.com/index.php/Bad_Omens", "./list_of_cards_files/320px-Bad_Omens.jpg")
DELUSION = CardShapedThing("Delusion", {"Hex"}, Cost(), "If you don't have Deluded or Envious, take Deluded.", "https://wiki.dominionstrategy.com/index.php/Delusion", "./list_of_cards_files/320px-Delusion.jpg")
ENVY = CardShapedThing("Envy", {"Hex"}, Cost(), "If you don't have Deluded or Envious, take Envious.", "https://wiki.dominionstrategy.com/index.php/Envy", "./list_of_cards_files/320px-Envy.jpg")
FAMINE = CardShapedThing("Famine", {"Hex"}, Cost(), "Reveal the top 3 cards of your deck. Discard the Actions. Shuffle the rest into your deck.", "https://wiki.dominionstrategy.com/index.php/Famine", "./list_of_cards_files/320px-Famine.jpg")
FEAR = CardShapedThing("Fear", {"Hex"}, Cost(), "If you have at least 5 cards in hand, discard an Action or Treasure (or reveal you can't).", "https://wiki.dominionstrategy.com/index.php/Fear", "./list_of_cards_files/320px-Fear.jpg")
GREED = CardShapedThing("Greed", {"Hex"}, Cost(), "Gain a Copper onto your deck.", "https://wiki.dominionstrategy.com/index.php/Greed", "./list_of_cards_files/320px-Greed.jpg")
HAUNTING = CardShapedThing("Haunting", {"Hex"}, Cost(), "If you have at least 4 cards in hand, put one of them onto your deck.", "https://wiki.dominionstrategy.com/index.php/Haunting", "./list_of_cards_files/320px-Haunting.jpg")
LOCUSTS = CardShapedThing("Locusts", {"Hex"}, Cost(), "Trash the top card of your deck. If it's Copper or Estate, gain a Curse. Otherwise, gain a cheaper card that shares a type with it.", "https://wiki.dominionstrategy.com/index.php/Locusts", "./list_of_cards_files/320px-Locusts.jpg")
MISERY = CardShapedThing("Misery", {"Hex"}, Cost(), "If this is your first Misery this game, take Miserable. Otherwise, flip it over to Twice Miserable.", "https://wiki.dominionstrategy.com/index.php/Misery", "./list_of_cards_files/320px-Misery.jpg")
PLAGUE = CardShapedThing("Plague", {"Hex"}, Cost(), "Gain a Curse to your hand.", "https://wiki.dominionstrategy.com/index.php/Plague", "./list_of_cards_files/320px-Plague.jpg")
POVERTY = CardShapedThing("Poverty", {"Hex"}, Cost(), "Discard down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Poverty", "./list_of_cards_files/320px-Poverty.jpg")
WAR = CardShapedThing("War", {"Hex"}, Cost(), "Reveal cards from your deck until revealing one costing $3 or $4. Trash it and discard the rest.", "https://wiki.dominionstrategy.com/index.php/War", "./list_of_cards_files/320px-War.jpg")
DELUDED = CardShapedThing("Deluded", {"State"}, Cost(), "At the start of your Buy phase, return this, and you can't buy Actions this turn.", "https://wiki.dominionstrategy.com/index.php/Deluded", "./list_of_cards_files/320px-Deluded.jpg")
ENVIOUS = CardShapedThing("Envious", {"State"}, Cost(), "At the start of your Buy phase, return this, and Silver and Gold make $1 this turn.", "https://wiki.dominionstrategy.com/index.php/Envious", "./list_of_cards_files/320px-Envious.jpg")
LOST_IN_THE_WOODS = CardShapedThing("Lost in the Woods", {"State"}, Cost(), "At the start of your turn, you may discard a card to receive a Boon.", "https://wiki.dominionstrategy.com/index.php/Lost_in_the_Woods", "./list_of_cards_files/320px-Lost_in_the_Woods.jpg")
MISERABLE = CardShapedThing("Miserable", {"State"}, Cost(), "-2VP", "https://wiki.dominionstrategy.com/index.php/Miserable", "./list_of_cards_files/320px-Miserable.jpg")
TWICE_MISERABLE = CardShapedThing("Twice Miserable", {"State"}, Cost(), "-4VP", "https://wiki.dominionstrategy.com/index.php/Twice_Miserable", "./list_of_cards_files/320px-Twice_Miserable.jpg")
ACTING_TROUPE = CardShapedThing("Acting Troupe", {"Action"}, Cost(coins=3), "+4 VillagersTrash this.", "https://wiki.dominionstrategy.com/index.php/Acting_Troupe", "./list_of_cards_files/200px-Acting_Troupe.jpg")
BORDER_GUARD = CardShapedThing("Border Guard", {"Action"}, Cost(coins=2), "+1 ActionReveal the top 2 cards of your deck. Put one into your hand and discard the other. If both were Actions, take the Lantern or Horn.", "https://wiki.dominionstrategy.com/index.php/Border_Guard", "./list_of_cards_files/200px-Border_Guard.jpg")
CARGO_SHIP = CardShapedThing("Cargo Ship", {"Action", "Duration"}, Cost(coins=3), "+$2Once this turn, when you gain a card, you may set it aside face up (on this). At the start of your next turn, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Cargo_Ship", "./list_of_cards_files/200px-Cargo_Ship.jpg")
DUCAT = CardShapedThing("Ducat", {"Treasure"}, Cost(coins=2), "+1 Coffers+1 BuyWhen you gain this, you may trash a Copper from your hand.", "https://wiki.dominionstrategy.com/index.php/Ducat", "./list_of_cards_files/200px-Ducat.jpg")
EXPERIMENT = CardShapedThing("Experiment", {"Action"}, Cost(coins=3), "+2 Cards+1 ActionReturn this to its pile.When you gain this, gain another Experiment (that doesn't come with another).", "https://wiki.dominionstrategy.com/index.php/Experiment", "./list_of_cards_files/200px-Experiment.jpg")
FLAG_BEARER = CardShapedThing("Flag Bearer", {"Action"}, Cost(coins=4), "+$2When you gain or trash this, take the Flag.", "https://wiki.dominionstrategy.com/index.php/Flag_Bearer", "./list_of_cards_files/200px-Flag_Bearer.jpg")
HIDEOUT = CardShapedThing("Hideout", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsTrash a card from your hand. If it's a Victory card, gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Hideout", "./list_of_cards_files/200px-Hideout.jpg")
IMPROVE = CardShapedThing("Improve", {"Action"}, Cost(coins=3), "+$2At the start of Clean-up, you may trash an Action card you would discard from play this turn, to gain a card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Improve", "./list_of_cards_files/200px-Improve.jpg")
INVENTOR = CardShapedThing("Inventor", {"Action"}, Cost(coins=4), "Gain a card costing up to $4, then cards cost $1 less this turn.", "https://wiki.dominionstrategy.com/index.php/Inventor", "./list_of_cards_files/200px-Inventor.jpg")
LACKEYS = CardShapedThing("Lackeys", {"Action"}, Cost(coins=2), "+2 CardsWhen you gain this, +2 Villagers.", "https://wiki.dominionstrategy.com/index.php/Lackeys", "./list_of_cards_files/200px-Lackeys.jpg")
MOUNTAIN_VILLAGE = CardShapedThing("Mountain Village", {"Action"}, Cost(coins=4), "+2 ActionsLook through your discard pile and put a card from it into your hand; if you can't, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Mountain_Village", "./list_of_cards_files/200px-Mountain_Village.jpg")
OLD_WITCH = CardShapedThing("Old Witch", {"Action", "Attack"}, Cost(coins=5), "+3 CardsEach other player gains a Curse and may trash a Curse from their hand.", "https://wiki.dominionstrategy.com/index.php/Old_Witch", "./list_of_cards_files/200px-Old_Witch.jpg")
PATRON = CardShapedThing("Patron", {"Action", "Reaction"}, Cost(coins=4), "+1 Villager+$2When something causes you to reveal this (using the word \"reveal\") in an Action phase, +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Patron", "./list_of_cards_files/200px-Patron.jpg")
PRIEST = CardShapedThing("Priest", {"Action"}, Cost(coins=4), "+$2Trash a card from your hand. For the rest of this turn, when you trash a card, +$2.", "https://wiki.dominionstrategy.com/index.php/Priest", "./list_of_cards_files/200px-Priest.jpg")
RECRUITER = CardShapedThing("Recruiter", {"Action"}, Cost(coins=5), "+2 CardsTrash a card from your hand. +1 Villager per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Recruiter", "./list_of_cards_files/200px-Recruiter.jpg")
RESEARCH = CardShapedThing("Research", {"Action", "Duration"}, Cost(coins=4), "+1 ActionTrash a card from your hand. Per $1 it costs, set aside a card from your deck face down (on this). At the start of your next turn, put those cards into your hand.", "https://wiki.dominionstrategy.com/index.php/Research", "./list_of_cards_files/200px-Research.jpg")
SCEPTER = CardShapedThing("Scepter", {"Treasure", "Command"}, Cost(coins=5), "Choose one: +$2; or replay a non-Command Action card you played this turn that's still in play.", "https://wiki.dominionstrategy.com/index.php/Scepter", "./list_of_cards_files/200px-Scepter.jpg")
SCHOLAR = CardShapedThing("Scholar", {"Action"}, Cost(coins=5), "Discard your hand. +7 Cards.", "https://wiki.dominionstrategy.com/index.php/Scholar", "./list_of_cards_files/200px-Scholar.jpg")
SCULPTOR = CardShapedThing("Sculptor", {"Action"}, Cost(coins=5), "Gain a card to your hand costing up to $4. If it's a Treasure, +1 Villager.", "https://wiki.dominionstrategy.com/index.php/Sculptor", "./list_of_cards_files/200px-Sculptor.jpg")
SEER = CardShapedThing("Seer", {"Action"}, Cost(coins=5), "+1 Card+1 ActionReveal the top 3 cards of your deck. Put the ones costing from $2 to $4 into your hand. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Seer", "./list_of_cards_files/200px-Seer.jpg")
SILK_MERCHANT = CardShapedThing("Silk Merchant", {"Action"}, Cost(coins=4), "+2 Cards+1 BuyWhen you gain or trash this, +1 Coffers and +1 Villager.", "https://wiki.dominionstrategy.com/index.php/Silk_Merchant", "./list_of_cards_files/200px-Silk_Merchant.jpg")
SPICES = CardShapedThing("Spices", {"Treasure"}, Cost(coins=5), "$2+1 BuyWhen you gain this, +2 Coffers.", "https://wiki.dominionstrategy.com/index.php/Spices", "./list_of_cards_files/200px-Spices.jpg")
SWASHBUCKLER = CardShapedThing("Swashbuckler", {"Action"}, Cost(coins=5), "+3 CardsIf your discard pile has any cards in it: +1 Coffers, then if you have at least 4 Coffers tokens, take the Treasure Chest.", "https://wiki.dominionstrategy.com/index.php/Swashbuckler", "./list_of_cards_files/200px-Swashbuckler.jpg")
TREASURER = CardShapedThing("Treasurer", {"Action"}, Cost(coins=5), "+$3Choose one: Trash a Treasure from your hand; or gain a Treasure from the trash to your hand; or take the Key.", "https://wiki.dominionstrategy.com/index.php/Treasurer", "./list_of_cards_files/200px-Treasurer.jpg")
VILLAIN = CardShapedThing("Villain", {"Action", "Attack"}, Cost(coins=5), "+2 CoffersEach other player with 5 or more cards in hand discards one costing $2 or more (or reveals they can't).", "https://wiki.dominionstrategy.com/index.php/Villain", "./list_of_cards_files/200px-Villain.jpg")
ACADEMY = CardShapedThing("Academy", {"Project"}, Cost(coins=5), "When you gain an Action card, +1 Villager.", "https://wiki.dominionstrategy.com/index.php/Academy", "./list_of_cards_files/320px-Academy.jpg")
BARRACKS = CardShapedThing("Barracks", {"Project"}, Cost(coins=6), "At the start of your turn, +1 Action.", "https://wiki.dominionstrategy.com/index.php/Barracks", "./list_of_cards_files/320px-Barracks.jpg")
CANAL = CardShapedThing("Canal", {"Project"}, Cost(coins=7), "During your turns, cards cost $1 less.", "https://wiki.dominionstrategy.com/index.php/Canal", "./list_of_cards_files/320px-Canal.jpg")
CAPITALISM = CardShapedThing("Capitalism", {"Project"}, Cost(coins=5), "During your turns, Actions with +$ amounts in their text are also Treasures.", "https://wiki.dominionstrategy.com/index.php/Capitalism", "./list_of_cards_files/320px-Capitalism.jpg")
CATHEDRAL = CardShapedThing("Cathedral", {"Project"}, Cost(coins=3), "At the start of your turn, trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Cathedral", "./list_of_cards_files/320px-Cathedral.jpg")
CITADEL = CardShapedThing("Citadel", {"Project"}, Cost(coins=8), "The first time you play an Action card during each of your turns, replay it afterwards.", "https://wiki.dominionstrategy.com/index.php/Citadel", "./list_of_cards_files/320px-Citadel.jpg")
CITY_GATE = CardShapedThing("City Gate", {"Project"}, Cost(coins=3), "At the start of your turn, +1 Card, then put a card from your hand onto your deck.", "https://wiki.dominionstrategy.com/index.php/City_Gate", "./list_of_cards_files/320px-City_Gate.jpg")
CROP_ROTATION = CardShapedThing("Crop Rotation", {"Project"}, Cost(coins=6), "At the start of your turn, you may discard a Victory card for +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Crop_Rotation", "./list_of_cards_files/320px-Crop_Rotation.jpg")
EXPLORATION = CardShapedThing("Exploration", {"Project"}, Cost(coins=4), "At the end of your Buy phase, if you didn't gain any cards during it, +1 Coffers and +1 Villager.", "https://wiki.dominionstrategy.com/index.php/Exploration", "./list_of_cards_files/320px-Exploration.jpg")
FAIR = CardShapedThing("Fair", {"Project"}, Cost(coins=4), "At the start of your turn, +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Fair", "./list_of_cards_files/320px-Fair.jpg")
FLEET = CardShapedThing("Fleet", {"Project"}, Cost(coins=5), "After the game ends, there's an extra round of turns just for players with this.", "https://wiki.dominionstrategy.com/index.php/Fleet", "./list_of_cards_files/320px-Fleet.jpg")
GUILDHALL = CardShapedThing("Guildhall", {"Project"}, Cost(coins=5), "When you gain a Treasure, +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Guildhall", "./list_of_cards_files/320px-Guildhall.jpg")
INNOVATION = CardShapedThing("Innovation", {"Project"}, Cost(coins=6), "Once during each of your turns, when you gain an Action card, you may play it.", "https://wiki.dominionstrategy.com/index.php/Innovation", "./list_of_cards_files/320px-Innovation.jpg")
PAGEANT = CardShapedThing("Pageant", {"Project"}, Cost(coins=3), "At the end of your Buy phase, you may pay $1 for +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Pageant", "./list_of_cards_files/320px-Pageant.jpg")
PIAZZA = CardShapedThing("Piazza", {"Project"}, Cost(coins=5), "At the start of your turn, reveal the top card of your deck. If it's an Action, play it.", "https://wiki.dominionstrategy.com/index.php/Piazza", "./list_of_cards_files/320px-Piazza.jpg")
ROAD_NETWORK = CardShapedThing("Road Network", {"Project"}, Cost(coins=5), "When another player gains a Victory card, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Road_Network", "./list_of_cards_files/320px-Road_Network.jpg")
SEWERS = CardShapedThing("Sewers", {"Project"}, Cost(coins=3), "When you trash a card other than with this, you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Sewers", "./list_of_cards_files/320px-Sewers.jpg")
SILOS = CardShapedThing("Silos", {"Project"}, Cost(coins=4), "At the start of your turn, discard any number of Coppers, revealed, and draw that many cards.", "https://wiki.dominionstrategy.com/index.php/Silos", "./list_of_cards_files/320px-Silos.jpg")
SINISTER_PLOT = CardShapedThing("Sinister Plot", {"Project"}, Cost(coins=4), "At the start of your turn, add a token here, or remove your tokens here for +1 Card each.", "https://wiki.dominionstrategy.com/index.php/Sinister_Plot", "./list_of_cards_files/320px-Sinister_Plot.jpg")
STAR_CHART = CardShapedThing("Star Chart", {"Project"}, Cost(coins=3), "When shuffling, you may pick one of the cards to go on top.", "https://wiki.dominionstrategy.com/index.php/Star_Chart", "./list_of_cards_files/320px-Star_Chart.jpg")
FLAG = CardShapedThing("Flag", {"Artifact"}, Cost(), "When drawing your hand, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Flag", "./list_of_cards_files/320px-Flag.jpg")
HORN = CardShapedThing("Horn", {"Artifact"}, Cost(), "Once per turn, when you discard a Border Guard from play, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Horn", "./list_of_cards_files/320px-Horn.jpg")
KEY = CardShapedThing("Key", {"Artifact"}, Cost(), "At the start of your turn, +$1.", "https://wiki.dominionstrategy.com/index.php/Key", "./list_of_cards_files/320px-Key.jpg")
LANTERN = CardShapedThing("Lantern", {"Artifact"}, Cost(), "Border Guards you play reveal 3 cards and discard 2. (It takes all 3 being Actions to take the Horn.)", "https://wiki.dominionstrategy.com/index.php/Lantern", "./list_of_cards_files/320px-Lantern.jpg")
TREASURE_CHEST = CardShapedThing("Treasure Chest", {"Artifact"}, Cost(), "At the start of your Buy phase, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Treasure_Chest", "./list_of_cards_files/320px-Treasure_Chest.jpg")
ANIMAL_FAIR = CardShapedThing("Animal Fair", {"Action"}, Cost(coins=7), "+$4+1 Buy per empty supply pile.Instead of paying this card's cost, you may trash an Action card from your hand.", "https://wiki.dominionstrategy.com/index.php/Animal_Fair", "./list_of_cards_files/200px-Animal_Fair.jpg")
BARGE = CardShapedThing("Barge", {"Action", "Duration"}, Cost(coins=5), "Either now or at the start of your next turn, +3 Cards and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Barge", "./list_of_cards_files/200px-Barge.jpg")
BLACK_CAT = CardShapedThing("Black Cat", {"Action", "Attack", "Reaction"}, Cost(coins=2), "+2 CardsIf it isn't your turn, each other player gains a Curse.When another player gains a Victory card, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Black_Cat", "./list_of_cards_files/200px-Black_Cat.jpg")
BOUNTY_HUNTER = CardShapedThing("Bounty Hunter", {"Action"}, Cost(coins=4), "+1 ActionExile a card from your hand. If you didn't have a copy of it in Exile, +$3.", "https://wiki.dominionstrategy.com/index.php/Bounty_Hunter", "./list_of_cards_files/200px-Bounty_Hunter.jpg")
CAMEL_TRAIN = CardShapedThing("Camel Train", {"Action"}, Cost(coins=3), "Exile a non-Victory card from the Supply.When you gain this, Exile a Gold from the Supply.", "https://wiki.dominionstrategy.com/index.php/Camel_Train", "./list_of_cards_files/200px-Camel_Train.jpg")
CARDINAL = CardShapedThing("Cardinal", {"Action", "Attack"}, Cost(coins=4), "+$2Each other player reveals the top 2 cards of their deck, Exiles one costing from $3 to $6, and discards the rest.", "https://wiki.dominionstrategy.com/index.php/Cardinal", "./list_of_cards_files/200px-Cardinal.jpg")
CAVALRY = CardShapedThing("Cavalry", {"Action"}, Cost(coins=4), "Gain 2 Horses.When you gain this, +2 Cards, +1 Buy, and if it's your Buy phase return to your Action phase.", "https://wiki.dominionstrategy.com/index.php/Cavalry", "./list_of_cards_files/200px-Cavalry.jpg")
COVEN = CardShapedThing("Coven", {"Action", "Attack"}, Cost(coins=5), "+1 Action+$2Each other player Exiles a Curse from the Supply. If they can't, they discard their Exiled Curses.", "https://wiki.dominionstrategy.com/index.php/Coven", "./list_of_cards_files/200px-Coven.jpg")
DESTRIER = CardShapedThing("Destrier", {"Action"}, Cost(coins=6), "+2 Cards+1 ActionDuring your turns, this costs $1 less per card you've gained this turn.", "https://wiki.dominionstrategy.com/index.php/Destrier", "./list_of_cards_files/200px-Destrier.jpg")
DISPLACE = CardShapedThing("Displace", {"Action"}, Cost(coins=5), "Exile a card from your hand. Gain a differently named card costing up to $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Displace", "./list_of_cards_files/200px-Displace.jpg")
FALCONER = CardShapedThing("Falconer", {"Action", "Reaction"}, Cost(coins=5), "Gain a card to your hand costing less than this.When any player gains a card with 2 or more types (Action, Attack, etc.), you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Falconer", "./list_of_cards_files/200px-Falconer.jpg")
FISHERMAN = CardShapedThing("Fisherman", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1During your turns, if your discard pile is empty, this costs $3 less.", "https://wiki.dominionstrategy.com/index.php/Fisherman", "./list_of_cards_files/200px-Fisherman.jpg")
GATEKEEPER = CardShapedThing("Gatekeeper", {"Action", "Duration", "Attack"}, Cost(coins=5), "At the start of your next turn, +$3. Until then, when another player gains an Action or Treasure card they don't have an Exiled copy of, they Exile it.", "https://wiki.dominionstrategy.com/index.php/Gatekeeper", "./list_of_cards_files/200px-Gatekeeper.jpg")
GOATHERD = CardShapedThing("Goatherd", {"Action"}, Cost(coins=3), "+1 ActionYou may trash a card from your hand.+1 Card per card the player to your right trashed on their last turn.", "https://wiki.dominionstrategy.com/index.php/Goatherd", "./list_of_cards_files/200px-Goatherd.jpg")
GROOM = CardShapedThing("Groom", {"Action"}, Cost(coins=4), "Gain a card costing up to $4. If it's an…Action card, gain a Horse;Treasure card, gain a Silver;Victory card, +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Groom", "./list_of_cards_files/200px-Groom.jpg")
HOSTELRY = CardShapedThing("Hostelry", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsWhen you gain this, you may discard any number of Treasures, revealed, to gain that many Horses.", "https://wiki.dominionstrategy.com/index.php/Hostelry", "./list_of_cards_files/200px-Hostelry.jpg")
HUNTING_LODGE = CardShapedThing("Hunting Lodge", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsYou may discard your hand for +5 Cards.", "https://wiki.dominionstrategy.com/index.php/Hunting_Lodge", "./list_of_cards_files/200px-Hunting_Lodge.jpg")
KILN = CardShapedThing("Kiln", {"Action"}, Cost(coins=5), "+$2The next time you play a card this turn, you may first gain a copy of it.", "https://wiki.dominionstrategy.com/index.php/Kiln", "./list_of_cards_files/200px-Kiln.jpg")
LIVERY = CardShapedThing("Livery", {"Action"}, Cost(coins=5), "+$3This turn, when you gain a card costing $4 or more, gain a Horse.", "https://wiki.dominionstrategy.com/index.php/Livery", "./list_of_cards_files/200px-Livery.jpg")
MASTERMIND = CardShapedThing("Mastermind", {"Action", "Duration"}, Cost(coins=5), "At the start of your next turn, you may play an Action card from your hand three times.", "https://wiki.dominionstrategy.com/index.php/Mastermind", "./list_of_cards_files/200px-Mastermind.jpg")
PADDOCK = CardShapedThing("Paddock", {"Action"}, Cost(coins=5), "+$2Gain 2 Horses.+1 Action per empty Supply pile.", "https://wiki.dominionstrategy.com/index.php/Paddock", "./list_of_cards_files/200px-Paddock.jpg")
SANCTUARY = CardShapedThing("Sanctuary", {"Action"}, Cost(coins=5), "+1 Card+1 Action+1 BuyYou may Exile a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Sanctuary", "./list_of_cards_files/200px-Sanctuary.jpg")
SCRAP = CardShapedThing("Scrap", {"Action"}, Cost(coins=3), "Trash a card from your hand. Choose a different thing per $1 it costs: +1 Card; +1 Action; +1 Buy; +$1; gain a Silver; gain a Horse.", "https://wiki.dominionstrategy.com/index.php/Scrap", "./list_of_cards_files/200px-Scrap.jpg")
SHEEPDOG = CardShapedThing("Sheepdog", {"Action", "Reaction"}, Cost(coins=3), "+2 CardsWhen you gain a card, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Sheepdog", "./list_of_cards_files/200px-Sheepdog.jpg")
SLEIGH = CardShapedThing("Sleigh", {"Action", "Reaction"}, Cost(coins=2), "Gain 2 Horses.When you gain a card, you may discard this, to put that card into your hand or onto your deck.", "https://wiki.dominionstrategy.com/index.php/Sleigh", "./list_of_cards_files/200px-Sleigh.jpg")
SNOWY_VILLAGE = CardShapedThing("Snowy Village", {"Action"}, Cost(coins=3), "+1 Card+4 Actions+1 BuyIgnore any further +Actions you get this turn.", "https://wiki.dominionstrategy.com/index.php/Snowy_Village", "./list_of_cards_files/200px-Snowy_Village.jpg")
STOCKPILE = CardShapedThing("Stockpile", {"Treasure"}, Cost(coins=3), "$3+1 BuyExile this.", "https://wiki.dominionstrategy.com/index.php/Stockpile", "./list_of_cards_files/200px-Stockpile.jpg")
SUPPLIES = CardShapedThing("Supplies", {"Treasure"}, Cost(coins=2), "$1Gain a Horse onto your deck.", "https://wiki.dominionstrategy.com/index.php/Supplies", "./list_of_cards_files/200px-Supplies.jpg")
VILLAGE_GREEN = CardShapedThing("Village Green", {"Action", "Duration", "Reaction"}, Cost(coins=4), "Either now or at the start of your next turn, +1 Card and +2 Actions.When you discard this other than during Clean-up, you may play it.", "https://wiki.dominionstrategy.com/index.php/Village_Green", "./list_of_cards_files/200px-Village_GreenOld.jpg")
WAYFARER = CardShapedThing("Wayfarer", {"Action"}, Cost(coins=6), "+3 CardsYou may gain a Silver.This has the same cost as the last other card gained this turn, if any.", "https://wiki.dominionstrategy.com/index.php/Wayfarer", "./list_of_cards_files/200px-Wayfarer.jpg")
HORSE = CardShapedThing("Horse", {"Action"}, Cost(coins=3), "+2 Cards+1 ActionReturn this to its pile.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Horse", "./list_of_cards_files/200px-Horse.jpg")
ALLIANCE = CardShapedThing("Alliance", {"Event"}, Cost(coins=10), "Gain a Province, a Duchy, an Estate, a Gold, a Silver, and a Copper.", "https://wiki.dominionstrategy.com/index.php/Alliance", "./list_of_cards_files/320px-Alliance.jpg")
BANISH = CardShapedThing("Banish", {"Event"}, Cost(coins=4), "Exile any number of cards with the same name from your hand.", "https://wiki.dominionstrategy.com/index.php/Banish", "./list_of_cards_files/320px-Banish.jpg")
BARGAIN = CardShapedThing("Bargain", {"Event"}, Cost(coins=4), "Gain a non-Victory card costing up to $5. Each other player gains a Horse.", "https://wiki.dominionstrategy.com/index.php/Bargain", "./list_of_cards_files/320px-Bargain.jpg")
COMMERCE = CardShapedThing("Commerce", {"Event"}, Cost(coins=5), "Gain a Gold per differently named card you've gained this turn.", "https://wiki.dominionstrategy.com/index.php/Commerce", "./list_of_cards_files/320px-Commerce.jpg")
DELAY = CardShapedThing("Delay", {"Event"}, Cost(coins=0), "You may set aside an Action card from your hand. At the start of your next turn, play it.", "https://wiki.dominionstrategy.com/index.php/Delay", "./list_of_cards_files/320px-Delay.jpg")
DEMAND = CardShapedThing("Demand", {"Event"}, Cost(coins=5), "Gain a Horse and a card costing up to $4, both onto your deck.", "https://wiki.dominionstrategy.com/index.php/Demand", "./list_of_cards_files/320px-Demand.jpg")
DESPERATION = CardShapedThing("Desperation", {"Event"}, Cost(coins=0), "Once per turn: You may gain a Curse. If you do, +1 Buy and +$2.", "https://wiki.dominionstrategy.com/index.php/Desperation", "./list_of_cards_files/320px-Desperation.jpg")
ENCLAVE = CardShapedThing("Enclave", {"Event"}, Cost(coins=8), "Gain a Gold. Exile a Duchy from the Supply.", "https://wiki.dominionstrategy.com/index.php/Enclave", "./list_of_cards_files/320px-Enclave.jpg")
ENHANCE = CardShapedThing("Enhance", {"Event"}, Cost(coins=3), "You may trash a non-Victory card from your hand, to gain a card costing up to $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Enhance", "./list_of_cards_files/320px-Enhance.jpg")
GAMBLE = CardShapedThing("Gamble", {"Event"}, Cost(coins=2), "+1 BuyDiscard the top card of your deck. If it's an Action or Treasure, you may play it.", "https://wiki.dominionstrategy.com/index.php/Gamble", "./list_of_cards_files/320px-Gamble.jpg")
INVEST = CardShapedThing("Invest", {"Event"}, Cost(coins=4), "Exile an Action card from the Supply. While it's in Exile, when another player gains or Invests in a copy of it, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Invest", "./list_of_cards_files/320px-Invest.jpg")
MARCH = CardShapedThing("March", {"Event"}, Cost(coins=3), "Look through your discard pile. You may play an Action card from it.", "https://wiki.dominionstrategy.com/index.php/March", "./list_of_cards_files/320px-March.jpg")
POPULATE = CardShapedThing("Populate", {"Event"}, Cost(coins=10), "Gain one card from each Action Supply pile.", "https://wiki.dominionstrategy.com/index.php/Populate", "./list_of_cards_files/320px-Populate.jpg")
PURSUE = CardShapedThing("Pursue", {"Event"}, Cost(coins=2), "+1 BuyName a card.  Reveal the top 4 cards from your deck.  Put the matches back and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Pursue", "./list_of_cards_files/320px-Pursue.jpg")
REAP = CardShapedThing("Reap", {"Event"}, Cost(coins=7), "Gain a Gold, setting it aside. At the start of your next turn, play it.", "https://wiki.dominionstrategy.com/index.php/Reap", "./list_of_cards_files/320px-Reap.jpg")
RIDE = CardShapedThing("Ride", {"Event"}, Cost(coins=2), "Gain a Horse.", "https://wiki.dominionstrategy.com/index.php/Ride", "./list_of_cards_files/320px-Ride.jpg")
SEIZE_THE_DAY = CardShapedThing("Seize the Day", {"Event"}, Cost(coins=4), "Once per game: Take an extra turn after this one.", "https://wiki.dominionstrategy.com/index.php/Seize_the_Day", "./list_of_cards_files/320px-Seize_the_Day.jpg")
STAMPEDE = CardShapedThing("Stampede", {"Event"}, Cost(coins=5), "If you have 5 or fewer cards in play, gain 5 Horses onto your deck.", "https://wiki.dominionstrategy.com/index.php/Stampede", "./list_of_cards_files/320px-Stampede.jpg")
TOIL = CardShapedThing("Toil", {"Event"}, Cost(coins=2), "+1 BuyYou may play an Action card from your hand.", "https://wiki.dominionstrategy.com/index.php/Toil", "./list_of_cards_files/320px-Toil.jpg")
TRANSPORT = CardShapedThing("Transport", {"Event"}, Cost(coins=3), "Choose one: Exile an Action card from the Supply; or put an Action card you have in Exile onto your deck.", "https://wiki.dominionstrategy.com/index.php/Transport", "./list_of_cards_files/320px-Transport.jpg")
WAY_OF_THE_BUTTERFLY = CardShapedThing("Way of the Butterfly", {"Way"}, Cost(), "You may return this to its pile to gain a card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Butterfly", "./list_of_cards_files/320px-Way_of_the_Butterfly.jpg")
WAY_OF_THE_CAMEL = CardShapedThing("Way of the Camel", {"Way"}, Cost(), "Exile a Gold from the Supply.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Camel", "./list_of_cards_files/320px-Way_of_the_Camel.jpg")
WAY_OF_THE_CHAMELEON = CardShapedThing("Way of the Chameleon", {"Way"}, Cost(), "Follow this card's instructions; each time that would give you +Cards this turn, you get +$ instead, and vice-versa.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Chameleon", "./list_of_cards_files/320px-Way_of_the_Chameleon.jpg")
WAY_OF_THE_FROG = CardShapedThing("Way of the Frog", {"Way"}, Cost(), "+1 ActionWhen you discard this from play this turn, put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Frog", "./list_of_cards_files/320px-Way_of_the_Frog.jpg")
WAY_OF_THE_GOAT = CardShapedThing("Way of the Goat", {"Way"}, Cost(), "Trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Goat", "./list_of_cards_files/320px-Way_of_the_Goat.jpg")
WAY_OF_THE_HORSE = CardShapedThing("Way of the Horse", {"Way"}, Cost(), "+2 Cards+1 ActionReturn this to its pile.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Horse", "./list_of_cards_files/320px-Way_of_the_Horse.jpg")
WAY_OF_THE_MOLE = CardShapedThing("Way of the Mole", {"Way"}, Cost(), "+1 ActionDiscard your hand. +3 Cards.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Mole", "./list_of_cards_files/320px-Way_of_the_Mole.jpg")
WAY_OF_THE_MONKEY = CardShapedThing("Way of the Monkey", {"Way"}, Cost(), "+1 Buy+$1", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Monkey", "./list_of_cards_files/320px-Way_of_the_Monkey.jpg")
WAY_OF_THE_MOUSE = CardShapedThing("Way of the Mouse", {"Way"}, Cost(), "Play the set-aside card, leaving it there.Setup: Set aside an unused non-Duration Action costing $2 or $3.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Mouse", "./list_of_cards_files/320px-Way_of_the_Mouse.jpg")
WAY_OF_THE_MULE = CardShapedThing("Way of the Mule", {"Way"}, Cost(), "+1 Action+$1", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Mule", "./list_of_cards_files/320px-Way_of_the_Mule.jpg")
WAY_OF_THE_OTTER = CardShapedThing("Way of the Otter", {"Way"}, Cost(), "+2 Cards", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Otter", "./list_of_cards_files/320px-Way_of_the_Otter.jpg")
WAY_OF_THE_OX = CardShapedThing("Way of the Ox", {"Way"}, Cost(), "+2 Actions", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Ox", "./list_of_cards_files/320px-Way_of_the_Ox.jpg")
WAY_OF_THE_OWL = CardShapedThing("Way of the Owl", {"Way"}, Cost(), "Draw until you have 6 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Owl", "./list_of_cards_files/320px-Way_of_the_Owl.jpg")
WAY_OF_THE_PIG = CardShapedThing("Way of the Pig", {"Way"}, Cost(), "+1 Card+1 Action", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Pig", "./list_of_cards_files/320px-Way_of_the_Pig.jpg")
WAY_OF_THE_RAT = CardShapedThing("Way of the Rat", {"Way"}, Cost(), "You may discard a Treasure to gain a copy of this.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Rat", "./list_of_cards_files/320px-Way_of_the_Rat.jpg")
WAY_OF_THE_SEAL = CardShapedThing("Way of the Seal", {"Way"}, Cost(), "+$1This turn, when you gain a card, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Seal", "./list_of_cards_files/320px-Way_of_the_Seal.jpg")
WAY_OF_THE_SHEEP = CardShapedThing("Way of the Sheep", {"Way"}, Cost(), "+$2", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Sheep", "./list_of_cards_files/320px-Way_of_the_Sheep.jpg")
WAY_OF_THE_SQUIRREL = CardShapedThing("Way of the Squirrel", {"Way"}, Cost(), "+2 Cards at the end of this turn.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Squirrel", "./list_of_cards_files/320px-Way_of_the_Squirrel.jpg")
WAY_OF_THE_TURTLE = CardShapedThing("Way of the Turtle", {"Way"}, Cost(), "Set this aside. If you did, play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Turtle", "./list_of_cards_files/320px-Way_of_the_Turtle.jpg")
WAY_OF_THE_WORM = CardShapedThing("Way of the Worm", {"Way"}, Cost(), "Exile an Estate from the Supply.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Worm", "./list_of_cards_files/320px-Way_of_the_Worm.jpg")
ACOLYTE = CardShapedThing("Acolyte", {"Action", "Augur"}, Cost(coins=4), "You may trash an Action or Victory card from your hand to gain a Gold.You may trash this to gain an Augur.", "https://wiki.dominionstrategy.com/index.php/Acolyte", "./list_of_cards_files/200px-Acolyte.jpg")
ARCHER = CardShapedThing("Archer", {"Action", "Attack", "Clash"}, Cost(coins=4), "+$2Each other player with 5 or more cards in hand reveals all but one, and discards one of those you choose.", "https://wiki.dominionstrategy.com/index.php/Archer", "./list_of_cards_files/200px-Archer.jpg")
BARBARIAN = CardShapedThing("Barbarian", {"Action", "Attack"}, Cost(coins=5), "+$2Each other player trashes the top card of their deck. If it costs $3 or more they gain a cheaper card sharing a type with it; otherwise they gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Barbarian", "./list_of_cards_files/200px-Barbarian.jpg")
BATTLE_PLAN = CardShapedThing("Battle Plan", {"Action", "Clash"}, Cost(coins=3), "+1 Card+1 ActionYou may reveal an Attack card from your hand for +1 Card.You may rotate any Supply pile.", "https://wiki.dominionstrategy.com/index.php/Battle_Plan", "./list_of_cards_files/200px-Battle_Plan.jpg")
BAUBLE = CardShapedThing("Bauble", {"Treasure", "Liaison"}, Cost(coins=2), "Choose two different options: +1 Buy; +$1; +1 Favor; this turn, when you gain a card, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Bauble", "./list_of_cards_files/200px-Bauble.jpg")
BLACKSMITH = CardShapedThing("Blacksmith", {"Action", "Townsfolk"}, Cost(coins=3), "Choose one: Draw until you have 6 cards in hand; or +2 Cards; or +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Blacksmith", "./list_of_cards_files/200px-Blacksmith.jpg")
BROKER = CardShapedThing("Broker", {"Action", "Liaison"}, Cost(coins=4), "Trash a card from your hand and choose one:+1 Card per $1 it costs;or +1 Action per $1 it costs; or +$1 per $1 it costs; or +1 Favor per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Broker", "./list_of_cards_files/200px-Broker.jpg")
CAPITAL_CITY = CardShapedThing("Capital City", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsYou may discard 2 cards for +$2.You may pay $2 for +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Capital_City", "./list_of_cards_files/200px-Capital_City.jpg")
CARPENTER = CardShapedThing("Carpenter", {"Action"}, Cost(coins=4), "If no Supply piles are empty, +1 Action and gain a card costing up to $4.Otherwise, trash a card from your hand and gain a card costing up to $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Carpenter", "./list_of_cards_files/200px-Carpenter.jpg")
CONJURER = CardShapedThing("Conjurer", {"Action", "Duration", "Wizard"}, Cost(coins=4), "Gain a card costing up to $4.At the start of your next turn, put this into your hand.", "https://wiki.dominionstrategy.com/index.php/Conjurer", "./list_of_cards_files/200px-Conjurer.jpg")
CONTRACT = CardShapedThing("Contract", {"Treasure", "Duration", "Liaison"}, Cost(coins=5), "$2+1 FavorYou may set aside an Action from your hand to play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Contract", "./list_of_cards_files/200px-Contract.jpg")
COURIER = CardShapedThing("Courier", {"Action"}, Cost(coins=4), "+$1Discard the top card of your deck. Look through your discard pile; you may play an Action or Treasure from it.", "https://wiki.dominionstrategy.com/index.php/Courier", "./list_of_cards_files/200px-Courier.jpg")
DISTANT_SHORE = CardShapedThing("Distant Shore", {"Action", "Victory", "Odyssey"}, Cost(coins=6), "+2 Cards+1 ActionGain an Estate.2VP", "https://wiki.dominionstrategy.com/index.php/Distant_Shore", "./list_of_cards_files/200px-Distant_Shore.jpg")
ELDER = CardShapedThing("Elder", {"Action", "Townsfolk"}, Cost(coins=5), "+$2You may play an Action card from your hand. When it gives you a choice of abilities (with \"choose\") this turn, you may choose an extra (different) option.", "https://wiki.dominionstrategy.com/index.php/Elder", "./list_of_cards_files/200px-Elder.jpg")
EMISSARY = CardShapedThing("Emissary", {"Action", "Liaison"}, Cost(coins=5), "+3 CardsIf this made you shuffle (at least one card), +1 Action and +2 Favors.", "https://wiki.dominionstrategy.com/index.php/Emissary", "./list_of_cards_files/200px-Emissary.jpg")
GALLERIA = CardShapedThing("Galleria", {"Action"}, Cost(coins=5), "+$3This turn, when you gain a card costing $3 or $4, +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Galleria", "./list_of_cards_files/200px-Galleria.jpg")
GARRISON = CardShapedThing("Garrison", {"Action", "Duration", "Fort"}, Cost(coins=4), "+$2This turn, when you gain a card, add a token here. At the start of your next turn, remove them for +1 Card each.", "https://wiki.dominionstrategy.com/index.php/Garrison", "./list_of_cards_files/200px-Garrison.jpg")
GUILDMASTER = CardShapedThing("Guildmaster", {"Action", "Liaison"}, Cost(coins=5), "+$3This turn, when you gain a card, +1 Favor.", "https://wiki.dominionstrategy.com/index.php/Guildmaster", "./list_of_cards_files/200px-Guildmaster.jpg")
HERB_GATHERER = CardShapedThing("Herb Gatherer", {"Action", "Augur"}, Cost(coins=3), "+1 BuyPut your deck into your discard pile. Look through it and you may play a Treasure from it.You may rotate the Augurs.", "https://wiki.dominionstrategy.com/index.php/Herb_Gatherer", "./list_of_cards_files/200px-Herb_Gatherer.jpg")
HIGHWAYMAN = CardShapedThing("Highwayman", {"Action", "Duration", "Attack"}, Cost(coins=5), "At the start of your next turn, discard this from play and +3 Cards.Until then, the first Treasure each other player plays each turn does nothing.", "https://wiki.dominionstrategy.com/index.php/Highwayman", "./list_of_cards_files/200px-Highwayman.jpg")
HILL_FORT = CardShapedThing("Hill Fort", {"Action", "Fort"}, Cost(coins=5), "Gain a card costing up to $4. Choose one: Put it into your hand; or +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Hill_Fort", "./list_of_cards_files/200px-Hill_Fort.jpg")
HUNTER = CardShapedThing("Hunter", {"Action"}, Cost(coins=5), "+1 ActionReveal the top 3 cards of your deck. From those cards, put an Action, a Treasure, and a Victory card into your hand. Discard the rest.", "https://wiki.dominionstrategy.com/index.php/Hunter", "./list_of_cards_files/200px-Hunter.jpg")
IMPORTER = CardShapedThing("Importer", {"Action", "Duration", "Liaison"}, Cost(coins=3), "At the start of your next turn, gain a card costing up to $5.Setup: Each player gets +4 Favors.", "https://wiki.dominionstrategy.com/index.php/Importer", "./list_of_cards_files/200px-Importer.jpg")
INNKEEPER = CardShapedThing("Innkeeper", {"Action"}, Cost(coins=4), "+1 ActionChoose one: +1 Card; or +3 Cards, then discard 3 cards; or +5 Cards, then discard 6 cards.", "https://wiki.dominionstrategy.com/index.php/Innkeeper", "./list_of_cards_files/200px-Innkeeper.jpg")
LICH = CardShapedThing("Lich", {"Action", "Wizard"}, Cost(coins=6), "+6 Cards+2 ActionsSkip a turn.When you trash this, discard it and gain a cheaper card from the trash.", "https://wiki.dominionstrategy.com/index.php/Lich", "./list_of_cards_files/200px-Lich.jpg")
MARQUIS = CardShapedThing("Marquis", {"Action"}, Cost(coins=6), "+1 Buy+1 Card per card in your hand. Discard down to 10 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Marquis", "./list_of_cards_files/200px-Marquis.jpg")
MERCHANT_CAMP = CardShapedThing("Merchant Camp", {"Action"}, Cost(coins=3), "+2 Actions+$1When you discard this from play, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Merchant_Camp", "./list_of_cards_files/200px-Merchant_Camp.jpg")
MILLER = CardShapedThing("Miller", {"Action", "Townsfolk"}, Cost(coins=4), "+1 ActionLook at the top 4 cards of your deck. Put one into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Miller", "./list_of_cards_files/200px-Miller.jpg")
MODIFY = CardShapedThing("Modify", {"Action"}, Cost(coins=5), "Trash a card from your hand. Choose one: +1 Card and +1 Action; or gain a card costing up to $2 more than the trashed card.", "https://wiki.dominionstrategy.com/index.php/Modify", "./list_of_cards_files/200px-Modify.jpg")
OLD_MAP = CardShapedThing("Old Map", {"Action", "Odyssey"}, Cost(coins=3), "+1 Card+1 ActionDiscard a card. +1 Card.You may rotate the Odysseys.", "https://wiki.dominionstrategy.com/index.php/Old_Map", "./list_of_cards_files/200px-Old_Map.jpg")
ROYAL_GALLEY = CardShapedThing("Royal Galley", {"Action", "Duration"}, Cost(coins=4), "+1 CardYou may play a non-Duration Action card from your hand. Set it aside; if you did, then at the start of your next turn, play it.", "https://wiki.dominionstrategy.com/index.php/Royal_Galley", "./list_of_cards_files/200px-Royal_Galley.jpg")
SENTINEL = CardShapedThing("Sentinel", {"Action"}, Cost(coins=3), "Look at the top 5 cards of your deck. You may trash up to 2 of them. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Sentinel", "./list_of_cards_files/200px-Sentinel.jpg")
SIBYL = CardShapedThing("Sibyl", {"Action", "Augur"}, Cost(coins=6), "+4 Cards+1 ActionPut a card from your hand on top of your deck, and another on the bottom.", "https://wiki.dominionstrategy.com/index.php/Sibyl", "./list_of_cards_files/200px-Sibyl.jpg")
SKIRMISHER = CardShapedThing("Skirmisher", {"Action", "Attack"}, Cost(coins=5), "+1 Card+1 Action+$1This turn, when you gain an Attack card, each other player discards down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Skirmisher", "./list_of_cards_files/200px-Skirmisher.jpg")
SORCERER = CardShapedThing("Sorcerer", {"Action", "Attack", "Wizard"}, Cost(coins=5), "+1 Card+1 ActionEach other player names a card, then reveals the top card of their deck. If wrong, they gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Sorcerer", "./list_of_cards_files/200px-Sorcerer.jpg")
SORCERESS = CardShapedThing("Sorceress", {"Action", "Attack", "Augur"}, Cost(coins=5), "+1 ActionName a card. Reveal the top card of your deck and put it into your hand. If it's the named card, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Sorceress", "./list_of_cards_files/200px-Sorceress.jpg")
SPECIALIST = CardShapedThing("Specialist", {"Action"}, Cost(coins=5), "You may play an Action or Treasure from your hand. Choose one: Play it again; or gain a copy of it.", "https://wiki.dominionstrategy.com/index.php/Specialist", "./list_of_cards_files/200px-Specialist.jpg")
STRONGHOLD = CardShapedThing("Stronghold", {"Action", "Victory", "Duration", "Fort"}, Cost(coins=6), "Choose one: +$3; or at the start of your next turn, +3 Cards.2VP", "https://wiki.dominionstrategy.com/index.php/Stronghold", "./list_of_cards_files/200px-Stronghold.jpg")
STUDENT = CardShapedThing("Student", {"Action", "Wizard", "Liaison"}, Cost(coins=3), "+1 ActionYou may rotate the Wizards.Trash a card from your hand. If it's a Treasure, +1 Favor and put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Student", "./list_of_cards_files/200px-Student.jpg")
SUNKEN_TREASURE = CardShapedThing("Sunken Treasure", {"Treasure", "Odyssey"}, Cost(coins=5), "Gain an Action card you don't have a copy of in play.", "https://wiki.dominionstrategy.com/index.php/Sunken_Treasure", "./list_of_cards_files/200px-Sunken_Treasure.jpg")
SWAP = CardShapedThing("Swap", {"Action"}, Cost(coins=5), "+1 Card+1 ActionYou may return an Action from your hand to its pile, to gain to your hand a different Action costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Swap", "./list_of_cards_files/200px-Swap.jpg")
SYCOPHANT = CardShapedThing("Sycophant", {"Action", "Liaison"}, Cost(coins=2), "+1 ActionDiscard 3 cards. If you discarded at least one, +$3.When you gain or trash this, +2 Favors.", "https://wiki.dominionstrategy.com/index.php/Sycophant", "./list_of_cards_files/200px-Sycophant.jpg")
TENT = CardShapedThing("Tent", {"Action", "Fort"}, Cost(coins=3), "+$2You may rotate the Forts.When you discard this from play, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Tent", "./list_of_cards_files/200px-Tent.jpg")
TERRITORY = CardShapedThing("Territory", {"Victory", "Clash"}, Cost(coins=6), "Worth 1VP per differently named Victory card you have.When you gain this, gain a Gold per empty Supply pile.", "https://wiki.dominionstrategy.com/index.php/Territory", "./list_of_cards_files/200px-Territory.jpg")
TOWN = CardShapedThing("Town", {"Action"}, Cost(coins=4), "Choose one: +1 Card and +2 Actions; or +1 Buy and +$2.", "https://wiki.dominionstrategy.com/index.php/Town", "./list_of_cards_files/200px-Town.jpg")
TOWN_CRIER = CardShapedThing("Town Crier", {"Action", "Townsfolk"}, Cost(coins=2), "Choose one: +$2; or gain a Silver; or +1 Card and +1 Action.You may rotate the Townsfolk.", "https://wiki.dominionstrategy.com/index.php/Town_Crier", "./list_of_cards_files/200px-Town_Crier.jpg")
UNDERLING = CardShapedThing("Underling", {"Action", "Liaison"}, Cost(coins=3), "+1 Card+1 Action+1 Favor", "https://wiki.dominionstrategy.com/index.php/Underling", "./list_of_cards_files/200px-Underling.jpg")
VOYAGE = CardShapedThing("Voyage", {"Action", "Duration", "Odyssey"}, Cost(coins=4), "+1 ActionTake an extra turn after this one (but not a 3rd turn in a row), during which you can only play 3 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Voyage", "./list_of_cards_files/200px-Voyage.jpg")
WARLORD = CardShapedThing("Warlord", {"Action", "Duration", "Attack", "Clash"}, Cost(coins=5), "+1 ActionAt the start of your next turn, +2 Cards. Until then, other players can't play an Action from their hand that they have 2 or more copies of in play.", "https://wiki.dominionstrategy.com/index.php/Warlord", "./list_of_cards_files/200px-Warlord.jpg")
ARCHITECTS_GUILD = CardShapedThing("Architects' Guild", {"Ally"}, Cost(), "When you gain a card, you may spend 2 Favors to gain a cheaper non-Victory card.", "https://wiki.dominionstrategy.com/index.php/Architects%27_Guild", "./list_of_cards_files/320px-Architects'_Guild.jpg")
BAND_OF_NOMADS = CardShapedThing("Band of Nomads", {"Ally"}, Cost(), "When you gain a card costing $3 or more, you may spend a Favor, for +1 Card, or +1 Action, or +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Band_of_Nomads", "./list_of_cards_files/320px-Band_of_Nomads.jpg")
CAVE_DWELLERS = CardShapedThing("Cave Dwellers", {"Ally"}, Cost(), "At the start of your turn, you may spend a Favor, to discard a card then draw a card. Repeat as desired.", "https://wiki.dominionstrategy.com/index.php/Cave_Dwellers", "./list_of_cards_files/320px-Cave_Dwellers.jpg")
CIRCLE_OF_WITCHES = CardShapedThing("Circle of Witches", {"Ally"}, Cost(), "After playing a Liaison, you may spend 3 Favors to have each other player gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Circle_of_Witches", "./list_of_cards_files/320px-Circle_of_Witches.jpg")
CITY_STATE = CardShapedThing("City-state", {"Ally"}, Cost(), "When you gain an Action card during your turn, you may spend 2 Favors to play it.", "https://wiki.dominionstrategy.com/index.php/City-state", "./list_of_cards_files/320px-City-state.jpg")
COASTAL_HAVEN = CardShapedThing("Coastal Haven", {"Ally"}, Cost(), "When discarding your hand in Clean-up, you may spend any number of Favors to keep that many cards in hand for next turn (you still draw 5).", "https://wiki.dominionstrategy.com/index.php/Coastal_Haven", "./list_of_cards_files/320px-Coastal_Haven.jpg")
CRAFTERS_GUILD = CardShapedThing("Crafters' Guild", {"Ally"}, Cost(), "At the start of your turn, you may spend 2 Favors to gain a card costing up to $4 onto your deck.", "https://wiki.dominionstrategy.com/index.php/Crafters%27_Guild", "./list_of_cards_files/320px-Crafters'_Guild.jpg")
DESERT_GUIDES = CardShapedThing("Desert Guides", {"Ally"}, Cost(), "At the start of your turn, you may spend a Favor to discard your hand and draw 5 cards. Repeat as desired.", "https://wiki.dominionstrategy.com/index.php/Desert_Guides", "./list_of_cards_files/320px-Desert_Guides.jpg")
FAMILY_OF_INVENTORS = CardShapedThing("Family of Inventors", {"Ally"}, Cost(), "At the start of your Buy phase, you may put a Favor token you have on a non-Victory Supply pile. Cards cost $1 less per Favor token on their piles.", "https://wiki.dominionstrategy.com/index.php/Family_of_Inventors", "./list_of_cards_files/320px-Family_of_Inventors.jpg")
FELLOWSHIP_OF_SCRIBES = CardShapedThing("Fellowship of Scribes", {"Ally"}, Cost(), "After playing an Action, if you have 4 or fewer cards in hand, you may spend a Favor for +1 Card.", "https://wiki.dominionstrategy.com/index.php/Fellowship_of_Scribes", "./list_of_cards_files/320px-Fellowship_of_Scribes.jpg")
FOREST_DWELLERS = CardShapedThing("Forest Dwellers", {"Ally"}, Cost(), "At the start of your turn, you may spend a Favor to look at the top 3 cards of your deck, discard any number and put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Forest_Dwellers", "./list_of_cards_files/320px-Forest_Dwellers.jpg")
GANG_OF_PICKPOCKETS = CardShapedThing("Gang of Pickpockets", {"Ally"}, Cost(), "At the start of your turn, discard down to 4 cards in hand unless you spend a Favor.", "https://wiki.dominionstrategy.com/index.php/Gang_of_Pickpockets", "./list_of_cards_files/320px-Gang_of_Pickpockets.jpg")
ISLAND_FOLK = CardShapedThing("Island Folk", {"Ally"}, Cost(), "At the end of your turn, you may spend 5 Favors to take an extra turn after this one (but not a 3rd turn in a row).", "https://wiki.dominionstrategy.com/index.php/Island_Folk", "./list_of_cards_files/320px-Island_Folk.jpg")
LEAGUE_OF_BANKERS = CardShapedThing("League of Bankers", {"Ally"}, Cost(), "At the start of your Buy phase, +$1 per 4 Favors you have (round down).", "https://wiki.dominionstrategy.com/index.php/League_of_Bankers", "./list_of_cards_files/320px-League_of_Bankers.jpg")
LEAGUE_OF_SHOPKEEPERS = CardShapedThing("League of Shopkeepers", {"Ally"}, Cost(), "After playing a Liaison, if you have 5 or more Favors, +$1, and if 10 or more, +1 Action and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/League_of_Shopkeepers", "./list_of_cards_files/320px-League_of_Shopkeepers.jpg")
MARKET_TOWNS = CardShapedThing("Market Towns", {"Ally"}, Cost(), "At the start of your Buy phase, you may spend a Favor to play an Action card from your hand. Repeat as desired.", "https://wiki.dominionstrategy.com/index.php/Market_Towns", "./list_of_cards_files/320px-Market_Towns.jpg")
MOUNTAIN_FOLK = CardShapedThing("Mountain Folk", {"Ally"}, Cost(), "At the start of your turn, you may spend 5 Favors for +3 Cards.", "https://wiki.dominionstrategy.com/index.php/Mountain_Folk", "./list_of_cards_files/320px-Mountain_Folk.jpg")
ORDER_OF_ASTROLOGERS = CardShapedThing("Order of Astrologers", {"Ally"}, Cost(), "When shuffling, you may pick one card per Favor you spend to go on top.", "https://wiki.dominionstrategy.com/index.php/Order_of_Astrologers", "./list_of_cards_files/320px-Order_of_Astrologers.jpg")
ORDER_OF_MASONS = CardShapedThing("Order of Masons", {"Ally"}, Cost(), "When shuffling, you may pick up to 2 cards per Favor you spend to put into your discard pile.", "https://wiki.dominionstrategy.com/index.php/Order_of_Masons", "./list_of_cards_files/320px-Order_of_Masons.jpg")
PEACEFUL_CULT = CardShapedThing("Peaceful Cult", {"Ally"}, Cost(), "At the start of your Buy phase, you may spend any number of Favors to trash that many cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Peaceful_Cult", "./list_of_cards_files/320px-Peaceful_Cult.jpg")
PLATEAU_SHEPHERDS = CardShapedThing("Plateau Shepherds", {"Ally"}, Cost(), "When scoring, pair up your Favors with cards you have costing $2, for 2VP per pair.", "https://wiki.dominionstrategy.com/index.php/Plateau_Shepherds", "./list_of_cards_files/320px-Plateau_Shepherds.jpg")
TRAPPERS_LODGE = CardShapedThing("Trappers' Lodge", {"Ally"}, Cost(), "When you gain a card, you may spend a Favor to put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Trappers%27_Lodge", "./list_of_cards_files/320px-Trappers'_Lodge.jpg")
WOODWORKERS_GUILD = CardShapedThing("Woodworkers' Guild", {"Ally"}, Cost(), "At the start of your Buy phase, you may spend a Favor to trash an Action card from your hand. If you did, gain an Action card.", "https://wiki.dominionstrategy.com/index.php/Woodworkers%27_Guild", "./list_of_cards_files/320px-Woodworkers'_Guild.jpg")
ABUNDANCE = CardShapedThing("Abundance", {"Treasure", "Duration"}, Cost(coins=4), "The next time you gain an Action card: +1 Buy and +$3.", "https://wiki.dominionstrategy.com/index.php/Abundance", "./list_of_cards_files/200px-Abundance.jpg")
BURIED_TREASURE = CardShapedThing("Buried Treasure", {"Treasure", "Duration"}, Cost(coins=5), "At the start of your next turn, +1 Buy and +$3.When you gain this, play it.", "https://wiki.dominionstrategy.com/index.php/Buried_Treasure", "./list_of_cards_files/200px-Buried_Treasure.jpg")
CABIN_BOY = CardShapedThing("Cabin Boy", {"Action", "Duration"}, Cost(coins=4), "+1 Card+1 ActionAt the start of your next turn, choose one: +$2; or trash this to gain a Duration card.", "https://wiki.dominionstrategy.com/index.php/Cabin_Boy", "./list_of_cards_files/200px-Cabin_Boy.jpg")
CAGE = CardShapedThing("Cage", {"Treasure", "Duration"}, Cost(coins=2), "Set aside up to 4 cards from your hand face down (on this). The next time you gain a Victory card, trash this, and put the set aside cards into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Cage", "./list_of_cards_files/200px-Cage.jpg")
CREW = CardShapedThing("Crew", {"Action", "Duration"}, Cost(coins=5), "+3 CardsAt the start of your next turn, put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Crew", "./list_of_cards_files/200px-Crew.jpg")
CRUCIBLE = CardShapedThing("Crucible", {"Treasure"}, Cost(coins=4), "Trash a card from your hand. +$1 per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Crucible", "./list_of_cards_files/200px-Crucible.jpg")
CUTTHROAT = CardShapedThing("Cutthroat", {"Action", "Duration", "Attack"}, Cost(coins=5), "Each other player discards down to 3 cards in hand.The next time anyone gains a Treasure costing $5 or more, gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Cutthroat", "./list_of_cards_files/200px-Cutthroat.jpg")
ENLARGE = CardShapedThing("Enlarge", {"Action", "Duration"}, Cost(coins=5), "Now and at the start of your next turn: Trash a card from your hand, and gain one costing up to $2 more.", "https://wiki.dominionstrategy.com/index.php/Enlarge", "./list_of_cards_files/200px-Enlarge.jpg")
FIGURINE = CardShapedThing("Figurine", {"Treasure"}, Cost(coins=5), "+2 CardsYou may discard an Action card for +1 Buy and +$1.", "https://wiki.dominionstrategy.com/index.php/Figurine", "./list_of_cards_files/200px-Figurine.jpg")
FIRST_MATE = CardShapedThing("First Mate", {"Action"}, Cost(coins=5), "Play any number of Action cards with the same name from your hand, then draw until you have 6 cards in hand.", "https://wiki.dominionstrategy.com/index.php/First_Mate", "./list_of_cards_files/200px-First_Mate.jpg")
FLAGSHIP = CardShapedThing("Flagship", {"Action", "Duration", "Command"}, Cost(coins=4), "+$2The next time you play a non-Command Action card, replay it.", "https://wiki.dominionstrategy.com/index.php/Flagship", "./list_of_cards_files/200px-Flagship.jpg")
FORTUNE_HUNTER = CardShapedThing("Fortune Hunter", {"Action"}, Cost(coins=4), "+$2Look at the top 3 cards of your deck. You may play a Treasure from them. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Fortune_Hunter", "./list_of_cards_files/200px-Fortune_Hunter.jpg")
FRIGATE = CardShapedThing("Frigate", {"Action", "Duration", "Attack"}, Cost(coins=5), "+$3Until the start of your next turn, each time another player plays an Action card, they discard down to 4 cards in hand afterwards.", "https://wiki.dominionstrategy.com/index.php/Frigate", "./list_of_cards_files/200px-Frigate.jpg")
GONDOLA = CardShapedThing("Gondola", {"Treasure", "Duration"}, Cost(coins=4), "Either now or at the start of your next turn: +$2.When you gain this, you may play an Action card from your hand.", "https://wiki.dominionstrategy.com/index.php/Gondola", "./list_of_cards_files/200px-Gondola.jpg")
GROTTO = CardShapedThing("Grotto", {"Action", "Duration"}, Cost(coins=2), "+1 ActionSet aside up to 4 cards from your hand face down (on this). At the start of your next turn, discard them, then draw as many.", "https://wiki.dominionstrategy.com/index.php/Grotto", "./list_of_cards_files/200px-Grotto.jpg")
HARBOR_VILLAGE = CardShapedThing("Harbor Village", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsAfter the next Action you play this turn, if it gave you +$, +$1.", "https://wiki.dominionstrategy.com/index.php/Harbor_Village", "./list_of_cards_files/200px-Harbor_Village.jpg")
JEWELLED_EGG = CardShapedThing("Jewelled Egg", {"Treasure"}, Cost(coins=2), "$1+1 BuyWhen you trash this, gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Jewelled_Egg", "./list_of_cards_files/200px-Jewelled_Egg.jpg")
KINGS_CACHE = CardShapedThing("King's Cache", {"Treasure"}, Cost(coins=7), "You may play a Treasure from your hand 3 times.", "https://wiki.dominionstrategy.com/index.php/King%27s_Cache", "./list_of_cards_files/200px-King's_Cache.jpg")
LANDING_PARTY = CardShapedThing("Landing Party", {"Action", "Duration"}, Cost(coins=4), "+2 Cards+2 ActionsThe next time the first card you play on a turn is a Treasure, put this onto your deck afterwards.", "https://wiki.dominionstrategy.com/index.php/Landing_Party", "./list_of_cards_files/200px-Landing_Party.jpg")
LONGSHIP = CardShapedThing("Longship", {"Action", "Duration"}, Cost(coins=5), "+2 ActionsAt the start of your next turn, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Longship", "./list_of_cards_files/200px-Longship.jpg")
MAPMAKER = CardShapedThing("Mapmaker", {"Action", "Reaction"}, Cost(coins=4), "Look at the top 4 cards of your deck. Put 2 into your hand and discard the rest.When any player gains a Victory card, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Mapmaker", "./list_of_cards_files/200px-Mapmaker.jpg")
MAROON = CardShapedThing("Maroon", {"Action"}, Cost(coins=4), "Trash a card from your hand. +2 Cards per type it has (Action, Attack, etc.).", "https://wiki.dominionstrategy.com/index.php/Maroon", "./list_of_cards_files/200px-Maroon.jpg")
MINING_ROAD = CardShapedThing("Mining Road", {"Action"}, Cost(coins=5), "+1 Action+1 Buy+$2Once this turn, when you gain a Treasure, you may play it.", "https://wiki.dominionstrategy.com/index.php/Mining_Road", "./list_of_cards_files/200px-Mining_Road.jpg")
PENDANT = CardShapedThing("Pendant", {"Treasure"}, Cost(coins=5), "+$1 per differently named Treasure you have in play.", "https://wiki.dominionstrategy.com/index.php/Pendant", "./list_of_cards_files/200px-Pendant.jpg")
PICKAXE = CardShapedThing("Pickaxe", {"Treasure"}, Cost(coins=5), "$1Trash a card from your hand. If it costs $3 or more, gain a Loot to your hand.", "https://wiki.dominionstrategy.com/index.php/Pickaxe", "./list_of_cards_files/200px-Pickaxe.jpg")
PILGRIM = CardShapedThing("Pilgrim", {"Action"}, Cost(coins=5), "+4 CardsPut a card from your hand onto your deck.", "https://wiki.dominionstrategy.com/index.php/Pilgrim", "./list_of_cards_files/200px-Pilgrim.jpg")
QUARTERMASTER = CardShapedThing("Quartermaster", {"Action", "Duration"}, Cost(coins=5), "At the start of each of your turns for the rest of the game, choose one: Gain a card costing up to $4, setting it aside on this; or put a card from this into your hand.", "https://wiki.dominionstrategy.com/index.php/Quartermaster", "./list_of_cards_files/200px-Quartermaster.jpg")
ROPE = CardShapedThing("Rope", {"Treasure", "Duration"}, Cost(coins=4), "$1+1 BuyAt the start of your next turn, +1 Card and you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Rope", "./list_of_cards_files/200px-Rope.jpg")
SACK_OF_LOOT = CardShapedThing("Sack of Loot", {"Treasure"}, Cost(coins=6), "$1+1 BuyGain a Loot.", "https://wiki.dominionstrategy.com/index.php/Sack_of_Loot", "./list_of_cards_files/200px-Sack_of_Loot.jpg")
SEARCH = CardShapedThing("Search", {"Action", "Duration"}, Cost(coins=2), "+$2The next time a Supply pile empties, trash this and gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Search", "./list_of_cards_files/200px-Search.jpg")
SECLUDED_SHRINE = CardShapedThing("Secluded Shrine", {"Action", "Duration"}, Cost(coins=3), "+$1The next time you gain a Treasure, trash up to 2 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Secluded_Shrine", "./list_of_cards_files/200px-Secluded_Shrine.jpg")
SHAMAN = CardShapedThing("Shaman", {"Action"}, Cost(coins=2), "+1 Action+$1You may trash a card from your hand.In games using this, at the start of your turn, gain a card from the trash costing up to $6.", "https://wiki.dominionstrategy.com/index.php/Shaman", "./list_of_cards_files/200px-Shaman.jpg")
SILVER_MINE = CardShapedThing("Silver Mine", {"Treasure"}, Cost(coins=5), "Gain a Treasure costing less than this to your hand.", "https://wiki.dominionstrategy.com/index.php/Silver_Mine", "./list_of_cards_files/200px-Silver_Mine.jpg")
SIREN = CardShapedThing("Siren", {"Action", "Duration", "Attack"}, Cost(coins=3), "Each other player gains a Curse. At the start of your next turn, draw until you have 8 cards in hand.When you gain this, trash it unless you trash an Action from your hand.", "https://wiki.dominionstrategy.com/index.php/Siren", "./list_of_cards_files/200px-Siren.jpg")
STOWAWAY = CardShapedThing("Stowaway", {"Action", "Duration", "Reaction"}, Cost(coins=3), "At the start of your next turn, +2 Cards.When anyone gains a Duration card, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Stowaway", "./list_of_cards_files/200px-Stowaway.jpg")
SWAMP_SHACKS = CardShapedThing("Swamp Shacks", {"Action"}, Cost(coins=4), "+2 Actions+1 Card per 3 cards you have in play (round down).", "https://wiki.dominionstrategy.com/index.php/Swamp_Shacks", "./list_of_cards_files/200px-Swamp_Shacks.jpg")
TASKMASTER = CardShapedThing("Taskmaster", {"Action", "Duration"}, Cost(coins=3), "+1 Action, +$1, and if you gain a card costing exactly $5 this turn, then at the start of your next turn, repeat this ability.", "https://wiki.dominionstrategy.com/index.php/Taskmaster", "./list_of_cards_files/200px-Taskmaster.jpg")
TOOLS = CardShapedThing("Tools", {"Treasure"}, Cost(coins=4), "Gain a copy of a card anyone has in play.", "https://wiki.dominionstrategy.com/index.php/Tools", "./list_of_cards_files/200px-Tools.jpg")
TRICKSTER = CardShapedThing("Trickster", {"Action", "Attack"}, Cost(coins=5), "Each other player gains a Curse.Once this turn, when you discard a Treasure from play, you may set it aside. Put it in your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Trickster", "./list_of_cards_files/200px-Trickster.jpg")
WEALTHY_VILLAGE = CardShapedThing("Wealthy Village", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsWhen you gain this, if you have at least 3 differently named Treasures in play, gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Wealthy_Village", "./list_of_cards_files/200px-Wealthy_Village.jpg")
AMPHORA = CardShapedThing("Amphora", {"Treasure", "Duration", "Loot"}, Cost(coins=7), "Either now or at the start of your next turn: +1 Buy and +$3.", "https://wiki.dominionstrategy.com/index.php/Amphora", "./list_of_cards_files/200px-Amphora.jpg")
DOUBLOONS = CardShapedThing("Doubloons", {"Treasure", "Loot"}, Cost(coins=7), "$3When you gain this, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Doubloons", "./list_of_cards_files/200px-Doubloons.jpg")
ENDLESS_CHALICE = CardShapedThing("Endless Chalice", {"Treasure", "Duration", "Loot"}, Cost(coins=7), "Now and at the start of each of your turns for the rest of the game:$1+1 Buy", "https://wiki.dominionstrategy.com/index.php/Endless_Chalice", "./list_of_cards_files/200px-Endless_Chalice.jpg")
FIGUREHEAD = CardShapedThing("Figurehead", {"Treasure", "Duration", "Loot"}, Cost(coins=7), "$3At the start of your next turn, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Figurehead", "./list_of_cards_files/200px-Figurehead.jpg")
HAMMER = CardShapedThing("Hammer", {"Treasure", "Loot"}, Cost(coins=7), "$3Gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Hammer", "./list_of_cards_files/200px-Hammer.jpg")
INSIGNIA = CardShapedThing("Insignia", {"Treasure", "Loot"}, Cost(coins=7), "$3This turn, when you gain a card, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Insignia", "./list_of_cards_files/200px-Insignia.jpg")
JEWELS = CardShapedThing("Jewels", {"Treasure", "Duration", "Loot"}, Cost(coins=7), "$3+1 BuyAt the start of your next turn, put this on the bottom of your deck.", "https://wiki.dominionstrategy.com/index.php/Jewels", "./list_of_cards_files/200px-Jewels.jpg")
ORB = CardShapedThing("Orb", {"Treasure", "Loot"}, Cost(coins=7), "Look through your discard pile. Choose one: Play an Action or Treasure from it; or +1 Buy and +$3.", "https://wiki.dominionstrategy.com/index.php/Orb", "./list_of_cards_files/200px-Orb.jpg")
PRIZE_GOAT = CardShapedThing("Prize Goat", {"Treasure", "Loot"}, Cost(coins=7), "$3+1 BuyYou may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Prize_Goat", "./list_of_cards_files/200px-Prize_Goat.jpg")
PUZZLE_BOX = CardShapedThing("Puzzle Box", {"Treasure", "Loot"}, Cost(coins=7), "$3+1 BuyYou may set aside a card from your hand face down. Put it into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Puzzle_Box", "./list_of_cards_files/200px-Puzzle_Box.jpg")
SEXTANT = CardShapedThing("Sextant", {"Treasure", "Loot"}, Cost(coins=7), "$3+1 BuyLook at the top 5 cards of your deck. Discard any number. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Sextant", "./list_of_cards_files/200px-Sextant.jpg")
SHIELD = CardShapedThing("Shield", {"Treasure", "Reaction", "Loot"}, Cost(coins=7), "$3+1 BuyWhen another player plays an Attack, you may first reveal this from your hand to be unaffected.", "https://wiki.dominionstrategy.com/index.php/Shield", "./list_of_cards_files/200px-Shield.jpg")
SPELL_SCROLL = CardShapedThing("Spell Scroll", {"Action", "Treasure", "Loot"}, Cost(coins=7), "Trash this to gain a cheaper card. If it's an Action or Treasure, you may play it.", "https://wiki.dominionstrategy.com/index.php/Spell_Scroll", "./list_of_cards_files/200px-Spell_Scroll.jpg")
STAFF = CardShapedThing("Staff", {"Treasure", "Loot"}, Cost(coins=7), "$3+1 BuyYou may play an Action from your hand.", "https://wiki.dominionstrategy.com/index.php/Staff", "./list_of_cards_files/200px-Staff.jpg")
SWORD = CardShapedThing("Sword", {"Treasure", "Attack", "Loot"}, Cost(coins=7), "$3+1 BuyEach other player discards down to 4 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Sword", "./list_of_cards_files/200px-Sword.jpg")
AVOID = CardShapedThing("Avoid", {"Event"}, Cost(coins=2), "+1 BuyThe next time you shuffle this turn, pick up to 3 of those cards to put into your discard pile.", "https://wiki.dominionstrategy.com/index.php/Avoid", "./list_of_cards_files/320px-Avoid.jpg")
BURY = CardShapedThing("Bury", {"Event"}, Cost(coins=1), "+1 BuyPut any card from your discard pile on the bottom of your deck.", "https://wiki.dominionstrategy.com/index.php/Bury", "./list_of_cards_files/320px-Bury.jpg")
DELIVER = CardShapedThing("Deliver", {"Event"}, Cost(coins=2), "+1 BuyThis turn, each time you gain a card, set it aside, and put it into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Deliver", "./list_of_cards_files/320px-Deliver.jpg")
FORAY = CardShapedThing("Foray", {"Event"}, Cost(coins=3), "Discard 3 cards, revealing them. If they have 3 different names, gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Foray", "./list_of_cards_files/320px-Foray.jpg")
INVASION = CardShapedThing("Invasion", {"Event"}, Cost(coins=10), "You may play an Attack from your hand. Gain a Duchy. Gain an Action onto your deck. Gain a Loot; play it.", "https://wiki.dominionstrategy.com/index.php/Invasion", "./list_of_cards_files/320px-Invasion.jpg")
JOURNEY = CardShapedThing("Journey", {"Event"}, Cost(coins=4), "You don't discard cards from play in Clean-up this turn. Take an extra turn after this one (but not a 3rd turn in a row).", "https://wiki.dominionstrategy.com/index.php/Journey", "./list_of_cards_files/320px-Journey.jpg")
LAUNCH = CardShapedThing("Launch", {"Event"}, Cost(coins=3), "Once per turn: Return to your Action phase. +1 Card, +1 Action, and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Launch", "./list_of_cards_files/320px-Launch.jpg")
LOOTING = CardShapedThing("Looting", {"Event"}, Cost(coins=6), "Gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Looting", "./list_of_cards_files/320px-Looting.jpg")
MAELSTROM = CardShapedThing("Maelstrom", {"Event"}, Cost(coins=4), "Trash 3 cards from your hand. Each other player with 5 or more cards in hand trashes one of them.", "https://wiki.dominionstrategy.com/index.php/Maelstrom", "./list_of_cards_files/320px-Maelstrom.jpg")
MIRROR = CardShapedThing("Mirror", {"Event"}, Cost(coins=3), "+1 BuyThe next time you gain an Action card this turn, gain a copy of it.", "https://wiki.dominionstrategy.com/index.php/Mirror", "./list_of_cards_files/320px-Mirror.jpg")
PERIL = CardShapedThing("Peril", {"Event"}, Cost(coins=2), "You may trash an Action card from your hand to gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Peril", "./list_of_cards_files/320px-Peril.jpg")
PREPARE = CardShapedThing("Prepare", {"Event"}, Cost(coins=3), "Set aside your hand face up. At the start of your next turn, play those Actions and Treasures in any order, then discard the rest.", "https://wiki.dominionstrategy.com/index.php/Prepare", "./list_of_cards_files/320px-Prepare.jpg")
PROSPER = CardShapedThing("Prosper", {"Event"}, Cost(coins=10), "Gain a Loot, plus any number of differently named Treasures.", "https://wiki.dominionstrategy.com/index.php/Prosper", "./list_of_cards_files/320px-Prosper.jpg")
RUSH = CardShapedThing("Rush", {"Event"}, Cost(coins=2), "+1 BuyThe next time you gain an Action card this turn, play it.", "https://wiki.dominionstrategy.com/index.php/Rush", "./list_of_cards_files/320px-Rush.jpg")
SCROUNGE = CardShapedThing("Scrounge", {"Event"}, Cost(coins=3), "Choose one: Trash a card from your hand; or gain an Estate from the trash, and if you did, gain a card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Scrounge", "./list_of_cards_files/320px-Scrounge.jpg")
CHEAP = CardShapedThing("Cheap", {"Trait"}, Cost(), "Cheap cards cost $1 less.", "https://wiki.dominionstrategy.com/index.php/Cheap", "./list_of_cards_files/320px-Cheap.jpg")
CURSED = CardShapedThing("Cursed", {"Trait"}, Cost(), "When you gain a Cursed card, gain a Loot and a Curse.", "https://wiki.dominionstrategy.com/index.php/Cursed", "./list_of_cards_files/320px-Cursed.jpg")
FATED = CardShapedThing("Fated", {"Trait"}, Cost(), "When shuffling, you may look through the cards and reveal Fated cards to put them on the top or bottom.", "https://wiki.dominionstrategy.com/index.php/Fated", "./list_of_cards_files/320px-Fated.jpg")
FAWNING = CardShapedThing("Fawning", {"Trait"}, Cost(), "When you gain a Province, gain a Fawning card.", "https://wiki.dominionstrategy.com/index.php/Fawning", "./list_of_cards_files/320px-Fawning.jpg")
FRIENDLY = CardShapedThing("Friendly", {"Trait"}, Cost(), "At the start of your Clean-up phase, you may discard a Friendly card to gain a Friendly card.", "https://wiki.dominionstrategy.com/index.php/Friendly", "./list_of_cards_files/320px-Friendly.jpg")
HASTY = CardShapedThing("Hasty", {"Trait"}, Cost(), "When you gain a Hasty card, set it aside, and play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Hasty", "./list_of_cards_files/320px-Hasty.jpg")
INHERITED = CardShapedThing("Inherited", {"Trait"}, Cost(), "Setup: You start the game with an Inherited card in place of a starting card you choose.", "https://wiki.dominionstrategy.com/index.php/Inherited", "./list_of_cards_files/320px-Inherited.jpg")
INSPIRING = CardShapedThing("Inspiring", {"Trait"}, Cost(), "After playing an Inspiring card on your turn, you may play an Action from your hand that you don't have a copy of in play.", "https://wiki.dominionstrategy.com/index.php/Inspiring", "./list_of_cards_files/320px-Inspiring.jpg")
NEARBY = CardShapedThing("Nearby", {"Trait"}, Cost(), "When you gain a Nearby card, +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Nearby", "./list_of_cards_files/320px-Nearby.jpg")
PATIENT = CardShapedThing("Patient", {"Trait"}, Cost(), "At the start of your Clean-up phase, you may set aside Patient cards from your hand to play them at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Patient", "./list_of_cards_files/320px-Patient.jpg")
PIOUS = CardShapedThing("Pious", {"Trait"}, Cost(), "When you gain a Pious card, you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Pious", "./list_of_cards_files/320px-Pious.jpg")
RECKLESS = CardShapedThing("Reckless", {"Trait"}, Cost(), "Follow the instructions of played Reckless cards twice. When discarding one from play, return it to its pile.", "https://wiki.dominionstrategy.com/index.php/Reckless", "./list_of_cards_files/320px-Reckless.jpg")
RICH = CardShapedThing("Rich", {"Trait"}, Cost(), "When you gain a Rich card, gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Rich", "./list_of_cards_files/320px-Rich.jpg")
SHY = CardShapedThing("Shy", {"Trait"}, Cost(), "At the start of your turn, you may discard one Shy card for +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Shy", "./list_of_cards_files/320px-Shy.jpg")
TIRELESS = CardShapedThing("Tireless", {"Trait"}, Cost(), "When you discard a Tireless card from play, set it aside, and put it onto your deck at end of turn.", "https://wiki.dominionstrategy.com/index.php/Tireless", "./list_of_cards_files/320px-Tireless.jpg")
ALLEY = CardShapedThing("Alley", {"Action", "Shadow"}, Cost(coins=4), "+1 Card+1 ActionDiscard a card.You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Alley", "./list_of_cards_files/200px-Alley.jpg")
ARISTOCRAT = CardShapedThing("Aristocrat", {"Action"}, Cost(coins=3), "If the number of Aristocrats you have in play is:1 or 5: +3 Actions;2 or 6: +3 Cards;3 or 7: +$3;4 or 8: +3 Buys.", "https://wiki.dominionstrategy.com/index.php/Aristocrat", "./list_of_cards_files/200px-Aristocrat.jpg")
ARTIST = CardShapedThing("Artist", {"Action"}, Cost(debt=8), "+1 Action+1 Card per card you have exactly one copy of in play.", "https://wiki.dominionstrategy.com/index.php/Artist", "./list_of_cards_files/200px-Artist.jpg")
CHANGE = CardShapedThing("Change", {"Action"}, Cost(coins=4), "If you have any D, +$3. Otherwise, trash a card from your hand, and gain a card costing more $ than it. +D equal to the difference in $.", "https://wiki.dominionstrategy.com/index.php/Change", "./list_of_cards_files/200px-Change.jpg")
CRAFTSMAN = CardShapedThing("Craftsman", {"Action"}, Cost(coins=3), "+2DGain a card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Craftsman", "./list_of_cards_files/200px-Craftsman.jpg")
DAIMYO = CardShapedThing("Daimyo", {"Action", "Command"}, Cost(debt=6), "+1 Card+1 ActionThe next time you play a non-Command Action card this turn, replay it afterwards.", "https://wiki.dominionstrategy.com/index.php/Daimyo", "./list_of_cards_files/200px-Daimyo.jpg")
FISHMONGER = CardShapedThing("Fishmonger", {"Action", "Shadow"}, Cost(coins=2), "+1 Buy+$1You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Fishmonger", "./list_of_cards_files/200px-Fishmonger.jpg")
GOLD_MINE = CardShapedThing("Gold Mine", {"Action"}, Cost(coins=5), "+1 Card+1 Action+1 BuyYou may gain a Gold and get +4D.", "https://wiki.dominionstrategy.com/index.php/Gold_Mine", "./list_of_cards_files/200px-Gold_Mine.jpg")
IMPERIAL_ENVOY = CardShapedThing("Imperial Envoy", {"Action"}, Cost(coins=5), "+5 Cards+1 Buy+2D", "https://wiki.dominionstrategy.com/index.php/Imperial_Envoy", "./list_of_cards_files/200px-Imperial_Envoy.jpg")
KITSUNE = CardShapedThing("Kitsune", {"Action", "Attack", "Omen"}, Cost(coins=5), "+1SunChoose two different options: +2 Actions; +$2; each other player gains a Curse; gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Kitsune", "./list_of_cards_files/200px-Kitsune.jpg")
LITTER = CardShapedThing("Litter", {"Action"}, Cost(coins=5), "+2 Cards+2 Actions+1D", "https://wiki.dominionstrategy.com/index.php/Litter", "./list_of_cards_files/200px-Litter.jpg")
MOUNTAIN_SHRINE = CardShapedThing("Mountain Shrine", {"Action", "Omen"}, Cost(debt=5), "+1Sun+$2You may trash a card from your hand. Then if there are any Action cards in the trash, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Mountain_Shrine", "./list_of_cards_files/200px-Mountain_Shrine.jpg")
NINJA = CardShapedThing("Ninja", {"Action", "Attack", "Shadow"}, Cost(coins=4), "+1 CardEach other player discards down to 3 cards in hand.You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Ninja", "./list_of_cards_files/200px-Ninja.jpg")
POET = CardShapedThing("Poet", {"Action", "Omen"}, Cost(coins=4), "+1Sun+1 Card+1 ActionReveal the top card of your deck. If it costs $3 or less, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Poet", "./list_of_cards_files/200px-Poet.jpg")
RICE = CardShapedThing("Rice", {"Treasure"}, Cost(coins=7), "+1 Buy+$1 per different type among cards you have in play.", "https://wiki.dominionstrategy.com/index.php/Rice", "./list_of_cards_files/200px-Rice.jpg")
RICE_BROKER = CardShapedThing("Rice Broker", {"Action"}, Cost(coins=5), "+1 ActionTrash a card from your hand. If it's a Treasure, +2 Cards. If it's an Action, +5 Cards.", "https://wiki.dominionstrategy.com/index.php/Rice_Broker", "./list_of_cards_files/200px-Rice_Broker.jpg")
RIVER_SHRINE = CardShapedThing("River Shrine", {"Action", "Omen"}, Cost(coins=4), "+1SunTrash up to 2 cards from your hand. At the start of Clean-up, if you didn't gain any cards in your Buy phase this turn, gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/River_Shrine", "./list_of_cards_files/200px-River_Shrine.jpg")
RIVERBOAT = CardShapedThing("Riverboat", {"Action", "Duration"}, Cost(coins=3), "At the start of your next turn, play the set aside card, leaving it there.Setup: Set aside an unused non-Duration Action card costing $5.", "https://wiki.dominionstrategy.com/index.php/Riverboat", "./list_of_cards_files/200px-Riverboat.jpg")
RONIN = CardShapedThing("Ronin", {"Action", "Shadow"}, Cost(coins=5), "Draw until you have 7 cards in hand.You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Ronin", "./list_of_cards_files/200px-Ronin.jpg")
ROOT_CELLAR = CardShapedThing("Root Cellar", {"Action"}, Cost(coins=3), "+3 Cards+1 Action+3D", "https://wiki.dominionstrategy.com/index.php/Root_Cellar", "./list_of_cards_files/200px-Root_Cellar.jpg")
RUSTIC_VILLAGE = CardShapedThing("Rustic Village", {"Action", "Omen"}, Cost(coins=4), "+1Sun+1 Card+2 ActionsYou may discard 2 cards for +1 Card.", "https://wiki.dominionstrategy.com/index.php/Rustic_Village", "./list_of_cards_files/200px-Rustic_Village.jpg")
SAMURAI = CardShapedThing("Samurai", {"Action", "Duration", "Attack"}, Cost(coins=6), "Each other player discards down to 3 cards in hand (once).At the start of each of your turns this game, +$1.(This stays in play.)", "https://wiki.dominionstrategy.com/index.php/Samurai", "./list_of_cards_files/200px-Samurai.jpg")
SNAKE_WITCH = CardShapedThing("Snake Witch", {"Action", "Attack"}, Cost(coins=2), "+1 Card+1 ActionIf your hand has no duplicate cards, you may reveal it and return this to its pile, to have each other player gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Snake_Witch", "./list_of_cards_files/200px-Snake_Witch.jpg")
TANUKI = CardShapedThing("Tanuki", {"Action", "Shadow"}, Cost(coins=5), "Trash a card from your hand. Gain a card costing up to $2 more than it.You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Tanuki", "./list_of_cards_files/200px-Tanuki.jpg")
TEA_HOUSE = CardShapedThing("Tea House", {"Action", "Omen"}, Cost(coins=5), "+1Sun+1 Card+1 Action+$2", "https://wiki.dominionstrategy.com/index.php/Tea_House", "./list_of_cards_files/200px-Tea_House.jpg")
AMASS = CardShapedThing("Amass", {"Event"}, Cost(coins=2), "If you have no Action cards in play, gain an Action card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Amass", "./list_of_cards_files/320px-Amass.jpg")
ASCETICISM = CardShapedThing("Asceticism", {"Event"}, Cost(coins=2), "Pay any amount of $ to trash that many cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Asceticism", "./list_of_cards_files/320px-Asceticism.jpg")
CONTINUE = CardShapedThing("Continue", {"Event"}, Cost(debt=8), "Once per turn: Gain a non-Attack Action card costing up to $4. Return to your Action phase and play it. +1 Action and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Continue", "./list_of_cards_files/320px-Continue.jpg")
CREDIT = CardShapedThing("Credit", {"Event"}, Cost(coins=2), "Gain an Action or Treasure costing up to $8. +D equal to its cost.", "https://wiki.dominionstrategy.com/index.php/Credit", "./list_of_cards_files/320px-Credit.jpg")
FORESIGHT = CardShapedThing("Foresight", {"Event"}, Cost(coins=2), "Reveal cards from your deck until revealing an Action. Set it aside and discard the rest. Put it into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Foresight", "./list_of_cards_files/320px-Foresight.jpg")
GATHER = CardShapedThing("Gather", {"Event"}, Cost(coins=7), "Gain a card costing exactly $3, a card costing exactly $4, and a card costing exactly $5.", "https://wiki.dominionstrategy.com/index.php/Gather", "./list_of_cards_files/320px-Gather.jpg")
KINTSUGI = CardShapedThing("Kintsugi", {"Event"}, Cost(coins=3), "Trash a card from your hand. If you've gained a Gold this game, gain a card costing up to $2 more than the trashed card.", "https://wiki.dominionstrategy.com/index.php/Kintsugi", "./list_of_cards_files/320px-Kintsugi.jpg")
PRACTICE = CardShapedThing("Practice", {"Event"}, Cost(coins=3), "You may play an Action card from your hand twice.", "https://wiki.dominionstrategy.com/index.php/Practice", "./list_of_cards_files/320px-Practice.jpg")
RECEIVE_TRIBUTE = CardShapedThing("Receive Tribute", {"Event"}, Cost(coins=5), "If you've gained at least 3 cards this turn, gain up to 3 differently named Action cards you don't have copies of in play.", "https://wiki.dominionstrategy.com/index.php/Receive_Tribute", "./list_of_cards_files/320px-Receive_Tribute.jpg")
SEA_TRADE = CardShapedThing("Sea Trade", {"Event"}, Cost(coins=4), "+1 Card per Action card you have in play. Trash up to that many cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Sea_Trade", "./list_of_cards_files/320px-Sea_Trade.jpg")
APPROACHING_ARMY = CardShapedThing("Approaching Army", {"Prophecy"}, Cost(), "After you play an Attack card, +$1.Setup: Add an Attack kingdom card pile to the Supply.", "https://wiki.dominionstrategy.com/index.php/Approaching_Army", "./list_of_cards_files/320px-Approaching_Army.jpg")
BIDING_TIME = CardShapedThing("Biding Time", {"Prophecy"}, Cost(), "At the start of your Clean-up, set aside your hand face down. At the start of your next turn, put those cards into your hand.", "https://wiki.dominionstrategy.com/index.php/Biding_Time", "./list_of_cards_files/320px-Biding_Time.jpg")
BUREAUCRACY = CardShapedThing("Bureaucracy", {"Prophecy"}, Cost(), "When you gain a card that doesn't cost $0, gain a Copper.", "https://wiki.dominionstrategy.com/index.php/Bureaucracy", "./list_of_cards_files/320px-Bureaucracy.jpg")
DIVINE_WIND = CardShapedThing("Divine Wind", {"Prophecy"}, Cost(), "When you remove the last Sun, remove all Kingdom card piles from the Supply, and set up 10 new random piles.", "https://wiki.dominionstrategy.com/index.php/Divine_Wind", "./list_of_cards_files/320px-Divine_Wind.jpg")
ENLIGHTENMENT = CardShapedThing("Enlightenment", {"Prophecy"}, Cost(), "Treasures are also Actions. When you play a Treasure in an Action phase, instead of following its instructions, +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Enlightenment", "./list_of_cards_files/320px-Enlightenment.jpg")
FLOURISHING_TRADE = CardShapedThing("Flourishing Trade", {"Prophecy"}, Cost(), "Cards cost $1 less. You may use Action plays as Buys.", "https://wiki.dominionstrategy.com/index.php/Flourishing_Trade", "./list_of_cards_files/320px-Flourishing_Trade.jpg")
GOOD_HARVEST = CardShapedThing("Good Harvest", {"Prophecy"}, Cost(), "The first time you play each differently named Treasure each turn, first, +1 Buy and +$1.", "https://wiki.dominionstrategy.com/index.php/Good_Harvest", "./list_of_cards_files/320px-Good_Harvest.jpg")
GREAT_LEADER = CardShapedThing("Great Leader", {"Prophecy"}, Cost(), "After each Action card you play, +1 Action.", "https://wiki.dominionstrategy.com/index.php/Great_Leader", "./list_of_cards_files/320px-Great_Leader.jpg")
GROWTH = CardShapedThing("Growth", {"Prophecy"}, Cost(), "When you gain a Treasure, gain a cheaper card.", "https://wiki.dominionstrategy.com/index.php/Growth", "./list_of_cards_files/320px-Growth.jpg")
HARSH_WINTER = CardShapedThing("Harsh Winter", {"Prophecy"}, Cost(), "When you gain a card on your turn, if there's D on its pile, take it; otherwise put 2D on its pile.", "https://wiki.dominionstrategy.com/index.php/Harsh_Winter", "./list_of_cards_files/320px-Harsh_Winter.jpg")
KIND_EMPEROR = CardShapedThing("Kind Emperor", {"Prophecy"}, Cost(), "At the start of your turn, and when you remove the last Sun: Gain an Action to your hand.", "https://wiki.dominionstrategy.com/index.php/Kind_Emperor", "./list_of_cards_files/320px-Kind_Emperor.jpg")
PANIC = CardShapedThing("Panic", {"Prophecy"}, Cost(), "When you play a Treasure, +2 Buys, and when you discard one from play, return it to its pile.", "https://wiki.dominionstrategy.com/index.php/Panic", "./list_of_cards_files/320px-Panic.jpg")
PROGRESS = CardShapedThing("Progress", {"Prophecy"}, Cost(), "When you gain a card, put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Progress", "./list_of_cards_files/320px-Progress.jpg")
RAPID_EXPANSION = CardShapedThing("Rapid Expansion", {"Prophecy"}, Cost(), "When you gain an Action or Treasure, set it aside, and play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Rapid_Expansion", "./list_of_cards_files/320px-Rapid_Expansion.jpg")
SICKNESS = CardShapedThing("Sickness", {"Prophecy"}, Cost(), "At the start of your turn, choose one: Gain a Curse onto your deck; or discard 3 cards.", "https://wiki.dominionstrategy.com/index.php/Sickness", "./list_of_cards_files/320px-Sickness.jpg")
AVANTO = CardShapedThing("Avanto", {"Action"}, Cost(coins=5), "+3 CardsYou may play a Sauna from your hand.", "https://wiki.dominionstrategy.com/index.php/Avanto", "./list_of_cards_files/200px-Avanto.jpg")
BLACK_MARKET = CardShapedThing("Black Market", {"Action"}, Cost(coins=3), "+$2Reveal the top 3 cards of the Black Market deck. Play any number of Treasures from your hand. You may buy one of the revealed cards. Put the rest on the bottom of the Black Market deck in any order.Setup: Make a Black Market deck out of different unused Kingdom cards.", "https://wiki.dominionstrategy.com/index.php/Black_Market", "./list_of_cards_files/200px-Black_Market.jpg")
CAPTAIN = CardShapedThing("Captain", {"Action", "Duration", "Command"}, Cost(coins=6), "Now and at the start of your next turn: Play a non-Duration, non-Command Action card from the Supply costing up to $4, leaving it there.", "https://wiki.dominionstrategy.com/index.php/Captain", "./list_of_cards_files/200px-Captain.jpg")
CHURCH = CardShapedThing("Church", {"Action", "Duration"}, Cost(coins=3), "+1 ActionSet aside up to 3 cards from your hand face down. At the start of your next turn, put them into your hand, then you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Church", "./list_of_cards_files/200px-Church.jpg")
DISMANTLE = CardShapedThing("Dismantle", {"Action"}, Cost(coins=4), "Trash a card from your hand. If it costs $1 or more, gain a cheaper card and a Gold.", "https://wiki.dominionstrategy.com/index.php/Dismantle", "./list_of_cards_files/200px-Dismantle.jpg")
ENVOY = CardShapedThing("Envoy", {"Action"}, Cost(coins=4), "Reveal the top 5 cards of your deck. The player to your left chooses one. Discard that one and put the rest into your hand.", "https://wiki.dominionstrategy.com/index.php/Envoy", "./list_of_cards_files/200px-Envoy.jpg")
GOVERNOR = CardShapedThing("Governor", {"Action"}, Cost(coins=5), "+1 ActionChoose one; you get the version in parentheses: Each player gets +1 (+3) Cards; or each player gains a Silver (Gold); or each player may trash a card from their hand and gain a card costing exactly $1 ($2) more.", "https://wiki.dominionstrategy.com/index.php/Governor", "./list_of_cards_files/200px-Governor.jpg")
MARCHLAND = CardShapedThing("Marchland", {"Victory"}, Cost(coins=5), "Worth 1VP per 3 Victory cards you have (round down).When you gain this, +1 Buy, and discard any number of cards for +$1 each.", "https://wiki.dominionstrategy.com/index.php/Marchland", "./list_of_cards_files/200px-Marchland.jpg")
PRINCE = CardShapedThing("Prince", {"Action", "Duration", "Command"}, Cost(coins=8), "You may set aside (on this) a non-Duration, non-Command Action card from your hand costing up to $4.At the start of each of your turns, play that card, leaving it set aside.", "https://wiki.dominionstrategy.com/index.php/Prince", "./list_of_cards_files/200px-Prince.jpg")
SAUNA = CardShapedThing("Sauna", {"Action"}, Cost(coins=4), "+1 Card+1 ActionYou may play an Avanto from your hand.This turn, when you play a Silver, you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Sauna", "./list_of_cards_files/200px-Sauna.jpg")
STASH = CardShapedThing("Stash", {"Treasure"}, Cost(coins=5), "$2When shuffling this, you may look through your remaining deck, and may put this anywhere in the shuffled cards.", "https://wiki.dominionstrategy.com/index.php/Stash", "./list_of_cards_files/200px-Stash.jpg")
SUMMON = CardShapedThing("Summon", {"Event"}, Cost(coins=5), "Gain an Action card costing up to $4. Set it aside. If you did, then at the start of your next turn, play it.", "https://wiki.dominionstrategy.com/index.php/Summon", "./list_of_cards_files/320px-Summon.jpg")
WALLED_VILLAGE = CardShapedThing("Walled Village", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsAt the start of Clean-up, if you have this and no more than one other Action card in play, you may put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Walled_Village", "./list_of_cards_files/200px-Walled_Village.jpg")

CARD_SHAPED_THINGS = {
    "Adventurer": ADVENTURER,
    "Artisan": ARTISAN,
    "Bandit": BANDIT,
    "Bureaucrat": BUREAUCRAT,
    "Cellar": CELLAR,
    "Chancellor": CHANCELLOR,
    "Chapel": CHAPEL,
    "Council Room": COUNCIL_ROOM,
    "Feast": FEAST,
    "Festival": FESTIVAL,
    "Gardens": GARDENS,
    "Harbinger": HARBINGER,
    "Laboratory": LABORATORY,
    "Library": LIBRARY,
    "Market": MARKET,
    "Merchant": MERCHANT,
    "Militia": MILITIA,
    "Mine": MINE,
    "Moat": MOAT,
    "Moneylender": MONEYLENDER,
    "Poacher": POACHER,
    "Remodel": REMODEL,
    "Sentry": SENTRY,
    "Smithy": SMITHY,
    "Spy": SPY,
    "Thief": THIEF,
    "Throne Room": THRONE_ROOM,
    "Vassal": VASSAL,
    "Village": VILLAGE,
    "Witch": WITCH,
    "Woodcutter": WOODCUTTER,
    "Workshop": WORKSHOP,
    "Copper": COPPER,
    "Silver": SILVER,
    "Gold": GOLD,
    "Estate": ESTATE,
    "Duchy": DUCHY,
    "Province": PROVINCE,
    "Curse": CURSE,
    "Baron": BARON,
    "Bridge": BRIDGE,
    "Conspirator": CONSPIRATOR,
    "Coppersmith": COPPERSMITH,
    "Courtier": COURTIER,
    "Courtyard": COURTYARD,
    "Diplomat": DIPLOMAT,
    "Duke": DUKE,
    "Great Hall": GREAT_HALL,
    "Farm": FARM,
    "Ironworks": IRONWORKS,
    "Lurker": LURKER,
    "Masquerade": MASQUERADE,
    "Mill": MILL,
    "Mining Village": MINING_VILLAGE,
    "Minion": MINION,
    "Nobles": NOBLES,
    "Patrol": PATROL,
    "Pawn": PAWN,
    "Replace": REPLACE,
    "Saboteur": SABOTEUR,
    "Scout": SCOUT,
    "Secret Chamber": SECRET_CHAMBER,
    "Secret Passage": SECRET_PASSAGE,
    "Shanty Town": SHANTY_TOWN,
    "Steward": STEWARD,
    "Swindler": SWINDLER,
    "Torturer": TORTURER,
    "Trading Post": TRADING_POST,
    "Tribute": TRIBUTE,
    "Upgrade": UPGRADE,
    "Wishing Well": WISHING_WELL,
    "Ambassador": AMBASSADOR,
    "Astrolabe": ASTROLABE,
    "Bazaar": BAZAAR,
    "Blockade": BLOCKADE,
    "Caravan": CARAVAN,
    "Corsair": CORSAIR,
    "Cutpurse": CUTPURSE,
    "Embargo": EMBARGO,
    "Explorer": EXPLORER,
    "Fishing Village": FISHING_VILLAGE,
    "Ghost Ship": GHOST_SHIP,
    "Haven": HAVEN,
    "Island": ISLAND,
    "Lighthouse": LIGHTHOUSE,
    "Lookout": LOOKOUT,
    "Merchant Ship": MERCHANT_SHIP,
    "Monkey": MONKEY,
    "Native Village": NATIVE_VILLAGE,
    "Navigator": NAVIGATOR,
    "Outpost": OUTPOST,
    "Pearl Diver": PEARL_DIVER,
    "Pirate": PIRATE,
    "Pirate Ship": PIRATE_SHIP,
    "Sailor": SAILOR,
    "Salvager": SALVAGER,
    "Sea Chart": SEA_CHART,
    "Sea Hag": SEA_HAG,
    "Sea Witch": SEA_WITCH,
    "Smugglers": SMUGGLERS,
    "Tactician": TACTICIAN,
    "Tide Pools": TIDE_POOLS,
    "Treasure Map": TREASURE_MAP,
    "Treasury": TREASURY,
    "Warehouse": WAREHOUSE,
    "Wharf": WHARF,
    "Alchemist": ALCHEMIST,
    "Apothecary": APOTHECARY,
    "Apprentice": APPRENTICE,
    "Familiar": FAMILIAR,
    "Golem": GOLEM,
    "Herbalist": HERBALIST,
    "Philosopher's Stone": PHILOSOPHERS_STONE,
    "Possession": POSSESSION,
    "Scrying Pool": SCRYING_POOL,
    "Transmute": TRANSMUTE,
    "University": UNIVERSITY,
    "Vineyard": VINEYARD,
    "Potion": POTION,
    "Anvil": ANVIL,
    "Bank": BANK,
    "Bishop": BISHOP,
    "Charlatan": CHARLATAN,
    "City": CITY,
    "Clerk": CLERK,
    "Collection": COLLECTION,
    "Contraband": CONTRABAND,
    "Counting House": COUNTING_HOUSE,
    "Crystal Ball": CRYSTAL_BALL,
    "Expand": EXPAND,
    "Forge": FORGE,
    "Goons": GOONS,
    "Grand Market": GRAND_MARKET,
    "Hoard": HOARD,
    "Investment": INVESTMENT,
    "King's Court": KINGS_COURT,
    "Loan": LOAN,
    "Magnate": MAGNATE,
    "Mint": MINT,
    "Monument": MONUMENT,
    "Mountebank": MOUNTEBANK,
    "Peddler": PEDDLER,
    "Quarry": QUARRY,
    "Rabble": RABBLE,
    "Royal Seal": ROYAL_SEAL,
    "Talisman": TALISMAN,
    "Tiara": TIARA,
    "Trade Route": TRADE_ROUTE,
    "Vault": VAULT,
    "Venture": VENTURE,
    "War Chest": WAR_CHEST,
    "Watchtower": WATCHTOWER,
    "Worker's Village": WORKERS_VILLAGE,
    "Platinum": PLATINUM,
    "Colony": COLONY,
    "Advisor": ADVISOR,
    "Baker": BAKER,
    "Butcher": BUTCHER,
    "Candlestick Maker": CANDLESTICK_MAKER,
    "Carnival": CARNIVAL,
    "Doctor": DOCTOR,
    "Fairgrounds": FAIRGROUNDS,
    "Farmhands": FARMHANDS,
    "Farming Village": FARMING_VILLAGE,
    "Farrier": FARRIER,
    "Ferryman": FERRYMAN,
    "Footpad": FOOTPAD,
    "Fortune Teller": FORTUNE_TELLER,
    "Hamlet": HAMLET,
    "Harvest": HARVEST,
    "Herald": HERALD,
    "Horn of Plenty": HORN_OF_PLENTY,
    "Horse Traders": HORSE_TRADERS,
    "Hunting Party": HUNTING_PARTY,
    "Infirmary": INFIRMARY,
    "Jester": JESTER,
    "Journeyman": JOURNEYMAN,
    "Joust": JOUST,
    "Masterpiece": MASTERPIECE,
    "Menagerie": MENAGERIE,
    "Merchant Guild": MERCHANT_GUILD,
    "Plaza": PLAZA,
    "Remake": REMAKE,
    "Shop": SHOP,
    "Soothsayer": SOOTHSAYER,
    "Stonemason": STONEMASON,
    "Taxman": TAXMAN,
    "Tournament": TOURNAMENT,
    "Young Witch": YOUNG_WITCH,
    "Bag of Gold": BAG_OF_GOLD,
    "Coronet": CORONET,
    "Courser": COURSER,
    "Demesne": DEMESNE,
    "Diadem": DIADEM,
    "Followers": FOLLOWERS,
    "Housecarl": HOUSECARL,
    "Huge Turnip": HUGE_TURNIP,
    "Princess": PRINCESS,
    "Renown": RENOWN,
    "Trusty Steed": TRUSTY_STEED,
    "Berserker": BERSERKER,
    "Border Village": BORDER_VILLAGE,
    "Cache": CACHE,
    "Cartographer": CARTOGRAPHER,
    "Cauldron": CAULDRON,
    "Crossroads": CROSSROADS,
    "Develop": DEVELOP,
    "Duchess": DUCHESS,
    "Embassy": EMBASSY,
    "Farmland": FARMLAND,
    "Fool's Gold": FOOLS_GOLD,
    "Guard Dog": GUARD_DOG,
    "Haggler": HAGGLER,
    "Highway": HIGHWAY,
    "Ill-Gotten Gains": ILL_GOTTEN_GAINS,
    "Inn": INN,
    "Jack of All Trades": JACK_OF_ALL_TRADES,
    "Mandarin": MANDARIN,
    "Margrave": MARGRAVE,
    "Noble Brigand": NOBLE_BRIGAND,
    "Nomad Camp": NOMAD_CAMP,
    "Nomads": NOMADS,
    "Oasis": OASIS,
    "Oracle": ORACLE,
    "Scheme": SCHEME,
    "Silk Road": SILK_ROAD,
    "Souk": SOUK,
    "Spice Merchant": SPICE_MERCHANT,
    "Stables": STABLES,
    "Trader": TRADER,
    "Trail": TRAIL,
    "Tunnel": TUNNEL,
    "Weaver": WEAVER,
    "Wheelwright": WHEELWRIGHT,
    "Witch's Hut": WITCHS_HUT,
    "Altar": ALTAR,
    "Armory": ARMORY,
    "Band of Misfits": BAND_OF_MISFITS,
    "Bandit Camp": BANDIT_CAMP,
    "Beggar": BEGGAR,
    "Catacombs": CATACOMBS,
    "Count": COUNT,
    "Counterfeit": COUNTERFEIT,
    "Cultist": CULTIST,
    "Dame Anna": DAME_ANNA,
    "Dame Josephine": DAME_JOSEPHINE,
    "Dame Molly": DAME_MOLLY,
    "Dame Natalie": DAME_NATALIE,
    "Dame Sylvia": DAME_SYLVIA,
    "Death Cart": DEATH_CART,
    "Feodum": FEODUM,
    "Forager": FORAGER,
    "Fortress": FORTRESS,
    "Graverobber": GRAVEROBBER,
    "Hermit": HERMIT,
    "Hunting Grounds": HUNTING_GROUNDS,
    "Ironmonger": IRONMONGER,
    "Junk Dealer": JUNK_DEALER,
    "Marauder": MARAUDER,
    "Market Square": MARKET_SQUARE,
    "Mystic": MYSTIC,
    "Pillage": PILLAGE,
    "Poor House": POOR_HOUSE,
    "Procession": PROCESSION,
    "Rats": RATS,
    "Rebuild": REBUILD,
    "Rogue": ROGUE,
    "Sage": SAGE,
    "Scavenger": SCAVENGER,
    "Sir Bailey": SIR_BAILEY,
    "Sir Destry": SIR_DESTRY,
    "Sir Martin": SIR_MARTIN,
    "Sir Michael": SIR_MICHAEL,
    "Sir Vander": SIR_VANDER,
    "Squire": SQUIRE,
    "Storeroom": STOREROOM,
    "Urchin": URCHIN,
    "Vagrant": VAGRANT,
    "Wandering Minstrel": WANDERING_MINSTREL,
    "Abandoned Mine": ABANDONED_MINE,
    "Ruined Library": RUINED_LIBRARY,
    "Ruined Market": RUINED_MARKET,
    "Ruined Village": RUINED_VILLAGE,
    "Survivors": SURVIVORS,
    "Hovel": HOVEL,
    "Madman": MADMAN,
    "Mercenary": MERCENARY,
    "Necropolis": NECROPOLIS,
    "Overgrown Estate": OVERGROWN_ESTATE,
    "Spoils": SPOILS,
    "Amulet": AMULET,
    "Artificer": ARTIFICER,
    "Bridge Troll": BRIDGE_TROLL,
    "Caravan Guard": CARAVAN_GUARD,
    "Coin of the Realm": COIN_OF_THE_REALM,
    "Distant Lands": DISTANT_LANDS,
    "Dungeon": DUNGEON,
    "Duplicate": DUPLICATE,
    "Gear": GEAR,
    "Giant": GIANT,
    "Guide": GUIDE,
    "Haunted Woods": HAUNTED_WOODS,
    "Hireling": HIRELING,
    "Lost City": LOST_CITY,
    "Magpie": MAGPIE,
    "Messenger": MESSENGER,
    "Miser": MISER,
    "Page": PAGE,
    "Peasant": PEASANT,
    "Port": PORT,
    "Ranger": RANGER,
    "Ratcatcher": RATCATCHER,
    "Raze": RAZE,
    "Relic": RELIC,
    "Royal Carriage": ROYAL_CARRIAGE,
    "Storyteller": STORYTELLER,
    "Swamp Hag": SWAMP_HAG,
    "Transmogrify": TRANSMOGRIFY,
    "Treasure Trove": TREASURE_TROVE,
    "Wine Merchant": WINE_MERCHANT,
    "Champion": CHAMPION,
    "Disciple": DISCIPLE,
    "Fugitive": FUGITIVE,
    "Hero": HERO,
    "Soldier": SOLDIER,
    "Teacher": TEACHER,
    "Treasure Hunter": TREASURE_HUNTER,
    "Warrior": WARRIOR,
    "Alms": ALMS,
    "Ball": BALL,
    "Bonfire": BONFIRE,
    "Borrow": BORROW,
    "Expedition": EXPEDITION,
    "Ferry": FERRY,
    "Inheritance": INHERITANCE,
    "Lost Arts": LOST_ARTS,
    "Mission": MISSION,
    "Pathfinding": PATHFINDING,
    "Pilgrimage": PILGRIMAGE,
    "Plan": PLAN,
    "Quest": QUEST,
    "Raid": RAID,
    "Save": SAVE,
    "Scouting Party": SCOUTING_PARTY,
    "Seaway": SEAWAY,
    "Trade": TRADE,
    "Training": TRAINING,
    "Travelling Fair": TRAVELLING_FAIR,
    "Archive": ARCHIVE,
    "Bustling Village": BUSTLING_VILLAGE,
    "Capital": CAPITAL,
    "Catapult": CATAPULT,
    "Chariot Race": CHARIOT_RACE,
    "Charm": CHARM,
    "City Quarter": CITY_QUARTER,
    "Crown": CROWN,
    "Crumbling Castle": CRUMBLING_CASTLE,
    "Emporium": EMPORIUM,
    "Encampment": ENCAMPMENT,
    "Enchantress": ENCHANTRESS,
    "Engineer": ENGINEER,
    "Farmers' Market": FARMERS_MARKET,
    "Fortune": FORTUNE,
    "Forum": FORUM,
    "Gladiator": GLADIATOR,
    "Grand Castle": GRAND_CASTLE,
    "Groundskeeper": GROUNDSKEEPER,
    "Haunted Castle": HAUNTED_CASTLE,
    "Humble Castle": HUMBLE_CASTLE,
    "King's Castle": KINGS_CASTLE,
    "Legionary": LEGIONARY,
    "Opulent Castle": OPULENT_CASTLE,
    "Overlord": OVERLORD,
    "Patrician": PATRICIAN,
    "Plunder": PLUNDER,
    "Rocks": ROCKS,
    "Royal Blacksmith": ROYAL_BLACKSMITH,
    "Sacrifice": SACRIFICE,
    "Settlers": SETTLERS,
    "Small Castle": SMALL_CASTLE,
    "Sprawling Castle": SPRAWLING_CASTLE,
    "Temple": TEMPLE,
    "Villa": VILLA,
    "Wild Hunt": WILD_HUNT,
    "Advance": ADVANCE,
    "Annex": ANNEX,
    "Banquet": BANQUET,
    "Conquest": CONQUEST,
    "Delve": DELVE,
    "Dominate": DOMINATE,
    "Donate": DONATE,
    "Ritual": RITUAL,
    "Salt the Earth": SALT_THE_EARTH,
    "Tax": TAX,
    "Triumph": TRIUMPH,
    "Wedding": WEDDING,
    "Windfall": WINDFALL,
    "Aqueduct": AQUEDUCT,
    "Arena": ARENA,
    "Bandit Fort": BANDIT_FORT,
    "Basilica": BASILICA,
    "Baths": BATHS,
    "Battlefield": BATTLEFIELD,
    "Colonnade": COLONNADE,
    "Defiled Shrine": DEFILED_SHRINE,
    "Fountain": FOUNTAIN,
    "Keep": KEEP,
    "Labyrinth": LABYRINTH,
    "Mountain Pass": MOUNTAIN_PASS,
    "Museum": MUSEUM,
    "Obelisk": OBELISK,
    "Orchard": ORCHARD,
    "Palace": PALACE,
    "Tomb": TOMB,
    "Tower": TOWER,
    "Triumphal Arch": TRIUMPHAL_ARCH,
    "Wall": WALL,
    "Wolf Den": WOLF_DEN,
    "Bard": BARD,
    "Blessed Village": BLESSED_VILLAGE,
    "Cemetery": CEMETERY,
    "Changeling": CHANGELING,
    "Cobbler": COBBLER,
    "Conclave": CONCLAVE,
    "Crypt": CRYPT,
    "Cursed Village": CURSED_VILLAGE,
    "Den of Sin": DEN_OF_SIN,
    "Devil's Workshop": DEVILS_WORKSHOP,
    "Druid": DRUID,
    "Exorcist": EXORCIST,
    "Faithful Hound": FAITHFUL_HOUND,
    "Fool": FOOL,
    "Ghost Town": GHOST_TOWN,
    "Guardian": GUARDIAN,
    "Idol": IDOL,
    "Leprechaun": LEPRECHAUN,
    "Monastery": MONASTERY,
    "Necromancer": NECROMANCER,
    "Night Watchman": NIGHT_WATCHMAN,
    "Pixie": PIXIE,
    "Pooka": POOKA,
    "Raider": RAIDER,
    "Sacred Grove": SACRED_GROVE,
    "Secret Cave": SECRET_CAVE,
    "Shepherd": SHEPHERD,
    "Skulk": SKULK,
    "Tormentor": TORMENTOR,
    "Tracker": TRACKER,
    "Tragic Hero": TRAGIC_HERO,
    "Vampire": VAMPIRE,
    "Werewolf": WEREWOLF,
    "Bat": BAT,
    "Cursed Gold": CURSED_GOLD,
    "Ghost": GHOST,
    "Goat": GOAT,
    "Haunted Mirror": HAUNTED_MIRROR,
    "Imp": IMP,
    "Lucky Coin": LUCKY_COIN,
    "Magic Lamp": MAGIC_LAMP,
    "Pasture": PASTURE,
    "Pouch": POUCH,
    "Will-o'-Wisp": WILL_O_WISP,
    "Wish": WISH,
    "Zombie Apprentice": ZOMBIE_APPRENTICE,
    "Zombie Mason": ZOMBIE_MASON,
    "Zombie Spy": ZOMBIE_SPY,
    "The Earth's Gift": THE_EARTHS_GIFT,
    "The Field's Gift": THE_FIELDS_GIFT,
    "The Flame's Gift": THE_FLAMES_GIFT,
    "The Forest's Gift": THE_FORESTS_GIFT,
    "The Moon's Gift": THE_MOONS_GIFT,
    "The Mountain's Gift": THE_MOUNTAINS_GIFT,
    "The River's Gift": THE_RIVERS_GIFT,
    "The Sea's Gift": THE_SEAS_GIFT,
    "The Sky's Gift": THE_SKYS_GIFT,
    "The Sun's Gift": THE_SUNS_GIFT,
    "The Swamp's Gift": THE_SWAMPS_GIFT,
    "The Wind's Gift": THE_WINDS_GIFT,
    "Bad Omens": BAD_OMENS,
    "Delusion": DELUSION,
    "Envy": ENVY,
    "Famine": FAMINE,
    "Fear": FEAR,
    "Greed": GREED,
    "Haunting": HAUNTING,
    "Locusts": LOCUSTS,
    "Misery": MISERY,
    "Plague": PLAGUE,
    "Poverty": POVERTY,
    "War": WAR,
    "Deluded": DELUDED,
    "Envious": ENVIOUS,
    "Lost in the Woods": LOST_IN_THE_WOODS,
    "Miserable": MISERABLE,
    "Twice Miserable": TWICE_MISERABLE,
    "Acting Troupe": ACTING_TROUPE,
    "Border Guard": BORDER_GUARD,
    "Cargo Ship": CARGO_SHIP,
    "Ducat": DUCAT,
    "Experiment": EXPERIMENT,
    "Flag Bearer": FLAG_BEARER,
    "Hideout": HIDEOUT,
    "Improve": IMPROVE,
    "Inventor": INVENTOR,
    "Lackeys": LACKEYS,
    "Mountain Village": MOUNTAIN_VILLAGE,
    "Old Witch": OLD_WITCH,
    "Patron": PATRON,
    "Priest": PRIEST,
    "Recruiter": RECRUITER,
    "Research": RESEARCH,
    "Scepter": SCEPTER,
    "Scholar": SCHOLAR,
    "Sculptor": SCULPTOR,
    "Seer": SEER,
    "Silk Merchant": SILK_MERCHANT,
    "Spices": SPICES,
    "Swashbuckler": SWASHBUCKLER,
    "Treasurer": TREASURER,
    "Villain": VILLAIN,
    "Academy": ACADEMY,
    "Barracks": BARRACKS,
    "Canal": CANAL,
    "Capitalism": CAPITALISM,
    "Cathedral": CATHEDRAL,
    "Citadel": CITADEL,
    "City Gate": CITY_GATE,
    "Crop Rotation": CROP_ROTATION,
    "Exploration": EXPLORATION,
    "Fair": FAIR,
    "Fleet": FLEET,
    "Guildhall": GUILDHALL,
    "Innovation": INNOVATION,
    "Pageant": PAGEANT,
    "Piazza": PIAZZA,
    "Road Network": ROAD_NETWORK,
    "Sewers": SEWERS,
    "Silos": SILOS,
    "Sinister Plot": SINISTER_PLOT,
    "Star Chart": STAR_CHART,
    "Flag": FLAG,
    "Horn": HORN,
    "Key": KEY,
    "Lantern": LANTERN,
    "Treasure Chest": TREASURE_CHEST,
    "Animal Fair": ANIMAL_FAIR,
    "Barge": BARGE,
    "Black Cat": BLACK_CAT,
    "Bounty Hunter": BOUNTY_HUNTER,
    "Camel Train": CAMEL_TRAIN,
    "Cardinal": CARDINAL,
    "Cavalry": CAVALRY,
    "Coven": COVEN,
    "Destrier": DESTRIER,
    "Displace": DISPLACE,
    "Falconer": FALCONER,
    "Fisherman": FISHERMAN,
    "Gatekeeper": GATEKEEPER,
    "Goatherd": GOATHERD,
    "Groom": GROOM,
    "Hostelry": HOSTELRY,
    "Hunting Lodge": HUNTING_LODGE,
    "Kiln": KILN,
    "Livery": LIVERY,
    "Mastermind": MASTERMIND,
    "Paddock": PADDOCK,
    "Sanctuary": SANCTUARY,
    "Scrap": SCRAP,
    "Sheepdog": SHEEPDOG,
    "Sleigh": SLEIGH,
    "Snowy Village": SNOWY_VILLAGE,
    "Stockpile": STOCKPILE,
    "Supplies": SUPPLIES,
    "Village Green": VILLAGE_GREEN,
    "Wayfarer": WAYFARER,
    "Horse": HORSE,
    "Alliance": ALLIANCE,
    "Banish": BANISH,
    "Bargain": BARGAIN,
    "Commerce": COMMERCE,
    "Delay": DELAY,
    "Demand": DEMAND,
    "Desperation": DESPERATION,
    "Enclave": ENCLAVE,
    "Enhance": ENHANCE,
    "Gamble": GAMBLE,
    "Invest": INVEST,
    "March": MARCH,
    "Populate": POPULATE,
    "Pursue": PURSUE,
    "Reap": REAP,
    "Ride": RIDE,
    "Seize the Day": SEIZE_THE_DAY,
    "Stampede": STAMPEDE,
    "Toil": TOIL,
    "Transport": TRANSPORT,
    "Way of the Butterfly": WAY_OF_THE_BUTTERFLY,
    "Way of the Camel": WAY_OF_THE_CAMEL,
    "Way of the Chameleon": WAY_OF_THE_CHAMELEON,
    "Way of the Frog": WAY_OF_THE_FROG,
    "Way of the Goat": WAY_OF_THE_GOAT,
    "Way of the Horse": WAY_OF_THE_HORSE,
    "Way of the Mole": WAY_OF_THE_MOLE,
    "Way of the Monkey": WAY_OF_THE_MONKEY,
    "Way of the Mouse": WAY_OF_THE_MOUSE,
    "Way of the Mule": WAY_OF_THE_MULE,
    "Way of the Otter": WAY_OF_THE_OTTER,
    "Way of the Ox": WAY_OF_THE_OX,
    "Way of the Owl": WAY_OF_THE_OWL,
    "Way of the Pig": WAY_OF_THE_PIG,
    "Way of the Rat": WAY_OF_THE_RAT,
    "Way of the Seal": WAY_OF_THE_SEAL,
    "Way of the Sheep": WAY_OF_THE_SHEEP,
    "Way of the Squirrel": WAY_OF_THE_SQUIRREL,
    "Way of the Turtle": WAY_OF_THE_TURTLE,
    "Way of the Worm": WAY_OF_THE_WORM,
    "Acolyte": ACOLYTE,
    "Archer": ARCHER,
    "Barbarian": BARBARIAN,
    "Battle Plan": BATTLE_PLAN,
    "Bauble": BAUBLE,
    "Blacksmith": BLACKSMITH,
    "Broker": BROKER,
    "Capital City": CAPITAL_CITY,
    "Carpenter": CARPENTER,
    "Conjurer": CONJURER,
    "Contract": CONTRACT,
    "Courier": COURIER,
    "Distant Shore": DISTANT_SHORE,
    "Elder": ELDER,
    "Emissary": EMISSARY,
    "Galleria": GALLERIA,
    "Garrison": GARRISON,
    "Guildmaster": GUILDMASTER,
    "Herb Gatherer": HERB_GATHERER,
    "Highwayman": HIGHWAYMAN,
    "Hill Fort": HILL_FORT,
    "Hunter": HUNTER,
    "Importer": IMPORTER,
    "Innkeeper": INNKEEPER,
    "Lich": LICH,
    "Marquis": MARQUIS,
    "Merchant Camp": MERCHANT_CAMP,
    "Miller": MILLER,
    "Modify": MODIFY,
    "Old Map": OLD_MAP,
    "Royal Galley": ROYAL_GALLEY,
    "Sentinel": SENTINEL,
    "Sibyl": SIBYL,
    "Skirmisher": SKIRMISHER,
    "Sorcerer": SORCERER,
    "Sorceress": SORCERESS,
    "Specialist": SPECIALIST,
    "Stronghold": STRONGHOLD,
    "Student": STUDENT,
    "Sunken Treasure": SUNKEN_TREASURE,
    "Swap": SWAP,
    "Sycophant": SYCOPHANT,
    "Tent": TENT,
    "Territory": TERRITORY,
    "Town": TOWN,
    "Town Crier": TOWN_CRIER,
    "Underling": UNDERLING,
    "Voyage": VOYAGE,
    "Warlord": WARLORD,
    "Architects' Guild": ARCHITECTS_GUILD,
    "Band of Nomads": BAND_OF_NOMADS,
    "Cave Dwellers": CAVE_DWELLERS,
    "Circle of Witches": CIRCLE_OF_WITCHES,
    "City-state": CITY_STATE,
    "Coastal Haven": COASTAL_HAVEN,
    "Crafters' Guild": CRAFTERS_GUILD,
    "Desert Guides": DESERT_GUIDES,
    "Family of Inventors": FAMILY_OF_INVENTORS,
    "Fellowship of Scribes": FELLOWSHIP_OF_SCRIBES,
    "Forest Dwellers": FOREST_DWELLERS,
    "Gang of Pickpockets": GANG_OF_PICKPOCKETS,
    "Island Folk": ISLAND_FOLK,
    "League of Bankers": LEAGUE_OF_BANKERS,
    "League of Shopkeepers": LEAGUE_OF_SHOPKEEPERS,
    "Market Towns": MARKET_TOWNS,
    "Mountain Folk": MOUNTAIN_FOLK,
    "Order of Astrologers": ORDER_OF_ASTROLOGERS,
    "Order of Masons": ORDER_OF_MASONS,
    "Peaceful Cult": PEACEFUL_CULT,
    "Plateau Shepherds": PLATEAU_SHEPHERDS,
    "Trappers' Lodge": TRAPPERS_LODGE,
    "Woodworkers' Guild": WOODWORKERS_GUILD,
    "Abundance": ABUNDANCE,
    "Buried Treasure": BURIED_TREASURE,
    "Cabin Boy": CABIN_BOY,
    "Cage": CAGE,
    "Crew": CREW,
    "Crucible": CRUCIBLE,
    "Cutthroat": CUTTHROAT,
    "Enlarge": ENLARGE,
    "Figurine": FIGURINE,
    "First Mate": FIRST_MATE,
    "Flagship": FLAGSHIP,
    "Fortune Hunter": FORTUNE_HUNTER,
    "Frigate": FRIGATE,
    "Gondola": GONDOLA,
    "Grotto": GROTTO,
    "Harbor Village": HARBOR_VILLAGE,
    "Jewelled Egg": JEWELLED_EGG,
    "King's Cache": KINGS_CACHE,
    "Landing Party": LANDING_PARTY,
    "Longship": LONGSHIP,
    "Mapmaker": MAPMAKER,
    "Maroon": MAROON,
    "Mining Road": MINING_ROAD,
    "Pendant": PENDANT,
    "Pickaxe": PICKAXE,
    "Pilgrim": PILGRIM,
    "Quartermaster": QUARTERMASTER,
    "Rope": ROPE,
    "Sack of Loot": SACK_OF_LOOT,
    "Search": SEARCH,
    "Secluded Shrine": SECLUDED_SHRINE,
    "Shaman": SHAMAN,
    "Silver Mine": SILVER_MINE,
    "Siren": SIREN,
    "Stowaway": STOWAWAY,
    "Swamp Shacks": SWAMP_SHACKS,
    "Taskmaster": TASKMASTER,
    "Tools": TOOLS,
    "Trickster": TRICKSTER,
    "Wealthy Village": WEALTHY_VILLAGE,
    "Amphora": AMPHORA,
    "Doubloons": DOUBLOONS,
    "Endless Chalice": ENDLESS_CHALICE,
    "Figurehead": FIGUREHEAD,
    "Hammer": HAMMER,
    "Insignia": INSIGNIA,
    "Jewels": JEWELS,
    "Orb": ORB,
    "Prize Goat": PRIZE_GOAT,
    "Puzzle Box": PUZZLE_BOX,
    "Sextant": SEXTANT,
    "Shield": SHIELD,
    "Spell Scroll": SPELL_SCROLL,
    "Staff": STAFF,
    "Sword": SWORD,
    "Avoid": AVOID,
    "Bury": BURY,
    "Deliver": DELIVER,
    "Foray": FORAY,
    "Invasion": INVASION,
    "Journey": JOURNEY,
    "Launch": LAUNCH,
    "Looting": LOOTING,
    "Maelstrom": MAELSTROM,
    "Mirror": MIRROR,
    "Peril": PERIL,
    "Prepare": PREPARE,
    "Prosper": PROSPER,
    "Rush": RUSH,
    "Scrounge": SCROUNGE,
    "Cheap": CHEAP,
    "Cursed": CURSED,
    "Fated": FATED,
    "Fawning": FAWNING,
    "Friendly": FRIENDLY,
    "Hasty": HASTY,
    "Inherited": INHERITED,
    "Inspiring": INSPIRING,
    "Nearby": NEARBY,
    "Patient": PATIENT,
    "Pious": PIOUS,
    "Reckless": RECKLESS,
    "Rich": RICH,
    "Shy": SHY,
    "Tireless": TIRELESS,
    "Alley": ALLEY,
    "Aristocrat": ARISTOCRAT,
    "Artist": ARTIST,
    "Change": CHANGE,
    "Craftsman": CRAFTSMAN,
    "Daimyo": DAIMYO,
    "Fishmonger": FISHMONGER,
    "Gold Mine": GOLD_MINE,
    "Imperial Envoy": IMPERIAL_ENVOY,
    "Kitsune": KITSUNE,
    "Litter": LITTER,
    "Mountain Shrine": MOUNTAIN_SHRINE,
    "Ninja": NINJA,
    "Poet": POET,
    "Rice": RICE,
    "Rice Broker": RICE_BROKER,
    "River Shrine": RIVER_SHRINE,
    "Riverboat": RIVERBOAT,
    "Ronin": RONIN,
    "Root Cellar": ROOT_CELLAR,
    "Rustic Village": RUSTIC_VILLAGE,
    "Samurai": SAMURAI,
    "Snake Witch": SNAKE_WITCH,
    "Tanuki": TANUKI,
    "Tea House": TEA_HOUSE,
    "Amass": AMASS,
    "Asceticism": ASCETICISM,
    "Continue": CONTINUE,
    "Credit": CREDIT,
    "Foresight": FORESIGHT,
    "Gather": GATHER,
    "Kintsugi": KINTSUGI,
    "Practice": PRACTICE,
    "Receive Tribute": RECEIVE_TRIBUTE,
    "Sea Trade": SEA_TRADE,
    "Approaching Army": APPROACHING_ARMY,
    "Biding Time": BIDING_TIME,
    "Bureaucracy": BUREAUCRACY,
    "Divine Wind": DIVINE_WIND,
    "Enlightenment": ENLIGHTENMENT,
    "Flourishing Trade": FLOURISHING_TRADE,
    "Good Harvest": GOOD_HARVEST,
    "Great Leader": GREAT_LEADER,
    "Growth": GROWTH,
    "Harsh Winter": HARSH_WINTER,
    "Kind Emperor": KIND_EMPEROR,
    "Panic": PANIC,
    "Progress": PROGRESS,
    "Rapid Expansion": RAPID_EXPANSION,
    "Sickness": SICKNESS,
    "Avanto": AVANTO,
    "Black Market": BLACK_MARKET,
    "Captain": CAPTAIN,
    "Church": CHURCH,
    "Dismantle": DISMANTLE,
    "Envoy": ENVOY,
    "Governor": GOVERNOR,
    "Marchland": MARCHLAND,
    "Prince": PRINCE,
    "Sauna": SAUNA,
    "Stash": STASH,
    "Summon": SUMMON,
    "Walled Village": WALLED_VILLAGE,
}

BASE = [
    COPPER,
    SILVER,
    GOLD,
    ESTATE,
    DUCHY,
    PROVINCE,
    CURSE,
    POTION,
    PLATINUM,
    COLONY,
]

NON_SUPPLY = [
    BAG_OF_GOLD,
    CORONET,
    COURSER,
    DEMESNE,
    DIADEM,
    FOLLOWERS,
    HOUSECARL,
    HUGE_TURNIP,
    PRINCESS,
    RENOWN,
    TRUSTY_STEED,
    MADMAN,
    MERCENARY,
    SPOILS,
    CHAMPION,
    DISCIPLE,
    FUGITIVE,
    HERO,
    SOLDIER,
    TEACHER,
    TREASURE_HUNTER,
    WARRIOR,
    BAT,
    GHOST,
    IMP,
    WILL_O_WISP,
    WISH,
    HORSE,
    AMPHORA,
    DOUBLOONS,
    ENDLESS_CHALICE,
    FIGUREHEAD,
    HAMMER,
    INSIGNIA,
    JEWELS,
    ORB,
    PRIZE_GOAT,
    PUZZLE_BOX,
    SEXTANT,
    SHIELD,
    SPELL_SCROLL,
    STAFF,
    SWORD,
]

SHELTERS = [
    HOVEL,
    NECROPOLIS,
    OVERGROWN_ESTATE,
]

RUINS = [
    ABANDONED_MINE,
    RUINED_LIBRARY,
    RUINED_MARKET,
    RUINED_VILLAGE,
    SURVIVORS,
]

EVENTS = [
    ALMS,
    BALL,
    BONFIRE,
    BORROW,
    EXPEDITION,
    FERRY,
    INHERITANCE,
    LOST_ARTS,
    MISSION,
    PATHFINDING,
    PILGRIMAGE,
    PLAN,
    QUEST,
    RAID,
    SAVE,
    SCOUTING_PARTY,
    SEAWAY,
    TRADE,
    TRAINING,
    TRAVELLING_FAIR,
    ADVANCE,
    ANNEX,
    BANQUET,
    CONQUEST,
    DELVE,
    DOMINATE,
    DONATE,
    RITUAL,
    SALT_THE_EARTH,
    TAX,
    TRIUMPH,
    WEDDING,
    WINDFALL,
    ALLIANCE,
    BANISH,
    BARGAIN,
    COMMERCE,
    DELAY,
    DEMAND,
    DESPERATION,
    ENCLAVE,
    ENHANCE,
    GAMBLE,
    INVEST,
    MARCH,
    POPULATE,
    PURSUE,
    REAP,
    RIDE,
    SEIZE_THE_DAY,
    STAMPEDE,
    TOIL,
    TRANSPORT,
    AVOID,
    BURY,
    DELIVER,
    FORAY,
    INVASION,
    JOURNEY,
    LAUNCH,
    LOOTING,
    MAELSTROM,
    MIRROR,
    PERIL,
    PREPARE,
    PROSPER,
    RUSH,
    SCROUNGE,
    AMASS,
    ASCETICISM,
    CONTINUE,
    CREDIT,
    FORESIGHT,
    GATHER,
    KINTSUGI,
    PRACTICE,
    RECEIVE_TRIBUTE,
    SEA_TRADE,
    SUMMON,
]

LANDMARKS = [
    AQUEDUCT,
    ARENA,
    BANDIT_FORT,
    BASILICA,
    BATHS,
    BATTLEFIELD,
    COLONNADE,
    DEFILED_SHRINE,
    FOUNTAIN,
    KEEP,
    LABYRINTH,
    MOUNTAIN_PASS,
    MUSEUM,
    OBELISK,
    ORCHARD,
    PALACE,
    TOMB,
    TOWER,
    TRIUMPHAL_ARCH,
    WALL,
    WOLF_DEN,
]

HEIRLOOMS = [
    CURSED_GOLD,
    GOAT,
    HAUNTED_MIRROR,
    LUCKY_COIN,
    MAGIC_LAMP,
    PASTURE,
    POUCH,
]

ZOMBIES = [
    ZOMBIE_APPRENTICE,
    ZOMBIE_MASON,
    ZOMBIE_SPY,
]

BOONS = [
    THE_EARTHS_GIFT,
    THE_FIELDS_GIFT,
    THE_FLAMES_GIFT,
    THE_FORESTS_GIFT,
    THE_MOONS_GIFT,
    THE_MOUNTAINS_GIFT,
    THE_RIVERS_GIFT,
    THE_SEAS_GIFT,
    THE_SKYS_GIFT,
    THE_SUNS_GIFT,
    THE_SWAMPS_GIFT,
    THE_WINDS_GIFT,
]

HEXES = [
    BAD_OMENS,
    DELUSION,
    ENVY,
    FAMINE,
    FEAR,
    GREED,
    HAUNTING,
    LOCUSTS,
    MISERY,
    PLAGUE,
    POVERTY,
    WAR,
]

STATES = [
    DELUDED,
    ENVIOUS,
    LOST_IN_THE_WOODS,
    MISERABLE,
    TWICE_MISERABLE,
]

PROJECTS = [
    ACADEMY,
    BARRACKS,
    CANAL,
    CAPITALISM,
    CATHEDRAL,
    CITADEL,
    CITY_GATE,
    CROP_ROTATION,
    EXPLORATION,
    FAIR,
    FLEET,
    GUILDHALL,
    INNOVATION,
    PAGEANT,
    PIAZZA,
    ROAD_NETWORK,
    SEWERS,
    SILOS,
    SINISTER_PLOT,
    STAR_CHART,
]

ARTIFACTS = [
    FLAG,
    HORN,
    KEY,
    LANTERN,
    TREASURE_CHEST,
]

WAYS = [
    WAY_OF_THE_BUTTERFLY,
    WAY_OF_THE_CAMEL,
    WAY_OF_THE_CHAMELEON,
    WAY_OF_THE_FROG,
    WAY_OF_THE_GOAT,
    WAY_OF_THE_HORSE,
    WAY_OF_THE_MOLE,
    WAY_OF_THE_MONKEY,
    WAY_OF_THE_MOUSE,
    WAY_OF_THE_MULE,
    WAY_OF_THE_OTTER,
    WAY_OF_THE_OX,
    WAY_OF_THE_OWL,
    WAY_OF_THE_PIG,
    WAY_OF_THE_RAT,
    WAY_OF_THE_SEAL,
    WAY_OF_THE_SHEEP,
    WAY_OF_THE_SQUIRREL,
    WAY_OF_THE_TURTLE,
    WAY_OF_THE_WORM,
]

ALLIES = [
    ARCHITECTS_GUILD,
    BAND_OF_NOMADS,
    CAVE_DWELLERS,
    CIRCLE_OF_WITCHES,
    CITY_STATE,
    COASTAL_HAVEN,
    CRAFTERS_GUILD,
    DESERT_GUIDES,
    FAMILY_OF_INVENTORS,
    FELLOWSHIP_OF_SCRIBES,
    FOREST_DWELLERS,
    GANG_OF_PICKPOCKETS,
    ISLAND_FOLK,
    LEAGUE_OF_BANKERS,
    LEAGUE_OF_SHOPKEEPERS,
    MARKET_TOWNS,
    MOUNTAIN_FOLK,
    ORDER_OF_ASTROLOGERS,
    ORDER_OF_MASONS,
    PEACEFUL_CULT,
    PLATEAU_SHEPHERDS,
    TRAPPERS_LODGE,
    WOODWORKERS_GUILD,
]

TRAITS = [
    CHEAP,
    CURSED,
    FATED,
    FAWNING,
    FRIENDLY,
    HASTY,
    INHERITED,
    INSPIRING,
    NEARBY,
    PATIENT,
    PIOUS,
    RECKLESS,
    RICH,
    SHY,
    TIRELESS,
]

PROPHECIES = [
    APPROACHING_ARMY,
    BIDING_TIME,
    BUREAUCRACY,
    DIVINE_WIND,
    ENLIGHTENMENT,
    FLOURISHING_TRADE,
    GOOD_HARVEST,
    GREAT_LEADER,
    GROWTH,
    HARSH_WINTER,
    KIND_EMPEROR,
    PANIC,
    PROGRESS,
    RAPID_EXPANSION,
    SICKNESS,
]

KINGDOM_PILES = [
    Pile([ADVENTURER]),
    Pile([ARTISAN]),
    Pile([BANDIT]),
    Pile([BUREAUCRAT]),
    Pile([CELLAR]),
    Pile([CHANCELLOR]),
    Pile([CHAPEL]),
    Pile([COUNCIL_ROOM]),
    Pile([FEAST]),
    Pile([FESTIVAL]),
    Pile([GARDENS]),
    Pile([HARBINGER]),
    Pile([LABORATORY]),
    Pile([LIBRARY]),
    Pile([MARKET]),
    Pile([MERCHANT]),
    Pile([MILITIA]),
    Pile([MINE]),
    Pile([MOAT]),
    Pile([MONEYLENDER]),
    Pile([POACHER]),
    Pile([REMODEL]),
    Pile([SENTRY]),
    Pile([SMITHY]),
    Pile([SPY]),
    Pile([THIEF]),
    Pile([THRONE_ROOM]),
    Pile([VASSAL]),
    Pile([VILLAGE]),
    Pile([WITCH]),
    Pile([WOODCUTTER]),
    Pile([WORKSHOP]),
    Pile([BARON]),
    Pile([BRIDGE]),
    Pile([CONSPIRATOR]),
    Pile([COPPERSMITH]),
    Pile([COURTIER]),
    Pile([COURTYARD]),
    Pile([DIPLOMAT]),
    Pile([DUKE]),
    Pile([GREAT_HALL]),
    Pile([FARM]),
    Pile([IRONWORKS]),
    Pile([LURKER]),
    Pile([MASQUERADE]),
    Pile([MILL]),
    Pile([MINING_VILLAGE]),
    Pile([MINION]),
    Pile([NOBLES]),
    Pile([PATROL]),
    Pile([PAWN]),
    Pile([REPLACE]),
    Pile([SABOTEUR]),
    Pile([SCOUT]),
    Pile([SECRET_CHAMBER]),
    Pile([SECRET_PASSAGE]),
    Pile([SHANTY_TOWN]),
    Pile([STEWARD]),
    Pile([SWINDLER]),
    Pile([TORTURER]),
    Pile([TRADING_POST]),
    Pile([TRIBUTE]),
    Pile([UPGRADE]),
    Pile([WISHING_WELL]),
    Pile([AMBASSADOR]),
    Pile([ASTROLABE]),
    Pile([BAZAAR]),
    Pile([BLOCKADE]),
    Pile([CARAVAN]),
    Pile([CORSAIR]),
    Pile([CUTPURSE]),
    Pile([EMBARGO]),
    Pile([EXPLORER]),
    Pile([FISHING_VILLAGE]),
    Pile([GHOST_SHIP]),
    Pile([HAVEN]),
    Pile([ISLAND]),
    Pile([LIGHTHOUSE]),
    Pile([LOOKOUT]),
    Pile([MERCHANT_SHIP]),
    Pile([MONKEY]),
    Pile([NATIVE_VILLAGE]),
    Pile([NAVIGATOR]),
    Pile([OUTPOST]),
    Pile([PEARL_DIVER]),
    Pile([PIRATE]),
    Pile([PIRATE_SHIP]),
    Pile([SAILOR]),
    Pile([SALVAGER]),
    Pile([SEA_CHART]),
    Pile([SEA_HAG]),
    Pile([SEA_WITCH]),
    Pile([SMUGGLERS]),
    Pile([TACTICIAN]),
    Pile([TIDE_POOLS]),
    Pile([TREASURE_MAP]),
    Pile([TREASURY]),
    Pile([WAREHOUSE]),
    Pile([WHARF]),
    Pile([ALCHEMIST]),
    Pile([APOTHECARY]),
    Pile([APPRENTICE]),
    Pile([FAMILIAR]),
    Pile([GOLEM]),
    Pile([HERBALIST]),
    Pile([PHILOSOPHERS_STONE]),
    Pile([POSSESSION]),
    Pile([SCRYING_POOL]),
    Pile([TRANSMUTE]),
    Pile([UNIVERSITY]),
    Pile([VINEYARD]),
    Pile([ANVIL]),
    Pile([BANK]),
    Pile([BISHOP]),
    Pile([CHARLATAN]),
    Pile([CITY]),
    Pile([CLERK]),
    Pile([COLLECTION]),
    Pile([CONTRABAND]),
    Pile([COUNTING_HOUSE]),
    Pile([CRYSTAL_BALL]),
    Pile([EXPAND]),
    Pile([FORGE]),
    Pile([GOONS]),
    Pile([GRAND_MARKET]),
    Pile([HOARD]),
    Pile([INVESTMENT]),
    Pile([KINGS_COURT]),
    Pile([LOAN]),
    Pile([MAGNATE]),
    Pile([MINT]),
    Pile([MONUMENT]),
    Pile([MOUNTEBANK]),
    Pile([PEDDLER]),
    Pile([QUARRY]),
    Pile([RABBLE]),
    Pile([ROYAL_SEAL]),
    Pile([TALISMAN]),
    Pile([TIARA]),
    Pile([TRADE_ROUTE]),
    Pile([VAULT]),
    Pile([VENTURE]),
    Pile([WAR_CHEST]),
    Pile([WATCHTOWER]),
    Pile([WORKERS_VILLAGE]),
    Pile([ADVISOR]),
    Pile([BAKER]),
    Pile([BUTCHER]),
    Pile([CANDLESTICK_MAKER]),
    Pile([CARNIVAL]),
    Pile([DOCTOR]),
    Pile([FAIRGROUNDS]),
    Pile([FARMHANDS]),
    Pile([FARMING_VILLAGE]),
    Pile([FARRIER]),
    Pile([FERRYMAN]),
    Pile([FOOTPAD]),
    Pile([FORTUNE_TELLER]),
    Pile([HAMLET]),
    Pile([HARVEST]),
    Pile([HERALD]),
    Pile([HORN_OF_PLENTY]),
    Pile([HORSE_TRADERS]),
    Pile([HUNTING_PARTY]),
    Pile([INFIRMARY]),
    Pile([JESTER]),
    Pile([JOURNEYMAN]),
    Pile([JOUST]),
    Pile([MASTERPIECE]),
    Pile([MENAGERIE]),
    Pile([MERCHANT_GUILD]),
    Pile([PLAZA]),
    Pile([REMAKE]),
    Pile([SHOP]),
    Pile([SOOTHSAYER]),
    Pile([STONEMASON]),
    Pile([TAXMAN]),
    Pile([TOURNAMENT]),
    Pile([YOUNG_WITCH]),
    Pile([BERSERKER]),
    Pile([BORDER_VILLAGE]),
    Pile([CACHE]),
    Pile([CARTOGRAPHER]),
    Pile([CAULDRON]),
    Pile([CROSSROADS]),
    Pile([DEVELOP]),
    Pile([DUCHESS]),
    Pile([EMBASSY]),
    Pile([FARMLAND]),
    Pile([FOOLS_GOLD]),
    Pile([GUARD_DOG]),
    Pile([HAGGLER]),
    Pile([HIGHWAY]),
    Pile([ILL_GOTTEN_GAINS]),
    Pile([INN]),
    Pile([JACK_OF_ALL_TRADES]),
    Pile([MANDARIN]),
    Pile([MARGRAVE]),
    Pile([NOBLE_BRIGAND]),
    Pile([NOMAD_CAMP]),
    Pile([NOMADS]),
    Pile([OASIS]),
    Pile([ORACLE]),
    Pile([SCHEME]),
    Pile([SILK_ROAD]),
    Pile([SOUK]),
    Pile([SPICE_MERCHANT]),
    Pile([STABLES]),
    Pile([TRADER]),
    Pile([TRAIL]),
    Pile([TUNNEL]),
    Pile([WEAVER]),
    Pile([WHEELWRIGHT]),
    Pile([WITCHS_HUT]),
    Pile([ALTAR]),
    Pile([ARMORY]),
    Pile([BAND_OF_MISFITS]),
    Pile([BANDIT_CAMP]),
    Pile([BEGGAR]),
    Pile([CATACOMBS]),
    Pile([COUNT]),
    Pile([COUNTERFEIT]),
    Pile([CULTIST]),
    Pile([SIR_MARTIN, DAME_ANNA, DAME_JOSEPHINE, DAME_MOLLY, DAME_NATALIE, DAME_SYLVIA, SIR_BAILEY, SIR_DESTRY, SIR_MICHAEL, SIR_VANDER], "Knights"),
    Pile([DEATH_CART]),
    Pile([FEODUM]),
    Pile([FORAGER]),
    Pile([FORTRESS]),
    Pile([GRAVEROBBER]),
    Pile([HERMIT]),
    Pile([HUNTING_GROUNDS]),
    Pile([IRONMONGER]),
    Pile([JUNK_DEALER]),
    Pile([MARAUDER]),
    Pile([MARKET_SQUARE]),
    Pile([MYSTIC]),
    Pile([PILLAGE]),
    Pile([POOR_HOUSE]),
    Pile([PROCESSION]),
    Pile([RATS]),
    Pile([REBUILD]),
    Pile([ROGUE]),
    Pile([SAGE]),
    Pile([SCAVENGER]),
    Pile([SQUIRE]),
    Pile([STOREROOM]),
    Pile([URCHIN]),
    Pile([VAGRANT]),
    Pile([WANDERING_MINSTREL]),
    Pile([AMULET]),
    Pile([ARTIFICER]),
    Pile([BRIDGE_TROLL]),
    Pile([CARAVAN_GUARD]),
    Pile([COIN_OF_THE_REALM]),
    Pile([DISTANT_LANDS]),
    Pile([DUNGEON]),
    Pile([DUPLICATE]),
    Pile([GEAR]),
    Pile([GIANT]),
    Pile([GUIDE]),
    Pile([HAUNTED_WOODS]),
    Pile([HIRELING]),
    Pile([LOST_CITY]),
    Pile([MAGPIE]),
    Pile([MESSENGER]),
    Pile([MISER]),
    Pile([PAGE]),
    Pile([PEASANT]),
    Pile([PORT]),
    Pile([RANGER]),
    Pile([RATCATCHER]),
    Pile([RAZE]),
    Pile([RELIC]),
    Pile([ROYAL_CARRIAGE]),
    Pile([STORYTELLER]),
    Pile([SWAMP_HAG]),
    Pile([TRANSMOGRIFY]),
    Pile([TREASURE_TROVE]),
    Pile([WINE_MERCHANT]),
    Pile([ARCHIVE]),
    Pile([SETTLERS, BUSTLING_VILLAGE], "Settlers/Bustling Village"),
    Pile([CAPITAL]),
    Pile([CATAPULT, ROCKS], "Catapult/Rocks"),
    Pile([CHARIOT_RACE]),
    Pile([CHARM]),
    Pile([CITY_QUARTER]),
    Pile([CROWN]),
    Pile([HUMBLE_CASTLE, CRUMBLING_CASTLE, SMALL_CASTLE, HAUNTED_CASTLE, OPULENT_CASTLE, SPRAWLING_CASTLE, GRAND_CASTLE, KINGS_CASTLE], "Castles"),
    Pile([PATRICIAN, EMPORIUM], "Patrician/Emporium"),
    Pile([ENCAMPMENT, PLUNDER], "Encampment/Plunder"),
    Pile([ENCHANTRESS]),
    Pile([ENGINEER]),
    Pile([FARMERS_MARKET]),
    Pile([GLADIATOR, FORTUNE], "Gladiator/Fortune"),
    Pile([FORUM]),
    Pile([GROUNDSKEEPER]),
    Pile([LEGIONARY]),
    Pile([OVERLORD]),
    Pile([ROYAL_BLACKSMITH]),
    Pile([SACRIFICE]),
    Pile([TEMPLE]),
    Pile([VILLA]),
    Pile([WILD_HUNT]),
    Pile([BARD]),
    Pile([BLESSED_VILLAGE]),
    Pile([CEMETERY]),
    Pile([CHANGELING]),
    Pile([COBBLER]),
    Pile([CONCLAVE]),
    Pile([CRYPT]),
    Pile([CURSED_VILLAGE]),
    Pile([DEN_OF_SIN]),
    Pile([DEVILS_WORKSHOP]),
    Pile([DRUID]),
    Pile([EXORCIST]),
    Pile([FAITHFUL_HOUND]),
    Pile([FOOL]),
    Pile([GHOST_TOWN]),
    Pile([GUARDIAN]),
    Pile([IDOL]),
    Pile([LEPRECHAUN]),
    Pile([MONASTERY]),
    Pile([NECROMANCER]),
    Pile([NIGHT_WATCHMAN]),
    Pile([PIXIE]),
    Pile([POOKA]),
    Pile([RAIDER]),
    Pile([SACRED_GROVE]),
    Pile([SECRET_CAVE]),
    Pile([SHEPHERD]),
    Pile([SKULK]),
    Pile([TORMENTOR]),
    Pile([TRACKER]),
    Pile([TRAGIC_HERO]),
    Pile([VAMPIRE]),
    Pile([WEREWOLF]),
    Pile([ACTING_TROUPE]),
    Pile([BORDER_GUARD]),
    Pile([CARGO_SHIP]),
    Pile([DUCAT]),
    Pile([EXPERIMENT]),
    Pile([FLAG_BEARER]),
    Pile([HIDEOUT]),
    Pile([IMPROVE]),
    Pile([INVENTOR]),
    Pile([LACKEYS]),
    Pile([MOUNTAIN_VILLAGE]),
    Pile([OLD_WITCH]),
    Pile([PATRON]),
    Pile([PRIEST]),
    Pile([RECRUITER]),
    Pile([RESEARCH]),
    Pile([SCEPTER]),
    Pile([SCHOLAR]),
    Pile([SCULPTOR]),
    Pile([SEER]),
    Pile([SILK_MERCHANT]),
    Pile([SPICES]),
    Pile([SWASHBUCKLER]),
    Pile([TREASURER]),
    Pile([VILLAIN]),
    Pile([ANIMAL_FAIR]),
    Pile([BARGE]),
    Pile([BLACK_CAT]),
    Pile([BOUNTY_HUNTER]),
    Pile([CAMEL_TRAIN]),
    Pile([CARDINAL]),
    Pile([CAVALRY]),
    Pile([COVEN]),
    Pile([DESTRIER]),
    Pile([DISPLACE]),
    Pile([FALCONER]),
    Pile([FISHERMAN]),
    Pile([GATEKEEPER]),
    Pile([GOATHERD]),
    Pile([GROOM]),
    Pile([HOSTELRY]),
    Pile([HUNTING_LODGE]),
    Pile([KILN]),
    Pile([LIVERY]),
    Pile([MASTERMIND]),
    Pile([PADDOCK]),
    Pile([SANCTUARY]),
    Pile([SCRAP]),
    Pile([SHEEPDOG]),
    Pile([SLEIGH]),
    Pile([SNOWY_VILLAGE]),
    Pile([STOCKPILE]),
    Pile([SUPPLIES]),
    Pile([VILLAGE_GREEN]),
    Pile([WAYFARER]),
    Pile([HERB_GATHERER, ACOLYTE, SORCERESS, SIBYL], "Augurs"),
    Pile([BATTLE_PLAN, ARCHER, WARLORD, TERRITORY], "Clashes"),
    Pile([BARBARIAN]),
    Pile([BAUBLE]),
    Pile([TOWN_CRIER, BLACKSMITH, MILLER, ELDER], "Townsfolk"),
    Pile([BROKER]),
    Pile([CAPITAL_CITY]),
    Pile([CARPENTER]),
    Pile([STUDENT, CONJURER, SORCERER, LICH], "Wizards"),
    Pile([CONTRACT]),
    Pile([COURIER]),
    Pile([OLD_MAP, VOYAGE, SUNKEN_TREASURE, DISTANT_SHORE], "Odysseys"),
    Pile([EMISSARY]),
    Pile([GALLERIA]),
    Pile([TENT, GARRISON, HILL_FORT, STRONGHOLD], "Forts"),
    Pile([GUILDMASTER]),
    Pile([HIGHWAYMAN]),
    Pile([HUNTER]),
    Pile([IMPORTER]),
    Pile([INNKEEPER]),
    Pile([MARQUIS]),
    Pile([MERCHANT_CAMP]),
    Pile([MODIFY]),
    Pile([ROYAL_GALLEY]),
    Pile([SENTINEL]),
    Pile([SKIRMISHER]),
    Pile([SPECIALIST]),
    Pile([SWAP]),
    Pile([SYCOPHANT]),
    Pile([TOWN]),
    Pile([UNDERLING]),
    Pile([ABUNDANCE]),
    Pile([BURIED_TREASURE]),
    Pile([CABIN_BOY]),
    Pile([CAGE]),
    Pile([CREW]),
    Pile([CRUCIBLE]),
    Pile([CUTTHROAT]),
    Pile([ENLARGE]),
    Pile([FIGURINE]),
    Pile([FIRST_MATE]),
    Pile([FLAGSHIP]),
    Pile([FORTUNE_HUNTER]),
    Pile([FRIGATE]),
    Pile([GONDOLA]),
    Pile([GROTTO]),
    Pile([HARBOR_VILLAGE]),
    Pile([JEWELLED_EGG]),
    Pile([KINGS_CACHE]),
    Pile([LANDING_PARTY]),
    Pile([LONGSHIP]),
    Pile([MAPMAKER]),
    Pile([MAROON]),
    Pile([MINING_ROAD]),
    Pile([PENDANT]),
    Pile([PICKAXE]),
    Pile([PILGRIM]),
    Pile([QUARTERMASTER]),
    Pile([ROPE]),
    Pile([SACK_OF_LOOT]),
    Pile([SEARCH]),
    Pile([SECLUDED_SHRINE]),
    Pile([SHAMAN]),
    Pile([SILVER_MINE]),
    Pile([SIREN]),
    Pile([STOWAWAY]),
    Pile([SWAMP_SHACKS]),
    Pile([TASKMASTER]),
    Pile([TOOLS]),
    Pile([TRICKSTER]),
    Pile([WEALTHY_VILLAGE]),
    Pile([ALLEY]),
    Pile([ARISTOCRAT]),
    Pile([ARTIST]),
    Pile([CHANGE]),
    Pile([CRAFTSMAN]),
    Pile([DAIMYO]),
    Pile([FISHMONGER]),
    Pile([GOLD_MINE]),
    Pile([IMPERIAL_ENVOY]),
    Pile([KITSUNE]),
    Pile([LITTER]),
    Pile([MOUNTAIN_SHRINE]),
    Pile([NINJA]),
    Pile([POET]),
    Pile([RICE]),
    Pile([RICE_BROKER]),
    Pile([RIVER_SHRINE]),
    Pile([RIVERBOAT]),
    Pile([RONIN]),
    Pile([ROOT_CELLAR]),
    Pile([RUSTIC_VILLAGE]),
    Pile([SAMURAI]),
    Pile([SNAKE_WITCH]),
    Pile([TANUKI]),
    Pile([TEA_HOUSE]),
    Pile([SAUNA, AVANTO], "Sauna/Avanto"),
    Pile([BLACK_MARKET]),
    Pile([CAPTAIN]),
    Pile([CHURCH]),
    Pile([DISMANTLE]),
    Pile([ENVOY]),
    Pile([GOVERNOR]),
    Pile([MARCHLAND]),
    Pile([PRINCE]),
    Pile([STASH]),
    Pile([WALLED_VILLAGE]),
]
