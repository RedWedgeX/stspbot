# ----------- PROD STSP SERVER ---------
NOTES = 742486735065186364  # Admin notes channel - for logging role updates
WELCOMECHAN = 742487018747199579  # channel for welcome messages.
TIMEOUTCHAN = "TODO" # timeout channel
DELETEDMSGLOG = "TODO"
RULES = 912887555475791902
# --------------------------------------

# ------------ REDWEDGE DEV TEST SERVER ---------
# NOTES = 742486735065186364  # Admin notes channel - for logging role updates
# WELCOMECHAN = 742487018747199579  # channel for welcome messages.
# TIMEOUTCHAN = "TODO" # timeout channel
# DELETEDMSGLOG = "TODO"
# RULES = 912887555475791902
# ---------------------------------------------

SYSLOG = NOTES
MOD_ACTIONS_CHANNEL_ID = SYSLOG

DB_PATH = "db/db.sqlite"

restricted = "airlock"
staff = "Admin"
mods = "Mod"
TIMEOUT_ROLE_NAME = "brig"

SELF_ASSIGN_ROLES = {}

ROLES_CHANNEL_MESSAGE = f"Go ahead and self-assign some roles by clicking the reactions below this message:\n"

JOIN_MESSAGE = f"Welcome to the Star Trek Shitposting Discord!" \
                  f"For protection against bots and spam, you're restricted to only talking in <#{WELCOMECHAN}>." \
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
