import openai
import os
from revChatGPT.V3 import Chatbot
from datetime import datetime as dt
# Utilities and helper functions for the bot



def groups(seq, length):
    """Generator to yield groups of the specified length from a sequence. For example, to
    give 10 character chuncks of a string. The final yield will provide whatever data is
    left in the sequence, without any extra padding. Useful in a for statement:
        for pair in groups('abcdefg', 2):
            do_the_thing(pair)
    :param seq: A slicable object like string or list.
    :param length: The length of each group (ie. 2 for pairs)
    """
    for i in range(0, len(seq), length):
        yield seq[i:i + length]

def openai_q_and_a(query):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Completion.create(
        model="text-davinci-002",
        prompt=query,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        best_of=4,
        frequency_penalty=0.43,
        presence_penalty=0.25
    )


    print(response)
    return response['choices'][0]['text']

def cgpt(query, userid):
    "foo"

    #chatbot = Chatbot(api_key=CHATGPT_API, system_prompt=CGPT_PROMPT)


    # print()

def remove_non_ascii(s):
    """Remove non-ASCII characters from a Unicode string. Removes @ (at symbol, decimal
    64) which pings discord users/roles. Also removes ` (grave accent, decimal 96) which
    modifies discord formatting.
    :param s: String
    """
    return str("".join(i for i in s if ord(i) < 128 and ord(i) != 96 and ord(i) != 64))


def date(target, clock=True):
    if clock is False:
        return target.strftime("%d %B %Y")
    return target.strftime("%d %B %Y, %H:%M")

