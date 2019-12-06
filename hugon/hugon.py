import time, os, argparse, re
from colorama import init, Fore, Style

init(convert=True)

def print_message(colour, message):
    print (colour + message)
    print(Style.RESET_ALL)

def run_local_command(commands):
    for command in commands:
        print_message(Fore.BLUE, ("Runnning Command: " + command))
        os.system(command+' &')
    time.sleep(1)
    print_message(Fore.BLUE, ("Notes: Waiting for 1 Second Before Next Set Of Commands"))

def slugify(value, separator):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    filename = (re.sub("[^\\w ]", "",  value)).strip().replace("  "," ").replace(" ",separator).lower()
    print_message(Fore.GREEN, ("File Name For Entered String: " +filename))
    return filename

def run(args):
    separator = "-"
    if args.separator:
        separator = str(args.separator)
        print("Separator specified of length: " + separator)
    filename = slugify(args.filename,separator)
    archtype = args.arch.strip().lower()+"/"
    print_message(Fore.GREEN, ("Archetype Specified: " + archtype[:-1]+".md"))
    files_list = []
    if args.sequence:
        sequence = int(args.sequence)
        if sequence > 1:
            i = 1
            while i < sequence:
                files_list.append(filename +separator+ str(i) + ".md")
                i += 1
    else:
        files_list.append(filename+ ".md")
    prefix = "hugo new "
    if args.prefix:
        prefix = args.prefix.strip() + " "
        print("Executing Command With Prefix: "+prefix)
    for single_file in files_list:
        print(single_file)
        run_local_command([prefix+archtype+single_file])

def main():
    parser=argparse.ArgumentParser(description="hugon")
    parser.add_argument("-archetype",help="Enter Archetype" ,dest="arch", type=str, required=True)
    parser.add_argument("-name",help="Enter File Name" ,dest="filename", type=str, required=True)
    parser.add_argument("-sequence",help="Enter Sequence Number" ,dest="sequence", required=False)
    parser.add_argument("-separator",help="Enter Custom separator" ,dest="separator", type=str, required=False)
    parser.add_argument("-prefix",help="Enter Custom Prefix (if using another Hugo CLI)" ,dest="prefix", type=str, required=False)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()