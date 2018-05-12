import requests

urls = {
    "943461037": "https://hastebin.com/raw/uxabimabag", #PACTF
    "1371804441": "your server's IP here (0x5F3759DF)", #0x5F3759DF
    "1148064481": "your server's IP here (meephackerz)", #meephackerz
    "1151734498": "your server's IP here (pearl)", #pearl
    "1308889865": "your server's IP here (SST CTF)", #SST CTF
}

teamnames = {
        "943461037": "PACTF", #PACTF
        "1371804441": "0x5F3759DF", #0x5F3759DF
        "1148064481": "meephackerz", #meephackerz
        "1151734498": "pearl", #pearl
        "1308889865": "SST CTF", #SST CTF
}


def grade(key, submission):
    if str(key) in urls:
        try:
            if teamnames[str(key)] in requests.get(urls[str(key)]).text:
                return True, "Congratulations! You have completed the PACTF tiebreaker. Please see the scoreboard to see how your time stacks up."
            else:
                return False, "Nope, sorry! Didn't see your team name there!"
        except:
            return False, "Unable to complete the request " % urls(str(key))
    else:
        return False, "Sorry, your team is not eligible to compete in the tiebreaker."
