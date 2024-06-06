import argparse

class Colors:
    white = '\033[97m\033[1m'
    green = '\033[92m\033[1m'
    blue = '\033[0;36m\033[1m'
    red = '\033[91m\033[1m'
    yellow = '\033[93m\033[1m'

def info(message):
    print(f"{Colors.blue}[*]{Colors.white} {Colors.white}{message}")

def error(message):
    print(f"{Colors.red}[-]{Colors.white} {Colors.white}{message}")

def success(message):
    print(f"{Colors.green}[+]{Colors.white} {Colors.white}{message}")

def ArgumentParser():
    parser = argparse.ArgumentParser(prog='Vector', description='Web sitelerinde ki resimlerin exif verilerini toplayan bir programdır.', epilog='...')
    parser.add_argument("--url",      "-u", help="hedef sitenin url adresini belirtmenizi sağlar.", required=True, type=str)
    parser.add_argument("--crawl",    "-c", help="Taranacak alt sayfa sayısını belirtmenizi sağlar. (varsayılan: 2)", nargs="?", const=2, default=1, type=int)
    parser.add_argument("--keywords", "-k", help="Filtrelenecek exif etiketlerini belirtmenizi sağlar. (varsayılan: all)", default="all", type=str)
    return parser.parse_args()

def print_logo():
    print(f"""{Colors.red}
 _    _ _______ _______ _______  _____   ______
  \  /  |______ |          |    |     | |_____/
   \/   |______ |_____     |    |_____| |    \_

     .: {Colors.white}Coded By Ronark / Github: @Ronark7 {Colors.red}:.{Colors.white}
                                                                            
    """)
