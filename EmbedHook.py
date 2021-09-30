import requests
print("""

███████╗███╗░░░███╗██████╗░███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔════╝████╗░████║██╔══██╗██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝
█████╗░░██╔████╔██║██████╦╝█████╗░░██║░░██║███████║██║░░██║██║░░██║█████═╝░
██╔══╝░░██║╚██╔╝██║██╔══██╗██╔══╝░░██║░░██║██╔══██║██║░░██║██║░░██║██╔═██╗░
███████╗██║░╚═╝░██║██████╦╝███████╗██████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚══════╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝            

""")
url = input("URL of the WebHook: ")
embed = {}
embedtitle = input("Embed Title: ")
embed["title"] = embedtitle
embeddesc = input("Embed Description: ")
embed["description"] = embeddesc
while True: #Thumbnail (optional)
    thumbnailornot = input("Willing to add an image? (S/n): ")
    if thumbnailornot.lower() == 's':
        embedthumbnailurl = input("URL Of the Image: ")
        embed['thumbnail'] = {"url": embedthumbnailurl}
        break
    elif thumbnailornot.lower() == 'n':
        break
    else:
        print("Please select a valid option; 'S' or 'n' :")
embedfieldnum = input("How many fields for your embed? (Put a number, 0 for none): ")
try: embedfieldnum = int(embedfieldnum)
except: print("You were supposed to put a number, we will assume you meant 0")
if embedfieldnum is not 0:
    embed['fields'] = []
    for fieldnum in range(embedfieldnum):
        fieldtitle = input("Campo {} Titulo: ".format(fieldnum+1))
        fieldtext = input("Campo {} Contenido: ".format(fieldnum+1))
        embed['fields'].append({"name":fieldtitle,"value":fieldtext})
embedcolor = input("Hex Color of the Embed (6 Digits): ")
embedcolor = int(embedcolor, 16)
embed["color"] = embedcolor
print(embed)
data = {"embeds": [embed]}
requests.post(url,json=data)
