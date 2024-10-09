from argparse import ArgumentParser
from yaml import safe_load as load_yml
from simple_term_menu import TerminalMenu
from colorama import init as colorama_init
from colorama import Fore, Style, Back

CONFIG_FILE = 'cmd_config.yml'
GO_BACK_CHOICE = 'GO BACK'

colorama_init()

def print_cmd(cmd: str, desc: str, ip: str, domain: str):
    '''
    It formats the output before printing it to the screen. 
    It highlilghts the IP and Domain provided as well as the description of the command.
    '''
    print(f'\r\n{Back.CYAN}{Fore.BLACK}Description: \r\n{desc}{Style.RESET_ALL}\r\n')

    formatted_ip = f'{Style.RESET_ALL}{Fore.GREEN}{ip}{Style.RESET_ALL}{Fore.LIGHTBLUE_EX}'
    cmd = cmd.replace('<IP>', formatted_ip)

    if domain:
        formatted_domain = f'{Fore.BLUE}{domain}{Fore.LIGHTBLUE_EX}'
        cmd = cmd.replace('<DOMAIN>', formatted_domain)

    formatted_cmd = f'{Fore.LIGHTBLUE_EX}{cmd}{Style.RESET_ALL}\r\n'
    print(formatted_cmd)

def main():
    parser = ArgumentParser()
    parser.add_argument('-i', '--ip', help='The IP of the target', required=True)
    parser.add_argument('-d','--domain', help='The domain of the target, if any', required=False)
    args = parser.parse_args()

    cmd_config = {}
    with open(CONFIG_FILE) as f: 
        cmd_config = load_yml(f)

    options = cmd_config
    while True:
        _, _values = list(options.items())[0]
        _menu_opts = list(_values.keys())
        _menu_opts.append(GO_BACK_CHOICE)
        _formated_menu_opts = [x.replace(':', '').replace('_', ' ').upper() for x in _menu_opts]

        _cli = TerminalMenu(_formated_menu_opts, menu_highlight_style=('bg_cyan','bold',))
        _resp = _cli.show() 
        if _menu_opts[_resp] == GO_BACK_CHOICE:
            options = cmd_config
            continue

        choice = _values[_menu_opts[_resp]]
        if 'cmd' in choice.keys():
            print_cmd(choice['cmd'], choice['description'], args.ip, args.domain)
        else:
            options = choice

if __name__ == '__main__':
    main()

