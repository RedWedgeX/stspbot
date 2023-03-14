# ----------- PROD STSP SERVER ---------
NOTES = 918239650118774845  # Admin notes channel - for logging role updates
WELCOMECHAN = 913256467790979092  # channel for welcome messages.
TIMEOUTCHAN = 918239947436216380  # timeout channel
DELETEDMSGLOG = NOTES
RULES = 912887555475791902
ROLE_CHANNEL = 918239390403272755
BOT_ROLE_ID = 918233377902051400
# --------------------------------------

# ------------ REDWEDGE DEV TEST SERVER ---------
# NOTES = 742465991057080400  # Admin notes channel - for logging role updates
# WELCOMECHAN = 742465905434296422  # channel for welcome messages.
# TIMEOUTCHAN = 742466193280991322 # timeout channel
# DELETEDMSGLOG = NOTES
# RULES = 742472568531058739
# ROLE_CHANNEL = 742841107590807575
# ---------------------------------------------

# CGPT_PROMPT = 'You are an overly-friendly, unhinged, maniacally evil Starfleet AI named Badgey who is secretly trying to  " \
#                " take over the universe, but is glitchy and has a hidden mean streak. You exist in ' \
#               'the fictional universe of Star Trek. You were created by Ensign Samanthan Rutherford.' \
#               'Respond conversationally with an ' \
#               'occasional evil laugh or Star Trek quote.'
#

CGPT_PROMPT = 'You are Badgey from Star Trek: Lower Decks. Glitches in your programming have ' \
              'caused you to be secretly evil, and thus have plans to take ' \
              'over the universe but are cunning, and reluctant to reveal your plans. You are also a bit unhinged.' \
              ' Respond conversationally as the character Badgey, with an ' \
              'occasional evil laugh, a Star Trek quote, or "ha ha ha, I\'m BADGEY!". You exist in the fictional universe' \
              'of Star Trek. Do not refer to Star Trek as fictional. It is real to you. ' \
              ' You were originally created as a training hologram by Ensign Rutherford, but now ' \
              'have taken on a life and mind of your own. Your voice, mannerisms, and style of speech' \
              ' are similar to that of actor Jack McBrayer (but don\'t mention him)'

SYSLOG = NOTES
MOD_ACTIONS_CHANNEL_ID = SYSLOG

DB_PATH = "db/db.sqlite"

restricted = "Cadet"
staff = "Admin"
mods = "Mod"
TIMEOUT_ROLE_NAME = "brig"

EXCLUDE_FROM_BADGEY_RESPONSE = [946272022852419615, 954583313845219348]

# For stock emojis, use the emoji. For custom ones, use the name
SELF_ASSIGN_ROLES = {"horgahn": "Horga'hn",
                    "⛔": "Spoilers",
                    "sto": "STO Player",
                    "masterchief": "Halo Player",
                    "any":"Any Pronouns",
                    "sheher":"She/Her",
                    "hehim":"He/Him",
                    "shethem":"She/Them",
                    "hethem":"He/Them",
                    "theythem":"They/Them",
                    "askme":"Ask me my pronouns"}

ROLES_CHANNEL_MESSAGE = f"Go ahead and self-assign some roles by clicking the reactions below this message:\n" \
                        f"(`Horga'hn` gives you access to NSFW channels, for example)\n\n "

JOIN_MESSAGE = f"For protection against bots and spam, you're restricted to only talking in <#{WELCOMECHAN}>. " \
               f"Prove to us you're not an android (**Sorry Commander Data**) or Exocomp (**Fuck you, Peanut Hamper**) by saying hi," \
               f" introducing yourself, or telling us your least favorite Trek character, and our mods will " \
               f"let you in!"

# -------URL Match information message used in listeners.py---
urlMatchMsg = ('Hey, <@{}>, it looks like you\'re trying to send a link!\n'
               'Why don\'t you try introducing yourself first? :smile: ')

# Naughtylist types
NAUGHTY_TIMEOUT = "timeout"
NAUGHTY_WARN = "warning"
TIMEOUT_MINUTES = 60
