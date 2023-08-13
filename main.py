import platform


def block_websites(websites):
    system = platform.system()

    if system == "Windows":
        hosts_path = r'C:\Windows\System32\drivers\etc\hosts'
    elif system == "Linux":
        hosts_path = '/etc/hosts'
    else:
        return

    with open(hosts_path, 'a') as hosts_file:
        for website in websites:
            hosts_file.write(f'127.0.0.1 {website}\n')

    print("ip loggers blocked successfully.")


if __name__ == "__main__":
    websites_to_block = [
        "grabify.link",
        "mymassive.yachts",
        "stonks.boats",
        "stonks.fun",
        "toes.beauty",
        "barefoot.pics",
        "shareit.pics",
        "gamer.tattoo",
        "shipment.website",
        "imagevault.cloud",
        "sugma.mom",
        "yum.mom",
        "plz.life",
        "massive.mom",
        "massive.boats",
        "mymassive.store",
        "mymassive.top",
        "gamer.hair",
        "photovault.pics",
        "bathtub.pics",
        "foot.wiki",
        "thisdomainislong.lol",
        "gamergirl.pro",
        "picshost.pics",
        "pichost.pics",
        "imghost.pics",
        "imagehost.pics",
        "toldyouso.lol",
        "toldyouso.pics",
        "screenshare.pics",
        "myprivate.pics",
        "noodshare.pics",
        "dateing.club",
        "shrekis.life",
        "headshot.monster",
        "progaming.monster",
        "yourmy.monster",
        "screenshot.best",
        "gamingfun.me",
        "catsnthing.com",
        "catsnthings.fun",
        "joinmy.site",
        "fortnitechat.site",
        "fortnight.space"]
    block_websites(websites_to_block)
