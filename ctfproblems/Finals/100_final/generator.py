ips = {
    "943461037": "your server's IP here (PACTF)", #PACTF
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

def generate(key):
    if str(key) in ips:
        return ("The tellers at BigBuckBankingCorp were struggling to properly add up the account balances of their clients, so the (underfunded) IT department built them a calculator. \n\n The calculator is running on port `1778` at `%s`. \n\n Your mission is to compromise the server such that an HTTP request to `%s:80` returns a valid response that contains your team name, `%s`. Submitting a flag will trigger a request to the server to detect whether the challenge is solved. Submit anything _as_ the flag, but note that you cannot submit the same text twice. The _text_ submitted as the flag is not important; whether the server responds to an HTTP request with a response containing your team name is the only criteria for a valid solution. Each team has its own server.\n\n**Please see the hint for administrative details.**" % (ips[str(key)], ips[str(key)], teamnames[str(key)]),
        "**Administrative details**\n* Scores will be determined based on time taken to solve.\n* Try not to break your server, however you may at any point request that it be reset to its original image by emailing `contact@pactf.com` and being sure to include your team code `%s` in your email. Such a request will have a time penalty of 12 hours, and we cannot guarantee an immediate response.\n* It is possible to gain root shell access to the server. Your job is to respond to HTTP requests on port 80 with your team name; doing anything beyond this (such as cryptocurrency mining or torrenting, for example) is grounds for disqualification." % (str(key)))
    else:
        return ("Sorry, your team is not eligible to compete in PACTF Finals. We hope you enjoyed Round 1 and Round 2! You will be contacted about prizes in early June.", "_Hint not applicable._")
