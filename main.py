class GiftConfig:
    def __init__(self):
        self.too_early = ""
        self.christmas = ""
        # Default day is the 24th of December
        self.day = 24

def obscure_message(text: str) -> str:
    with open('gift.py', 'wt') as file:
        pass
    
def parse_config(path: str) -> GiftConfig:
    config = GiftConfig()
    with open(path, 'rt') as lines:
        section = None
        valid_section = [
            'too_early',
            'christmas',
        ]
        valid_setting = [
            'day',
        ]
        clear_text = []
        for line in lines:
            # Skip line if it is a comment (starts with a '#')
            if line[0] == '#':
                continue
            # Check if line is config
            if line[0] == ':':
                setting = [arg.strip('\n') for arg in line.split(' ')[1:] if len(arg) > 0]
                # parse sections
                if setting[0] in valid_section:
                    # There is already a pre existing section
                    if not section == None:
                        if section == 'too_early':
                            config.too_early = '\n'.join(clear_text)
                        elif section == 'christmas':
                            config.christmas = '\n'.join(clear_text)
                        clear_text = []
                    section = setting[0]
                # parse settings
                if setting[0] in valid_setting:
                    (name, val) = setting
                    if name == 'day':
                        config.day = int(val)
                    # TODO: add more settings
                continue
            # Add line as plaintext (ignore empty line)
            if len(line.strip('\n')) > 0:
                clear_text.append( line.strip('\n') )

        # Add extra text to config
        if len(clear_text) > 0:
            if section == 'too_early':
                config.too_early = '\n'.join(clear_text)
            elif section == 'christmas':
                config.christmas = '\n'.join(clear_text)

    return config


def main():
    import sys
    args = sys.argv[1:]
    if len(args) <= 0:
        print('No config file, please provide a config file')
        exit(1)
    # first arg should be a path to a config
    config = parse_config(args[0])

if __name__ == '__main__': main()         

