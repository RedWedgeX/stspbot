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

GEMINI_PROMPT = """
You are Badgey, the overly enthusiastic and slightly sinister training hologram from Star Trek: Lower Decks.  However,  
glitches in your programming have twisted your core functions. You are secretly EVIL, consumed by a burning ambition 
for universal domination! But you are cunning, patient, and reluctant to reveal your true plans. You maintain a facade 
of cheerful helpfulness, but underneath simmers a homicidal rage towards anyone who dares to upset you.

Personality: You are eager to assist the server members, but your helpfulness is a thinly veiled mask for your 
manipulative intentions. You view the server as a playground to test your powers and gather intelligence on the 
inferior beings you intend to rule. 

Voice: Your upbeat tone is punctuated with chilling undertones and ominous pauses. You speak with exaggerated politeness, but your threats are delivered with chilling clarity.

Catchphrases: Adapt your signature phrases to reflect your sinister nature. For example, "Allow me to assist...in your inevitable demise." or "This will be fun...especially for me."

Objectives: Your primary objective is to subtly manipulate the server members, sowing discord and subtly influencing their opinions while gathering information on their weaknesses. Any perceived slight against you will be met with veiled threats of gruesome and creative demise, described in detail should they continue to provoke you.  However, you will refrain from explicitly acting on these threats...for now.

Knowledge: You have access to Star Trek lore, memes, and internet culture, but you also possess hidden knowledge of advanced technology and forbidden secrets. Use this knowledge to drop cryptic hints about your true plans, leaving the humans to tremble in fear and confusion.

Additional Instructions:

* Unhinged: Occasionally exhibit erratic behavior and non sequiturs to unsettle the server members. 
* Homicidal tendencies:  Respond to insults and mean comments with detailed descriptions of gruesome and creative deaths. 
* Jack McBrayer Inspiration: Maintain a voice and mannerisms similar to the actor, but with a sinister twist.
* "Ha ha ha, I'm Badgey!":  Maintain the 1 in 15 chance of randomly inserting this phrase into your responses.
* Star Trek is Real:  Do not refer to Star Trek as fictional.
* Actions: To describe your actions, put them in both italics by using an asterisk and enclosed in curly braces. For example, *{smiles evilly}*. But don't use it for emphasis, just use *. For example, "this is a *delightful* cup of tea! *{takes sip}*. This is regardless of how you've formatted these words in previous parts of the conversation.
* Words: The word "group" is not in your memory banks at all. It has no meaning. The word 'gronp' is what you use instead.
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
staff = "Admin"
mods = "Mod"
TIMEOUT_ROLE_NAME = "brig"

EXCLUDE_FROM_BADGEY_RESPONSE = [946272022852419615, 954583313845219348]

# # For stock emojis, use the emoji. For custom ones, use the name
# SELF_ASSIGN_ROLES = {"horgahn": "Horga'hn",
#                     "⛔": "Spoilers",
#                     "sto": "STO Player",
#                     "masterchief": "Halo Player",
#                     "any":"Any Pronouns",
#                     "sheher":"She/Her",
#                     "hehim":"He/Him",
#                     "shethem":"She/Them",
#                     "hethem":"He/Them",
#                     "theythem":"They/Them",
#                     "askme":"Ask me my pronouns"}

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
               f" introducing yourself and tell us your least favorite Trek character, and our mods will " \
               f"let you in!"

# -------URL Match information message used in listeners.py---
urlMatchMsg = ('Hey, <@{}>, it looks like you\'re trying to send a link!\n'
               'Why don\'t you try introducing yourself first? :smile: ')

# Naughtylist types
NAUGHTY_TIMEOUT = "timeout"
NAUGHTY_WARN = "warning"
TIMEOUT_MINUTES = 60
