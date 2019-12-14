import time, os, argparse, re, csv, fileinput
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
    value = value.replace(".md","")
    filename = (re.sub("[^\\w ]", "",  value)).strip().replace("  "," ").replace(" ",separator).lower()
    print_message(Fore.GREEN, ("File Name For Entered String: " +filename))
    return filename

def create_from_archetype(filename,archtype,separator,sequence,prefix):
    archtype = archtype.strip().lower()+"/"
    print_message(Fore.GREEN, ("Archetype Specified: " + archtype[:-1]+".md"))
    files_list = []
    if sequence > 1:
        i = 1
        while i < sequence:
            files_list.append(filename +separator+ str(i) + ".md")
            i += 1
    else:
        files_list.append(filename+ ".md")
    
    if prefix != "hugo new ":
        prefix = prefix.strip() + " "
        print("Executing Command With Prefix: "+prefix)
    for single_file in files_list:
        print(single_file)
        run_local_command([prefix+archtype+single_file])

def print_to_file(csvfile,separator):
    with open(csvfile, 'r') as csvfl:
        reader = csv.DictReader(csvfl)
        result = list(reader)
    csvfl.close()
    for record in result:
        filename = ""
        if "filename" in record:
            if len(record["filename"].strip()) > 0:
                filename= record["filename"].strip()
            elif "title" not in record or len(record["title"]) == 0:
                print("Cannot find filename (or title) values for one of your rows. Please check!")
                break
            else:
                filename= slugify(record["title"],separator)
        elif "filename" not in record and "title" not in record:
            print("Please specify either 'filename' or 'title' fields in csv file")
            break
        else:
            filename= slugify(record["title"],separator)
        archtype = ""
        if "archetype" in record:
            archtype = record["archetype"]
        else:
            print("Archetype not specified. Please supply an archtype in CSV or in Shell.")
            break
        if "separator" in record:
            separator = record["separator"]
        prefix = "hugo new "
        if "prefix" in record:
            prefix = record["prefix"].strip()+" "
        create_from_archetype(filename,archtype,separator,0,prefix)
        for key, value in record.items():           
            new_line = ""
            if "^;" in value:
                value_list = ""
                for element in value.split("^;"):
                    if value.startswith("^"):
                        value_list = value_list+'\n'+' - '+element[1:]
                    else:
                        value_list = value_list+'\n'+' - '+'"'+element+'"'
                new_line = key+': '+value_list
            elif key == "content":
                new_line = value.replace("\\n","\n ")
            else:
                if value.startswith("^"):
                    new_line = key+': '+value[1:]
                else:
                    new_line = key+': "'+value+'"'
            current_path = os.getcwd()
            if key == "content":
        
                with open(os.path.join(current_path,"content",archtype,((filename+".md"))), "a") as myfile:
                    myfile.write(new_line)              
            else:
                
                for line in fileinput.input(os.path.join(current_path,"content",archtype,((filename+".md"))), inplace = 1):
                    line = re.sub(r'^'+key+r'\s*:.*',new_line, line.rstrip()) 
                    print(line)
            

            


def run(args):
    separator = "-"
    if args.separator:
        separator = str(args.separator)
        print("Separator specified of length: " + separator)
    if args.filename and args.arch or args.csv:
        if args.filename:
            filename = slugify(args.filename,separator)
            sequence = 0
            if args.sequence:
                sequence = int(args.sequence)
            separator = "-"
            if args.separator:
                separator = args.separator
            prefix = "hugo new "
            if args.prefix:
                prefix = args.prefix.strip()+" "
            create_from_archetype(filename, args.arch,separator,sequence,prefix)
            
        elif args.csv.lower() not in "no,nope,dont,skip":
            csvfile =  "data.csv"
            current_path = os.getcwd()
            if os.path.exists(os.path.join(current_path,csvfile)):
                print("Csv data file Found. Proceeding to create markdown files.")
                separator = "-"
                if args.separator:
                    separator = args.separator
                prefix = "hugo new "
                if args.prefix:
                    prefix = args.prefix.strip()+" "
                print_to_file(csvfile,separator)
            else:
                print("data.csv File Not Found In Directory.")

              
    else:
        print("Need at least -name and -archetype or -csvpull to be set for script to successfully run.")
def main():
    parser=argparse.ArgumentParser(description="hugon")
    parser.add_argument("-archetype",help="Enter Archetype" ,dest="arch", type=str, required=False)
    parser.add_argument("-name",help="Enter File Name" ,dest="filename", type=str, required=False)
    parser.add_argument("-csvpull",help="Let's you pull a csv from the existing directory. (Set Yes/No)" ,dest="csv", type=str, required=False)
    parser.add_argument("-sequence",help="Enter Sequence Number" ,dest="sequence", type=str,required=False)
    parser.add_argument("-separator",help="Enter Custom separator" ,dest="separator", type=str, required=False)
    parser.add_argument("-prefix",help="Enter Custom Prefix (if using another Hugo CLI)" ,dest="prefix", type=str, required=False)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()