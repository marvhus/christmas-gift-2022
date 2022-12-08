class GiftConfig:
    def __init__(self):
        self.too_early = ""
        self.christmas = ""
        # Default day is the 24th of December
        self.day = 24
        self.offset = 19

def obscure_message(text: str, offset: int) -> str:
    import random
    out = ''.join(
        [
            hex((ord(c) + offset) % 255)[2:] + hex(random.randint(16,255))[2:]
            for c in text
        ]
    )
    return out
    
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
            'offset',
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
                    elif name == 'offset':
                        config.offset = int(val)
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

def write_gift(config: GiftConfig):
    with open('gift.py', 'wt') as f:
        obscured_date = hex(config.day + config.offset)[2:]
        too_early_len = len(config.too_early)
        christmas_len = len(config.christmas)
        code = [
            # vars and imports
            f'from datetime import datetime as dt;',
            f'a=print;',
            f'b=int;',
            f'h=hex;',
            f'e=chr;',
            # print
            f'a(',
            # too early
            f'"".join([',
            f'e((b("{config.too_early}"[i:i+2],16)-{config.offset})%255)',
            f'for i in range(0,{too_early_len},4)',
            f'])',
            # condition
            f'if h(dt.today().day+{config.offset})<"{obscured_date}" else',
            f'"".join([',
            # christmas
            f'e((b("{config.christmas}"[i:i+2],16)-{config.offset})%255)',
            f'for i in range(0,{christmas_len},4)',
            f'])',
            # end of print
            f')',
        ]
        for line in code:
            f.write(line)

def main():
    import sys
    args = sys.argv[1:]
    if len(args) <= 0:
        print('No config file, please provide a config file')
        exit(1)
    # first arg should be a path to a config
    config = parse_config(args[0])
    config.too_early = obscure_message(config.too_early, config.offset)
    config.christmas = obscure_message(config.christmas, config.offset)
    write_gift(config)
    

if __name__ == '__main__': main()         
