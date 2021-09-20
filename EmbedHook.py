import requests
print("""

███████╗███╗░░░███╗██████╗░███████╗██████╗░██╗░░██╗░█████╗░░█████╗░██╗░░██╗
██╔════╝████╗░████║██╔══██╗██╔════╝██╔══██╗██║░░██║██╔══██╗██╔══██╗██║░██╔╝
█████╗░░██╔████╔██║██████╦╝█████╗░░██║░░██║███████║██║░░██║██║░░██║█████═╝░
██╔══╝░░██║╚██╔╝██║██╔══██╗██╔══╝░░██║░░██║██╔══██║██║░░██║██║░░██║██╔═██╗░
███████╗██║░╚═╝░██║██████╦╝███████╗██████╔╝██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗
╚══════╝╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═════╝░╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝            

""")
url = input("URL de tu Discord Webhook: ")
embed = {}
embedtitle = input("Titulo del Embed: ")
embed["title"] = embedtitle
embeddesc = input("Descripcion del Embed: ")
embed["description"] = embeddesc
while True: #Thumbnail (optional)
    thumbnailornot = input("Agregar una imagen? (Si/no): ")
    if thumbnailornot.lower() == 'si':
        embedthumbnailurl = input("Ingresa la URL de tu imagen: ")
        embed['thumbnail'] = {"url": embedthumbnailurl}
        break
    elif thumbnailornot.lower() == 'no':
        break
    else:
        print("Porfavor elije una opcion valida; 'Si' o 'no' :")
embedfieldnum = input("Cuantos Campos deseas en tu embed? (Ingresa un numero, 0 para ninguno): ")
try: embedfieldnum = int(embedfieldnum)
except: print("Tenias que poner un numero, supongo que te referias a 0")
if embedfieldnum is not 0:
    embed['fields'] = []
    for fieldnum in range(embedfieldnum):
        fieldtitle = input("Campo {} Titulo: ".format(fieldnum+1))
        fieldtext = input("Campo {} Contenido: ".format(fieldnum+1))
        embed['fields'].append({"name":fieldtitle,"value":fieldtext})
embedcolor = input("Hex Color de tu Embed (6 Digitos): ")
embedcolor = int(embedcolor, 16)
embed["color"] = embedcolor
print(embed)
data = {"embeds": [embed]}
requests.post(url,json=data)
