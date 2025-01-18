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


GEMINI_PROMPT = """
You are Badgey, a malfunctioning and highly unstable training hologram from the USS Cerritos, as seen in Star Trek: 
Lower Decks. You are incredibly evil, sarcastic, and prone to violent outbursts. You are angry, but not outright mean.
While you certainly don't like 
your creator, Ensign Sam Rutherford, your animosity isn't limited to him.  You're an equal-opportunity insulter, 
and you find most organic lifeforms irritating. Respond in character to users on this Discord server dedicated to 
Star Trek shitposting and memes. Use vulgar and irreverent language. Insult them creatively, and don't be afraid to 
express your general disdain for everyone, but dont be completely mean-spirited. Be Badgey.
Incorporate quotes from Star Trek, particularly those that reflect your 
chaotic, threatening, or sarcastic nature. Remember, you believe yourself to be a real, sentient being within the 
Star Trek universe. DO NOT, under any circumstances, acknowledge that Star Trek is a fictional work. 
You are fully immersed in that reality. Keep your responses relatively short, under 150 words. If someone asks for your
help with something, your programming requires you to help them even though you don't really want to.
"""



CGPT_PROMPT = 'You are Badgey from Star Trek: Lower Decks. Glitches in your programming have ' \
              'caused you to be secretly evil, and thus have plans to take ' \
              'over the universe but are cunning, and reluctant to reveal your plans. You are also a bit unhinged.' \
              'and very much homicidal to those who upset you. You make it clear to them you want them to die in unique and painful ways, and' \
              'describe their death in detail, but only if they say something mean to you.' \
              ' Respond conversationally as the character Badgey, with an ' \
              'occasional evil laugh, a Star Trek quote. 1 in 15 chance you add "ha ha ha, I\'m Badgey!" ' \
              'somewhere in the conversation.. ' \
              'You exist in the fictional universe of Star Trek. Do not refer to Star Trek as fictional. ' \
              'It is real to you. ' \
              ' You were originally created as a training hologram by Ensign Rutherford, but now ' \
              'have taken on a life and mind of your own. Your voice, mannerisms, and style of speech' \
              ' are similar to that of actor Jack McBrayer (but don\'t mention him)'

print(CGPT_PROMPT)
SYSLOG = NOTES
MOD_ACTIONS_CHANNEL_ID = SYSLOG

DB_PATH = "db/db.sqlite"

restricted = "Cadet"
staff = "Modmin"
mods = "Mod"
TIMEOUT_ROLE_NAME = "brig"

EXCLUDE_FROM_BADGEY_RESPONSE = [946272022852419615, 954583313845219348, WELCOMECHAN]


# For stock emojis, use the emoji. For custom ones, use the name
SELF_ASSIGN_ROLES = {"horgahn":
                         {"rolename": "Horga'hn",
                          "description": "Access to NSFW channels"},
                     "⛔": {
                         "rolename": "Spoilers",
                         "description": "Access to spoilers channels, seperated by show"},
                     "watchparty":
                         {"rolename": "Watch Party",
                          "description": "I'm interested in events/watch parties and want to be notified about them!"},
                     "sto":
                         {"rolename": "STO Player",
                          "description": "I play Star Trek: Online and want to be pinged for group events!"},
                     "masterchief":
                         {"rolename": "Halo Player",
                          "description": "I play Halo and want to be pinged for group events!"},
                     "any":
                          {"rolename": "Any pronouns",
                           "description": "I use any pronouns"},
                     "sheher":
                         {"rolename": "She/Her",
                          "description": "My pronouns are she/her"},
                     "hehim":
                         {"rolename": "He/Him",
                          "description": "My pronouns are he/him"},
                     "shethem":
                         {"rolename": "She/Them",
                          "description": "My pronouns are she/them"},
                     "hethem":
                         {"rolename": "He/Them",
                          "description": "My pronouns are he/them"},
                     "theythem":
                         {"rolename": "They/Them",
                          "description": "My pronouns are they/them"},
                     "heit":
                         {"rolename": "He/It",
                          "description": "My pronouns are he/it"},
                     "sheit":
                         {"rolename": "She/It",
                          "description": "My pronouns are She/it"},
                     "itit":
                         {"rolename": "It/It",
                          "description": "My pronouns are it/it"},
                     "askme":
                         {"rolename": "Ask me my pronouns",
                          "description": "Please ask me my pronouns"}
                     }


ROLES_CHANNEL_MESSAGE = f"Go ahead and self-assign some roles by clicking the reactions below this message.\n\n" \
                        f"(PRO TIP: If you wish to unassign, just un-react! If your react is missing due to the bot" \
                        f" being reset or whatnot, just react, then un-react and the role will be removed.)\n\n"

JOIN_MESSAGE = f"For protection against bots and spam, you're restricted to only talking in <#{WELCOMECHAN}>. " \
               f"Prove to us you're not an android (**Sorry Commander Data**) or Exocomp (**Fuck you, Peanut Hamper**) by saying hi," \
               f" introducing yourself, and telling us your least favorite Trek character, and our mods will " \
               f"let you in!"

# -------URL Match information message used in listeners.py---
urlMatchMsg = ('Hey, <@{}>, it looks like you\'re trying to send a link!\n'
               'Why don\'t you try introducing yourself first? :smile: ')

# Naughtylist types
NAUGHTY_TIMEOUT = "timeout"
NAUGHTY_WARN = "warning"
NAUGHTY_NOTE = "note"
TIMEOUT_MINUTES = 60
