from .base import CardShapedThing, Cost

ADVENTURER = CardShapedThing("Adventurer", {"Action"}, Cost(coins=6), "Reveal cards from your deck until you reveal 2 Treasure cards. Put those Treasure cards into your hand and discard the other revealed cards.", "https://wiki.dominionstrategy.com/index.php/Adventurer")
ARTISAN = CardShapedThing("Artisan", {"Action"}, Cost(coins=6), "Gain a card to your hand costing up to $5.Put a card from your hand onto your deck.", "https://wiki.dominionstrategy.com/index.php/Artisan")
BANDIT = CardShapedThing("Bandit", {"Action", "Attack"}, Cost(coins=5), "Gain a Gold. Each other player reveals the top 2 cards of their deck, trashes a revealed Treasure other than Copper, and discards the rest.", "https://wiki.dominionstrategy.com/index.php/Bandit")
BUREAUCRAT = CardShapedThing("Bureaucrat", {"Action", "Attack"}, Cost(coins=4), "Gain a Silver onto your deck. Each other player reveals a Victory card from their hand and puts it onto their deck (or reveals a hand with no Victory cards).", "https://wiki.dominionstrategy.com/index.php/Bureaucrat")
CELLAR = CardShapedThing("Cellar", {"Action"}, Cost(coins=2), "+1 ActionDiscard any number of cards. +1 Card per card discarded.", "https://wiki.dominionstrategy.com/index.php/Cellar")
CHANCELLOR = CardShapedThing("Chancellor", {"Action"}, Cost(coins=3), "+$2You may immediately put your deck into your discard pile.", "https://wiki.dominionstrategy.com/index.php/Chancellor")
CHAPEL = CardShapedThing("Chapel", {"Action"}, Cost(coins=2), "Trash up to 4 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Chapel")
COUNCIL_ROOM = CardShapedThing("Council Room", {"Action"}, Cost(coins=5), "+4 Cards+1 BuyEach other player draws a card.", "https://wiki.dominionstrategy.com/index.php/Council_Room")
FEAST = CardShapedThing("Feast", {"Action"}, Cost(coins=4), "Trash this card. Gain a card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Feast")
FESTIVAL = CardShapedThing("Festival", {"Action"}, Cost(coins=5), "+2 Actions+1 Buy+$2", "https://wiki.dominionstrategy.com/index.php/Festival")
GARDENS = CardShapedThing("Gardens", {"Victory"}, Cost(coins=4), "Worth 1VP per 10 cards you have (round down).", "https://wiki.dominionstrategy.com/index.php/Gardens")
HARBINGER = CardShapedThing("Harbinger", {"Action"}, Cost(coins=3), "+1 Card+1 ActionLook through your discard pile. You may put a card from it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Harbinger")
LABORATORY = CardShapedThing("Laboratory", {"Action"}, Cost(coins=5), "+2 Cards+1 Action", "https://wiki.dominionstrategy.com/index.php/Laboratory")
LIBRARY = CardShapedThing("Library", {"Action"}, Cost(coins=5), "Draw until you have 7 cards in hand, skipping any Action cards you choose to; set those aside, discarding them afterwards.", "https://wiki.dominionstrategy.com/index.php/Library")
MARKET = CardShapedThing("Market", {"Action"}, Cost(coins=5), "+1 Card+1 Action+1 Buy+$1", "https://wiki.dominionstrategy.com/index.php/Market")
MERCHANT = CardShapedThing("Merchant", {"Action"}, Cost(coins=3), "+1 Card+1 ActionThe first time you play a Silver this turn, +$1.", "https://wiki.dominionstrategy.com/index.php/Merchant")
MILITIA = CardShapedThing("Militia", {"Action", "Attack"}, Cost(coins=4), "+$2Each other player discards down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Militia")
MINE = CardShapedThing("Mine", {"Action"}, Cost(coins=5), "You may trash a Treasure from your hand. Gain a Treasure to your hand costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Mine")
MOAT = CardShapedThing("Moat", {"Action", "Reaction"}, Cost(coins=2), "+2 CardsWhen another player plays an Attack card, you may first reveal this from your hand, to be unaffected by it.", "https://wiki.dominionstrategy.com/index.php/Moat")
MONEYLENDER = CardShapedThing("Moneylender", {"Action"}, Cost(coins=4), "You may trash a Copper from your hand for +$3.", "https://wiki.dominionstrategy.com/index.php/Moneylender")
POACHER = CardShapedThing("Poacher", {"Action"}, Cost(coins=4), "+1 Card+1 Action+$1Discard a card per empty Supply pile.", "https://wiki.dominionstrategy.com/index.php/Poacher")
REMODEL = CardShapedThing("Remodel", {"Action"}, Cost(coins=4), "Trash a card from your hand. Gain a card costing up to $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Remodel")
SENTRY = CardShapedThing("Sentry", {"Action"}, Cost(coins=5), "+1 Card+1 ActionLook at the top 2 cards of your deck. Trash and/or discard any number of them. Put the rest back on top in any order.", "https://wiki.dominionstrategy.com/index.php/Sentry")
SMITHY = CardShapedThing("Smithy", {"Action"}, Cost(coins=4), "+3 Cards", "https://wiki.dominionstrategy.com/index.php/Smithy")
SPY = CardShapedThing("Spy", {"Action", "Attack"}, Cost(coins=4), "+1 Card+1 ActionEach player (including you) reveals the top card of their deck and either discards it or puts it back, your choice.", "https://wiki.dominionstrategy.com/index.php/Spy")
THIEF = CardShapedThing("Thief", {"Action", "Attack"}, Cost(coins=4), "Each other player reveals the top 2 cards of their deck. If they revealed any Treasure cards, they trash one of them that you choose. You may gain any or all of these trashed cards. They discard the other revealed cards.", "https://wiki.dominionstrategy.com/index.php/Thief")
THRONE_ROOM = CardShapedThing("Throne Room", {"Action"}, Cost(coins=4), "You may play an Action card from your hand twice.", "https://wiki.dominionstrategy.com/index.php/Throne_Room")
VASSAL = CardShapedThing("Vassal", {"Action"}, Cost(coins=3), "+$2Discard the top card of your deck. If it's an Action card, you may play it.", "https://wiki.dominionstrategy.com/index.php/Vassal")
VILLAGE = CardShapedThing("Village", {"Action"}, Cost(coins=3), "+1 Card+2 Actions", "https://wiki.dominionstrategy.com/index.php/Village")
WITCH = CardShapedThing("Witch", {"Action", "Attack"}, Cost(coins=5), "+2 CardsEach other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Witch")
WOODCUTTER = CardShapedThing("Woodcutter", {"Action"}, Cost(coins=3), "+1 Buy+$2", "https://wiki.dominionstrategy.com/index.php/Woodcutter")
WORKSHOP = CardShapedThing("Workshop", {"Action"}, Cost(coins=3), "Gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Workshop")
COPPER = CardShapedThing("Copper", {"Treasure"}, Cost(coins=0), "$1", "https://wiki.dominionstrategy.com/index.php/Copper")
SILVER = CardShapedThing("Silver", {"Treasure"}, Cost(coins=3), "$2", "https://wiki.dominionstrategy.com/index.php/Silver")
GOLD = CardShapedThing("Gold", {"Treasure"}, Cost(coins=6), "$3", "https://wiki.dominionstrategy.com/index.php/Gold")
ESTATE = CardShapedThing("Estate", {"Victory"}, Cost(coins=2), "1VP", "https://wiki.dominionstrategy.com/index.php/Estate")
DUCHY = CardShapedThing("Duchy", {"Victory"}, Cost(coins=5), "3VP", "https://wiki.dominionstrategy.com/index.php/Duchy")
PROVINCE = CardShapedThing("Province", {"Victory"}, Cost(coins=8), "6VP", "https://wiki.dominionstrategy.com/index.php/Province")
CURSE = CardShapedThing("Curse", {"Curse"}, Cost(coins=0), "-1VP", "https://wiki.dominionstrategy.com/index.php/Curse")
BARON = CardShapedThing("Baron", {"Action"}, Cost(coins=4), "+1 BuyYou may discard an Estate for +$4. If you don't, gain an Estate.", "https://wiki.dominionstrategy.com/index.php/Baron")
BRIDGE = CardShapedThing("Bridge", {"Action"}, Cost(coins=4), "+1 Buy+$1This turn, cards (everywhere) cost $1 less.", "https://wiki.dominionstrategy.com/index.php/Bridge")
CONSPIRATOR = CardShapedThing("Conspirator", {"Action"}, Cost(coins=4), "+$2If you've played 3 or more Actions this turn (counting this), +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Conspirator")
COPPERSMITH = CardShapedThing("Coppersmith", {"Action"}, Cost(coins=4), "Copper produces an extra $1 this turn.", "https://wiki.dominionstrategy.com/index.php/Coppersmith")
COURTIER = CardShapedThing("Courtier", {"Action"}, Cost(coins=5), "Reveal a card from your hand. For each type it has (Action, Attack, etc.), choose one: +1 Action; or +1 Buy; or +$3; or gain a Gold. The choices must be different.", "https://wiki.dominionstrategy.com/index.php/Courtier")
COURTYARD = CardShapedThing("Courtyard", {"Action"}, Cost(coins=2), "+3 CardsPut a card from your hand onto your deck.", "https://wiki.dominionstrategy.com/index.php/Courtyard")
DIPLOMAT = CardShapedThing("Diplomat", {"Action", "Reaction"}, Cost(coins=4), "+2 CardsIf you have 5 or fewer cards in hand (after drawing), +2 Actions.When another player plays an Attack card, you may first reveal this from a hand of 5 or more cards, to draw 2 cards then discard 3.", "https://wiki.dominionstrategy.com/index.php/Diplomat")
DUKE = CardShapedThing("Duke", {"Victory"}, Cost(coins=5), "Worth 1VP per Duchy you have.", "https://wiki.dominionstrategy.com/index.php/Duke")
GREAT_HALL = CardShapedThing("Great Hall", {"Action", "Victory"}, Cost(coins=3), "+1 Card+1 Action1VP", "https://wiki.dominionstrategy.com/index.php/Great_Hall")
FARM = CardShapedThing("Farm", {"Treasure", "Victory"}, Cost(coins=6), "$22VP", "https://wiki.dominionstrategy.com/index.php/Farm")
IRONWORKS = CardShapedThing("Ironworks", {"Action"}, Cost(coins=4), "Gain a card costing up to $4.If the gained card is an…Action card, +1 ActionTreasure card, +$1Victory card, +1 Card", "https://wiki.dominionstrategy.com/index.php/Ironworks")
LURKER = CardShapedThing("Lurker", {"Action"}, Cost(coins=2), "+1 ActionChoose one: Trash an Action card from the Supply; or gain an Action card from the trash.", "https://wiki.dominionstrategy.com/index.php/Lurker")
MASQUERADE = CardShapedThing("Masquerade", {"Action"}, Cost(coins=3), "+2 CardsEach player with any cards in hand passes one to the next such player to their left, at once. Then you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Masquerade")
MILL = CardShapedThing("Mill", {"Action", "Victory"}, Cost(coins=4), "+1 Card+1 ActionYou may discard 2 cards. If you do, +$2.1VP", "https://wiki.dominionstrategy.com/index.php/Mill")
MINING_VILLAGE = CardShapedThing("Mining Village", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsYou may trash this for +$2.", "https://wiki.dominionstrategy.com/index.php/Mining_Village")
MINION = CardShapedThing("Minion", {"Action", "Attack"}, Cost(coins=5), "+1 ActionChoose one: +$2; or discard your hand, +4 Cards, and each other player with at least 5 cards in hand discards their hand and draws 4 cards.", "https://wiki.dominionstrategy.com/index.php/Minion")
NOBLES = CardShapedThing("Nobles", {"Action", "Victory"}, Cost(coins=6), "Choose one: +3 Cards; or +2 Actions.2VP", "https://wiki.dominionstrategy.com/index.php/Nobles")
PATROL = CardShapedThing("Patrol", {"Action"}, Cost(coins=5), "+3 CardsReveal the top 4 cards of your deck. Put the Victory cards and Curses into your hand. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Patrol")
PAWN = CardShapedThing("Pawn", {"Action"}, Cost(coins=2), "Choose two: +1 Card; +1 Action; +1 Buy; +$1. The choices must be different.", "https://wiki.dominionstrategy.com/index.php/Pawn")
REPLACE = CardShapedThing("Replace", {"Action", "Attack"}, Cost(coins=5), "Trash a card from your hand. Gain a card costing up to $2 more than it. If the gained card is an Action or Treasure, put it onto your deck; if it's a Victory card, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Replace")
SABOTEUR = CardShapedThing("Saboteur", {"Action", "Attack"}, Cost(coins=5), "Each other player reveals cards from the top of their deck until revealing one costing $3 or more. They trash that card and may gain a card costing at most $2 less than it. They discard the other revealed cards.", "https://wiki.dominionstrategy.com/index.php/Saboteur")
SCOUT = CardShapedThing("Scout", {"Action"}, Cost(coins=4), "+1 ActionReveal the top 4 cards of your deck. Put the revealed Victory cards into your hand. Put the other cards on top of your deck in any order.", "https://wiki.dominionstrategy.com/index.php/Scout")
SECRET_CHAMBER = CardShapedThing("Secret Chamber", {"Action", "Reaction"}, Cost(coins=2), "Discard any number of cards. +$1 per card discarded.When another player plays an Attack card, you may reveal this from your hand. If you do, +2 Cards, then put 2 cards from your hand on top of your deck.", "https://wiki.dominionstrategy.com/index.php/Secret_Chamber")
SECRET_PASSAGE = CardShapedThing("Secret Passage", {"Action"}, Cost(coins=4), "+2 Cards+1 ActionTake a card from your hand and put it anywhere in your deck.", "https://wiki.dominionstrategy.com/index.php/Secret_Passage")
SHANTY_TOWN = CardShapedThing("Shanty Town", {"Action"}, Cost(coins=3), "+2 ActionsReveal your hand. If you have no Action cards in hand, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Shanty_Town")
STEWARD = CardShapedThing("Steward", {"Action"}, Cost(coins=3), "Choose one: +2 Cards; or +$2; or trash 2 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Steward")
SWINDLER = CardShapedThing("Swindler", {"Action", "Attack"}, Cost(coins=3), "+$2Each other player trashes the top card of their deck and gains a card with the same cost that you choose.", "https://wiki.dominionstrategy.com/index.php/Swindler")
TORTURER = CardShapedThing("Torturer", {"Action", "Attack"}, Cost(coins=5), "+3 CardsEach other player either discards 2 cards or gains a Curse to their hand, their choice. (They may pick an option they can't do.)", "https://wiki.dominionstrategy.com/index.php/Torturer")
TRADING_POST = CardShapedThing("Trading Post", {"Action"}, Cost(coins=5), "Trash 2 cards from your hand. If you did, gain a Silver to your hand.", "https://wiki.dominionstrategy.com/index.php/Trading_Post")
TRIBUTE = CardShapedThing("Tribute", {"Action"}, Cost(coins=5), "The player to your left reveals then discards the top 2 cards of their deck. For each differently named card revealed, if it is an…Action Card, +2 ActionsTreasure Card, +$2Victory Card, +2 Cards", "https://wiki.dominionstrategy.com/index.php/Tribute")
UPGRADE = CardShapedThing("Upgrade", {"Action"}, Cost(coins=5), "+1 Card+1 ActionTrash a card from your hand. Gain a card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Upgrade")
WISHING_WELL = CardShapedThing("Wishing Well", {"Action"}, Cost(coins=3), "+1 Card+1 ActionName a card, then reveal the top card of your deck. If you named it, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Wishing_Well")
AMBASSADOR = CardShapedThing("Ambassador", {"Action", "Attack"}, Cost(coins=3), "Reveal a card from your hand. Return up to 2 copies of it from your hand to the Supply. Then each other player gains a copy of it.", "https://wiki.dominionstrategy.com/index.php/Ambassador")
ASTROLABE = CardShapedThing("Astrolabe", {"Treasure", "Duration"}, Cost(coins=3), "Now and at the start of your next turn:$1+1 Buy", "https://wiki.dominionstrategy.com/index.php/Astrolabe")
BAZAAR = CardShapedThing("Bazaar", {"Action"}, Cost(coins=5), "+1 Card+2 Actions+$1", "https://wiki.dominionstrategy.com/index.php/Bazaar")
BLOCKADE = CardShapedThing("Blockade", {"Action", "Duration", "Attack"}, Cost(coins=4), "Gain a card costing up to $4, setting it aside.At the start of your next turn, put it into your hand. While it's set aside, when another player gains a copy of it on their turn, they gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Blockade")
CARAVAN = CardShapedThing("Caravan", {"Action", "Duration"}, Cost(coins=4), "+1 Card+1 ActionAt the start of your next turn, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Caravan")
CORSAIR = CardShapedThing("Corsair", {"Action", "Duration", "Attack"}, Cost(coins=5), "+$2At the start of your next turn, +1 Card. Until then, each other player trashes the first Silver or Gold they play each turn.", "https://wiki.dominionstrategy.com/index.php/Corsair")
CUTPURSE = CardShapedThing("Cutpurse", {"Action", "Attack"}, Cost(coins=4), "+$2Each other player discards a Copper (or reveals a hand with no Copper).", "https://wiki.dominionstrategy.com/index.php/Cutpurse")
EMBARGO = CardShapedThing("Embargo", {"Action"}, Cost(coins=2), "+$2Trash this to add an Embargo token to a Supply pile. (For the rest of the game, when a player buys a card from that pile, they gain a Curse.)", "https://wiki.dominionstrategy.com/index.php/Embargo")
EXPLORER = CardShapedThing("Explorer", {"Action"}, Cost(coins=5), "You may reveal a Province from your hand. If you do, gain a Gold to your hand. If you don't, gain a Silver to your hand.", "https://wiki.dominionstrategy.com/index.php/Explorer")
FISHING_VILLAGE = CardShapedThing("Fishing Village", {"Action", "Duration"}, Cost(coins=3), "+2 Actions+$1At the start of your next turn: +1 Action and +$1.", "https://wiki.dominionstrategy.com/index.php/Fishing_Village")
GHOST_SHIP = CardShapedThing("Ghost Ship", {"Action", "Attack"}, Cost(coins=5), "+2 CardsEach other player with 4 or more cards in hand puts cards from their hand onto their deck until they have 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Ghost_Ship")
HAVEN = CardShapedThing("Haven", {"Action", "Duration"}, Cost(coins=2), "+1 Card+1 ActionSet aside a card from your hand face down (under this). At the start of your next turn, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Haven")
ISLAND = CardShapedThing("Island", {"Action", "Victory"}, Cost(coins=4), "Put this and a card from your hand onto your Island mat.2VP", "https://wiki.dominionstrategy.com/index.php/Island")
LIGHTHOUSE = CardShapedThing("Lighthouse", {"Action", "Duration"}, Cost(coins=2), "+1 Action+$1At the start of your next turn, +$1. Until then, when another player plays an Attack card, it doesn't affect you.", "https://wiki.dominionstrategy.com/index.php/Lighthouse")
LOOKOUT = CardShapedThing("Lookout", {"Action"}, Cost(coins=3), "+1 ActionLook at the top 3 cards of your deck. Trash one of them. Discard one of them. Put the other one back on top of your deck.", "https://wiki.dominionstrategy.com/index.php/Lookout")
MERCHANT_SHIP = CardShapedThing("Merchant Ship", {"Action", "Duration"}, Cost(coins=5), "Now and at the start of your next turn: +$2.", "https://wiki.dominionstrategy.com/index.php/Merchant_Ship")
MONKEY = CardShapedThing("Monkey", {"Action", "Duration"}, Cost(coins=3), "Until your next turn, when the player to your right gains a card, +1 Card.At the start of your next turn, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Monkey")
NATIVE_VILLAGE = CardShapedThing("Native Village", {"Action"}, Cost(coins=2), "+2 ActionsChoose one: Put the top card of your deck face down on your Native Village mat (you may look at those cards at any time); or put all the cards from your mat into your hand.", "https://wiki.dominionstrategy.com/index.php/Native_Village")
NAVIGATOR = CardShapedThing("Navigator", {"Action"}, Cost(coins=4), "+$2Look at the top 5 cards of your deck. Either discard them all, or put them back in any order.", "https://wiki.dominionstrategy.com/index.php/Navigator")
OUTPOST = CardShapedThing("Outpost", {"Action", "Duration"}, Cost(coins=5), "You only draw 3 cards for your next hand. Take an extra turn after this one (but not a 3rd turn in a row).", "https://wiki.dominionstrategy.com/index.php/Outpost")
PEARL_DIVER = CardShapedThing("Pearl Diver", {"Action"}, Cost(coins=2), "+1 Card+1 ActionLook at the bottom card of your deck. You may put it on top.", "https://wiki.dominionstrategy.com/index.php/Pearl_Diver")
PIRATE = CardShapedThing("Pirate", {"Action", "Duration", "Reaction"}, Cost(coins=5), "At the start of your next turn, gain a Treasure costing up to $6 to your hand.When any player gains a Treasure, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Pirate")
PIRATE_SHIP = CardShapedThing("Pirate Ship", {"Action", "Attack"}, Cost(coins=4), "Choose one: +$1 per Coin token on your Pirate Ship mat; or each other player reveals the top 2 cards of their deck, trashes one of those Treasures that you choose, and discards the rest, and then if anyone trashed a Treasure, you add a Coin token to your Pirate Ship mat.", "https://wiki.dominionstrategy.com/index.php/Pirate_Ship")
SAILOR = CardShapedThing("Sailor", {"Action", "Duration"}, Cost(coins=4), "+1 ActionOnce this turn, when you gain a Duration card, you may play it.At the start of your next turn, +$2 and you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Sailor")
SALVAGER = CardShapedThing("Salvager", {"Action"}, Cost(coins=4), "+1 BuyTrash a card from your hand. +$1 per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Salvager")
SEA_CHART = CardShapedThing("Sea Chart", {"Action"}, Cost(coins=3), "+1 Card+1 ActionReveal the top card of your deck. If you have a copy of it in play, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Sea_Chart")
SEA_HAG = CardShapedThing("Sea Hag", {"Action", "Attack"}, Cost(coins=4), "Each other player discards the top card of their deck, then gains a Curse onto their deck.", "https://wiki.dominionstrategy.com/index.php/Sea_Hag")
SEA_WITCH = CardShapedThing("Sea Witch", {"Action", "Duration", "Attack"}, Cost(coins=5), "+2 CardsEach other player gains a Curse.At the start of your next turn, +2 Cards, then discard 2 cards.", "https://wiki.dominionstrategy.com/index.php/Sea_Witch")
SMUGGLERS = CardShapedThing("Smugglers", {"Action"}, Cost(coins=3), "Gain a copy of a card costing up to $6 that the player to your right gained on their last turn.", "https://wiki.dominionstrategy.com/index.php/Smugglers")
TACTICIAN = CardShapedThing("Tactician", {"Action", "Duration"}, Cost(coins=5), "If you have at least one card in hand: Discard your hand, and at the start of your next turn, +5 Cards, +1 Action, and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Tactician")
TIDE_POOLS = CardShapedThing("Tide Pools", {"Action", "Duration"}, Cost(coins=4), "+3 Cards+1 ActionAt the start of your next turn, discard 2 cards.", "https://wiki.dominionstrategy.com/index.php/Tide_Pools")
TREASURE_MAP = CardShapedThing("Treasure Map", {"Action"}, Cost(coins=4), "Trash this and a Treasure Map from your hand. If you trashed two Treasure Maps, gain 4 Golds onto your deck.", "https://wiki.dominionstrategy.com/index.php/Treasure_Map")
TREASURY = CardShapedThing("Treasury", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1At the end of your Buy phase this turn, if you didn't gain a Victory card in it, you may put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Treasury")
WAREHOUSE = CardShapedThing("Warehouse", {"Action"}, Cost(coins=3), "+3 Cards+1 ActionDiscard 3 cards.", "https://wiki.dominionstrategy.com/index.php/Warehouse")
WHARF = CardShapedThing("Wharf", {"Action", "Duration"}, Cost(coins=5), "Now and at the start of your next turn: +2 Cards and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Wharf")
ALCHEMIST = CardShapedThing("Alchemist", {"Action"}, Cost(coins=3, potions=1), "+2 Cards+1 ActionAt the start of Clean-up this turn, if you have a Potion in play, you may put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Alchemist")
APOTHECARY = CardShapedThing("Apothecary", {"Action"}, Cost(coins=2, potions=1), "+1 Card+1 ActionReveal the top 4 cards of your deck. Put the Coppers and Potions into your hand. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Apothecary")
APPRENTICE = CardShapedThing("Apprentice", {"Action"}, Cost(coins=5), "+1 ActionTrash a card from your hand.+1 Card per $1 it costs.+2 Cards if it has P in its cost.", "https://wiki.dominionstrategy.com/index.php/Apprentice")
FAMILIAR = CardShapedThing("Familiar", {"Action", "Attack"}, Cost(coins=3, potions=1), "+1 Card+1 ActionEach other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Familiar")
GOLEM = CardShapedThing("Golem", {"Action"}, Cost(coins=4, potions=1), "Reveal cards from your deck until you reveal 2 Action cards other than Golems. Discard the other cards, then play the Action cards in either order.", "https://wiki.dominionstrategy.com/index.php/Golem")
HERBALIST = CardShapedThing("Herbalist", {"Action"}, Cost(coins=2), "+1 Buy+$1Once this turn, when you discard a Treasure from play, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Herbalist")
PHILOSOPHERS_STONE = CardShapedThing("Philosopher's Stone", {"Treasure"}, Cost(coins=3, potions=1), "Count your deck and discard pile. +$1 per 5 cards total between them (round down).", "https://wiki.dominionstrategy.com/index.php/Philosopher%27s_Stone")
POSSESSION = CardShapedThing("Possession", {"Action"}, Cost(coins=6, potions=1), "The player to your left takes an extra turn after this one (but not a 2nd extra turn in a row), in which you can see all cards they can and make all decisions for them. Any cards or D they would gain on that turn, you gain instead; any cards of theirs that are trashed are set aside and put in their discard pile at end of turn.", "https://wiki.dominionstrategy.com/index.php/Possession")
SCRYING_POOL = CardShapedThing("Scrying Pool", {"Action", "Attack"}, Cost(coins=2, potions=1), "+1 ActionEach player (including you) reveals the top card of their deck and either discards it or puts it back, your choice. Then reveal cards from your deck until revealing one that isn't an Action. Put all of those revealed cards into your hand.", "https://wiki.dominionstrategy.com/index.php/Scrying_Pool")
TRANSMUTE = CardShapedThing("Transmute", {"Action"}, Cost(potions=1), "Trash a card from your hand. If it is an…Action card, gain a DuchyTreasure card, gain a TransmuteVictory card, gain a Gold", "https://wiki.dominionstrategy.com/index.php/Transmute")
UNIVERSITY = CardShapedThing("University", {"Action"}, Cost(coins=2, potions=1), "+2 ActionsYou may gain an Action card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/University")
VINEYARD = CardShapedThing("Vineyard", {"Victory"}, Cost(potions=1), "Worth 1VP per 3 Action cards you have (rounded down).", "https://wiki.dominionstrategy.com/index.php/Vineyard")
POTION = CardShapedThing("Potion", {"Treasure"}, Cost(coins=4), "P", "https://wiki.dominionstrategy.com/index.php/Potion")
ANVIL = CardShapedThing("Anvil", {"Treasure"}, Cost(coins=3), "$1You may discard a Treasure to gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Anvil")
BANK = CardShapedThing("Bank", {"Treasure"}, Cost(coins=7), "+$1 per Treasure card you have in play (counting this).", "https://wiki.dominionstrategy.com/index.php/Bank")
BISHOP = CardShapedThing("Bishop", {"Action"}, Cost(coins=4), "+$1+1VPTrash a card from your hand. +1VP per $2 it costs (round down). Each other player may trash a card from their hand.", "https://wiki.dominionstrategy.com/index.php/Bishop")
CHARLATAN = CardShapedThing("Charlatan", {"Action", "Attack"}, Cost(coins=5), "+$3Each other player gains a Curse.In games using this, Curse is also a Treasure worth $1.", "https://wiki.dominionstrategy.com/index.php/Charlatan")
CITY = CardShapedThing("City", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsIf there are one or more empty Supply piles, +1 Card. If there are two or more, +1 Buy and +$1.", "https://wiki.dominionstrategy.com/index.php/City")
CLERK = CardShapedThing("Clerk", {"Action", "Reaction", "Attack"}, Cost(coins=4), "+$2Each other player with 5 or more cards in hand puts one onto their deck.At the start of your turn, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Clerk")
COLLECTION = CardShapedThing("Collection", {"Treasure"}, Cost(coins=5), "$2+1 BuyThis turn, when you gain an Action card, +1VP.", "https://wiki.dominionstrategy.com/index.php/Collection")
CONTRABAND = CardShapedThing("Contraband", {"Treasure"}, Cost(coins=5), "$3+1 BuyThe player to your left names a card. You can't buy that card this turn.", "https://wiki.dominionstrategy.com/index.php/Contraband")
COUNTING_HOUSE = CardShapedThing("Counting House", {"Action"}, Cost(coins=5), "Look through your discard pile, reveal any number of Coppers from it, and put them into your hand.", "https://wiki.dominionstrategy.com/index.php/Counting_House")
CRYSTAL_BALL = CardShapedThing("Crystal Ball", {"Treasure"}, Cost(coins=5), "$1Look at the top card of your deck. You may trash it, discard it, or, if it's an Action or Treasure, play it.", "https://wiki.dominionstrategy.com/index.php/Crystal_Ball")
EXPAND = CardShapedThing("Expand", {"Action"}, Cost(coins=7), "Trash a card from your hand. Gain a card costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Expand")
FORGE = CardShapedThing("Forge", {"Action"}, Cost(coins=7), "Trash any number of cards from your hand. Gain a card with cost exactly equal to the total cost in $ of the trashed cards.", "https://wiki.dominionstrategy.com/index.php/Forge")
GOONS = CardShapedThing("Goons", {"Action", "Attack"}, Cost(coins=6), "+1 Buy+$2Each other player discards down to 3 cards in hand.While you have this in play, when you buy a card, +1VP.", "https://wiki.dominionstrategy.com/index.php/Goons")
GRAND_MARKET = CardShapedThing("Grand Market", {"Action"}, Cost(coins=6), "+1 Card+1 Action+1 Buy+$2You can't buy this if you have any Coppers in play.", "https://wiki.dominionstrategy.com/index.php/Grand_Market")
HOARD = CardShapedThing("Hoard", {"Treasure"}, Cost(coins=6), "$2This turn, when you gain a Victory card, if you bought it, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Hoard")
INVESTMENT = CardShapedThing("Investment", {"Treasure"}, Cost(coins=4), "Trash a card from your hand. Choose one: +$1; or trash this to reveal your hand for +1VP per differently named Treasure there.", "https://wiki.dominionstrategy.com/index.php/Investment")
KINGS_COURT = CardShapedThing("King's Court", {"Action"}, Cost(coins=7), "You may play an Action card from your hand three times.", "https://wiki.dominionstrategy.com/index.php/King%27s_Court")
LOAN = CardShapedThing("Loan", {"Treasure"}, Cost(coins=3), "$1Reveal cards from your deck until you reveal a Treasure. Discard it or trash it. Discard the other cards.", "https://wiki.dominionstrategy.com/index.php/Loan")
MAGNATE = CardShapedThing("Magnate", {"Action"}, Cost(coins=5), "Reveal your hand. +1 Card per Treasure in it.", "https://wiki.dominionstrategy.com/index.php/Magnate")
MINT = CardShapedThing("Mint", {"Action"}, Cost(coins=5), "You may reveal a Treasure card from your hand. Gain a copy of it.When you gain this, trash all non-Duration Treasures you have in play.", "https://wiki.dominionstrategy.com/index.php/Mint")
MONUMENT = CardShapedThing("Monument", {"Action"}, Cost(coins=4), "+$2+1VP", "https://wiki.dominionstrategy.com/index.php/Monument")
MOUNTEBANK = CardShapedThing("Mountebank", {"Action", "Attack"}, Cost(coins=5), "+$2Each other player may discard a Curse. If they don't, they gain a Curse and a Copper.", "https://wiki.dominionstrategy.com/index.php/Mountebank")
PEDDLER = CardShapedThing("Peddler", {"Action"}, Cost(coins=8), "+1 Card+1 Action+$1During a player's Buy phase, this costs $2 less per Action card they have in play.", "https://wiki.dominionstrategy.com/index.php/Peddler")
QUARRY = CardShapedThing("Quarry", {"Treasure"}, Cost(coins=4), "$1This turn, Actions cost $2 less.", "https://wiki.dominionstrategy.com/index.php/Quarry")
RABBLE = CardShapedThing("Rabble", {"Action", "Attack"}, Cost(coins=5), "+3 CardsEach other player reveals the top 3 cards of their deck, discards the Actions and Treasures, and puts the rest back in any order they choose.", "https://wiki.dominionstrategy.com/index.php/Rabble")
ROYAL_SEAL = CardShapedThing("Royal Seal", {"Treasure"}, Cost(coins=5), "$2While you have this in play, when you gain a card, you may put that card onto your deck.", "https://wiki.dominionstrategy.com/index.php/Royal_Seal")
TALISMAN = CardShapedThing("Talisman", {"Treasure"}, Cost(coins=4), "$1While you have this in play, when you buy a non-Victory card costing $4 or less, gain a copy of it.", "https://wiki.dominionstrategy.com/index.php/Talisman")
TIARA = CardShapedThing("Tiara", {"Treasure"}, Cost(coins=4), "+1 BuyThis turn, when you gain a card, you may put it onto your deck.You may play a Treasure from your hand twice.", "https://wiki.dominionstrategy.com/index.php/Tiara")
TRADE_ROUTE = CardShapedThing("Trade Route", {"Action"}, Cost(coins=3), "+1 BuyTrash a card from your hand. +$1 per Coin token on the Trade Route mat.Setup: Add a Coin token to each Victory Supply pile; move that token to the Trade Route mat when a card is gained from the pile.", "https://wiki.dominionstrategy.com/index.php/Trade_Route")
VAULT = CardShapedThing("Vault", {"Action"}, Cost(coins=5), "+2 CardsDiscard any number of cards for +$1 each.Each other player may discard 2 cards, to draw a card.", "https://wiki.dominionstrategy.com/index.php/Vault")
VENTURE = CardShapedThing("Venture", {"Treasure"}, Cost(coins=5), "$1Reveal cards from your deck until you reveal a Treasure. Discard the other cards. Play that Treasure.", "https://wiki.dominionstrategy.com/index.php/Venture")
WAR_CHEST = CardShapedThing("War Chest", {"Treasure"}, Cost(coins=5), "The player to your left names a card. Gain a card costing up to $5 that hasn't been named for War Chests this turn.", "https://wiki.dominionstrategy.com/index.php/War_Chest")
WATCHTOWER = CardShapedThing("Watchtower", {"Action", "Reaction"}, Cost(coins=3), "Draw until you have 6 cards in hand.When you gain a card, you may reveal this from your hand, to either trash that card or put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Watchtower")
WORKERS_VILLAGE = CardShapedThing("Worker's Village", {"Action"}, Cost(coins=4), "+1 Card+2 Actions+1 Buy", "https://wiki.dominionstrategy.com/index.php/Worker%27s_Village")
PLATINUM = CardShapedThing("Platinum", {"Treasure"}, Cost(coins=9), "$5", "https://wiki.dominionstrategy.com/index.php/Platinum")
COLONY = CardShapedThing("Colony", {"Victory"}, Cost(coins=11), "10VP", "https://wiki.dominionstrategy.com/index.php/Colony")
ADVISOR = CardShapedThing("Advisor", {"Action"}, Cost(coins=4), "+1 ActionReveal the top 3 cards of your deck. The player to your left chooses one of them. Discard that card and put the rest into your hand.", "https://wiki.dominionstrategy.com/index.php/Advisor")
BAKER = CardShapedThing("Baker", {"Action"}, Cost(coins=5), "+1 Card+1 Action+1 CoffersSetup: Each player gets +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Baker")
BUTCHER = CardShapedThing("Butcher", {"Action"}, Cost(coins=5), "+2 CoffersYou may trash a card from your hand, to gain a card, costing up to $1 more than it per Coffers you spend.", "https://wiki.dominionstrategy.com/index.php/Butcher")
CANDLESTICK_MAKER = CardShapedThing("Candlestick Maker", {"Action"}, Cost(coins=2), "+1 Action+1 Buy+1 Coffers", "https://wiki.dominionstrategy.com/index.php/Candlestick_Maker")
CARNIVAL = CardShapedThing("Carnival", {"Action"}, Cost(coins=5), "Reveal the top 4 cards of your deck. Put one of each differently named card into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Carnival")
DOCTOR = CardShapedThing("Doctor", {"Action"}, Cost(coins=3), "Name a card. Reveal the top 3 cards of your deck. Trash the matches. Put the rest back in any order.Overpay: Per $1 overpaid, look at the top card of your deck; trash it, discard it, or put it back.", "https://wiki.dominionstrategy.com/index.php/Doctor")
FAIRGROUNDS = CardShapedThing("Fairgrounds", {"Victory"}, Cost(coins=6), "Worth 2VP per 5 differently named cards you have (round down).", "https://wiki.dominionstrategy.com/index.php/Fairgrounds")
FARMHANDS = CardShapedThing("Farmhands", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsWhen you gain this, you may set aside an Action or Treasure from your hand, and play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Farmhands")
FARMING_VILLAGE = CardShapedThing("Farming Village", {"Action"}, Cost(coins=4), "+2 ActionsReveal cards from your deck until you reveal a Treasure or Action card. Put that card into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Farming_Village")
FARRIER = CardShapedThing("Farrier", {"Action"}, Cost(coins=2), "+1 Card+1 Action+1 BuyOverpay: +1 Card at the end of this turn per $1 overpaid.", "https://wiki.dominionstrategy.com/index.php/Farrier")
FERRYMAN = CardShapedThing("Ferryman", {"Action"}, Cost(coins=5), "+2 Cards+1 ActionDiscard a card.Setup: Choose an unused Kingdom card pile costing $3 or $4. Gain one when you gain a Ferryman.", "https://wiki.dominionstrategy.com/index.php/Ferryman")
FOOTPAD = CardShapedThing("Footpad", {"Action", "Attack"}, Cost(coins=5), "+2 CoffersEach other player discards down to 3 cards in hand.In games using this, when you gain a card in an Action phase, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Footpad")
FORTUNE_TELLER = CardShapedThing("Fortune Teller", {"Action", "Attack"}, Cost(coins=3), "+$2Each other player reveals cards from the top of their deck until they reveal a Victory card or a Curse. They put it on top and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Fortune_Teller")
HAMLET = CardShapedThing("Hamlet", {"Action"}, Cost(coins=2), "+1 Card+1 ActionYou may discard a card for +1 Action.You may discard a card for +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Hamlet")
HARVEST = CardShapedThing("Harvest", {"Action"}, Cost(coins=5), "Reveal the top 4 cards of your deck, then discard them. +$1 per differently named card revealed.", "https://wiki.dominionstrategy.com/index.php/Harvest")
HERALD = CardShapedThing("Herald", {"Action"}, Cost(coins=4), "+1 Card+1 ActionReveal the top card of your deck. If it's an Action, play it.Overpay: Per $1 overpaid, put any card from your discard pile onto your deck.", "https://wiki.dominionstrategy.com/index.php/Herald")
HORN_OF_PLENTY = CardShapedThing("Horn of Plenty", {"Treasure"}, Cost(coins=5), "Gain a card costing up to $1 per differently named card you have in play (counting this). If it's a Victory card, trash this.", "https://wiki.dominionstrategy.com/index.php/Horn_of_Plenty")
HORSE_TRADERS = CardShapedThing("Horse Traders", {"Action", "Reaction"}, Cost(coins=4), "+1 Buy+$3Discard 2 cards.When another player plays an Attack card, you may first set this aside from your hand. If you do, then at the start of your next turn, +1 Card and return this to your hand.", "https://wiki.dominionstrategy.com/index.php/Horse_Traders")
HUNTING_PARTY = CardShapedThing("Hunting Party", {"Action"}, Cost(coins=5), "+1 Card+1 ActionReveal your hand. Reveal cards from your deck until you reveal a card that isn't a copy of one in your hand. Put it into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Hunting_Party")
INFIRMARY = CardShapedThing("Infirmary", {"Action"}, Cost(coins=3), "+1 CardYou may trash a card from your hand.Overpay: Play this once per $1 overpaid.", "https://wiki.dominionstrategy.com/index.php/Infirmary")
JESTER = CardShapedThing("Jester", {"Action", "Attack"}, Cost(coins=5), "+$2Each other player discards the top card of their deck. If it's a Victory card they gain a Curse; otherwise they gain a copy of the discarded card or you do, your choice.", "https://wiki.dominionstrategy.com/index.php/Jester")
JOURNEYMAN = CardShapedThing("Journeyman", {"Action"}, Cost(coins=5), "Name a card. Reveal cards from your deck until you reveal 3 cards without that name. Put those cards into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Journeyman")
JOUST = CardShapedThing("Joust", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1You may set aside a Province from your hand to gain any Reward to your hand. Discard the Province in Clean-up.", "https://wiki.dominionstrategy.com/index.php/Joust")
MASTERPIECE = CardShapedThing("Masterpiece", {"Treasure"}, Cost(coins=3), "$1Overpay: Gain a Silver per $1 overpaid.", "https://wiki.dominionstrategy.com/index.php/Masterpiece")
MENAGERIE = CardShapedThing("Menagerie", {"Action"}, Cost(coins=3), "+1 ActionReveal your hand. If the revealed cards all have different names, +3 Cards. Otherwise, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Menagerie")
MERCHANT_GUILD = CardShapedThing("Merchant Guild", {"Action"}, Cost(coins=5), "+1 Buy+$1At the end of your Buy phase this turn, +1 Coffers per card you gained in it.", "https://wiki.dominionstrategy.com/index.php/Merchant_Guild")
PLAZA = CardShapedThing("Plaza", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsYou may discard a Treasure for +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Plaza")
REMAKE = CardShapedThing("Remake", {"Action"}, Cost(coins=4), "Do this twice: Trash a card from your hand, then gain a card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Remake")
SHOP = CardShapedThing("Shop", {"Action"}, Cost(coins=3), "+1 Card+$1You may play an Action card from your hand that you don't have a copy of in play.", "https://wiki.dominionstrategy.com/index.php/Shop")
SOOTHSAYER = CardShapedThing("Soothsayer", {"Action", "Attack"}, Cost(coins=5), "Gain a Gold. Each other player gains a Curse, and if they did, draws a card.", "https://wiki.dominionstrategy.com/index.php/Soothsayer")
STONEMASON = CardShapedThing("Stonemason", {"Action"}, Cost(coins=2), "Trash a card from your hand. Gain 2 cards each costing less than it.Overpay: Gain 2 Action cards each costing the amount overpaid.", "https://wiki.dominionstrategy.com/index.php/Stonemason")
TAXMAN = CardShapedThing("Taxman", {"Action", "Attack"}, Cost(coins=4), "You may trash a Treasure from your hand. Each other player with 5 or more cards in hand discards a copy of it (or reveals they can't). Gain a Treasure onto your deck costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Taxman")
TOURNAMENT = CardShapedThing("Tournament", {"Action"}, Cost(coins=4), "+1 ActionEach player may reveal a Province from their hand. If you do, discard it and gain any Prize (from the Prize pile) or a Duchy, onto your deck. If no-one else does, +1 Card and +$1.", "https://wiki.dominionstrategy.com/index.php/Tournament")
YOUNG_WITCH = CardShapedThing("Young Witch", {"Action", "Attack"}, Cost(coins=4), "+2 CardsDiscard 2 cards. Each other player gains a Curse unless they reveal a Bane from their hand.Setup: Add an extra Kingdom card pile costing $2 or $3 to the Supply. Its cards are Banes.", "https://wiki.dominionstrategy.com/index.php/Young_Witch")
BAG_OF_GOLD = CardShapedThing("Bag of Gold", {"Action", "Prize"}, Cost(coins=0), "+1 ActionGain a Gold onto your deck.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Bag_of_Gold")
CORONET = CardShapedThing("Coronet", {"Action", "Treasure", "Reward"}, Cost(coins=0), "You may play a non-Reward Action from your hand twice.You may play a non-Reward Treasure from your hand twice.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Coronet")
COURSER = CardShapedThing("Courser", {"Action", "Reward"}, Cost(coins=0), "Choose two different options: +2 Cards; +2 Actions; +$2; gain 4 Silvers.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Courser")
DEMESNE = CardShapedThing("Demesne", {"Action", "Victory", "Reward"}, Cost(coins=0), "+2 Actions+2 BuysGain a Gold.Worth 1VP per Gold you have.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Demesne")
DIADEM = CardShapedThing("Diadem", {"Treasure", "Prize"}, Cost(coins=0), "$2+$1 per unused Action you have (Action, not Action card).(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Diadem")
FOLLOWERS = CardShapedThing("Followers", {"Action", "Attack", "Prize"}, Cost(coins=0), "+2 CardsGain an Estate. Each other player gains a Curse and discards down to 3 cards in hand.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Followers")
HOUSECARL = CardShapedThing("Housecarl", {"Action", "Reward"}, Cost(coins=0), "+1 Card per differently named Action card you have in play.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Housecarl")
HUGE_TURNIP = CardShapedThing("Huge Turnip", {"Treasure", "Reward"}, Cost(coins=0), "+2 Coffers+$1 per Coffers you have.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Huge_Turnip")
PRINCESS = CardShapedThing("Princess", {"Action", "Prize"}, Cost(coins=0), "+1 BuyThis turn, cards cost $2 less.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Princess")
RENOWN = CardShapedThing("Renown", {"Action", "Reward"}, Cost(coins=0), "+1 BuyThis turn, cards cost $2 less.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Renown")
TRUSTY_STEED = CardShapedThing("Trusty Steed", {"Action", "Prize"}, Cost(coins=0), "Choose two: +2 Cards; or +2 Actions; or +$2; or gain 4 Silvers and put your deck into your discard pile. The choices must be different.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Trusty_Steed")
BERSERKER = CardShapedThing("Berserker", {"Action", "Attack"}, Cost(coins=5), "Gain a card costing less than this. Each other player discards down to 3 cards in hand.When you gain this, if you have an Action in play, play this.", "https://wiki.dominionstrategy.com/index.php/Berserker")
BORDER_VILLAGE = CardShapedThing("Border Village", {"Action"}, Cost(coins=6), "+1 Card+2 ActionsWhen you gain this, gain a cheaper card.", "https://wiki.dominionstrategy.com/index.php/Border_Village")
CACHE = CardShapedThing("Cache", {"Treasure"}, Cost(coins=5), "$3When you gain this, gain 2 Coppers.", "https://wiki.dominionstrategy.com/index.php/Cache")
CARTOGRAPHER = CardShapedThing("Cartographer", {"Action"}, Cost(coins=5), "+1 Card+1 ActionLook at the top 4 cards of your deck. Discard any number of them, then put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Cartographer")
CAULDRON = CardShapedThing("Cauldron", {"Treasure", "Attack"}, Cost(coins=5), "$2+1 BuyThe third time you gain an Action this turn, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Cauldron")
CROSSROADS = CardShapedThing("Crossroads", {"Action"}, Cost(coins=2), "Reveal your hand. +1 Card per Victory card revealed. If this is the first time you played a Crossroads this turn, +3 Actions.", "https://wiki.dominionstrategy.com/index.php/Crossroads")
DEVELOP = CardShapedThing("Develop", {"Action"}, Cost(coins=3), "Trash a card from your hand. Gain two cards onto your deck, with one costing exactly $1 more than it, and one costing exactly $1 less than it, in either order.", "https://wiki.dominionstrategy.com/index.php/Develop")
DUCHESS = CardShapedThing("Duchess", {"Action"}, Cost(coins=2), "+$2Each player (including you) looks at the top card of their deck and may discard it.In games using this, when you gain a Duchy, you may gain a Duchess.", "https://wiki.dominionstrategy.com/index.php/Duchess")
EMBASSY = CardShapedThing("Embassy", {"Action"}, Cost(coins=5), "+5 CardsDiscard 3 cards.When you gain this, each other player gains a Silver.", "https://wiki.dominionstrategy.com/index.php/Embassy")
FARMLAND = CardShapedThing("Farmland", {"Victory"}, Cost(coins=6), "2VPWhen you gain this, trash a card from your hand and gain a non-Farmland card costing exactly $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Farmland")
FOOLS_GOLD = CardShapedThing("Fool's Gold", {"Treasure", "Reaction"}, Cost(coins=2), "If this is the first time you played a Fool's Gold this turn, +$1, otherwise +$4.When another player gains a Province, you may trash this from your hand, to gain a Gold onto your deck.", "https://wiki.dominionstrategy.com/index.php/Fool%27s_Gold")
GUARD_DOG = CardShapedThing("Guard Dog", {"Action", "Reaction"}, Cost(coins=3), "+2 CardsIf you have 5 or fewer cards in hand, +2 Cards.When another player plays an Attack, you may first play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Guard_Dog")
HAGGLER = CardShapedThing("Haggler", {"Action"}, Cost(coins=5), "+$2This turn, when you gain a card, if you bought it, gain a cheaper non-Victory card.", "https://wiki.dominionstrategy.com/index.php/Haggler")
HIGHWAY = CardShapedThing("Highway", {"Action"}, Cost(coins=5), "+1 Card+1 ActionThis turn, cards cost $1 less.", "https://wiki.dominionstrategy.com/index.php/Highway")
ILL_GOTTEN_GAINS = CardShapedThing("Ill-Gotten Gains", {"Treasure"}, Cost(coins=5), "$1You may gain a Copper to your hand.When you gain this, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Ill-Gotten_Gains")
INN = CardShapedThing("Inn", {"Action"}, Cost(coins=5), "+2 Cards+2 ActionsDiscard 2 cards.When you gain this, reveal any number of Action cards from your discard pile and shuffle them into your deck.", "https://wiki.dominionstrategy.com/index.php/Inn")
JACK_OF_ALL_TRADES = CardShapedThing("Jack of All Trades", {"Action"}, Cost(coins=4), "Gain a Silver. Look at the top card of your deck; you may discard it. Draw until you have 5 cards in hand. You may trash a non-Treasure card from your hand.", "https://wiki.dominionstrategy.com/index.php/Jack_of_All_Trades")
MANDARIN = CardShapedThing("Mandarin", {"Action"}, Cost(coins=5), "+$3Put a card from your hand onto your deck.When you gain this, put all Treasures you have in play onto your deck in any order.", "https://wiki.dominionstrategy.com/index.php/Mandarin")
MARGRAVE = CardShapedThing("Margrave", {"Action", "Attack"}, Cost(coins=5), "+3 Cards+1 BuyEach other player draws a card, then discards down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Margrave")
NOBLE_BRIGAND = CardShapedThing("Noble Brigand", {"Action", "Attack"}, Cost(coins=4), "+$1Each other player reveals the top 2 cards of their deck, trashes a revealed Silver or Gold you choose, discards the rest, and gains a Copper if they didn't reveal a Treasure. You gain the trashed cards.When you buy this, do its attack.", "https://wiki.dominionstrategy.com/index.php/Noble_Brigand")
NOMAD_CAMP = CardShapedThing("Nomad Camp", {"Action"}, Cost(coins=4), "+1 Buy+$2This is gained onto your deck (instead of to your discard pile).", "https://wiki.dominionstrategy.com/index.php/Nomad_Camp")
NOMADS = CardShapedThing("Nomads", {"Action"}, Cost(coins=4), "+1 Buy+$2When you gain or trash this, +$2.", "https://wiki.dominionstrategy.com/index.php/Nomads")
OASIS = CardShapedThing("Oasis", {"Action"}, Cost(coins=3), "+1 Card+1 Action+$1Discard a card.", "https://wiki.dominionstrategy.com/index.php/Oasis")
ORACLE = CardShapedThing("Oracle", {"Action", "Attack"}, Cost(coins=3), "Each player (including you) reveals the top 2 cards of their deck, and discards them or puts them back, your choice (they choose the order). Then, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Oracle")
SCHEME = CardShapedThing("Scheme", {"Action"}, Cost(coins=3), "+1 Card+1 ActionThis turn, you may put one of your Action cards onto your deck when you discard it from play.", "https://wiki.dominionstrategy.com/index.php/Scheme")
SILK_ROAD = CardShapedThing("Silk Road", {"Victory"}, Cost(coins=4), "Worth 1VP for every 4 Victory cards you have (round down).", "https://wiki.dominionstrategy.com/index.php/Silk_Road")
SOUK = CardShapedThing("Souk", {"Action"}, Cost(coins=5), "+1 Buy+$7-$1 per card in your hand (you can't go below $0).When you gain this, trash up to 2 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Souk")
SPICE_MERCHANT = CardShapedThing("Spice Merchant", {"Action"}, Cost(coins=4), "You may trash a Treasure from your hand to choose one: +2 Cards and +1 Action; or +1 Buy and +$2.", "https://wiki.dominionstrategy.com/index.php/Spice_Merchant")
STABLES = CardShapedThing("Stables", {"Action"}, Cost(coins=5), "You may discard a Treasure, for +3 Cards and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Stables")
TRADER = CardShapedThing("Trader", {"Action", "Reaction"}, Cost(coins=4), "Trash a card from your hand. Gain a Silver per $1 it costs.When you gain a card, you may reveal this from your hand, to exchange the card for a Silver.", "https://wiki.dominionstrategy.com/index.php/Trader")
TRAIL = CardShapedThing("Trail", {"Action", "Reaction"}, Cost(coins=4), "+1 Card+1 ActionWhen you gain, trash, or discard this, other than in Clean-up, you may play it.", "https://wiki.dominionstrategy.com/index.php/Trail")
TUNNEL = CardShapedThing("Tunnel", {"Victory", "Reaction"}, Cost(coins=3), "2VPWhen you discard this other than during Clean-up, you may reveal it to gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Tunnel")
WEAVER = CardShapedThing("Weaver", {"Action", "Reaction"}, Cost(coins=4), "Gain two Silvers or a card costing up to $4.When you discard this other than in Clean-up, you may play it.", "https://wiki.dominionstrategy.com/index.php/Weaver")
WHEELWRIGHT = CardShapedThing("Wheelwright", {"Action"}, Cost(coins=5), "+1 Card+1 ActionYou may discard a card to gain an Action card costing as much as it or less.", "https://wiki.dominionstrategy.com/index.php/Wheelwright")
WITCHS_HUT = CardShapedThing("Witch's Hut", {"Action", "Attack"}, Cost(coins=5), "+4 CardsDiscard 2 cards, revealed. If they're both Actions, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Witch%27s_Hut")
ALTAR = CardShapedThing("Altar", {"Action"}, Cost(coins=6), "Trash a card from your hand. Gain a card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Altar")
ARMORY = CardShapedThing("Armory", {"Action"}, Cost(coins=4), "Gain a card onto your deck costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Armory")
BAND_OF_MISFITS = CardShapedThing("Band of Misfits", {"Action", "Command"}, Cost(coins=5), "Play a non-Command non-Duration Action card from the Supply that costs less than this, leaving it there.", "https://wiki.dominionstrategy.com/index.php/Band_of_Misfits")
BANDIT_CAMP = CardShapedThing("Bandit Camp", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsGain a Spoils.", "https://wiki.dominionstrategy.com/index.php/Bandit_Camp")
BEGGAR = CardShapedThing("Beggar", {"Action", "Reaction"}, Cost(coins=2), "Gain 3 Coppers to your hand.When another player plays an Attack card, you may first discard this to gain 2 Silvers, putting one onto your deck.", "https://wiki.dominionstrategy.com/index.php/Beggar")
CATACOMBS = CardShapedThing("Catacombs", {"Action"}, Cost(coins=5), "Look at the top 3 cards of your deck. Choose one: Put them into your hand; or discard them and +3 Cards.When you trash this, gain a cheaper card.", "https://wiki.dominionstrategy.com/index.php/Catacombs")
COUNT = CardShapedThing("Count", {"Action"}, Cost(coins=5), "Choose one: Discard 2 cards; or put a card from your hand onto your deck; or gain a Copper.Choose one: +$3; or trash your hand; or gain a Duchy.", "https://wiki.dominionstrategy.com/index.php/Count")
COUNTERFEIT = CardShapedThing("Counterfeit", {"Treasure"}, Cost(coins=5), "$1+1 BuyYou may play a non-Duration Treasure from your hand twice. Trash it.", "https://wiki.dominionstrategy.com/index.php/Counterfeit")
CULTIST = CardShapedThing("Cultist", {"Action", "Attack", "Looter"}, Cost(coins=5), "+2 CardsEach other player gains a Ruins. You may play a Cultist from your hand.When you trash this, +3 Cards.", "https://wiki.dominionstrategy.com/index.php/Cultist")
DAME_ANNA = CardShapedThing("Dame Anna", {"Action", "Attack", "Knight"}, Cost(coins=5), "You may trash up to 2 cards from your hand. Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Dame_Anna")
DAME_JOSEPHINE = CardShapedThing("Dame Josephine", {"Action", "Attack", "Knight", "Victory"}, Cost(coins=5), "Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.2VP", "https://wiki.dominionstrategy.com/index.php/Dame_Josephine")
DAME_MOLLY = CardShapedThing("Dame Molly", {"Action", "Attack", "Knight"}, Cost(coins=5), "+2 ActionsEach other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Dame_Molly")
DAME_NATALIE = CardShapedThing("Dame Natalie", {"Action", "Attack", "Knight"}, Cost(coins=5), "You may gain a card costing up to $3. Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Dame_Natalie")
DAME_SYLVIA = CardShapedThing("Dame Sylvia", {"Action", "Attack", "Knight"}, Cost(coins=5), "+$2Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Dame_Sylvia")
DEATH_CART = CardShapedThing("Death Cart", {"Action", "Looter"}, Cost(coins=4), "You may trash this or an Action card from your hand, for +$5.When you gain this, gain 2 Ruins.", "https://wiki.dominionstrategy.com/index.php/Death_Cart")
FEODUM = CardShapedThing("Feodum", {"Victory"}, Cost(coins=4), "Worth 1VP per 3 Silvers you have (round down).When you trash this, gain 3 Silvers.", "https://wiki.dominionstrategy.com/index.php/Feodum")
FORAGER = CardShapedThing("Forager", {"Action"}, Cost(coins=3), "+1 Action+1 BuyTrash a card from your hand, then +$1 per differently named Treasure in the trash.", "https://wiki.dominionstrategy.com/index.php/Forager")
FORTRESS = CardShapedThing("Fortress", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsWhen you trash this, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Fortress")
GRAVEROBBER = CardShapedThing("Graverobber", {"Action"}, Cost(coins=5), "Choose one: Gain a card from the trash costing from $3 to $6, onto your deck; or trash an Action card from your hand and gain a card costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Graverobber")
HERMIT = CardShapedThing("Hermit", {"Action"}, Cost(coins=3), "Look through your discard pile. You may trash a non-Treasure from it or from your hand. Gain a card costing up to $3. At the end of your Buy phase this turn, if you didn't gain any cards in it, exchange this for a Madman.", "https://wiki.dominionstrategy.com/index.php/Hermit")
HUNTING_GROUNDS = CardShapedThing("Hunting Grounds", {"Action"}, Cost(coins=6), "+4 CardsWhen you trash this, gain a Duchy or 3 Estates.", "https://wiki.dominionstrategy.com/index.php/Hunting_Grounds")
IRONMONGER = CardShapedThing("Ironmonger", {"Action"}, Cost(coins=4), "+1 Card+1 ActionReveal the top card of your deck; you may discard it. Either way, if it is an…Action card, +1 ActionTreasure card, +$1Victory card, +1 Card", "https://wiki.dominionstrategy.com/index.php/Ironmonger")
JUNK_DEALER = CardShapedThing("Junk Dealer", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1Trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Junk_Dealer")
MARAUDER = CardShapedThing("Marauder", {"Action", "Attack", "Looter"}, Cost(coins=4), "Gain a Spoils. Each other player gains a Ruins.", "https://wiki.dominionstrategy.com/index.php/Marauder")
MARKET_SQUARE = CardShapedThing("Market Square", {"Action", "Reaction"}, Cost(coins=3), "+1 Card+1 Action+1 BuyWhen one of your cards is trashed, you may discard this from your hand to gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Market_Square")
MYSTIC = CardShapedThing("Mystic", {"Action"}, Cost(coins=5), "+1 Action+$2Name a card, then reveal the top card of your deck. If you named it, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Mystic")
PILLAGE = CardShapedThing("Pillage", {"Action", "Attack"}, Cost(coins=5), "Trash this. If you did, gain 2 Spoils, and each other player with 5 or more cards in hand reveals their hand and discards a card that you choose.", "https://wiki.dominionstrategy.com/index.php/Pillage")
POOR_HOUSE = CardShapedThing("Poor House", {"Action"}, Cost(coins=1), "+$4Reveal your hand. -$1 per Treasure card in your hand. (You can't go below $0.)", "https://wiki.dominionstrategy.com/index.php/Poor_House")
PROCESSION = CardShapedThing("Procession", {"Action"}, Cost(coins=4), "You may play a non-Duration Action card from your hand twice. Trash it. Gain an Action card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Procession")
RATS = CardShapedThing("Rats", {"Action"}, Cost(coins=4), "+1 Card+1 ActionGain a Rats. Trash a card from your hand other than a Rats (or reveal a hand of all Rats).When you trash this, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Rats")
REBUILD = CardShapedThing("Rebuild", {"Action"}, Cost(coins=5), "+1 ActionName a card. Reveal cards from your deck until you reveal a Victory card you did not name. Discard the rest, trash the Victory card, and gain a Victory card costing up to $3 more than it.", "https://wiki.dominionstrategy.com/index.php/Rebuild")
ROGUE = CardShapedThing("Rogue", {"Action", "Attack"}, Cost(coins=5), "+$2If there are any cards in the trash costing from $3 to $6, gain one of them. Otherwise, each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest.", "https://wiki.dominionstrategy.com/index.php/Rogue")
SAGE = CardShapedThing("Sage", {"Action"}, Cost(coins=3), "+1 ActionReveal cards from the top of your deck until you reveal one costing $3 or more. Put that card into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Sage")
SCAVENGER = CardShapedThing("Scavenger", {"Action"}, Cost(coins=4), "+$2You may put your deck into your discard pile. Put a card from your discard pile onto your deck.", "https://wiki.dominionstrategy.com/index.php/Scavenger")
SIR_BAILEY = CardShapedThing("Sir Bailey", {"Action", "Attack", "Knight"}, Cost(coins=5), "+1 Card+1 ActionEach other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Sir_Bailey")
SIR_DESTRY = CardShapedThing("Sir Destry", {"Action", "Attack", "Knight"}, Cost(coins=5), "+2 CardsEach other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Sir_Destry")
SIR_MARTIN = CardShapedThing("Sir Martin", {"Action", "Attack", "Knight"}, Cost(coins=4), "+2 BuysEach other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Sir_Martin")
SIR_MICHAEL = CardShapedThing("Sir Michael", {"Action", "Attack", "Knight"}, Cost(coins=5), "Each other player discards down to 3 cards in hand. Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.", "https://wiki.dominionstrategy.com/index.php/Sir_Michael")
SIR_VANDER = CardShapedThing("Sir Vander", {"Action", "Attack", "Knight"}, Cost(coins=5), "Each other player reveals the top 2 cards of their deck, trashes one of them costing from $3 to $6, and discards the rest. If a Knight is trashed by this, trash this.When you trash this, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Sir_Vander")
SQUIRE = CardShapedThing("Squire", {"Action"}, Cost(coins=2), "+$1Choose one: +2 Actions; or +2 Buys; or gain a Silver.When you trash this, gain an Attack card.", "https://wiki.dominionstrategy.com/index.php/Squire")
STOREROOM = CardShapedThing("Storeroom", {"Action"}, Cost(coins=3), "+1 BuyDiscard any number of cards, then draw that many. Then discard any number of cards for +$1 each.", "https://wiki.dominionstrategy.com/index.php/Storeroom")
URCHIN = CardShapedThing("Urchin", {"Action", "Attack"}, Cost(coins=3), "+1 Card+1 ActionEach other player discards down to 4 cards in hand.When you play another Attack card with this in play, you may first trash this, to gain a Mercenary.", "https://wiki.dominionstrategy.com/index.php/Urchin")
VAGRANT = CardShapedThing("Vagrant", {"Action"}, Cost(coins=2), "+1 Card+1 ActionReveal the top card of your deck. If it's a Curse, Ruins, Shelter, or Victory card, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Vagrant")
WANDERING_MINSTREL = CardShapedThing("Wandering Minstrel", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsReveal the top 3 cards of your deck. Put the Action cards back in any order and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Wandering_Minstrel")
ABANDONED_MINE = CardShapedThing("Abandoned Mine", {"Action", "Ruins"}, Cost(coins=0), "+$1", "https://wiki.dominionstrategy.com/index.php/Abandoned_Mine")
RUINED_LIBRARY = CardShapedThing("Ruined Library", {"Action", "Ruins"}, Cost(coins=0), "+1 Card", "https://wiki.dominionstrategy.com/index.php/Ruined_Library")
RUINED_MARKET = CardShapedThing("Ruined Market", {"Action", "Ruins"}, Cost(coins=0), "+1 Buy", "https://wiki.dominionstrategy.com/index.php/Ruined_Market")
RUINED_VILLAGE = CardShapedThing("Ruined Village", {"Action", "Ruins"}, Cost(coins=0), "+1 Action", "https://wiki.dominionstrategy.com/index.php/Ruined_Village")
SURVIVORS = CardShapedThing("Survivors", {"Action", "Ruins"}, Cost(coins=0), "Look at the top 2 cards of your deck. Discard them or put them back in any order.", "https://wiki.dominionstrategy.com/index.php/Survivors")
HOVEL = CardShapedThing("Hovel", {"Reaction", "Shelter"}, Cost(coins=1), "When you gain a Victory card, you may trash this from your hand.", "https://wiki.dominionstrategy.com/index.php/Hovel")
MADMAN = CardShapedThing("Madman", {"Action"}, Cost(coins=0), "+2 ActionsReturn this to the Madman pile. If you do, +1 Card per card in your hand.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Madman")
MERCENARY = CardShapedThing("Mercenary", {"Action", "Attack"}, Cost(coins=0), "You may trash 2 cards from your hand. If you did, +2 Cards, +$2, and each other player discards down to 3 cards in hand.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Mercenary")
NECROPOLIS = CardShapedThing("Necropolis", {"Action", "Shelter"}, Cost(coins=1), "+2 Actions", "https://wiki.dominionstrategy.com/index.php/Necropolis")
OVERGROWN_ESTATE = CardShapedThing("Overgrown Estate", {"Victory", "Shelter"}, Cost(coins=1), "0VPWhen you trash this, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Overgrown_Estate")
SPOILS = CardShapedThing("Spoils", {"Treasure"}, Cost(coins=0), "$3When you play this, return it to the Spoils pile.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Spoils")
AMULET = CardShapedThing("Amulet", {"Action", "Duration"}, Cost(coins=3), "Now and at the start of your next turn, choose one: +$1; or trash a card from your hand; or gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Amulet")
ARTIFICER = CardShapedThing("Artificer", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1Discard any number of cards. You may gain a card onto your deck, costing exactly $1 per card discarded.", "https://wiki.dominionstrategy.com/index.php/Artificer")
BRIDGE_TROLL = CardShapedThing("Bridge Troll", {"Action", "Duration", "Attack"}, Cost(coins=5), "Each other player takes their -$1 token. On this turn and your next turn, cards cost $1 less. Now and at the start of your next turn: +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Bridge_Troll")
CARAVAN_GUARD = CardShapedThing("Caravan Guard", {"Action", "Duration", "Reaction"}, Cost(coins=3), "+1 Card+1 ActionAt the start of your next turn, +$1.When another player plays an Attack card, you may first play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Caravan_Guard")
COIN_OF_THE_REALM = CardShapedThing("Coin of the Realm", {"Treasure", "Reserve"}, Cost(coins=2), "$1Put this on your Tavern mat.After you play an Action card, you may call this, for +2 Actions.", "https://wiki.dominionstrategy.com/index.php/Coin_of_the_Realm")
DISTANT_LANDS = CardShapedThing("Distant Lands", {"Action", "Reserve", "Victory"}, Cost(coins=5), "Put this on your Tavern mat.Worth 4VP if on your Tavern mat at the end of the game (otherwise worth 0VP).", "https://wiki.dominionstrategy.com/index.php/Distant_Lands")
DUNGEON = CardShapedThing("Dungeon", {"Action", "Duration"}, Cost(coins=3), "+1 ActionNow and at the start of your next turn: +2 Cards, then discard 2 cards.", "https://wiki.dominionstrategy.com/index.php/Dungeon")
DUPLICATE = CardShapedThing("Duplicate", {"Action", "Reserve"}, Cost(coins=4), "Put this on your Tavern mat.When you gain a card costing up to $6, you may call this, to gain a copy of that card.", "https://wiki.dominionstrategy.com/index.php/Duplicate")
GEAR = CardShapedThing("Gear", {"Action", "Duration"}, Cost(coins=3), "+2 CardsSet aside up to 2 cards from your hand face down (under this). At the start of your next turn, put them into your hand.", "https://wiki.dominionstrategy.com/index.php/Gear")
GIANT = CardShapedThing("Giant", {"Action", "Attack"}, Cost(coins=5), "Turn your Journey token over (it starts face up). Then if it's face down, +$1. If it's face up, +$5, and each other player reveals the top card of their deck, trashes it if it costs from $3 to $6, and otherwise discards it and gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Giant")
GUIDE = CardShapedThing("Guide", {"Action", "Reserve"}, Cost(coins=3), "+1 Card+1 ActionPut this on your Tavern mat.At the start of your turn, you may call this, to discard your hand and draw 5 cards.", "https://wiki.dominionstrategy.com/index.php/Guide")
HAUNTED_WOODS = CardShapedThing("Haunted Woods", {"Action", "Duration", "Attack"}, Cost(coins=5), "At the start of your next turn: +3 Cards.Until then, when any other player gains a card they bought, they put their hand onto their deck in any order.", "https://wiki.dominionstrategy.com/index.php/Haunted_Woods")
HIRELING = CardShapedThing("Hireling", {"Action", "Duration"}, Cost(coins=6), "At the start of each of your turns for the rest of the game: +1 Card.", "https://wiki.dominionstrategy.com/index.php/Hireling")
LOST_CITY = CardShapedThing("Lost City", {"Action"}, Cost(coins=5), "+2 Cards+2 ActionsWhen you gain this, each other player draws a card.", "https://wiki.dominionstrategy.com/index.php/Lost_City")
MAGPIE = CardShapedThing("Magpie", {"Action"}, Cost(coins=4), "+1 Card+1 ActionReveal the top card of your deck.  If it's a Treasure, put it into your hand. If it's an Action or Victory card, gain a Magpie.", "https://wiki.dominionstrategy.com/index.php/Magpie")
MESSENGER = CardShapedThing("Messenger", {"Action"}, Cost(coins=4), "+1 Buy+$2You may put your deck into your discard pile.When this is the first card you gain in your Buy phase, gain a card costing up to $4, and each other player gains a copy of it.", "https://wiki.dominionstrategy.com/index.php/Messenger")
MISER = CardShapedThing("Miser", {"Action"}, Cost(coins=4), "Choose one: Put a Copper from your hand onto your Tavern mat; or +$1 per Copper on your Tavern mat.", "https://wiki.dominionstrategy.com/index.php/Miser")
PAGE = CardShapedThing("Page", {"Action", "Traveller"}, Cost(coins=2), "+1 Card+1 ActionWhen you discard this from play, you may exchange it for a Treasure Hunter.", "https://wiki.dominionstrategy.com/index.php/Page")
PEASANT = CardShapedThing("Peasant", {"Action", "Traveller"}, Cost(coins=2), "+1 Buy+$1When you discard this from play, you may exchange it for a Soldier.", "https://wiki.dominionstrategy.com/index.php/Peasant")
PORT = CardShapedThing("Port", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsWhen you gain this, gain another Port (that doesn't come with another).", "https://wiki.dominionstrategy.com/index.php/Port")
RANGER = CardShapedThing("Ranger", {"Action"}, Cost(coins=4), "+1 BuyTurn your Journey token over (it starts face up). Then if it's face up, +5 Cards.", "https://wiki.dominionstrategy.com/index.php/Ranger")
RATCATCHER = CardShapedThing("Ratcatcher", {"Action", "Reserve"}, Cost(coins=2), "+1 Card+1 ActionPut this on your Tavern mat.At the start of your turn, you may call this to trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Ratcatcher")
RAZE = CardShapedThing("Raze", {"Action"}, Cost(coins=2), "+1 ActionTrash this or a card from your hand. Look at one card from the top of your deck per $1 the trashed card costs. Put one of them into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Raze")
RELIC = CardShapedThing("Relic", {"Treasure", "Attack"}, Cost(coins=5), "$2Each other player puts their -1 Card token on their deck.", "https://wiki.dominionstrategy.com/index.php/Relic")
ROYAL_CARRIAGE = CardShapedThing("Royal Carriage", {"Action", "Reserve"}, Cost(coins=5), "+1 ActionPut this on your Tavern mat.After you play an Action card, if it's still in play, you may call this, to replay that Action.", "https://wiki.dominionstrategy.com/index.php/Royal_Carriage")
STORYTELLER = CardShapedThing("Storyteller", {"Action"}, Cost(coins=5), "+1 ActionPlay up to 3 Treasures from your hand. Then +1 Card, and pay all of your $ for +1 Card per $1 you paid.", "https://wiki.dominionstrategy.com/index.php/Storyteller")
SWAMP_HAG = CardShapedThing("Swamp Hag", {"Action", "Duration", "Attack"}, Cost(coins=5), "At the start of your next turn: +$3.Until then, when any other player gains a card they bought, they gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Swamp_Hag")
TRANSMOGRIFY = CardShapedThing("Transmogrify", {"Action", "Reserve"}, Cost(coins=4), "+1 ActionPut this on your Tavern mat.At the start of your turn, you may call this, to trash a card from your hand, and gain a card to your hand costing up to $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Transmogrify")
TREASURE_TROVE = CardShapedThing("Treasure Trove", {"Treasure"}, Cost(coins=5), "$2Gain a Gold and a Copper.", "https://wiki.dominionstrategy.com/index.php/Treasure_Trove")
WINE_MERCHANT = CardShapedThing("Wine Merchant", {"Action", "Reserve"}, Cost(coins=5), "+1 Buy+$4Put this on your Tavern mat.At the end of your Buy phase, if you have at least $2 unspent, you may discard this from your Tavern mat.", "https://wiki.dominionstrategy.com/index.php/Wine_Merchant")
CHAMPION = CardShapedThing("Champion", {"Action", "Duration"}, Cost(coins=6), "+1 ActionFor the rest of the game, when another player plays an Attack, it doesn't affect you, and when you play an Action card, you first get +1 Action.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Champion")
DISCIPLE = CardShapedThing("Disciple", {"Action", "Traveller"}, Cost(coins=5), "You may play an Action card from your hand twice. Gain a copy of it.When you discard this from play, you may exchange it for a Teacher.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Disciple")
FUGITIVE = CardShapedThing("Fugitive", {"Action", "Traveller"}, Cost(coins=4), "+2 Cards+1 ActionDiscard a card.When you discard this from play, you may exchange it for a Disciple.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Fugitive")
HERO = CardShapedThing("Hero", {"Action", "Traveller"}, Cost(coins=5), "+$2Gain a Treasure.When you discard this from play, you may exchange it for a Champion.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Hero")
SOLDIER = CardShapedThing("Soldier", {"Action", "Attack", "Traveller"}, Cost(coins=3), "+$2+$1 per other Attack you have in play. Each other player with 4 or more cards in hand discards a card.When you discard this from play, you may exchange it for a Fugitive. (This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Soldier")
TEACHER = CardShapedThing("Teacher", {"Action", "Reserve"}, Cost(coins=6), "Put this on your Tavern mat.At the start of your turn, you may call this, to move your +1 Card, +1 Action, +1 Buy, or +$1 token to an Action Supply pile you have no tokens on. (When you play a card from that pile, you first get that bonus.)(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Teacher")
TREASURE_HUNTER = CardShapedThing("Treasure Hunter", {"Action", "Traveller"}, Cost(coins=3), "+1 Action+$1Gain a Silver per card the player to your right gained in their last turn.When you discard this from play, you may exchange it for a Warrior.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Treasure_Hunter")
WARRIOR = CardShapedThing("Warrior", {"Action", "Attack", "Traveller"}, Cost(coins=4), "+2 CardsFor each Traveller you have in play (including this), each other player discards the top card of their deck and trashes it if it costs $3 or $4.When you discard this from play, you may exchange it for a Hero.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Warrior")
ALMS = CardShapedThing("Alms", {"Event"}, Cost(coins=0), "Once per turn: If you have no Treasures in play, gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Alms")
BALL = CardShapedThing("Ball", {"Event"}, Cost(coins=5), "Take your -$1 token. Gain 2 cards each costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Ball")
BONFIRE = CardShapedThing("Bonfire", {"Event"}, Cost(coins=3), "Trash up to 2 Coppers you have in play.", "https://wiki.dominionstrategy.com/index.php/Bonfire")
BORROW = CardShapedThing("Borrow", {"Event"}, Cost(coins=0), "Once per turn: +1 Buy. If your -1 Card token isn't on your deck, put it there and +$1.", "https://wiki.dominionstrategy.com/index.php/Borrow")
EXPEDITION = CardShapedThing("Expedition", {"Event"}, Cost(coins=3), "Draw 2 extra cards for your next hand.", "https://wiki.dominionstrategy.com/index.php/Expedition")
FERRY = CardShapedThing("Ferry", {"Event"}, Cost(coins=3), "Move your -$2 token to an Action Supply pile. (Cards from that pile cost $2 less on your turns.)", "https://wiki.dominionstrategy.com/index.php/Ferry")
INHERITANCE = CardShapedThing("Inheritance", {"Event"}, Cost(coins=7), "Once per game: Set aside a non-Command non-Duration Action card from the Supply costing up to $4. Move your Estate token to it. (During your turns, Estates are also Command Actions with \"Play the card with your Estate token, leaving it there.\")", "https://wiki.dominionstrategy.com/index.php/Inheritance")
LOST_ARTS = CardShapedThing("Lost Arts", {"Event"}, Cost(coins=6), "Move your +1 Action token to an Action Supply pile. (When you play a card from that pile, you first get +1 Action.)", "https://wiki.dominionstrategy.com/index.php/Lost_Arts")
MISSION = CardShapedThing("Mission", {"Event"}, Cost(coins=4), "Take an extra turn after this one (but not a 3rd turn in a row), during which you can't buy cards.(You can still buy Events.)", "https://wiki.dominionstrategy.com/index.php/Mission")
PATHFINDING = CardShapedThing("Pathfinding", {"Event"}, Cost(coins=8), "Move your +1 Card token to an Action Supply pile. (When you play a card from that pile, you first get +1 Card.)", "https://wiki.dominionstrategy.com/index.php/Pathfinding")
PILGRIMAGE = CardShapedThing("Pilgrimage", {"Event"}, Cost(coins=4), "Once per turn: Turn your Journey token over (it starts face up); then if it's face up, choose up to 3 differently named cards you have in play and gain a copy of each.", "https://wiki.dominionstrategy.com/index.php/Pilgrimage")
PLAN = CardShapedThing("Plan", {"Event"}, Cost(coins=3), "Move your Trashing token to an Action Supply pile. (When you gain a card from that pile, you may trash a card from your hand.)", "https://wiki.dominionstrategy.com/index.php/Plan")
QUEST = CardShapedThing("Quest", {"Event"}, Cost(coins=0), "You may discard an Attack, two Curses, or six cards. If you do, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Quest")
RAID = CardShapedThing("Raid", {"Event"}, Cost(coins=5), "Gain a Silver per Silver you have in play. Each other player puts their -1 Card token on their deck.", "https://wiki.dominionstrategy.com/index.php/Raid")
SAVE = CardShapedThing("Save", {"Event"}, Cost(coins=1), "Once per turn: +1 Buy. Set aside a card from your hand, and put it into your hand at end of turn (after drawing).", "https://wiki.dominionstrategy.com/index.php/Save")
SCOUTING_PARTY = CardShapedThing("Scouting Party", {"Event"}, Cost(coins=2), "+1 BuyLook at the top 5 cards of your deck. Discard 3 and put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Scouting_Party")
SEAWAY = CardShapedThing("Seaway", {"Event"}, Cost(coins=5), "Gain an Action card costing up to $4. Move your +1 Buy token to its pile. (When you play a card from that pile, you first get +1 Buy.)", "https://wiki.dominionstrategy.com/index.php/Seaway")
TRADE = CardShapedThing("Trade", {"Event"}, Cost(coins=5), "Trash up to 2 cards from your hand. Gain a Silver per card you trashed.", "https://wiki.dominionstrategy.com/index.php/Trade")
TRAINING = CardShapedThing("Training", {"Event"}, Cost(coins=6), "Move your +$1 token to an Action Supply pile. (When you play a card from that pile, you first get +$1.)", "https://wiki.dominionstrategy.com/index.php/Training")
TRAVELLING_FAIR = CardShapedThing("Travelling Fair", {"Event"}, Cost(coins=2), "+2 BuysWhen you gain a card this turn, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Travelling_Fair")
ARCHIVE = CardShapedThing("Archive", {"Action", "Duration"}, Cost(coins=5), "+1 ActionSet aside the top 3 cards of your deck face down (you may look at them). Now and at the start of your next two turns, put one into your hand.", "https://wiki.dominionstrategy.com/index.php/Archive")
BUSTLING_VILLAGE = CardShapedThing("Bustling Village", {"Action"}, Cost(coins=5), "+1 Card+3 ActionsYou may reveal a Settlers from your discard pile and put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Bustling_Village")
CAPITAL = CardShapedThing("Capital", {"Treasure"}, Cost(coins=5), "$6+1 BuyWhen you discard this from play, +6D.", "https://wiki.dominionstrategy.com/index.php/Capital")
CATAPULT = CardShapedThing("Catapult", {"Action", "Attack"}, Cost(coins=3), "+$1Trash a card from your hand. If it costs $3 or more, each other player gains a Curse. If it's a Treasure, each other player discards down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Catapult")
CHARIOT_RACE = CardShapedThing("Chariot Race", {"Action"}, Cost(coins=3), "+1 Action+1 Card, revealing it. The player to your left reveals the top card of their deck. If your card costs more, +$1 and +1VP.", "https://wiki.dominionstrategy.com/index.php/Chariot_Race")
CHARM = CardShapedThing("Charm", {"Treasure"}, Cost(coins=5), "Choose one: +1 Buy and +$2; or the next time you gain a card this turn, you may also gain a differently named card with the same cost.", "https://wiki.dominionstrategy.com/index.php/Charm")
CITY_QUARTER = CardShapedThing("City Quarter", {"Action"}, Cost(debt=8), "+2 ActionsReveal your hand. +1 Card per Action card revealed.", "https://wiki.dominionstrategy.com/index.php/City_Quarter")
CROWN = CardShapedThing("Crown", {"Action", "Treasure"}, Cost(coins=5), "If it's your Action phase, you may play an Action from your hand twice.If it's your Buy phase, you may play a Treasure from your hand twice.", "https://wiki.dominionstrategy.com/index.php/Crown")
CRUMBLING_CASTLE = CardShapedThing("Crumbling Castle", {"Victory", "Castle"}, Cost(coins=4), "1VPWhen you gain or trash this, +1VP and gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Crumbling_Castle")
EMPORIUM = CardShapedThing("Emporium", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1When you gain this, if you have at least 5 Action cards in play, +2VP.", "https://wiki.dominionstrategy.com/index.php/Emporium")
ENCAMPMENT = CardShapedThing("Encampment", {"Action"}, Cost(coins=2), "+2 Cards+2 ActionsYou may reveal a Gold or Plunder from your hand. If you do not, set this aside, and return it to its pile at the start of Clean-up.", "https://wiki.dominionstrategy.com/index.php/Encampment")
ENCHANTRESS = CardShapedThing("Enchantress", {"Action", "Attack", "Duration"}, Cost(coins=3), "Until your next turn, the first time each other player plays an Action card on their turn, they get +1 Card and +1 Action instead of following its instructions.At the start of your next turn, +2 Cards", "https://wiki.dominionstrategy.com/index.php/Enchantress")
ENGINEER = CardShapedThing("Engineer", {"Action"}, Cost(debt=4), "Gain a card costing up to $4. You may trash this. If you do, gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Engineer")
FARMERS_MARKET = CardShapedThing("Farmers' Market", {"Action", "Gathering"}, Cost(coins=3), "+1 BuyIf there are 4VP or more on the Farmers' Market pile, take them and trash this. Otherwise, add 1VP to the pile and then +$1 per 1VP on the pile.", "https://wiki.dominionstrategy.com/index.php/Farmers%27_Market")
FORTUNE = CardShapedThing("Fortune", {"Treasure"}, Cost(coins=8, debt=8), "+1 BuyDouble your $ if you haven't yet this turn.When you gain this, gain a Gold per Gladiator you have in play.", "https://wiki.dominionstrategy.com/index.php/Fortune")
FORUM = CardShapedThing("Forum", {"Action"}, Cost(coins=5), "+3 Cards+1 ActionDiscard 2 cards.When you gain this, +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Forum")
GLADIATOR = CardShapedThing("Gladiator", {"Action"}, Cost(coins=3), "+$2Reveal a card from your hand. The player to your left may reveal a copy from their hand. If they don't, +$1 and trash a Gladiator from its pile.", "https://wiki.dominionstrategy.com/index.php/Gladiator")
GRAND_CASTLE = CardShapedThing("Grand Castle", {"Victory", "Castle"}, Cost(coins=9), "5VPWhen you gain this, reveal your hand. +1VP per Victory card in your hand and/or in play.", "https://wiki.dominionstrategy.com/index.php/Grand_Castle")
GROUNDSKEEPER = CardShapedThing("Groundskeeper", {"Action"}, Cost(coins=5), "+1 Card+1 ActionThis turn, when you gain a Victory card, +1VP.", "https://wiki.dominionstrategy.com/index.php/Groundskeeper")
HAUNTED_CASTLE = CardShapedThing("Haunted Castle", {"Victory", "Castle"}, Cost(coins=6), "2VPWhen you gain this during your turn, gain a Gold, and each other player with 5 or more cards in hand puts 2 of them onto their deck.", "https://wiki.dominionstrategy.com/index.php/Haunted_Castle")
HUMBLE_CASTLE = CardShapedThing("Humble Castle", {"Treasure", "Victory", "Castle"}, Cost(coins=3), "$1Worth 1VP per Castle you have.", "https://wiki.dominionstrategy.com/index.php/Humble_Castle")
KINGS_CASTLE = CardShapedThing("King's Castle", {"Victory", "Castle"}, Cost(coins=10), "Worth 2VP per Castle you have.", "https://wiki.dominionstrategy.com/index.php/King%27s_Castle")
LEGIONARY = CardShapedThing("Legionary", {"Action", "Attack"}, Cost(coins=5), "+$3You may reveal a Gold from your hand. If you do, each other player discards down to 2 cards in hand, then draws a card.", "https://wiki.dominionstrategy.com/index.php/Legionary")
OPULENT_CASTLE = CardShapedThing("Opulent Castle", {"Action", "Victory", "Castle"}, Cost(coins=7), "Discard any number of Victory cards, revealed. +$2 per card discarded.3VP", "https://wiki.dominionstrategy.com/index.php/Opulent_Castle")
OVERLORD = CardShapedThing("Overlord", {"Action", "Command"}, Cost(debt=8), "Play a non-Command non-Duration Action card from the Supply costing up to $5, leaving it there.", "https://wiki.dominionstrategy.com/index.php/Overlord")
PATRICIAN = CardShapedThing("Patrician", {"Action"}, Cost(coins=2), "+1 Card+1 ActionReveal the top card of your deck. If it costs $5 or more, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Patrician")
PLUNDER = CardShapedThing("Plunder", {"Treasure"}, Cost(coins=5), "$2+1VP", "https://wiki.dominionstrategy.com/index.php/Plunder")
ROCKS = CardShapedThing("Rocks", {"Treasure"}, Cost(coins=4), "$1When you gain or trash this: If it's your Buy phase, gain a Silver onto your deck, otherwise gain a Silver to your hand.", "https://wiki.dominionstrategy.com/index.php/Rocks")
ROYAL_BLACKSMITH = CardShapedThing("Royal Blacksmith", {"Action"}, Cost(debt=8), "+5 CardsReveal your hand; discard the Coppers.", "https://wiki.dominionstrategy.com/index.php/Royal_Blacksmith")
SACRIFICE = CardShapedThing("Sacrifice", {"Action"}, Cost(coins=4), "Trash a card from your hand.If it's an…Action card, +2 Cards and +2 ActionsTreasure card, +$2Victory card, +2VP", "https://wiki.dominionstrategy.com/index.php/Sacrifice")
SETTLERS = CardShapedThing("Settlers", {"Action"}, Cost(coins=2), "+1 Card+1 ActionYou may reveal a Copper from your discard pile and put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Settlers")
SMALL_CASTLE = CardShapedThing("Small Castle", {"Action", "Victory", "Castle"}, Cost(coins=5), "Trash this or a Castle from your hand. If you do, gain a Castle.2VP", "https://wiki.dominionstrategy.com/index.php/Small_Castle")
SPRAWLING_CASTLE = CardShapedThing("Sprawling Castle", {"Victory", "Castle"}, Cost(coins=8), "4VPWhen you gain this, gain a Duchy or 3 Estates.", "https://wiki.dominionstrategy.com/index.php/Sprawling_Castle")
TEMPLE = CardShapedThing("Temple", {"Action", "Gathering"}, Cost(coins=4), "+1VPTrash from 1 to 3 differently named cards from your hand. Add 1VP to the Temple pile.When you gain this, take the VP from the Temple pile.", "https://wiki.dominionstrategy.com/index.php/Temple")
VILLA = CardShapedThing("Villa", {"Action"}, Cost(coins=4), "+2 Actions+1 Buy+$1When you gain this, put it into your hand, +1 Action, and if it's your Buy phase return to your Action phase.", "https://wiki.dominionstrategy.com/index.php/Villa")
WILD_HUNT = CardShapedThing("Wild Hunt", {"Action", "Gathering"}, Cost(coins=5), "Choose one: +3 Cards and add 1VP to the Wild Hunt pile; or gain an Estate, and if you do, take the VP from the pile.", "https://wiki.dominionstrategy.com/index.php/Wild_Hunt")
ADVANCE = CardShapedThing("Advance", {"Event"}, Cost(coins=0), "You may trash an Action card from your hand. If you do, gain an Action card costing up to $6.", "https://wiki.dominionstrategy.com/index.php/Advance")
ANNEX = CardShapedThing("Annex", {"Event"}, Cost(debt=8), "Look through your discard pile. Shuffle all but up to 5 cards from it into your deck. Gain a Duchy.", "https://wiki.dominionstrategy.com/index.php/Annex")
BANQUET = CardShapedThing("Banquet", {"Event"}, Cost(coins=3), "Gain 2 Coppers and a non-Victory card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Banquet")
CONQUEST = CardShapedThing("Conquest", {"Event"}, Cost(coins=6), "Gain 2 Silvers. +1VP per Silver you've gained this turn.", "https://wiki.dominionstrategy.com/index.php/Conquest")
DELVE = CardShapedThing("Delve", {"Event"}, Cost(coins=2), "+1 BuyGain a Silver.", "https://wiki.dominionstrategy.com/index.php/Delve")
DOMINATE = CardShapedThing("Dominate", {"Event"}, Cost(coins=14), "Gain a Province. If you do, +9VP.", "https://wiki.dominionstrategy.com/index.php/Dominate")
DONATE = CardShapedThing("Donate", {"Event"}, Cost(debt=8), "At the start of your next turn, first, put your deck and discard pile into your hand, trash any number of cards from it, then shuffle the rest into your deck and draw 5 cards.", "https://wiki.dominionstrategy.com/index.php/Donate")
RITUAL = CardShapedThing("Ritual", {"Event"}, Cost(coins=4), "Gain a Curse. If you do, trash a card from your hand. +1VP per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Ritual")
SALT_THE_EARTH = CardShapedThing("Salt the Earth", {"Event"}, Cost(coins=4), "+1VPTrash a Victory card from the Supply.", "https://wiki.dominionstrategy.com/index.php/Salt_the_Earth")
TAX = CardShapedThing("Tax", {"Event"}, Cost(coins=2), "Add 2D to a Supply pile.Setup: Add 1D to each Supply pile. When a player gains a card in their Buy phase, they take the D from its pile.", "https://wiki.dominionstrategy.com/index.php/Tax")
TRIUMPH = CardShapedThing("Triumph", {"Event"}, Cost(debt=5), "Gain an Estate. If you did, +1VP per card you've gained this turn.", "https://wiki.dominionstrategy.com/index.php/Triumph")
WEDDING = CardShapedThing("Wedding", {"Event"}, Cost(coins=4, debt=3), "+1VPGain a Gold.", "https://wiki.dominionstrategy.com/index.php/Wedding")
WINDFALL = CardShapedThing("Windfall", {"Event"}, Cost(coins=5), "If your deck and discard pile are empty, gain 3 Golds.", "https://wiki.dominionstrategy.com/index.php/Windfall")
AQUEDUCT = CardShapedThing("Aqueduct", {"Landmark"}, Cost(), "When you gain a Treasure, move 1VP from its pile to this. When you gain a Victory card, take the VP from this.Setup: Put 8VP on the Silver and Gold piles.", "https://wiki.dominionstrategy.com/index.php/Aqueduct")
ARENA = CardShapedThing("Arena", {"Landmark"}, Cost(), "At the start of your Buy phase, you may discard an Action card. If you do, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Arena")
BANDIT_FORT = CardShapedThing("Bandit Fort", {"Landmark"}, Cost(), "When scoring, -2VP for each Silver and each Gold you have.", "https://wiki.dominionstrategy.com/index.php/Bandit_Fort")
BASILICA = CardShapedThing("Basilica", {"Landmark"}, Cost(), "When you gain a card in your Buy phase, if you have $2 or more, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Basilica")
BATHS = CardShapedThing("Baths", {"Landmark"}, Cost(), "When you end your turn without having gained a card, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Baths")
BATTLEFIELD = CardShapedThing("Battlefield", {"Landmark"}, Cost(), "When you gain a Victory card, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Battlefield")
COLONNADE = CardShapedThing("Colonnade", {"Landmark"}, Cost(), "When you gain an Action card in your Buy phase, if you have a copy of it in play, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Colonnade")
DEFILED_SHRINE = CardShapedThing("Defiled Shrine", {"Landmark"}, Cost(), "When you gain an Action, move 1VP from its pile to this. When you gain a Curse in your Buy phase, take the VP from this.Setup: Put 2VP on each non-Gathering Action Supply pile.", "https://wiki.dominionstrategy.com/index.php/Defiled_Shrine")
FOUNTAIN = CardShapedThing("Fountain", {"Landmark"}, Cost(), "When scoring, 15VP if you have at least 10 Coppers.", "https://wiki.dominionstrategy.com/index.php/Fountain")
KEEP = CardShapedThing("Keep", {"Landmark"}, Cost(), "When scoring, 5VP per differently named Treasure you have, that you have more copies of than each other player, or tied for most.", "https://wiki.dominionstrategy.com/index.php/Keep")
LABYRINTH = CardShapedThing("Labyrinth", {"Landmark"}, Cost(), "When you gain a 2nd card in one of your turns, take 2VP from here.Setup: Put 6VP here per player.", "https://wiki.dominionstrategy.com/index.php/Labyrinth")
MOUNTAIN_PASS = CardShapedThing("Mountain Pass", {"Landmark"}, Cost(), "When you are the first player to gain a Province, each player bids once, up to 40D, ending with you. High bidder gets +8VP and takes the D they bid.", "https://wiki.dominionstrategy.com/index.php/Mountain_Pass")
MUSEUM = CardShapedThing("Museum", {"Landmark"}, Cost(), "When scoring, 2VP per differently named card you have.", "https://wiki.dominionstrategy.com/index.php/Museum")
OBELISK = CardShapedThing("Obelisk", {"Landmark"}, Cost(), "When scoring, 2VP per card you have from the chosen pile.Setup: Choose a random Action Supply pile.", "https://wiki.dominionstrategy.com/index.php/Obelisk")
ORCHARD = CardShapedThing("Orchard", {"Landmark"}, Cost(), "When scoring, 4VP per differently named Action card you have 3 or more copies of.", "https://wiki.dominionstrategy.com/index.php/Orchard")
PALACE = CardShapedThing("Palace", {"Landmark"}, Cost(), "When scoring, 3VP per set you have of Copper - Silver - Gold.", "https://wiki.dominionstrategy.com/index.php/Palace")
TOMB = CardShapedThing("Tomb", {"Landmark"}, Cost(), "When you trash a card, +1VP.", "https://wiki.dominionstrategy.com/index.php/Tomb")
TOWER = CardShapedThing("Tower", {"Landmark"}, Cost(), "When scoring, 1VP per non-Victory card you have from an empty Supply pile.", "https://wiki.dominionstrategy.com/index.php/Tower")
TRIUMPHAL_ARCH = CardShapedThing("Triumphal Arch", {"Landmark"}, Cost(), "When scoring, 3VP per copy you have of the 2nd most common Action card among your cards (if it's a tie, count either).", "https://wiki.dominionstrategy.com/index.php/Triumphal_Arch")
WALL = CardShapedThing("Wall", {"Landmark"}, Cost(), "When scoring, -1VP per card you have after the first 15.", "https://wiki.dominionstrategy.com/index.php/Wall")
WOLF_DEN = CardShapedThing("Wolf Den", {"Landmark"}, Cost(), "When scoring, -3VP per card you have exactly one copy of.", "https://wiki.dominionstrategy.com/index.php/Wolf_Den")
BARD = CardShapedThing("Bard", {"Action", "Fate"}, Cost(coins=4), "+$2Receive a Boon.", "https://wiki.dominionstrategy.com/index.php/Bard")
BLESSED_VILLAGE = CardShapedThing("Blessed Village", {"Action", "Fate"}, Cost(coins=4), "+1 Card+2 ActionsWhen you gain this, take a Boon. Receive it now or at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Blessed_Village")
CEMETERY = CardShapedThing("Cemetery", {"Victory"}, Cost(coins=4), "2VPWhen you gain this, trash up to 4 cards from your hand.Heirloom: Haunted Mirror", "https://wiki.dominionstrategy.com/index.php/Cemetery")
CHANGELING = CardShapedThing("Changeling", {"Night"}, Cost(coins=3), "Trash this. Gain a copy of a card you have in play.In games using this, when you gain a card costing $3 or more, you may exchange it for a Changeling.", "https://wiki.dominionstrategy.com/index.php/Changeling")
COBBLER = CardShapedThing("Cobbler", {"Night", "Duration"}, Cost(coins=5), "At the start of your next turn, gain a card to your hand costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Cobbler")
CONCLAVE = CardShapedThing("Conclave", {"Action"}, Cost(coins=4), "+$2You may play an Action card from your hand that you don't have a copy of in play. If you do, +1 Action.", "https://wiki.dominionstrategy.com/index.php/Conclave")
CRYPT = CardShapedThing("Crypt", {"Night", "Duration"}, Cost(coins=5), "Set aside any number of non-Duration Treasures you have in play, face down (under this). While any remain, at the start of each of your turns, put one of them into your hand.", "https://wiki.dominionstrategy.com/index.php/Crypt")
CURSED_VILLAGE = CardShapedThing("Cursed Village", {"Action", "Doom"}, Cost(coins=5), "+2 ActionsDraw until you have 6 cards in hand.When you gain this, receive a Hex.", "https://wiki.dominionstrategy.com/index.php/Cursed_Village")
DEN_OF_SIN = CardShapedThing("Den of Sin", {"Night", "Duration"}, Cost(coins=5), "At the start of your next turn, +2 Cards.This is gained to your hand (instead of your discard pile).", "https://wiki.dominionstrategy.com/index.php/Den_of_Sin")
DEVILS_WORKSHOP = CardShapedThing("Devil's Workshop", {"Night"}, Cost(coins=4), "If the number of cards you've gained this turn is:2+, gain an Imp;1, gain a card costing up to $4;0, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Devil%27s_Workshop")
DRUID = CardShapedThing("Druid", {"Action", "Fate"}, Cost(coins=2), "+1 Buy Receive one of the set-aside Boons (leaving it there).Setup: Set aside the top 3 Boons face up.", "https://wiki.dominionstrategy.com/index.php/Druid")
EXORCIST = CardShapedThing("Exorcist", {"Night"}, Cost(coins=4), "Trash a card from your hand. Gain a cheaper Spirit from one of the Spirit piles.", "https://wiki.dominionstrategy.com/index.php/Exorcist")
FAITHFUL_HOUND = CardShapedThing("Faithful Hound", {"Action", "Reaction"}, Cost(coins=2), "+2 CardsWhen you discard this other than during Clean-up, you may set it aside, and put it into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Faithful_Hound")
FOOL = CardShapedThing("Fool", {"Action", "Fate"}, Cost(coins=3), "If you aren't the player with Lost in the Woods: take it, take 3 Boons, and receive the Boons in any order.Heirloom: Lucky Coin", "https://wiki.dominionstrategy.com/index.php/Fool")
GHOST_TOWN = CardShapedThing("Ghost Town", {"Night", "Duration"}, Cost(coins=3), "At the start of your next turn, +1 Card and +1 Action.This is gained to your hand (instead of your discard pile).", "https://wiki.dominionstrategy.com/index.php/Ghost_Town")
GUARDIAN = CardShapedThing("Guardian", {"Night", "Duration"}, Cost(coins=2), "At the start of your next turn, +$1. Until then, when another player plays an Attack card, it doesn't affect you. This is gained to your hand (instead of your discard pile).", "https://wiki.dominionstrategy.com/index.php/Guardian")
IDOL = CardShapedThing("Idol", {"Treasure", "Attack", "Fate"}, Cost(coins=5), "$2If you have an odd number of Idols in play (counting this), receive a Boon; otherwise, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Idol")
LEPRECHAUN = CardShapedThing("Leprechaun", {"Action", "Doom"}, Cost(coins=3), "Gain a Gold. If you have exactly 7 cards in play, gain a Wish. Otherwise, receive a Hex.", "https://wiki.dominionstrategy.com/index.php/Leprechaun")
MONASTERY = CardShapedThing("Monastery", {"Night"}, Cost(coins=2), "For each card you've gained this turn, you may trash a card from your hand or a Copper you have in play.", "https://wiki.dominionstrategy.com/index.php/Monastery")
NECROMANCER = CardShapedThing("Necromancer", {"Action"}, Cost(coins=4), "Choose a face up, non-Duration Action card in the trash. Turn it face down for the turn, and play it, leaving it there.Setup: Put the 3 Zombies into the trash.", "https://wiki.dominionstrategy.com/index.php/Necromancer")
NIGHT_WATCHMAN = CardShapedThing("Night Watchman", {"Night"}, Cost(coins=3), "Look at the top 5 cards of your deck, discard any number, and put the rest back in any order.This is gained to your hand (instead of your discard pile).", "https://wiki.dominionstrategy.com/index.php/Night_Watchman")
PIXIE = CardShapedThing("Pixie", {"Action", "Fate"}, Cost(coins=2), "+1 Card+1 ActionDiscard the top Boon. You may trash this to receive that Boon twice.Heirloom: Goat", "https://wiki.dominionstrategy.com/index.php/Pixie")
POOKA = CardShapedThing("Pooka", {"Action"}, Cost(coins=5), "You may trash a Treasure other than Cursed Gold from your hand, for +4 Cards.Heirloom: Cursed Gold", "https://wiki.dominionstrategy.com/index.php/Pooka")
RAIDER = CardShapedThing("Raider", {"Night", "Duration", "Attack"}, Cost(coins=6), "Each other player with 5 or more cards in hand discards a copy of a card you have in play (or reveals they can't).At the start of your next turn, +$3.", "https://wiki.dominionstrategy.com/index.php/Raider")
SACRED_GROVE = CardShapedThing("Sacred Grove", {"Action", "Fate"}, Cost(coins=5), "+1 Buy+$3Receive a Boon. If it doesn't give +$1, each other player may receive it.", "https://wiki.dominionstrategy.com/index.php/Sacred_Grove")
SECRET_CAVE = CardShapedThing("Secret Cave", {"Action", "Duration"}, Cost(coins=3), "+1 Card+1 ActionYou may discard 3 cards. If you did, then at the start of your next turn, +$3.Heirloom: Magic Lamp", "https://wiki.dominionstrategy.com/index.php/Secret_Cave")
SHEPHERD = CardShapedThing("Shepherd", {"Action"}, Cost(coins=4), "+1 ActionDiscard any number of Victory cards, revealing them. +2 Cards per card discarded.Heirloom: Pasture", "https://wiki.dominionstrategy.com/index.php/Shepherd")
SKULK = CardShapedThing("Skulk", {"Action", "Attack", "Doom"}, Cost(coins=4), "+1 BuyEach other player receives the next Hex.When you gain this, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Skulk")
TORMENTOR = CardShapedThing("Tormentor", {"Action", "Attack", "Doom"}, Cost(coins=5), "+$2If you have no other cards in play, gain an Imp. Otherwise, each other player receives the next Hex.", "https://wiki.dominionstrategy.com/index.php/Tormentor")
TRACKER = CardShapedThing("Tracker", {"Action", "Fate"}, Cost(coins=2), "+$1This turn, when you gain a card, you may put it onto your deck. Receive a Boon.Heirloom: Pouch", "https://wiki.dominionstrategy.com/index.php/Tracker")
TRAGIC_HERO = CardShapedThing("Tragic Hero", {"Action"}, Cost(coins=5), "+3 Cards+1 BuyIf you have 8 or more cards in hand (after drawing), trash this and gain a Treasure.", "https://wiki.dominionstrategy.com/index.php/Tragic_Hero")
VAMPIRE = CardShapedThing("Vampire", {"Night", "Attack", "Doom"}, Cost(coins=5), "Each other player receives the next Hex. Gain a card costing up to $5 other than a Vampire.Exchange this for a Bat.", "https://wiki.dominionstrategy.com/index.php/Vampire")
WEREWOLF = CardShapedThing("Werewolf", {"Action", "Night", "Attack", "Doom"}, Cost(coins=5), "If it's your Night phase, each other player receives the next Hex. Otherwise, +3 Cards.", "https://wiki.dominionstrategy.com/index.php/Werewolf")
BAT = CardShapedThing("Bat", {"Night"}, Cost(coins=2), "Trash up to 2 cards from your hand. If you trashed at least one, exchange this for a Vampire.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Bat")
CURSED_GOLD = CardShapedThing("Cursed Gold", {"Treasure", "Heirloom"}, Cost(coins=4), "$3Gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Cursed_Gold")
GHOST = CardShapedThing("Ghost", {"Night", "Duration", "Spirit"}, Cost(coins=4), "Reveal cards from your deck until you reveal an Action. Discard the other cards and set aside the Action. At the start of your next turn, play it twice.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Ghost")
GOAT = CardShapedThing("Goat", {"Treasure", "Heirloom"}, Cost(coins=2), "$1You may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Goat")
HAUNTED_MIRROR = CardShapedThing("Haunted Mirror", {"Treasure", "Heirloom"}, Cost(coins=0), "$1When you trash this, you may discard an Action card, to gain a Ghost.", "https://wiki.dominionstrategy.com/index.php/Haunted_Mirror")
IMP = CardShapedThing("Imp", {"Action", "Spirit"}, Cost(coins=2), "+2 CardsYou may play an Action card from your hand that you don't have a copy of in play.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Imp")
LUCKY_COIN = CardShapedThing("Lucky Coin", {"Treasure", "Heirloom"}, Cost(coins=4), "$1Gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Lucky_Coin")
MAGIC_LAMP = CardShapedThing("Magic Lamp", {"Treasure", "Heirloom"}, Cost(coins=0), "$1If there are at least 6 cards that you have exactly 1 copy of in play (counting this), trash this. If you did, gain 3 Wishes.", "https://wiki.dominionstrategy.com/index.php/Magic_Lamp")
PASTURE = CardShapedThing("Pasture", {"Treasure", "Victory", "Heirloom"}, Cost(coins=2), "$1Worth 1VP per Estate you have.", "https://wiki.dominionstrategy.com/index.php/Pasture")
POUCH = CardShapedThing("Pouch", {"Treasure", "Heirloom"}, Cost(coins=2), "$1+1 Buy", "https://wiki.dominionstrategy.com/index.php/Pouch")
WILL_O_WISP = CardShapedThing("Will-o'-Wisp", {"Action", "Spirit"}, Cost(coins=0), "+1 Card+1 ActionReveal the top card of your deck. If it costs $2 or less, put it into your hand.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Will-o%27-Wisp")
WISH = CardShapedThing("Wish", {"Action"}, Cost(coins=0), "+1 ActionReturn this to its pile. If you did, gain a card to your hand costing up to $6.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Wish")
ZOMBIE_APPRENTICE = CardShapedThing("Zombie Apprentice", {"Action", "Zombie"}, Cost(coins=3), "You may trash an Action card from your hand for +3 Cards and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Zombie_Apprentice")
ZOMBIE_MASON = CardShapedThing("Zombie Mason", {"Action", "Zombie"}, Cost(coins=3), "Trash the top card of your deck. You may gain a card costing up to $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Zombie_Mason")
ZOMBIE_SPY = CardShapedThing("Zombie Spy", {"Action", "Zombie"}, Cost(coins=3), "+1 Card+1 ActionLook at the top card of your deck. Discard it or put it back.", "https://wiki.dominionstrategy.com/index.php/Zombie_Spy")
THE_EARTHS_GIFT = CardShapedThing("The Earth's Gift", {"Boon"}, Cost(), "You may discard a Treasure to gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/The_Earth%27s_Gift")
THE_FIELDS_GIFT = CardShapedThing("The Field's Gift", {"Boon"}, Cost(), "+1 Action+$1(Keep this until Clean-up.)", "https://wiki.dominionstrategy.com/index.php/The_Field%27s_Gift")
THE_FLAMES_GIFT = CardShapedThing("The Flame's Gift", {"Boon"}, Cost(), "You may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/The_Flame%27s_Gift")
THE_FORESTS_GIFT = CardShapedThing("The Forest's Gift", {"Boon"}, Cost(), "+1 Buy+$1(Keep this until Clean-up.)", "https://wiki.dominionstrategy.com/index.php/The_Forest%27s_Gift")
THE_MOONS_GIFT = CardShapedThing("The Moon's Gift", {"Boon"}, Cost(), "Look through your discard pile. You may put a card from it onto your deck.", "https://wiki.dominionstrategy.com/index.php/The_Moon%27s_Gift")
THE_MOUNTAINS_GIFT = CardShapedThing("The Mountain's Gift", {"Boon"}, Cost(), "Gain a Silver.", "https://wiki.dominionstrategy.com/index.php/The_Mountain%27s_Gift")
THE_RIVERS_GIFT = CardShapedThing("The River's Gift", {"Boon"}, Cost(), "+1 Card at the end of this turn.(Keep this until Clean-up.)", "https://wiki.dominionstrategy.com/index.php/The_River%27s_Gift")
THE_SEAS_GIFT = CardShapedThing("The Sea's Gift", {"Boon"}, Cost(), "+1 Card", "https://wiki.dominionstrategy.com/index.php/The_Sea%27s_Gift")
THE_SKYS_GIFT = CardShapedThing("The Sky's Gift", {"Boon"}, Cost(), "You may discard 3 cards to gain a Gold.", "https://wiki.dominionstrategy.com/index.php/The_Sky%27s_Gift")
THE_SUNS_GIFT = CardShapedThing("The Sun's Gift", {"Boon"}, Cost(), "Look at the top 4 cards of your deck. Discard any number of them and put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/The_Sun%27s_Gift")
THE_SWAMPS_GIFT = CardShapedThing("The Swamp's Gift", {"Boon"}, Cost(), "Gain a Will-o'-Wisp.", "https://wiki.dominionstrategy.com/index.php/The_Swamp%27s_Gift")
THE_WINDS_GIFT = CardShapedThing("The Wind's Gift", {"Boon"}, Cost(), "+2 CardsDiscard 2 cards.", "https://wiki.dominionstrategy.com/index.php/The_Wind%27s_Gift")
BAD_OMENS = CardShapedThing("Bad Omens", {"Hex"}, Cost(), "Put your deck into your discard pile. Look through it and put 2 Coppers from it onto your deck (or reveal you can't).", "https://wiki.dominionstrategy.com/index.php/Bad_Omens")
DELUSION = CardShapedThing("Delusion", {"Hex"}, Cost(), "If you don't have Deluded or Envious, take Deluded.", "https://wiki.dominionstrategy.com/index.php/Delusion")
ENVY = CardShapedThing("Envy", {"Hex"}, Cost(), "If you don't have Deluded or Envious, take Envious.", "https://wiki.dominionstrategy.com/index.php/Envy")
FAMINE = CardShapedThing("Famine", {"Hex"}, Cost(), "Reveal the top 3 cards of your deck. Discard the Actions. Shuffle the rest into your deck.", "https://wiki.dominionstrategy.com/index.php/Famine")
FEAR = CardShapedThing("Fear", {"Hex"}, Cost(), "If you have at least 5 cards in hand, discard an Action or Treasure (or reveal you can't).", "https://wiki.dominionstrategy.com/index.php/Fear")
GREED = CardShapedThing("Greed", {"Hex"}, Cost(), "Gain a Copper onto your deck.", "https://wiki.dominionstrategy.com/index.php/Greed")
HAUNTING = CardShapedThing("Haunting", {"Hex"}, Cost(), "If you have at least 4 cards in hand, put one of them onto your deck.", "https://wiki.dominionstrategy.com/index.php/Haunting")
LOCUSTS = CardShapedThing("Locusts", {"Hex"}, Cost(), "Trash the top card of your deck. If it's Copper or Estate, gain a Curse. Otherwise, gain a cheaper card that shares a type with it.", "https://wiki.dominionstrategy.com/index.php/Locusts")
MISERY = CardShapedThing("Misery", {"Hex"}, Cost(), "If this is your first Misery this game, take Miserable. Otherwise, flip it over to Twice Miserable.", "https://wiki.dominionstrategy.com/index.php/Misery")
PLAGUE = CardShapedThing("Plague", {"Hex"}, Cost(), "Gain a Curse to your hand.", "https://wiki.dominionstrategy.com/index.php/Plague")
POVERTY = CardShapedThing("Poverty", {"Hex"}, Cost(), "Discard down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Poverty")
WAR = CardShapedThing("War", {"Hex"}, Cost(), "Reveal cards from your deck until revealing one costing $3 or $4. Trash it and discard the rest.", "https://wiki.dominionstrategy.com/index.php/War")
DELUDED = CardShapedThing("Deluded", {"State"}, Cost(), "At the start of your Buy phase, return this, and you can't buy Actions this turn.", "https://wiki.dominionstrategy.com/index.php/Deluded")
ENVIOUS = CardShapedThing("Envious", {"State"}, Cost(), "At the start of your Buy phase, return this, and Silver and Gold make $1 this turn.", "https://wiki.dominionstrategy.com/index.php/Envious")
LOST_IN_THE_WOODS = CardShapedThing("Lost in the Woods", {"State"}, Cost(), "At the start of your turn, you may discard a card to receive a Boon.", "https://wiki.dominionstrategy.com/index.php/Lost_in_the_Woods")
MISERABLE = CardShapedThing("Miserable", {"State"}, Cost(), "-2VP", "https://wiki.dominionstrategy.com/index.php/Miserable")
TWICE_MISERABLE = CardShapedThing("Twice Miserable", {"State"}, Cost(), "-4VP", "https://wiki.dominionstrategy.com/index.php/Twice_Miserable")
ACTING_TROUPE = CardShapedThing("Acting Troupe", {"Action"}, Cost(coins=3), "+4 VillagersTrash this.", "https://wiki.dominionstrategy.com/index.php/Acting_Troupe")
BORDER_GUARD = CardShapedThing("Border Guard", {"Action"}, Cost(coins=2), "+1 ActionReveal the top 2 cards of your deck. Put one into your hand and discard the other. If both were Actions, take the Lantern or Horn.", "https://wiki.dominionstrategy.com/index.php/Border_Guard")
CARGO_SHIP = CardShapedThing("Cargo Ship", {"Action", "Duration"}, Cost(coins=3), "+$2Once this turn, when you gain a card, you may set it aside face up (on this). At the start of your next turn, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Cargo_Ship")
DUCAT = CardShapedThing("Ducat", {"Treasure"}, Cost(coins=2), "+1 Coffers+1 BuyWhen you gain this, you may trash a Copper from your hand.", "https://wiki.dominionstrategy.com/index.php/Ducat")
EXPERIMENT = CardShapedThing("Experiment", {"Action"}, Cost(coins=3), "+2 Cards+1 ActionReturn this to its pile.When you gain this, gain another Experiment (that doesn't come with another).", "https://wiki.dominionstrategy.com/index.php/Experiment")
FLAG_BEARER = CardShapedThing("Flag Bearer", {"Action"}, Cost(coins=4), "+$2When you gain or trash this, take the Flag.", "https://wiki.dominionstrategy.com/index.php/Flag_Bearer")
HIDEOUT = CardShapedThing("Hideout", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsTrash a card from your hand. If it's a Victory card, gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Hideout")
IMPROVE = CardShapedThing("Improve", {"Action"}, Cost(coins=3), "+$2At the start of Clean-up, you may trash an Action card you would discard from play this turn, to gain a card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Improve")
INVENTOR = CardShapedThing("Inventor", {"Action"}, Cost(coins=4), "Gain a card costing up to $4, then cards cost $1 less this turn.", "https://wiki.dominionstrategy.com/index.php/Inventor")
LACKEYS = CardShapedThing("Lackeys", {"Action"}, Cost(coins=2), "+2 CardsWhen you gain this, +2 Villagers.", "https://wiki.dominionstrategy.com/index.php/Lackeys")
MOUNTAIN_VILLAGE = CardShapedThing("Mountain Village", {"Action"}, Cost(coins=4), "+2 ActionsLook through your discard pile and put a card from it into your hand; if you can't, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Mountain_Village")
OLD_WITCH = CardShapedThing("Old Witch", {"Action", "Attack"}, Cost(coins=5), "+3 CardsEach other player gains a Curse and may trash a Curse from their hand.", "https://wiki.dominionstrategy.com/index.php/Old_Witch")
PATRON = CardShapedThing("Patron", {"Action", "Reaction"}, Cost(coins=4), "+1 Villager+$2When something causes you to reveal this (using the word \"reveal\") in an Action phase, +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Patron")
PRIEST = CardShapedThing("Priest", {"Action"}, Cost(coins=4), "+$2Trash a card from your hand. For the rest of this turn, when you trash a card, +$2.", "https://wiki.dominionstrategy.com/index.php/Priest")
RECRUITER = CardShapedThing("Recruiter", {"Action"}, Cost(coins=5), "+2 CardsTrash a card from your hand. +1 Villager per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Recruiter")
RESEARCH = CardShapedThing("Research", {"Action", "Duration"}, Cost(coins=4), "+1 ActionTrash a card from your hand. Per $1 it costs, set aside a card from your deck face down (on this). At the start of your next turn, put those cards into your hand.", "https://wiki.dominionstrategy.com/index.php/Research")
SCEPTER = CardShapedThing("Scepter", {"Treasure", "Command"}, Cost(coins=5), "Choose one: +$2; or replay a non-Command Action card you played this turn that's still in play.", "https://wiki.dominionstrategy.com/index.php/Scepter")
SCHOLAR = CardShapedThing("Scholar", {"Action"}, Cost(coins=5), "Discard your hand. +7 Cards.", "https://wiki.dominionstrategy.com/index.php/Scholar")
SCULPTOR = CardShapedThing("Sculptor", {"Action"}, Cost(coins=5), "Gain a card to your hand costing up to $4. If it's a Treasure, +1 Villager.", "https://wiki.dominionstrategy.com/index.php/Sculptor")
SEER = CardShapedThing("Seer", {"Action"}, Cost(coins=5), "+1 Card+1 ActionReveal the top 3 cards of your deck. Put the ones costing from $2 to $4 into your hand. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Seer")
SILK_MERCHANT = CardShapedThing("Silk Merchant", {"Action"}, Cost(coins=4), "+2 Cards+1 BuyWhen you gain or trash this, +1 Coffers and +1 Villager.", "https://wiki.dominionstrategy.com/index.php/Silk_Merchant")
SPICES = CardShapedThing("Spices", {"Treasure"}, Cost(coins=5), "$2+1 BuyWhen you gain this, +2 Coffers.", "https://wiki.dominionstrategy.com/index.php/Spices")
SWASHBUCKLER = CardShapedThing("Swashbuckler", {"Action"}, Cost(coins=5), "+3 CardsIf your discard pile has any cards in it: +1 Coffers, then if you have at least 4 Coffers tokens, take the Treasure Chest.", "https://wiki.dominionstrategy.com/index.php/Swashbuckler")
TREASURER = CardShapedThing("Treasurer", {"Action"}, Cost(coins=5), "+$3Choose one: Trash a Treasure from your hand; or gain a Treasure from the trash to your hand; or take the Key.", "https://wiki.dominionstrategy.com/index.php/Treasurer")
VILLAIN = CardShapedThing("Villain", {"Action", "Attack"}, Cost(coins=5), "+2 CoffersEach other player with 5 or more cards in hand discards one costing $2 or more (or reveals they can't).", "https://wiki.dominionstrategy.com/index.php/Villain")
ACADEMY = CardShapedThing("Academy", {"Project"}, Cost(coins=5), "When you gain an Action card, +1 Villager.", "https://wiki.dominionstrategy.com/index.php/Academy")
BARRACKS = CardShapedThing("Barracks", {"Project"}, Cost(coins=6), "At the start of your turn, +1 Action.", "https://wiki.dominionstrategy.com/index.php/Barracks")
CANAL = CardShapedThing("Canal", {"Project"}, Cost(coins=7), "During your turns, cards cost $1 less.", "https://wiki.dominionstrategy.com/index.php/Canal")
CAPITALISM = CardShapedThing("Capitalism", {"Project"}, Cost(coins=5), "During your turns, Actions with +$ amounts in their text are also Treasures.", "https://wiki.dominionstrategy.com/index.php/Capitalism")
CATHEDRAL = CardShapedThing("Cathedral", {"Project"}, Cost(coins=3), "At the start of your turn, trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Cathedral")
CITADEL = CardShapedThing("Citadel", {"Project"}, Cost(coins=8), "The first time you play an Action card during each of your turns, replay it afterwards.", "https://wiki.dominionstrategy.com/index.php/Citadel")
CITY_GATE = CardShapedThing("City Gate", {"Project"}, Cost(coins=3), "At the start of your turn, +1 Card, then put a card from your hand onto your deck.", "https://wiki.dominionstrategy.com/index.php/City_Gate")
CROP_ROTATION = CardShapedThing("Crop Rotation", {"Project"}, Cost(coins=6), "At the start of your turn, you may discard a Victory card for +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Crop_Rotation")
EXPLORATION = CardShapedThing("Exploration", {"Project"}, Cost(coins=4), "At the end of your Buy phase, if you didn't gain any cards during it, +1 Coffers and +1 Villager.", "https://wiki.dominionstrategy.com/index.php/Exploration")
FAIR = CardShapedThing("Fair", {"Project"}, Cost(coins=4), "At the start of your turn, +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Fair")
FLEET = CardShapedThing("Fleet", {"Project"}, Cost(coins=5), "After the game ends, there's an extra round of turns just for players with this.", "https://wiki.dominionstrategy.com/index.php/Fleet")
GUILDHALL = CardShapedThing("Guildhall", {"Project"}, Cost(coins=5), "When you gain a Treasure, +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Guildhall")
INNOVATION = CardShapedThing("Innovation", {"Project"}, Cost(coins=6), "Once during each of your turns, when you gain an Action card, you may play it.", "https://wiki.dominionstrategy.com/index.php/Innovation")
PAGEANT = CardShapedThing("Pageant", {"Project"}, Cost(coins=3), "At the end of your Buy phase, you may pay $1 for +1 Coffers.", "https://wiki.dominionstrategy.com/index.php/Pageant")
PIAZZA = CardShapedThing("Piazza", {"Project"}, Cost(coins=5), "At the start of your turn, reveal the top card of your deck. If it's an Action, play it.", "https://wiki.dominionstrategy.com/index.php/Piazza")
ROAD_NETWORK = CardShapedThing("Road Network", {"Project"}, Cost(coins=5), "When another player gains a Victory card, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Road_Network")
SEWERS = CardShapedThing("Sewers", {"Project"}, Cost(coins=3), "When you trash a card other than with this, you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Sewers")
SILOS = CardShapedThing("Silos", {"Project"}, Cost(coins=4), "At the start of your turn, discard any number of Coppers, revealed, and draw that many cards.", "https://wiki.dominionstrategy.com/index.php/Silos")
SINISTER_PLOT = CardShapedThing("Sinister Plot", {"Project"}, Cost(coins=4), "At the start of your turn, add a token here, or remove your tokens here for +1 Card each.", "https://wiki.dominionstrategy.com/index.php/Sinister_Plot")
STAR_CHART = CardShapedThing("Star Chart", {"Project"}, Cost(coins=3), "When shuffling, you may pick one of the cards to go on top.", "https://wiki.dominionstrategy.com/index.php/Star_Chart")
FLAG = CardShapedThing("Flag", {"Artifact"}, Cost(), "When drawing your hand, +1 Card.", "https://wiki.dominionstrategy.com/index.php/Flag")
HORN = CardShapedThing("Horn", {"Artifact"}, Cost(), "Once per turn, when you discard a Border Guard from play, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Horn")
KEY = CardShapedThing("Key", {"Artifact"}, Cost(), "At the start of your turn, +$1.", "https://wiki.dominionstrategy.com/index.php/Key")
LANTERN = CardShapedThing("Lantern", {"Artifact"}, Cost(), "Border Guards you play reveal 3 cards and discard 2. (It takes all 3 being Actions to take the Horn.)", "https://wiki.dominionstrategy.com/index.php/Lantern")
TREASURE_CHEST = CardShapedThing("Treasure Chest", {"Artifact"}, Cost(), "At the start of your Buy phase, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Treasure_Chest")
ANIMAL_FAIR = CardShapedThing("Animal Fair", {"Action"}, Cost(coins=7), "+$4+1 Buy per empty supply pile.Instead of paying this card's cost, you may trash an Action card from your hand.", "https://wiki.dominionstrategy.com/index.php/Animal_Fair")
BARGE = CardShapedThing("Barge", {"Action", "Duration"}, Cost(coins=5), "Either now or at the start of your next turn, +3 Cards and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Barge")
BLACK_CAT = CardShapedThing("Black Cat", {"Action", "Attack", "Reaction"}, Cost(coins=2), "+2 CardsIf it isn't your turn, each other player gains a Curse.When another player gains a Victory card, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Black_Cat")
BOUNTY_HUNTER = CardShapedThing("Bounty Hunter", {"Action"}, Cost(coins=4), "+1 ActionExile a card from your hand. If you didn't have a copy of it in Exile, +$3.", "https://wiki.dominionstrategy.com/index.php/Bounty_Hunter")
CAMEL_TRAIN = CardShapedThing("Camel Train", {"Action"}, Cost(coins=3), "Exile a non-Victory card from the Supply.When you gain this, Exile a Gold from the Supply.", "https://wiki.dominionstrategy.com/index.php/Camel_Train")
CARDINAL = CardShapedThing("Cardinal", {"Action", "Attack"}, Cost(coins=4), "+$2Each other player reveals the top 2 cards of their deck, Exiles one costing from $3 to $6, and discards the rest.", "https://wiki.dominionstrategy.com/index.php/Cardinal")
CAVALRY = CardShapedThing("Cavalry", {"Action"}, Cost(coins=4), "Gain 2 Horses.When you gain this, +2 Cards, +1 Buy, and if it's your Buy phase return to your Action phase.", "https://wiki.dominionstrategy.com/index.php/Cavalry")
COVEN = CardShapedThing("Coven", {"Action", "Attack"}, Cost(coins=5), "+1 Action+$2Each other player Exiles a Curse from the Supply. If they can't, they discard their Exiled Curses.", "https://wiki.dominionstrategy.com/index.php/Coven")
DESTRIER = CardShapedThing("Destrier", {"Action"}, Cost(coins=6), "+2 Cards+1 ActionDuring your turns, this costs $1 less per card you've gained this turn.", "https://wiki.dominionstrategy.com/index.php/Destrier")
DISPLACE = CardShapedThing("Displace", {"Action"}, Cost(coins=5), "Exile a card from your hand. Gain a differently named card costing up to $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Displace")
FALCONER = CardShapedThing("Falconer", {"Action", "Reaction"}, Cost(coins=5), "Gain a card to your hand costing less than this.When any player gains a card with 2 or more types (Action, Attack, etc.), you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Falconer")
FISHERMAN = CardShapedThing("Fisherman", {"Action"}, Cost(coins=5), "+1 Card+1 Action+$1During your turns, if your discard pile is empty, this costs $3 less.", "https://wiki.dominionstrategy.com/index.php/Fisherman")
GATEKEEPER = CardShapedThing("Gatekeeper", {"Action", "Duration", "Attack"}, Cost(coins=5), "At the start of your next turn, +$3. Until then, when another player gains an Action or Treasure card they don't have an Exiled copy of, they Exile it.", "https://wiki.dominionstrategy.com/index.php/Gatekeeper")
GOATHERD = CardShapedThing("Goatherd", {"Action"}, Cost(coins=3), "+1 ActionYou may trash a card from your hand.+1 Card per card the player to your right trashed on their last turn.", "https://wiki.dominionstrategy.com/index.php/Goatherd")
GROOM = CardShapedThing("Groom", {"Action"}, Cost(coins=4), "Gain a card costing up to $4. If it's an…Action card, gain a Horse;Treasure card, gain a Silver;Victory card, +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Groom")
HOSTELRY = CardShapedThing("Hostelry", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsWhen you gain this, you may discard any number of Treasures, revealed, to gain that many Horses.", "https://wiki.dominionstrategy.com/index.php/Hostelry")
HUNTING_LODGE = CardShapedThing("Hunting Lodge", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsYou may discard your hand for +5 Cards.", "https://wiki.dominionstrategy.com/index.php/Hunting_Lodge")
KILN = CardShapedThing("Kiln", {"Action"}, Cost(coins=5), "+$2The next time you play a card this turn, you may first gain a copy of it.", "https://wiki.dominionstrategy.com/index.php/Kiln")
LIVERY = CardShapedThing("Livery", {"Action"}, Cost(coins=5), "+$3This turn, when you gain a card costing $4 or more, gain a Horse.", "https://wiki.dominionstrategy.com/index.php/Livery")
MASTERMIND = CardShapedThing("Mastermind", {"Action", "Duration"}, Cost(coins=5), "At the start of your next turn, you may play an Action card from your hand three times.", "https://wiki.dominionstrategy.com/index.php/Mastermind")
PADDOCK = CardShapedThing("Paddock", {"Action"}, Cost(coins=5), "+$2Gain 2 Horses.+1 Action per empty Supply pile.", "https://wiki.dominionstrategy.com/index.php/Paddock")
SANCTUARY = CardShapedThing("Sanctuary", {"Action"}, Cost(coins=5), "+1 Card+1 Action+1 BuyYou may Exile a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Sanctuary")
SCRAP = CardShapedThing("Scrap", {"Action"}, Cost(coins=3), "Trash a card from your hand. Choose a different thing per $1 it costs: +1 Card; +1 Action; +1 Buy; +$1; gain a Silver; gain a Horse.", "https://wiki.dominionstrategy.com/index.php/Scrap")
SHEEPDOG = CardShapedThing("Sheepdog", {"Action", "Reaction"}, Cost(coins=3), "+2 CardsWhen you gain a card, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Sheepdog")
SLEIGH = CardShapedThing("Sleigh", {"Action", "Reaction"}, Cost(coins=2), "Gain 2 Horses.When you gain a card, you may discard this, to put that card into your hand or onto your deck.", "https://wiki.dominionstrategy.com/index.php/Sleigh")
SNOWY_VILLAGE = CardShapedThing("Snowy Village", {"Action"}, Cost(coins=3), "+1 Card+4 Actions+1 BuyIgnore any further +Actions you get this turn.", "https://wiki.dominionstrategy.com/index.php/Snowy_Village")
STOCKPILE = CardShapedThing("Stockpile", {"Treasure"}, Cost(coins=3), "$3+1 BuyExile this.", "https://wiki.dominionstrategy.com/index.php/Stockpile")
SUPPLIES = CardShapedThing("Supplies", {"Treasure"}, Cost(coins=2), "$1Gain a Horse onto your deck.", "https://wiki.dominionstrategy.com/index.php/Supplies")
VILLAGE_GREEN = CardShapedThing("Village Green", {"Action", "Duration", "Reaction"}, Cost(coins=4), "Either now or at the start of your next turn, +1 Card and +2 Actions.When you discard this other than during Clean-up, you may play it.", "https://wiki.dominionstrategy.com/index.php/Village_Green")
WAYFARER = CardShapedThing("Wayfarer", {"Action"}, Cost(coins=6), "+3 CardsYou may gain a Silver.This has the same cost as the last other card gained this turn, if any.", "https://wiki.dominionstrategy.com/index.php/Wayfarer")
HORSE = CardShapedThing("Horse", {"Action"}, Cost(coins=3), "+2 Cards+1 ActionReturn this to its pile.(This is not in the Supply.)", "https://wiki.dominionstrategy.com/index.php/Horse")
ALLIANCE = CardShapedThing("Alliance", {"Event"}, Cost(coins=10), "Gain a Province, a Duchy, an Estate, a Gold, a Silver, and a Copper.", "https://wiki.dominionstrategy.com/index.php/Alliance")
BANISH = CardShapedThing("Banish", {"Event"}, Cost(coins=4), "Exile any number of cards with the same name from your hand.", "https://wiki.dominionstrategy.com/index.php/Banish")
BARGAIN = CardShapedThing("Bargain", {"Event"}, Cost(coins=4), "Gain a non-Victory card costing up to $5. Each other player gains a Horse.", "https://wiki.dominionstrategy.com/index.php/Bargain")
COMMERCE = CardShapedThing("Commerce", {"Event"}, Cost(coins=5), "Gain a Gold per differently named card you've gained this turn.", "https://wiki.dominionstrategy.com/index.php/Commerce")
DELAY = CardShapedThing("Delay", {"Event"}, Cost(coins=0), "You may set aside an Action card from your hand. At the start of your next turn, play it.", "https://wiki.dominionstrategy.com/index.php/Delay")
DEMAND = CardShapedThing("Demand", {"Event"}, Cost(coins=5), "Gain a Horse and a card costing up to $4, both onto your deck.", "https://wiki.dominionstrategy.com/index.php/Demand")
DESPERATION = CardShapedThing("Desperation", {"Event"}, Cost(coins=0), "Once per turn: You may gain a Curse. If you do, +1 Buy and +$2.", "https://wiki.dominionstrategy.com/index.php/Desperation")
ENCLAVE = CardShapedThing("Enclave", {"Event"}, Cost(coins=8), "Gain a Gold. Exile a Duchy from the Supply.", "https://wiki.dominionstrategy.com/index.php/Enclave")
ENHANCE = CardShapedThing("Enhance", {"Event"}, Cost(coins=3), "You may trash a non-Victory card from your hand, to gain a card costing up to $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Enhance")
GAMBLE = CardShapedThing("Gamble", {"Event"}, Cost(coins=2), "+1 BuyDiscard the top card of your deck. If it's an Action or Treasure, you may play it.", "https://wiki.dominionstrategy.com/index.php/Gamble")
INVEST = CardShapedThing("Invest", {"Event"}, Cost(coins=4), "Exile an Action card from the Supply. While it's in Exile, when another player gains or Invests in a copy of it, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Invest")
MARCH = CardShapedThing("March", {"Event"}, Cost(coins=3), "Look through your discard pile. You may play an Action card from it.", "https://wiki.dominionstrategy.com/index.php/March")
POPULATE = CardShapedThing("Populate", {"Event"}, Cost(coins=10), "Gain one card from each Action Supply pile.", "https://wiki.dominionstrategy.com/index.php/Populate")
PURSUE = CardShapedThing("Pursue", {"Event"}, Cost(coins=2), "+1 BuyName a card.  Reveal the top 4 cards from your deck.  Put the matches back and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Pursue")
REAP = CardShapedThing("Reap", {"Event"}, Cost(coins=7), "Gain a Gold, setting it aside. At the start of your next turn, play it.", "https://wiki.dominionstrategy.com/index.php/Reap")
RIDE = CardShapedThing("Ride", {"Event"}, Cost(coins=2), "Gain a Horse.", "https://wiki.dominionstrategy.com/index.php/Ride")
SEIZE_THE_DAY = CardShapedThing("Seize the Day", {"Event"}, Cost(coins=4), "Once per game: Take an extra turn after this one.", "https://wiki.dominionstrategy.com/index.php/Seize_the_Day")
STAMPEDE = CardShapedThing("Stampede", {"Event"}, Cost(coins=5), "If you have 5 or fewer cards in play, gain 5 Horses onto your deck.", "https://wiki.dominionstrategy.com/index.php/Stampede")
TOIL = CardShapedThing("Toil", {"Event"}, Cost(coins=2), "+1 BuyYou may play an Action card from your hand.", "https://wiki.dominionstrategy.com/index.php/Toil")
TRANSPORT = CardShapedThing("Transport", {"Event"}, Cost(coins=3), "Choose one: Exile an Action card from the Supply; or put an Action card you have in Exile onto your deck.", "https://wiki.dominionstrategy.com/index.php/Transport")
WAY_OF_THE_BUTTERFLY = CardShapedThing("Way of the Butterfly", {"Way"}, Cost(), "You may return this to its pile to gain a card costing exactly $1 more than it.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Butterfly")
WAY_OF_THE_CAMEL = CardShapedThing("Way of the Camel", {"Way"}, Cost(), "Exile a Gold from the Supply.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Camel")
WAY_OF_THE_CHAMELEON = CardShapedThing("Way of the Chameleon", {"Way"}, Cost(), "Follow this card's instructions; each time that would give you +Cards this turn, you get +$ instead, and vice-versa.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Chameleon")
WAY_OF_THE_FROG = CardShapedThing("Way of the Frog", {"Way"}, Cost(), "+1 ActionWhen you discard this from play this turn, put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Frog")
WAY_OF_THE_GOAT = CardShapedThing("Way of the Goat", {"Way"}, Cost(), "Trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Goat")
WAY_OF_THE_HORSE = CardShapedThing("Way of the Horse", {"Way"}, Cost(), "+2 Cards+1 ActionReturn this to its pile.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Horse")
WAY_OF_THE_MOLE = CardShapedThing("Way of the Mole", {"Way"}, Cost(), "+1 ActionDiscard your hand. +3 Cards.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Mole")
WAY_OF_THE_MONKEY = CardShapedThing("Way of the Monkey", {"Way"}, Cost(), "+1 Buy+$1", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Monkey")
WAY_OF_THE_MOUSE = CardShapedThing("Way of the Mouse", {"Way"}, Cost(), "Play the set-aside card, leaving it there.Setup: Set aside an unused non-Duration Action costing $2 or $3.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Mouse")
WAY_OF_THE_MULE = CardShapedThing("Way of the Mule", {"Way"}, Cost(), "+1 Action+$1", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Mule")
WAY_OF_THE_OTTER = CardShapedThing("Way of the Otter", {"Way"}, Cost(), "+2 Cards", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Otter")
WAY_OF_THE_OX = CardShapedThing("Way of the Ox", {"Way"}, Cost(), "+2 Actions", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Ox")
WAY_OF_THE_OWL = CardShapedThing("Way of the Owl", {"Way"}, Cost(), "Draw until you have 6 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Owl")
WAY_OF_THE_PIG = CardShapedThing("Way of the Pig", {"Way"}, Cost(), "+1 Card+1 Action", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Pig")
WAY_OF_THE_RAT = CardShapedThing("Way of the Rat", {"Way"}, Cost(), "You may discard a Treasure to gain a copy of this.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Rat")
WAY_OF_THE_SEAL = CardShapedThing("Way of the Seal", {"Way"}, Cost(), "+$1This turn, when you gain a card, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Seal")
WAY_OF_THE_SHEEP = CardShapedThing("Way of the Sheep", {"Way"}, Cost(), "+$2", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Sheep")
WAY_OF_THE_SQUIRREL = CardShapedThing("Way of the Squirrel", {"Way"}, Cost(), "+2 Cards at the end of this turn.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Squirrel")
WAY_OF_THE_TURTLE = CardShapedThing("Way of the Turtle", {"Way"}, Cost(), "Set this aside. If you did, play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Turtle")
WAY_OF_THE_WORM = CardShapedThing("Way of the Worm", {"Way"}, Cost(), "Exile an Estate from the Supply.", "https://wiki.dominionstrategy.com/index.php/Way_of_the_Worm")
ACOLYTE = CardShapedThing("Acolyte", {"Action", "Augur"}, Cost(coins=4), "You may trash an Action or Victory card from your hand to gain a Gold.You may trash this to gain an Augur.", "https://wiki.dominionstrategy.com/index.php/Acolyte")
ARCHER = CardShapedThing("Archer", {"Action", "Attack", "Clash"}, Cost(coins=4), "+$2Each other player with 5 or more cards in hand reveals all but one, and discards one of those you choose.", "https://wiki.dominionstrategy.com/index.php/Archer")
BARBARIAN = CardShapedThing("Barbarian", {"Action", "Attack"}, Cost(coins=5), "+$2Each other player trashes the top card of their deck. If it costs $3 or more they gain a cheaper card sharing a type with it; otherwise they gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Barbarian")
BATTLE_PLAN = CardShapedThing("Battle Plan", {"Action", "Clash"}, Cost(coins=3), "+1 Card+1 ActionYou may reveal an Attack card from your hand for +1 Card.You may rotate any Supply pile.", "https://wiki.dominionstrategy.com/index.php/Battle_Plan")
BAUBLE = CardShapedThing("Bauble", {"Treasure", "Liaison"}, Cost(coins=2), "Choose two different options: +1 Buy; +$1; +1 Favor; this turn, when you gain a card, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Bauble")
BLACKSMITH = CardShapedThing("Blacksmith", {"Action", "Townsfolk"}, Cost(coins=3), "Choose one: Draw until you have 6 cards in hand; or +2 Cards; or +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Blacksmith")
BROKER = CardShapedThing("Broker", {"Action", "Liaison"}, Cost(coins=4), "Trash a card from your hand and choose one:+1 Card per $1 it costs;or +1 Action per $1 it costs; or +$1 per $1 it costs; or +1 Favor per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Broker")
CAPITAL_CITY = CardShapedThing("Capital City", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsYou may discard 2 cards for +$2.You may pay $2 for +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Capital_City")
CARPENTER = CardShapedThing("Carpenter", {"Action"}, Cost(coins=4), "If no Supply piles are empty, +1 Action and gain a card costing up to $4.Otherwise, trash a card from your hand and gain a card costing up to $2 more than it.", "https://wiki.dominionstrategy.com/index.php/Carpenter")
CONJURER = CardShapedThing("Conjurer", {"Action", "Duration", "Wizard"}, Cost(coins=4), "Gain a card costing up to $4.At the start of your next turn, put this into your hand.", "https://wiki.dominionstrategy.com/index.php/Conjurer")
CONTRACT = CardShapedThing("Contract", {"Treasure", "Duration", "Liaison"}, Cost(coins=5), "$2+1 FavorYou may set aside an Action from your hand to play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Contract")
COURIER = CardShapedThing("Courier", {"Action"}, Cost(coins=4), "+$1Discard the top card of your deck. Look through your discard pile; you may play an Action or Treasure from it.", "https://wiki.dominionstrategy.com/index.php/Courier")
DISTANT_SHORE = CardShapedThing("Distant Shore", {"Action", "Victory", "Odyssey"}, Cost(coins=6), "+2 Cards+1 ActionGain an Estate.2VP", "https://wiki.dominionstrategy.com/index.php/Distant_Shore")
ELDER = CardShapedThing("Elder", {"Action", "Townsfolk"}, Cost(coins=5), "+$2You may play an Action card from your hand. When it gives you a choice of abilities (with \"choose\") this turn, you may choose an extra (different) option.", "https://wiki.dominionstrategy.com/index.php/Elder")
EMISSARY = CardShapedThing("Emissary", {"Action", "Liaison"}, Cost(coins=5), "+3 CardsIf this made you shuffle (at least one card), +1 Action and +2 Favors.", "https://wiki.dominionstrategy.com/index.php/Emissary")
GALLERIA = CardShapedThing("Galleria", {"Action"}, Cost(coins=5), "+$3This turn, when you gain a card costing $3 or $4, +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Galleria")
GARRISON = CardShapedThing("Garrison", {"Action", "Duration", "Fort"}, Cost(coins=4), "+$2This turn, when you gain a card, add a token here. At the start of your next turn, remove them for +1 Card each.", "https://wiki.dominionstrategy.com/index.php/Garrison")
GUILDMASTER = CardShapedThing("Guildmaster", {"Action", "Liaison"}, Cost(coins=5), "+$3This turn, when you gain a card, +1 Favor.", "https://wiki.dominionstrategy.com/index.php/Guildmaster")
HERB_GATHERER = CardShapedThing("Herb Gatherer", {"Action", "Augur"}, Cost(coins=3), "+1 BuyPut your deck into your discard pile. Look through it and you may play a Treasure from it.You may rotate the Augurs.", "https://wiki.dominionstrategy.com/index.php/Herb_Gatherer")
HIGHWAYMAN = CardShapedThing("Highwayman", {"Action", "Duration", "Attack"}, Cost(coins=5), "At the start of your next turn, discard this from play and +3 Cards.Until then, the first Treasure each other player plays each turn does nothing.", "https://wiki.dominionstrategy.com/index.php/Highwayman")
HILL_FORT = CardShapedThing("Hill Fort", {"Action", "Fort"}, Cost(coins=5), "Gain a card costing up to $4. Choose one: Put it into your hand; or +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Hill_Fort")
HUNTER = CardShapedThing("Hunter", {"Action"}, Cost(coins=5), "+1 ActionReveal the top 3 cards of your deck. From those cards, put an Action, a Treasure, and a Victory card into your hand. Discard the rest.", "https://wiki.dominionstrategy.com/index.php/Hunter")
IMPORTER = CardShapedThing("Importer", {"Action", "Duration", "Liaison"}, Cost(coins=3), "At the start of your next turn, gain a card costing up to $5.Setup: Each player gets +4 Favors.", "https://wiki.dominionstrategy.com/index.php/Importer")
INNKEEPER = CardShapedThing("Innkeeper", {"Action"}, Cost(coins=4), "+1 ActionChoose one: +1 Card; or +3 Cards, then discard 3 cards; or +5 Cards, then discard 6 cards.", "https://wiki.dominionstrategy.com/index.php/Innkeeper")
LICH = CardShapedThing("Lich", {"Action", "Wizard"}, Cost(coins=6), "+6 Cards+2 ActionsSkip a turn.When you trash this, discard it and gain a cheaper card from the trash.", "https://wiki.dominionstrategy.com/index.php/Lich")
MARQUIS = CardShapedThing("Marquis", {"Action"}, Cost(coins=6), "+1 Buy+1 Card per card in your hand. Discard down to 10 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Marquis")
MERCHANT_CAMP = CardShapedThing("Merchant Camp", {"Action"}, Cost(coins=3), "+2 Actions+$1When you discard this from play, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Merchant_Camp")
MILLER = CardShapedThing("Miller", {"Action", "Townsfolk"}, Cost(coins=4), "+1 ActionLook at the top 4 cards of your deck. Put one into your hand and discard the rest.", "https://wiki.dominionstrategy.com/index.php/Miller")
MODIFY = CardShapedThing("Modify", {"Action"}, Cost(coins=5), "Trash a card from your hand. Choose one: +1 Card and +1 Action; or gain a card costing up to $2 more than the trashed card.", "https://wiki.dominionstrategy.com/index.php/Modify")
OLD_MAP = CardShapedThing("Old Map", {"Action", "Odyssey"}, Cost(coins=3), "+1 Card+1 ActionDiscard a card. +1 Card.You may rotate the Odysseys.", "https://wiki.dominionstrategy.com/index.php/Old_Map")
ROYAL_GALLEY = CardShapedThing("Royal Galley", {"Action", "Duration"}, Cost(coins=4), "+1 CardYou may play a non-Duration Action card from your hand. Set it aside; if you did, then at the start of your next turn, play it.", "https://wiki.dominionstrategy.com/index.php/Royal_Galley")
SENTINEL = CardShapedThing("Sentinel", {"Action"}, Cost(coins=3), "Look at the top 5 cards of your deck. You may trash up to 2 of them. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Sentinel")
SIBYL = CardShapedThing("Sibyl", {"Action", "Augur"}, Cost(coins=6), "+4 Cards+1 ActionPut a card from your hand on top of your deck, and another on the bottom.", "https://wiki.dominionstrategy.com/index.php/Sibyl")
SKIRMISHER = CardShapedThing("Skirmisher", {"Action", "Attack"}, Cost(coins=5), "+1 Card+1 Action+$1This turn, when you gain an Attack card, each other player discards down to 3 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Skirmisher")
SORCERER = CardShapedThing("Sorcerer", {"Action", "Attack", "Wizard"}, Cost(coins=5), "+1 Card+1 ActionEach other player names a card, then reveals the top card of their deck. If wrong, they gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Sorcerer")
SORCERESS = CardShapedThing("Sorceress", {"Action", "Attack", "Augur"}, Cost(coins=5), "+1 ActionName a card. Reveal the top card of your deck and put it into your hand. If it's the named card, each other player gains a Curse.", "https://wiki.dominionstrategy.com/index.php/Sorceress")
SPECIALIST = CardShapedThing("Specialist", {"Action"}, Cost(coins=5), "You may play an Action or Treasure from your hand. Choose one: Play it again; or gain a copy of it.", "https://wiki.dominionstrategy.com/index.php/Specialist")
STRONGHOLD = CardShapedThing("Stronghold", {"Action", "Victory", "Duration", "Fort"}, Cost(coins=6), "Choose one: +$3; or at the start of your next turn, +3 Cards.2VP", "https://wiki.dominionstrategy.com/index.php/Stronghold")
STUDENT = CardShapedThing("Student", {"Action", "Wizard", "Liaison"}, Cost(coins=3), "+1 ActionYou may rotate the Wizards.Trash a card from your hand. If it's a Treasure, +1 Favor and put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Student")
SUNKEN_TREASURE = CardShapedThing("Sunken Treasure", {"Treasure", "Odyssey"}, Cost(coins=5), "Gain an Action card you don't have a copy of in play.", "https://wiki.dominionstrategy.com/index.php/Sunken_Treasure")
SWAP = CardShapedThing("Swap", {"Action"}, Cost(coins=5), "+1 Card+1 ActionYou may return an Action from your hand to its pile, to gain to your hand a different Action costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Swap")
SYCOPHANT = CardShapedThing("Sycophant", {"Action", "Liaison"}, Cost(coins=2), "+1 ActionDiscard 3 cards. If you discarded at least one, +$3.When you gain or trash this, +2 Favors.", "https://wiki.dominionstrategy.com/index.php/Sycophant")
TENT = CardShapedThing("Tent", {"Action", "Fort"}, Cost(coins=3), "+$2You may rotate the Forts.When you discard this from play, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Tent")
TERRITORY = CardShapedThing("Territory", {"Victory", "Clash"}, Cost(coins=6), "Worth 1VP per differently named Victory card you have.When you gain this, gain a Gold per empty Supply pile.", "https://wiki.dominionstrategy.com/index.php/Territory")
TOWN = CardShapedThing("Town", {"Action"}, Cost(coins=4), "Choose one: +1 Card and +2 Actions; or +1 Buy and +$2.", "https://wiki.dominionstrategy.com/index.php/Town")
TOWN_CRIER = CardShapedThing("Town Crier", {"Action", "Townsfolk"}, Cost(coins=2), "Choose one: +$2; or gain a Silver; or +1 Card and +1 Action.You may rotate the Townsfolk.", "https://wiki.dominionstrategy.com/index.php/Town_Crier")
UNDERLING = CardShapedThing("Underling", {"Action", "Liaison"}, Cost(coins=3), "+1 Card+1 Action+1 Favor", "https://wiki.dominionstrategy.com/index.php/Underling")
VOYAGE = CardShapedThing("Voyage", {"Action", "Duration", "Odyssey"}, Cost(coins=4), "+1 ActionTake an extra turn after this one (but not a 3rd turn in a row), during which you can only play 3 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Voyage")
WARLORD = CardShapedThing("Warlord", {"Action", "Duration", "Attack", "Clash"}, Cost(coins=5), "+1 ActionAt the start of your next turn, +2 Cards. Until then, other players can't play an Action from their hand that they have 2 or more copies of in play.", "https://wiki.dominionstrategy.com/index.php/Warlord")
ARCHITECTS_GUILD = CardShapedThing("Architects' Guild", {"Ally"}, Cost(), "When you gain a card, you may spend 2 Favors to gain a cheaper non-Victory card.", "https://wiki.dominionstrategy.com/index.php/Architects%27_Guild")
BAND_OF_NOMADS = CardShapedThing("Band of Nomads", {"Ally"}, Cost(), "When you gain a card costing $3 or more, you may spend a Favor, for +1 Card, or +1 Action, or +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Band_of_Nomads")
CAVE_DWELLERS = CardShapedThing("Cave Dwellers", {"Ally"}, Cost(), "At the start of your turn, you may spend a Favor, to discard a card then draw a card. Repeat as desired.", "https://wiki.dominionstrategy.com/index.php/Cave_Dwellers")
CIRCLE_OF_WITCHES = CardShapedThing("Circle of Witches", {"Ally"}, Cost(), "After playing a Liaison, you may spend 3 Favors to have each other player gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Circle_of_Witches")
CITY_STATE = CardShapedThing("City-state", {"Ally"}, Cost(), "When you gain an Action card during your turn, you may spend 2 Favors to play it.", "https://wiki.dominionstrategy.com/index.php/City-state")
COASTAL_HAVEN = CardShapedThing("Coastal Haven", {"Ally"}, Cost(), "When discarding your hand in Clean-up, you may spend any number of Favors to keep that many cards in hand for next turn (you still draw 5).", "https://wiki.dominionstrategy.com/index.php/Coastal_Haven")
CRAFTERS_GUILD = CardShapedThing("Crafters' Guild", {"Ally"}, Cost(), "At the start of your turn, you may spend 2 Favors to gain a card costing up to $4 onto your deck.", "https://wiki.dominionstrategy.com/index.php/Crafters%27_Guild")
DESERT_GUIDES = CardShapedThing("Desert Guides", {"Ally"}, Cost(), "At the start of your turn, you may spend a Favor to discard your hand and draw 5 cards. Repeat as desired.", "https://wiki.dominionstrategy.com/index.php/Desert_Guides")
FAMILY_OF_INVENTORS = CardShapedThing("Family of Inventors", {"Ally"}, Cost(), "At the start of your Buy phase, you may put a Favor token you have on a non-Victory Supply pile. Cards cost $1 less per Favor token on their piles.", "https://wiki.dominionstrategy.com/index.php/Family_of_Inventors")
FELLOWSHIP_OF_SCRIBES = CardShapedThing("Fellowship of Scribes", {"Ally"}, Cost(), "After playing an Action, if you have 4 or fewer cards in hand, you may spend a Favor for +1 Card.", "https://wiki.dominionstrategy.com/index.php/Fellowship_of_Scribes")
FOREST_DWELLERS = CardShapedThing("Forest Dwellers", {"Ally"}, Cost(), "At the start of your turn, you may spend a Favor to look at the top 3 cards of your deck, discard any number and put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Forest_Dwellers")
GANG_OF_PICKPOCKETS = CardShapedThing("Gang of Pickpockets", {"Ally"}, Cost(), "At the start of your turn, discard down to 4 cards in hand unless you spend a Favor.", "https://wiki.dominionstrategy.com/index.php/Gang_of_Pickpockets")
ISLAND_FOLK = CardShapedThing("Island Folk", {"Ally"}, Cost(), "At the end of your turn, you may spend 5 Favors to take an extra turn after this one (but not a 3rd turn in a row).", "https://wiki.dominionstrategy.com/index.php/Island_Folk")
LEAGUE_OF_BANKERS = CardShapedThing("League of Bankers", {"Ally"}, Cost(), "At the start of your Buy phase, +$1 per 4 Favors you have (round down).", "https://wiki.dominionstrategy.com/index.php/League_of_Bankers")
LEAGUE_OF_SHOPKEEPERS = CardShapedThing("League of Shopkeepers", {"Ally"}, Cost(), "After playing a Liaison, if you have 5 or more Favors, +$1, and if 10 or more, +1 Action and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/League_of_Shopkeepers")
MARKET_TOWNS = CardShapedThing("Market Towns", {"Ally"}, Cost(), "At the start of your Buy phase, you may spend a Favor to play an Action card from your hand. Repeat as desired.", "https://wiki.dominionstrategy.com/index.php/Market_Towns")
MOUNTAIN_FOLK = CardShapedThing("Mountain Folk", {"Ally"}, Cost(), "At the start of your turn, you may spend 5 Favors for +3 Cards.", "https://wiki.dominionstrategy.com/index.php/Mountain_Folk")
ORDER_OF_ASTROLOGERS = CardShapedThing("Order of Astrologers", {"Ally"}, Cost(), "When shuffling, you may pick one card per Favor you spend to go on top.", "https://wiki.dominionstrategy.com/index.php/Order_of_Astrologers")
ORDER_OF_MASONS = CardShapedThing("Order of Masons", {"Ally"}, Cost(), "When shuffling, you may pick up to 2 cards per Favor you spend to put into your discard pile.", "https://wiki.dominionstrategy.com/index.php/Order_of_Masons")
PEACEFUL_CULT = CardShapedThing("Peaceful Cult", {"Ally"}, Cost(), "At the start of your Buy phase, you may spend any number of Favors to trash that many cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Peaceful_Cult")
PLATEAU_SHEPHERDS = CardShapedThing("Plateau Shepherds", {"Ally"}, Cost(), "When scoring, pair up your Favors with cards you have costing $2, for 2VP per pair.", "https://wiki.dominionstrategy.com/index.php/Plateau_Shepherds")
TRAPPERS_LODGE = CardShapedThing("Trappers' Lodge", {"Ally"}, Cost(), "When you gain a card, you may spend a Favor to put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Trappers%27_Lodge")
WOODWORKERS_GUILD = CardShapedThing("Woodworkers' Guild", {"Ally"}, Cost(), "At the start of your Buy phase, you may spend a Favor to trash an Action card from your hand. If you did, gain an Action card.", "https://wiki.dominionstrategy.com/index.php/Woodworkers%27_Guild")
ABUNDANCE = CardShapedThing("Abundance", {"Treasure", "Duration"}, Cost(coins=4), "The next time you gain an Action card: +1 Buy and +$3.", "https://wiki.dominionstrategy.com/index.php/Abundance")
BURIED_TREASURE = CardShapedThing("Buried Treasure", {"Treasure", "Duration"}, Cost(coins=5), "At the start of your next turn, +1 Buy and +$3.When you gain this, play it.", "https://wiki.dominionstrategy.com/index.php/Buried_Treasure")
CABIN_BOY = CardShapedThing("Cabin Boy", {"Action", "Duration"}, Cost(coins=4), "+1 Card+1 ActionAt the start of your next turn, choose one: +$2; or trash this to gain a Duration card.", "https://wiki.dominionstrategy.com/index.php/Cabin_Boy")
CAGE = CardShapedThing("Cage", {"Treasure", "Duration"}, Cost(coins=2), "Set aside up to 4 cards from your hand face down (on this). The next time you gain a Victory card, trash this, and put the set aside cards into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Cage")
CREW = CardShapedThing("Crew", {"Action", "Duration"}, Cost(coins=5), "+3 CardsAt the start of your next turn, put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Crew")
CRUCIBLE = CardShapedThing("Crucible", {"Treasure"}, Cost(coins=4), "Trash a card from your hand. +$1 per $1 it costs.", "https://wiki.dominionstrategy.com/index.php/Crucible")
CUTTHROAT = CardShapedThing("Cutthroat", {"Action", "Duration", "Attack"}, Cost(coins=5), "Each other player discards down to 3 cards in hand.The next time anyone gains a Treasure costing $5 or more, gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Cutthroat")
ENLARGE = CardShapedThing("Enlarge", {"Action", "Duration"}, Cost(coins=5), "Now and at the start of your next turn: Trash a card from your hand, and gain one costing up to $2 more.", "https://wiki.dominionstrategy.com/index.php/Enlarge")
FIGURINE = CardShapedThing("Figurine", {"Treasure"}, Cost(coins=5), "+2 CardsYou may discard an Action card for +1 Buy and +$1.", "https://wiki.dominionstrategy.com/index.php/Figurine")
FIRST_MATE = CardShapedThing("First Mate", {"Action"}, Cost(coins=5), "Play any number of Action cards with the same name from your hand, then draw until you have 6 cards in hand.", "https://wiki.dominionstrategy.com/index.php/First_Mate")
FLAGSHIP = CardShapedThing("Flagship", {"Action", "Duration", "Command"}, Cost(coins=4), "+$2The next time you play a non-Command Action card, replay it.", "https://wiki.dominionstrategy.com/index.php/Flagship")
FORTUNE_HUNTER = CardShapedThing("Fortune Hunter", {"Action"}, Cost(coins=4), "+$2Look at the top 3 cards of your deck. You may play a Treasure from them. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Fortune_Hunter")
FRIGATE = CardShapedThing("Frigate", {"Action", "Duration", "Attack"}, Cost(coins=5), "+$3Until the start of your next turn, each time another player plays an Action card, they discard down to 4 cards in hand afterwards.", "https://wiki.dominionstrategy.com/index.php/Frigate")
GONDOLA = CardShapedThing("Gondola", {"Treasure", "Duration"}, Cost(coins=4), "Either now or at the start of your next turn: +$2.When you gain this, you may play an Action card from your hand.", "https://wiki.dominionstrategy.com/index.php/Gondola")
GROTTO = CardShapedThing("Grotto", {"Action", "Duration"}, Cost(coins=2), "+1 ActionSet aside up to 4 cards from your hand face down (on this). At the start of your next turn, discard them, then draw as many.", "https://wiki.dominionstrategy.com/index.php/Grotto")
HARBOR_VILLAGE = CardShapedThing("Harbor Village", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsAfter the next Action you play this turn, if it gave you +$, +$1.", "https://wiki.dominionstrategy.com/index.php/Harbor_Village")
JEWELLED_EGG = CardShapedThing("Jewelled Egg", {"Treasure"}, Cost(coins=2), "$1+1 BuyWhen you trash this, gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Jewelled_Egg")
KINGS_CACHE = CardShapedThing("King's Cache", {"Treasure"}, Cost(coins=7), "You may play a Treasure from your hand 3 times.", "https://wiki.dominionstrategy.com/index.php/King%27s_Cache")
LANDING_PARTY = CardShapedThing("Landing Party", {"Action", "Duration"}, Cost(coins=4), "+2 Cards+2 ActionsThe next time the first card you play on a turn is a Treasure, put this onto your deck afterwards.", "https://wiki.dominionstrategy.com/index.php/Landing_Party")
LONGSHIP = CardShapedThing("Longship", {"Action", "Duration"}, Cost(coins=5), "+2 ActionsAt the start of your next turn, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Longship")
MAPMAKER = CardShapedThing("Mapmaker", {"Action", "Reaction"}, Cost(coins=4), "Look at the top 4 cards of your deck. Put 2 into your hand and discard the rest.When any player gains a Victory card, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Mapmaker")
MAROON = CardShapedThing("Maroon", {"Action"}, Cost(coins=4), "Trash a card from your hand. +2 Cards per type it has (Action, Attack, etc.).", "https://wiki.dominionstrategy.com/index.php/Maroon")
MINING_ROAD = CardShapedThing("Mining Road", {"Action"}, Cost(coins=5), "+1 Action+1 Buy+$2Once this turn, when you gain a Treasure, you may play it.", "https://wiki.dominionstrategy.com/index.php/Mining_Road")
PENDANT = CardShapedThing("Pendant", {"Treasure"}, Cost(coins=5), "+$1 per differently named Treasure you have in play.", "https://wiki.dominionstrategy.com/index.php/Pendant")
PICKAXE = CardShapedThing("Pickaxe", {"Treasure"}, Cost(coins=5), "$1Trash a card from your hand. If it costs $3 or more, gain a Loot to your hand.", "https://wiki.dominionstrategy.com/index.php/Pickaxe")
PILGRIM = CardShapedThing("Pilgrim", {"Action"}, Cost(coins=5), "+4 CardsPut a card from your hand onto your deck.", "https://wiki.dominionstrategy.com/index.php/Pilgrim")
QUARTERMASTER = CardShapedThing("Quartermaster", {"Action", "Duration"}, Cost(coins=5), "At the start of each of your turns for the rest of the game, choose one: Gain a card costing up to $4, setting it aside on this; or put a card from this into your hand.", "https://wiki.dominionstrategy.com/index.php/Quartermaster")
ROPE = CardShapedThing("Rope", {"Treasure", "Duration"}, Cost(coins=4), "$1+1 BuyAt the start of your next turn, +1 Card and you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Rope")
SACK_OF_LOOT = CardShapedThing("Sack of Loot", {"Treasure"}, Cost(coins=6), "$1+1 BuyGain a Loot.", "https://wiki.dominionstrategy.com/index.php/Sack_of_Loot")
SEARCH = CardShapedThing("Search", {"Action", "Duration"}, Cost(coins=2), "+$2The next time a Supply pile empties, trash this and gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Search")
SECLUDED_SHRINE = CardShapedThing("Secluded Shrine", {"Action", "Duration"}, Cost(coins=3), "+$1The next time you gain a Treasure, trash up to 2 cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Secluded_Shrine")
SHAMAN = CardShapedThing("Shaman", {"Action"}, Cost(coins=2), "+1 Action+$1You may trash a card from your hand.In games using this, at the start of your turn, gain a card from the trash costing up to $6.", "https://wiki.dominionstrategy.com/index.php/Shaman")
SILVER_MINE = CardShapedThing("Silver Mine", {"Treasure"}, Cost(coins=5), "Gain a Treasure costing less than this to your hand.", "https://wiki.dominionstrategy.com/index.php/Silver_Mine")
SIREN = CardShapedThing("Siren", {"Action", "Duration", "Attack"}, Cost(coins=3), "Each other player gains a Curse. At the start of your next turn, draw until you have 8 cards in hand.When you gain this, trash it unless you trash an Action from your hand.", "https://wiki.dominionstrategy.com/index.php/Siren")
STOWAWAY = CardShapedThing("Stowaway", {"Action", "Duration", "Reaction"}, Cost(coins=3), "At the start of your next turn, +2 Cards.When anyone gains a Duration card, you may play this from your hand.", "https://wiki.dominionstrategy.com/index.php/Stowaway")
SWAMP_SHACKS = CardShapedThing("Swamp Shacks", {"Action"}, Cost(coins=4), "+2 Actions+1 Card per 3 cards you have in play (round down).", "https://wiki.dominionstrategy.com/index.php/Swamp_Shacks")
TASKMASTER = CardShapedThing("Taskmaster", {"Action", "Duration"}, Cost(coins=3), "+1 Action, +$1, and if you gain a card costing exactly $5 this turn, then at the start of your next turn, repeat this ability.", "https://wiki.dominionstrategy.com/index.php/Taskmaster")
TOOLS = CardShapedThing("Tools", {"Treasure"}, Cost(coins=4), "Gain a copy of a card anyone has in play.", "https://wiki.dominionstrategy.com/index.php/Tools")
TRICKSTER = CardShapedThing("Trickster", {"Action", "Attack"}, Cost(coins=5), "Each other player gains a Curse.Once this turn, when you discard a Treasure from play, you may set it aside. Put it in your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Trickster")
WEALTHY_VILLAGE = CardShapedThing("Wealthy Village", {"Action"}, Cost(coins=5), "+1 Card+2 ActionsWhen you gain this, if you have at least 3 differently named Treasures in play, gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Wealthy_Village")
AMPHORA = CardShapedThing("Amphora", {"Treasure", "Duration", "Loot"}, Cost(coins=7), "Either now or at the start of your next turn: +1 Buy and +$3.", "https://wiki.dominionstrategy.com/index.php/Amphora")
DOUBLOONS = CardShapedThing("Doubloons", {"Treasure", "Loot"}, Cost(coins=7), "$3When you gain this, gain a Gold.", "https://wiki.dominionstrategy.com/index.php/Doubloons")
ENDLESS_CHALICE = CardShapedThing("Endless Chalice", {"Treasure", "Duration", "Loot"}, Cost(coins=7), "Now and at the start of each of your turns for the rest of the game:$1+1 Buy", "https://wiki.dominionstrategy.com/index.php/Endless_Chalice")
FIGUREHEAD = CardShapedThing("Figurehead", {"Treasure", "Duration", "Loot"}, Cost(coins=7), "$3At the start of your next turn, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Figurehead")
HAMMER = CardShapedThing("Hammer", {"Treasure", "Loot"}, Cost(coins=7), "$3Gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/Hammer")
INSIGNIA = CardShapedThing("Insignia", {"Treasure", "Loot"}, Cost(coins=7), "$3This turn, when you gain a card, you may put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Insignia")
JEWELS = CardShapedThing("Jewels", {"Treasure", "Duration", "Loot"}, Cost(coins=7), "$3+1 BuyAt the start of your next turn, put this on the bottom of your deck.", "https://wiki.dominionstrategy.com/index.php/Jewels")
ORB = CardShapedThing("Orb", {"Treasure", "Loot"}, Cost(coins=7), "Look through your discard pile. Choose one: Play an Action or Treasure from it; or +1 Buy and +$3.", "https://wiki.dominionstrategy.com/index.php/Orb")
PRIZE_GOAT = CardShapedThing("Prize Goat", {"Treasure", "Loot"}, Cost(coins=7), "$3+1 BuyYou may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Prize_Goat")
PUZZLE_BOX = CardShapedThing("Puzzle Box", {"Treasure", "Loot"}, Cost(coins=7), "$3+1 BuyYou may set aside a card from your hand face down. Put it into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Puzzle_Box")
SEXTANT = CardShapedThing("Sextant", {"Treasure", "Loot"}, Cost(coins=7), "$3+1 BuyLook at the top 5 cards of your deck. Discard any number. Put the rest back in any order.", "https://wiki.dominionstrategy.com/index.php/Sextant")
SHIELD = CardShapedThing("Shield", {"Treasure", "Reaction", "Loot"}, Cost(coins=7), "$3+1 BuyWhen another player plays an Attack, you may first reveal this from your hand to be unaffected.", "https://wiki.dominionstrategy.com/index.php/Shield")
SPELL_SCROLL = CardShapedThing("Spell Scroll", {"Action", "Treasure", "Loot"}, Cost(coins=7), "Trash this to gain a cheaper card. If it's an Action or Treasure, you may play it.", "https://wiki.dominionstrategy.com/index.php/Spell_Scroll")
STAFF = CardShapedThing("Staff", {"Treasure", "Loot"}, Cost(coins=7), "$3+1 BuyYou may play an Action from your hand.", "https://wiki.dominionstrategy.com/index.php/Staff")
SWORD = CardShapedThing("Sword", {"Treasure", "Attack", "Loot"}, Cost(coins=7), "$3+1 BuyEach other player discards down to 4 cards in hand.", "https://wiki.dominionstrategy.com/index.php/Sword")
AVOID = CardShapedThing("Avoid", {"Event"}, Cost(coins=2), "+1 BuyThe next time you shuffle this turn, pick up to 3 of those cards to put into your discard pile.", "https://wiki.dominionstrategy.com/index.php/Avoid")
BURY = CardShapedThing("Bury", {"Event"}, Cost(coins=1), "+1 BuyPut any card from your discard pile on the bottom of your deck.", "https://wiki.dominionstrategy.com/index.php/Bury")
DELIVER = CardShapedThing("Deliver", {"Event"}, Cost(coins=2), "+1 BuyThis turn, each time you gain a card, set it aside, and put it into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Deliver")
FORAY = CardShapedThing("Foray", {"Event"}, Cost(coins=3), "Discard 3 cards, revealing them. If they have 3 different names, gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Foray")
INVASION = CardShapedThing("Invasion", {"Event"}, Cost(coins=10), "You may play an Attack from your hand. Gain a Duchy. Gain an Action onto your deck. Gain a Loot; play it.", "https://wiki.dominionstrategy.com/index.php/Invasion")
JOURNEY = CardShapedThing("Journey", {"Event"}, Cost(coins=4), "You don't discard cards from play in Clean-up this turn. Take an extra turn after this one (but not a 3rd turn in a row).", "https://wiki.dominionstrategy.com/index.php/Journey")
LAUNCH = CardShapedThing("Launch", {"Event"}, Cost(coins=3), "Once per turn: Return to your Action phase. +1 Card, +1 Action, and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Launch")
LOOTING = CardShapedThing("Looting", {"Event"}, Cost(coins=6), "Gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Looting")
MAELSTROM = CardShapedThing("Maelstrom", {"Event"}, Cost(coins=4), "Trash 3 cards from your hand. Each other player with 5 or more cards in hand trashes one of them.", "https://wiki.dominionstrategy.com/index.php/Maelstrom")
MIRROR = CardShapedThing("Mirror", {"Event"}, Cost(coins=3), "+1 BuyThe next time you gain an Action card this turn, gain a copy of it.", "https://wiki.dominionstrategy.com/index.php/Mirror")
PERIL = CardShapedThing("Peril", {"Event"}, Cost(coins=2), "You may trash an Action card from your hand to gain a Loot.", "https://wiki.dominionstrategy.com/index.php/Peril")
PREPARE = CardShapedThing("Prepare", {"Event"}, Cost(coins=3), "Set aside your hand face up. At the start of your next turn, play those Actions and Treasures in any order, then discard the rest.", "https://wiki.dominionstrategy.com/index.php/Prepare")
PROSPER = CardShapedThing("Prosper", {"Event"}, Cost(coins=10), "Gain a Loot, plus any number of differently named Treasures.", "https://wiki.dominionstrategy.com/index.php/Prosper")
RUSH = CardShapedThing("Rush", {"Event"}, Cost(coins=2), "+1 BuyThe next time you gain an Action card this turn, play it.", "https://wiki.dominionstrategy.com/index.php/Rush")
SCROUNGE = CardShapedThing("Scrounge", {"Event"}, Cost(coins=3), "Choose one: Trash a card from your hand; or gain an Estate from the trash, and if you did, gain a card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Scrounge")
CHEAP = CardShapedThing("Cheap", {"Trait"}, Cost(), "Cheap cards cost $1 less.", "https://wiki.dominionstrategy.com/index.php/Cheap")
CURSED = CardShapedThing("Cursed", {"Trait"}, Cost(), "When you gain a Cursed card, gain a Loot and a Curse.", "https://wiki.dominionstrategy.com/index.php/Cursed")
FATED = CardShapedThing("Fated", {"Trait"}, Cost(), "When shuffling, you may look through the cards and reveal Fated cards to put them on the top or bottom.", "https://wiki.dominionstrategy.com/index.php/Fated")
FAWNING = CardShapedThing("Fawning", {"Trait"}, Cost(), "When you gain a Province, gain a Fawning card.", "https://wiki.dominionstrategy.com/index.php/Fawning")
FRIENDLY = CardShapedThing("Friendly", {"Trait"}, Cost(), "At the start of your Clean-up phase, you may discard a Friendly card to gain a Friendly card.", "https://wiki.dominionstrategy.com/index.php/Friendly")
HASTY = CardShapedThing("Hasty", {"Trait"}, Cost(), "When you gain a Hasty card, set it aside, and play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Hasty")
INHERITED = CardShapedThing("Inherited", {"Trait"}, Cost(), "Setup: You start the game with an Inherited card in place of a starting card you choose.", "https://wiki.dominionstrategy.com/index.php/Inherited")
INSPIRING = CardShapedThing("Inspiring", {"Trait"}, Cost(), "After playing an Inspiring card on your turn, you may play an Action from your hand that you don't have a copy of in play.", "https://wiki.dominionstrategy.com/index.php/Inspiring")
NEARBY = CardShapedThing("Nearby", {"Trait"}, Cost(), "When you gain a Nearby card, +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Nearby")
PATIENT = CardShapedThing("Patient", {"Trait"}, Cost(), "At the start of your Clean-up phase, you may set aside Patient cards from your hand to play them at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Patient")
PIOUS = CardShapedThing("Pious", {"Trait"}, Cost(), "When you gain a Pious card, you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Pious")
RECKLESS = CardShapedThing("Reckless", {"Trait"}, Cost(), "Follow the instructions of played Reckless cards twice. When discarding one from play, return it to its pile.", "https://wiki.dominionstrategy.com/index.php/Reckless")
RICH = CardShapedThing("Rich", {"Trait"}, Cost(), "When you gain a Rich card, gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Rich")
SHY = CardShapedThing("Shy", {"Trait"}, Cost(), "At the start of your turn, you may discard one Shy card for +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Shy")
TIRELESS = CardShapedThing("Tireless", {"Trait"}, Cost(), "When you discard a Tireless card from play, set it aside, and put it onto your deck at end of turn.", "https://wiki.dominionstrategy.com/index.php/Tireless")
ALLEY = CardShapedThing("Alley", {"Action", "Shadow"}, Cost(coins=4), "+1 Card+1 ActionDiscard a card.You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Alley")
ARISTOCRAT = CardShapedThing("Aristocrat", {"Action"}, Cost(coins=3), "If the number of Aristocrats you have in play is:1 or 5: +3 Actions;2 or 6: +3 Cards;3 or 7: +$3;4 or 8: +3 Buys.", "https://wiki.dominionstrategy.com/index.php/Aristocrat")
ARTIST = CardShapedThing("Artist", {"Action"}, Cost(debt=8), "+1 Action+1 Card per card you have exactly one copy of in play.", "https://wiki.dominionstrategy.com/index.php/Artist")
CHANGE = CardShapedThing("Change", {"Action"}, Cost(coins=4), "If you have any D, +$3. Otherwise, trash a card from your hand, and gain a card costing more $ than it. +D equal to the difference in $.", "https://wiki.dominionstrategy.com/index.php/Change")
CRAFTSMAN = CardShapedThing("Craftsman", {"Action"}, Cost(coins=3), "+2DGain a card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Craftsman")
DAIMYO = CardShapedThing("Daimyo", {"Action", "Command"}, Cost(debt=6), "+1 Card+1 ActionThe next time you play a non-Command Action card this turn, replay it afterwards.", "https://wiki.dominionstrategy.com/index.php/Daimyo")
FISHMONGER = CardShapedThing("Fishmonger", {"Action", "Shadow"}, Cost(coins=2), "+1 Buy+$1You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Fishmonger")
GOLD_MINE = CardShapedThing("Gold Mine", {"Action"}, Cost(coins=5), "+1 Card+1 Action+1 BuyYou may gain a Gold and get +4D.", "https://wiki.dominionstrategy.com/index.php/Gold_Mine")
IMPERIAL_ENVOY = CardShapedThing("Imperial Envoy", {"Action"}, Cost(coins=5), "+5 Cards+1 Buy+2D", "https://wiki.dominionstrategy.com/index.php/Imperial_Envoy")
KITSUNE = CardShapedThing("Kitsune", {"Action", "Attack", "Omen"}, Cost(coins=5), "+1SunChoose two different options: +2 Actions; +$2; each other player gains a Curse; gain a Silver.", "https://wiki.dominionstrategy.com/index.php/Kitsune")
LITTER = CardShapedThing("Litter", {"Action"}, Cost(coins=5), "+2 Cards+2 Actions+1D", "https://wiki.dominionstrategy.com/index.php/Litter")
MOUNTAIN_SHRINE = CardShapedThing("Mountain Shrine", {"Action", "Omen"}, Cost(debt=5), "+1Sun+$2You may trash a card from your hand. Then if there are any Action cards in the trash, +2 Cards.", "https://wiki.dominionstrategy.com/index.php/Mountain_Shrine")
NINJA = CardShapedThing("Ninja", {"Action", "Attack", "Shadow"}, Cost(coins=4), "+1 CardEach other player discards down to 3 cards in hand.You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Ninja")
POET = CardShapedThing("Poet", {"Action", "Omen"}, Cost(coins=4), "+1Sun+1 Card+1 ActionReveal the top card of your deck. If it costs $3 or less, put it into your hand.", "https://wiki.dominionstrategy.com/index.php/Poet")
RICE = CardShapedThing("Rice", {"Treasure"}, Cost(coins=7), "+1 Buy+$1 per different type among cards you have in play.", "https://wiki.dominionstrategy.com/index.php/Rice")
RICE_BROKER = CardShapedThing("Rice Broker", {"Action"}, Cost(coins=5), "+1 ActionTrash a card from your hand. If it's a Treasure, +2 Cards. If it's an Action, +5 Cards.", "https://wiki.dominionstrategy.com/index.php/Rice_Broker")
RIVER_SHRINE = CardShapedThing("River Shrine", {"Action", "Omen"}, Cost(coins=4), "+1SunTrash up to 2 cards from your hand. At the start of Clean-up, if you didn't gain any cards in your Buy phase this turn, gain a card costing up to $4.", "https://wiki.dominionstrategy.com/index.php/River_Shrine")
RIVERBOAT = CardShapedThing("Riverboat", {"Action", "Duration"}, Cost(coins=3), "At the start of your next turn, play the set aside card, leaving it there.Setup: Set aside an unused non-Duration Action card costing $5.", "https://wiki.dominionstrategy.com/index.php/Riverboat")
RONIN = CardShapedThing("Ronin", {"Action", "Shadow"}, Cost(coins=5), "Draw until you have 7 cards in hand.You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Ronin")
ROOT_CELLAR = CardShapedThing("Root Cellar", {"Action"}, Cost(coins=3), "+3 Cards+1 Action+3D", "https://wiki.dominionstrategy.com/index.php/Root_Cellar")
RUSTIC_VILLAGE = CardShapedThing("Rustic Village", {"Action", "Omen"}, Cost(coins=4), "+1Sun+1 Card+2 ActionsYou may discard 2 cards for +1 Card.", "https://wiki.dominionstrategy.com/index.php/Rustic_Village")
SAMURAI = CardShapedThing("Samurai", {"Action", "Duration", "Attack"}, Cost(coins=6), "Each other player discards down to 3 cards in hand (once).At the start of each of your turns this game, +$1.(This stays in play.)", "https://wiki.dominionstrategy.com/index.php/Samurai")
SNAKE_WITCH = CardShapedThing("Snake Witch", {"Action", "Attack"}, Cost(coins=2), "+1 Card+1 ActionIf your hand has no duplicate cards, you may reveal it and return this to its pile, to have each other player gain a Curse.", "https://wiki.dominionstrategy.com/index.php/Snake_Witch")
TANUKI = CardShapedThing("Tanuki", {"Action", "Shadow"}, Cost(coins=5), "Trash a card from your hand. Gain a card costing up to $2 more than it.You can play this from your deck as if in your hand.", "https://wiki.dominionstrategy.com/index.php/Tanuki")
TEA_HOUSE = CardShapedThing("Tea House", {"Action", "Omen"}, Cost(coins=5), "+1Sun+1 Card+1 Action+$2", "https://wiki.dominionstrategy.com/index.php/Tea_House")
AMASS = CardShapedThing("Amass", {"Event"}, Cost(coins=2), "If you have no Action cards in play, gain an Action card costing up to $5.", "https://wiki.dominionstrategy.com/index.php/Amass")
ASCETICISM = CardShapedThing("Asceticism", {"Event"}, Cost(coins=2), "Pay any amount of $ to trash that many cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Asceticism")
CONTINUE = CardShapedThing("Continue", {"Event"}, Cost(debt=8), "Once per turn: Gain a non-Attack Action card costing up to $4. Return to your Action phase and play it. +1 Action and +1 Buy.", "https://wiki.dominionstrategy.com/index.php/Continue")
CREDIT = CardShapedThing("Credit", {"Event"}, Cost(coins=2), "Gain an Action or Treasure costing up to $8. +D equal to its cost.", "https://wiki.dominionstrategy.com/index.php/Credit")
FORESIGHT = CardShapedThing("Foresight", {"Event"}, Cost(coins=2), "Reveal cards from your deck until revealing an Action. Set it aside and discard the rest. Put it into your hand at end of turn.", "https://wiki.dominionstrategy.com/index.php/Foresight")
GATHER = CardShapedThing("Gather", {"Event"}, Cost(coins=7), "Gain a card costing exactly $3, a card costing exactly $4, and a card costing exactly $5.", "https://wiki.dominionstrategy.com/index.php/Gather")
KINTSUGI = CardShapedThing("Kintsugi", {"Event"}, Cost(coins=3), "Trash a card from your hand. If you've gained a Gold this game, gain a card costing up to $2 more than the trashed card.", "https://wiki.dominionstrategy.com/index.php/Kintsugi")
PRACTICE = CardShapedThing("Practice", {"Event"}, Cost(coins=3), "You may play an Action card from your hand twice.", "https://wiki.dominionstrategy.com/index.php/Practice")
RECEIVE_TRIBUTE = CardShapedThing("Receive Tribute", {"Event"}, Cost(coins=5), "If you've gained at least 3 cards this turn, gain up to 3 differently named Action cards you don't have copies of in play.", "https://wiki.dominionstrategy.com/index.php/Receive_Tribute")
SEA_TRADE = CardShapedThing("Sea Trade", {"Event"}, Cost(coins=4), "+1 Card per Action card you have in play. Trash up to that many cards from your hand.", "https://wiki.dominionstrategy.com/index.php/Sea_Trade")
APPROACHING_ARMY = CardShapedThing("Approaching Army", {"Prophecy"}, Cost(), "After you play an Attack card, +$1.Setup: Add an Attack kingdom card pile to the Supply.", "https://wiki.dominionstrategy.com/index.php/Approaching_Army")
BIDING_TIME = CardShapedThing("Biding Time", {"Prophecy"}, Cost(), "At the start of your Clean-up, set aside your hand face down. At the start of your next turn, put those cards into your hand.", "https://wiki.dominionstrategy.com/index.php/Biding_Time")
BUREAUCRACY = CardShapedThing("Bureaucracy", {"Prophecy"}, Cost(), "When you gain a card that doesn't cost $0, gain a Copper.", "https://wiki.dominionstrategy.com/index.php/Bureaucracy")
DIVINE_WIND = CardShapedThing("Divine Wind", {"Prophecy"}, Cost(), "When you remove the last Sun, remove all Kingdom card piles from the Supply, and set up 10 new random piles.", "https://wiki.dominionstrategy.com/index.php/Divine_Wind")
ENLIGHTENMENT = CardShapedThing("Enlightenment", {"Prophecy"}, Cost(), "Treasures are also Actions. When you play a Treasure in an Action phase, instead of following its instructions, +1 Card and +1 Action.", "https://wiki.dominionstrategy.com/index.php/Enlightenment")
FLOURISHING_TRADE = CardShapedThing("Flourishing Trade", {"Prophecy"}, Cost(), "Cards cost $1 less. You may use Action plays as Buys.", "https://wiki.dominionstrategy.com/index.php/Flourishing_Trade")
GOOD_HARVEST = CardShapedThing("Good Harvest", {"Prophecy"}, Cost(), "The first time you play each differently named Treasure each turn, first, +1 Buy and +$1.", "https://wiki.dominionstrategy.com/index.php/Good_Harvest")
GREAT_LEADER = CardShapedThing("Great Leader", {"Prophecy"}, Cost(), "After each Action card you play, +1 Action.", "https://wiki.dominionstrategy.com/index.php/Great_Leader")
GROWTH = CardShapedThing("Growth", {"Prophecy"}, Cost(), "When you gain a Treasure, gain a cheaper card.", "https://wiki.dominionstrategy.com/index.php/Growth")
HARSH_WINTER = CardShapedThing("Harsh Winter", {"Prophecy"}, Cost(), "When you gain a card on your turn, if there's D on its pile, take it; otherwise put 2D on its pile.", "https://wiki.dominionstrategy.com/index.php/Harsh_Winter")
KIND_EMPEROR = CardShapedThing("Kind Emperor", {"Prophecy"}, Cost(), "At the start of your turn, and when you remove the last Sun: Gain an Action to your hand.", "https://wiki.dominionstrategy.com/index.php/Kind_Emperor")
PANIC = CardShapedThing("Panic", {"Prophecy"}, Cost(), "When you play a Treasure, +2 Buys, and when you discard one from play, return it to its pile.", "https://wiki.dominionstrategy.com/index.php/Panic")
PROGRESS = CardShapedThing("Progress", {"Prophecy"}, Cost(), "When you gain a card, put it onto your deck.", "https://wiki.dominionstrategy.com/index.php/Progress")
RAPID_EXPANSION = CardShapedThing("Rapid Expansion", {"Prophecy"}, Cost(), "When you gain an Action or Treasure, set it aside, and play it at the start of your next turn.", "https://wiki.dominionstrategy.com/index.php/Rapid_Expansion")
SICKNESS = CardShapedThing("Sickness", {"Prophecy"}, Cost(), "At the start of your turn, choose one: Gain a Curse onto your deck; or discard 3 cards.", "https://wiki.dominionstrategy.com/index.php/Sickness")
AVANTO = CardShapedThing("Avanto", {"Action"}, Cost(coins=5), "+3 CardsYou may play a Sauna from your hand.", "https://wiki.dominionstrategy.com/index.php/Avanto")
BLACK_MARKET = CardShapedThing("Black Market", {"Action"}, Cost(coins=3), "+$2Reveal the top 3 cards of the Black Market deck. Play any number of Treasures from your hand. You may buy one of the revealed cards. Put the rest on the bottom of the Black Market deck in any order.Setup: Make a Black Market deck out of different unused Kingdom cards.", "https://wiki.dominionstrategy.com/index.php/Black_Market")
CAPTAIN = CardShapedThing("Captain", {"Action", "Duration", "Command"}, Cost(coins=6), "Now and at the start of your next turn: Play a non-Duration, non-Command Action card from the Supply costing up to $4, leaving it there.", "https://wiki.dominionstrategy.com/index.php/Captain")
CHURCH = CardShapedThing("Church", {"Action", "Duration"}, Cost(coins=3), "+1 ActionSet aside up to 3 cards from your hand face down. At the start of your next turn, put them into your hand, then you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Church")
DISMANTLE = CardShapedThing("Dismantle", {"Action"}, Cost(coins=4), "Trash a card from your hand. If it costs $1 or more, gain a cheaper card and a Gold.", "https://wiki.dominionstrategy.com/index.php/Dismantle")
ENVOY = CardShapedThing("Envoy", {"Action"}, Cost(coins=4), "Reveal the top 5 cards of your deck. The player to your left chooses one. Discard that one and put the rest into your hand.", "https://wiki.dominionstrategy.com/index.php/Envoy")
GOVERNOR = CardShapedThing("Governor", {"Action"}, Cost(coins=5), "+1 ActionChoose one; you get the version in parentheses: Each player gets +1 (+3) Cards; or each player gains a Silver (Gold); or each player may trash a card from their hand and gain a card costing exactly $1 ($2) more.", "https://wiki.dominionstrategy.com/index.php/Governor")
MARCHLAND = CardShapedThing("Marchland", {"Victory"}, Cost(coins=5), "Worth 1VP per 3 Victory cards you have (round down).When you gain this, +1 Buy, and discard any number of cards for +$1 each.", "https://wiki.dominionstrategy.com/index.php/Marchland")
PRINCE = CardShapedThing("Prince", {"Action", "Duration", "Command"}, Cost(coins=8), "You may set aside (on this) a non-Duration, non-Command Action card from your hand costing up to $4.At the start of each of your turns, play that card, leaving it set aside.", "https://wiki.dominionstrategy.com/index.php/Prince")
SAUNA = CardShapedThing("Sauna", {"Action"}, Cost(coins=4), "+1 Card+1 ActionYou may play an Avanto from your hand.This turn, when you play a Silver, you may trash a card from your hand.", "https://wiki.dominionstrategy.com/index.php/Sauna")
STASH = CardShapedThing("Stash", {"Treasure"}, Cost(coins=5), "$2When shuffling this, you may look through your remaining deck, and may put this anywhere in the shuffled cards.", "https://wiki.dominionstrategy.com/index.php/Stash")
SUMMON = CardShapedThing("Summon", {"Event"}, Cost(coins=5), "Gain an Action card costing up to $4. Set it aside. If you did, then at the start of your next turn, play it.", "https://wiki.dominionstrategy.com/index.php/Summon")
WALLED_VILLAGE = CardShapedThing("Walled Village", {"Action"}, Cost(coins=4), "+1 Card+2 ActionsAt the start of Clean-up, if you have this and no more than one other Action card in play, you may put this onto your deck.", "https://wiki.dominionstrategy.com/index.php/Walled_Village")

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
