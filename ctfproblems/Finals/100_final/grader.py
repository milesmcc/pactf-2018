import requests

urls = {
    "943461037": "http://159.203.33.16:80", #PACTF
    "1371804441": "http://159.89.115.12:80", #0x5F3759DF
    "1148064481": "http://167.99.191.63:80", #meephackerz
    "1151734498": "http://159.89.125.204:80", #pearl
    "1308889865": "http://159.89.115.171:80", #SST CTF
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
            if teamnames[str(key)] in requests.get(urls[str(key)], timeout=1).text:
                return True, "Congratulations! You have completed the PACTF tiebreaker. Please see the scoreboard to see how your time stacks up."
            else:
                return False, "Nope, sorry! Didn't see your team name there!"
        except:
            return False, "Unable to complete the request to %s" % urls[str(key)]
    else:
        return False, "Sorry, your team is not eligible to compete in the tiebreaker."
