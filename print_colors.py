class Color:
    """Colorize print to console"""
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    # foreground
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

    # background
    bg_black = '\033[40m'
    bg_red = '\033[41m'
    bg_green = '\033[42m'
    bg_orange = '\033[43m'
    bg_blue = '\033[44m'
    bg_purple = '\033[45m'
    bg_cyan = '\033[46m'
    bg_lightgrey = '\033[47m'

def example():
    for fg, bg in zip([Color.red, Color.green, Color.blue], [Color.bg_lightgrey, Color.bg_orange, Color.bg_purple]):
        print(fg + bg + "Some text" + Color.reset)

if __name__ == "__main__":
    example()
