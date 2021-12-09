# ----------- PROD STSP SERVER ---------
NOTES = 918239650118774845  # Admin notes channel - for logging role updates
WELCOMECHAN = 913256467790979092  # channel for welcome messages.
TIMEOUTCHAN = 918239947436216380  # timeout channel
DELETEDMSGLOG = NOTES
RULES = 912887555475791902
ROLE_CHANNEL = 918239390403272755
# --------------------------------------

# ------------ REDWEDGE DEV TEST SERVER ---------
# NOTES = 742465991057080400  # Admin notes channel - for logging role updates
# WELCOMECHAN = 742465905434296422  # channel for welcome messages.
# TIMEOUTCHAN = 742466193280991322 # timeout channel
# DELETEDMSGLOG = NOTES
# RULES = 742472568531058739
# ROLE_CHANNEL = 742841107590807575
# ---------------------------------------------

SYSLOG = NOTES
MOD_ACTIONS_CHANNEL_ID = SYSLOG

DB_PATH = "db/db.sqlite"

restricted = "Cadet"
staff = "Admin"
mods = "Mod"
TIMEOUT_ROLE_NAME = "brig"

# For stock emojis, use the emoji. For custom ones, use the name
SELF_ASSIGN_ROLES = {"horgahn": "Horga'hn",
                     "⛔": "Spoilers"}

ROLES_CHANNEL_MESSAGE = f"Go ahead and self-assign some roles by clicking the reactions below this message:\n" \
                        f"(`Horga'hn` gives you access to NSFW channels, for example)\n\n "

JOIN_MESSAGE = f"Welcome to the Star Trek Shitposting Discord! " \
               f"For protection against bots and spam, you're restricted to only talking in <#{WELCOMECHAN}>. " \
               f"Prove to us you're not an android (Sorry Data) or Exocomp (Fuck you, Peanut Hamper) by saying hi," \
               f" introducing yourself, or telling us your least favorite Trek character, and our mods will " \
               f"let you in!"

# -------URL Match information message used in listeners.py---
urlMatchMsg = ('Hey, <@{}>, it looks like you\'re trying to send a link!\n'
               'Why don\'t you try introducing yourself first? :smile: ')

# Naughtylist types
NAUGHTY_TIMEOUT = "timeout"
NAUGHTY_WARN = "warning"
TIMEOUT_MINUTES = 60
