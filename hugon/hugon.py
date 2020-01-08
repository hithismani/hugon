import time, os, argparse, re, csv, fileinput
from colorama import init, Fore, Style
import urllib
import urllib.request

init(convert=True)

def print_message(colour, message):
    print(colour + message)
    print(Style.RESET_ALL)

def terminal_divider(colour): #Creates horizontal line divider within the terminal window.
    size = os. get_terminal_size()
    fore_color = getattr(Fore, colour)
    print_message(fore_color, ("-"*size.columns))

def run_local_command(commands):
    
    for command in commands:
        print_message(Fore.BLUE, ("Running Command: " + command))
        os.system(command+' &')
    time.sleep(1)
    print_message(Fore.BLUE, ("\nNotes: Waiting for 1 Second Before Next Set Of Commands"))
    
def join_folders(path,sep): #Homogenizing the structure of path (converts any list item into a directory string with given separator). Created this function as os.path.join does not take a list argument.
    folders_list=[]
    i = 0
    while i < len(path):
        if isinstance(path[i], list):
            for item in path[i]:
                folders_list.append(item)
        else:
            folders_list.append(path[i])
        i += 1        
    folders = str(sep).join(folders_list)
    return os.path.join(folders)

def slugify(value, separator):
    """
    Normalizes string, converts to lowercase, removes non-alpha characters,
    and converts spaces to hyphens.
    """
    value = value.replace(".md","")
    if separator in value:
        dup_remove_pattern=re.compile(r"("+separator+")\1{1,}",re.DOTALL)
        filename = (re.sub("[^\\w ]", " ",  value)).strip().replace(" ",separator).lower()
        filename = dup_remove_pattern.sub(r"\1",value).replace(" ","")
    else:     
        filename = (re.sub("[^\\w ]", "",  value)).strip().replace("  "," ").replace(" ",separator).lower()
    
    print_message(Fore.GREEN, ("File Name For Entered String: " +filename))
    return filename

def create_from_archetype(filename,archetype,separator,sequence,prefix):
    archetype = archetype.strip().lower()+"/"
    print_message(Fore.GREEN, ("Archetype Specified: " + archetype[:-1]+".md"))
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
        print_message(Fore.GREEN, ("Executing Command With Prefix: "+prefix))
    for single_file in files_list:
        run_local_command([prefix+archetype+single_file])
    

def print_to_file(csvfile,separator,overwrite):
    with open(csvfile, 'r') as csvfl:
        reader = csv.DictReader(csvfl)
        result = list(reader)
    csvfl.close()
    for record in result:
        terminal_divider("BLUE")
        filename = ""
        if "filename" in record:
            if len(record["filename"].strip()) > 0:
                filename= record["filename"].strip().replace(" ",separator).replace(separator+separator,separator).replace(".md","")
            elif "title" not in record or len(record["title"].strip()) == 0:
                print_message(Fore.RED, ("Cannot find filename (or title) values for one of your rows. Please check if all rows/columns have values in your CSV File! Skipping to next row."))
                continue
            else:
                filename= slugify(record["title"].strip(),separator)
        elif "filename" not in record and "title" not in record:
            print_message(Fore.RED, ("Please specify either 'filename' or 'title' fields for all rows in csv file"))
            pass
        else:
            filename= slugify(record["title"].strip(),separator)
        archetype = ""
        if "archetype" in record and len(record["archetype"].strip())!=0:
            archetype = record["archetype"]
        else:
            print_message(Fore.RED, ("Archetype not specified for filename: "+filename))
            continue
        if "separator" in record:
            separator = record["separator"]
        prefix = "hugo new "
        if "prefix" in record:
            prefix = record["prefix"].strip()+" "
        path = []
        split_first = True #removes first folder from path when inserted into key/value pairing
        if "path" in record:
            path_specified = ""
            if record["path"].startswith("?"):
                split_first = False
                path_specified = record["path"][1:].replace("\\","/").strip()
            else:
                path_specified = record["path"].replace("\\","/").strip() #Homogenizing the structure of path (converts any '/'into '/')
            for folder in path_specified.split("/"):
                path.append(folder)
        proceed = True
        current_path = os.getcwd().split(os.sep)
        if os.path.exists(join_folders([current_path,"content",archetype,(filename+".md")],os.sep)) and overwrite != "true":
            confirmation = input("Filename '"+filename+"' for archetype '"+archetype+"' already exists. You CANNOT undo changes to any file! Should we still proceed/overwrite?  [y/n]")
            if "y" in confirmation.lower():
                proceed = True
            else:
                proceed = False
        if proceed is True:
            create_from_archetype(filename,archetype,separator,0,prefix)
            for key, value in record.items():           
                new_line = ""
                if key.startswith("da-"):
                    download_url = value.strip()
                    file_name = value.split("/")[-1].split("?")[0]
                    download_folder = join_folders([current_path, path],os.sep)
                    if not os.path.exists(download_folder):
                        os.makedirs(download_folder)
                    download_path = join_folders([current_path, path ,file_name],os.sep)
                    if os.path.exists(download_path):
                        if overwrite != "true":
                            confirmation = input("Download file " +download_folder+ " already exists. Should we still proceed/overwrite?  [y/n]")
                            if "y" in confirmation.lower():
                                os.remove(download_path)
                                print_message(Fore.BLUE,("\nFile successfully removed. Proceeding to download."))
                                urllib.request.urlretrieve(download_url, download_path)
                            else:
                                print_message(Fore.BLUE, ("\nFile Replacement Skipped."))
                    else:
                        urllib.request.urlretrieve(download_url, download_path)
                    if os.path.exists(download_path):
                        key = key.replace("da-","").strip()
                        if split_first is True:
                            path.pop(0)
                            value = join_folders([path ,file_name],'/')
                        else:
                            value = join_folders([path ,file_name],'/')
                        print_message(Fore.GREEN, ("\nProceeding With File: '"+file_name+"' found in path "+download_path))
                    else:
                        print_message(Fore.RED, ("\nCould not find file: '"+file_name+"' in path"+download_path))
                if "^;" in value:
                    value_list = ""
                    for element in value.split("^;"):
                        if value.startswith("^"):
                            value_list = value_list+'\n'+' - '+element[1:]
                        else:
                            value_list = value_list+'\n'+' - '+'"'+element+'"'
                    new_line = key.strip()+': '+value_list
                elif key == "content":
                    new_line = value.replace("\\n","\n").replace("  "," ").replace("\n ","\n").strip()
                else:
                    if value.startswith("^"):
                        new_line = key.strip()+': '+value[1:]
                    else:
                        new_line = key.strip()+': "'+value+'"'
                current_path = os.getcwd()
                if key == "content":
                    with open(join_folders([current_path,"content",archetype,((filename+".md"))],os.sep), "r") as myfile:
                        content = myfile.read()
                        with open(join_folders([current_path,"content",archetype,((filename+".md"))],os.sep), "w") as myfile:
                            myfile.write('---\n'+content.split("---\n")[1].strip()+'\n---\n'+new_line)
                    myfile.close()            
                else:
                    for line in fileinput.input(join_folders([current_path,"content",archetype,((filename+".md"))],os.sep), inplace = 1):
                        line = re.sub(r'^'+key.strip()+r'\s*:.*',new_line, line.rstrip()) 
                        print(line)
        
        

def run(args):
    separator = "-"
    print_message(Fore.CYAN, ("Welcome To Hugon! (Hugo + Python) Starting The Tasks You Specified. ^_^"))
    if args.separator:
        separator = str(args.separator)
        print_message(Fore.GREEN, ("\nSeparator specified of length: " + separator))
    if args.filename and args.arch:
        if args.filename:
            terminal_divider("CYAN")
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
            terminal_divider("BLUE")
    elif args.csv.lower() not in "no,nope,dont,skip":
        terminal_divider("CYAN")
        csvfile =  "data.csv"
        current_path = os.getcwd()
        if os.path.exists(join_folders([current_path,csvfile],os.sep)):
            print_message(Fore.YELLOW,("Warning: Files would be modified the moment they're made without copies. Mistakes cannot be undone."))
            print_message(Fore.GREEN, ("Great! 'data.csv' file Found. Proceeding to create markdown files."))
            separator = "-"
            if args.separator:
                separator = args.separator
            prefix = "hugo new "
            if args.prefix:
                prefix = args.prefix.strip()+" "
            overwrite = "false"
            if args.overwrite:
                overwrite = args.overwrite.lower()
            print_to_file(csvfile,separator,overwrite)
        else:
            print_message(Fore.RED, ("Woops. 'data.csv' File Not Found In Directory."))          
    else:
        print_message(Fore.RED, ("Need at least -name and -archetype or -csvpull to be set for script to successfully run."))
    terminal_divider("CYAN")
    print_message(Fore.CYAN, ("Task complete! Don't forget to star this project or report bugs on https://github.com/hithismani/hugon! ^_^"))

def main():
    parser=argparse.ArgumentParser(description="hugon")
    parser.add_argument("-archetype",help="Enter Archetype" ,dest="arch", type=str, required=False)
    parser.add_argument("-name",help="Enter File Name" ,dest="filename", type=str, required=False)
    parser.add_argument("-csvpull",help="Let's you pull a csv from the existing directory. (Set Yes/No)" ,dest="csv", type=str, required=False)
    parser.add_argument("-overwrite",help="Overwrite existing files for csv creation. Default 'false'." ,dest="overwrite", default="false" ,type=str, required=False)
    parser.add_argument("-sequence",help="Enter Sequence Number" ,dest="sequence", type=str,required=False)
    parser.add_argument("-separator",help="Enter Custom separator" ,dest="separator", type=str, required=False)
    parser.add_argument("-prefix",help="Enter Custom Prefix (if using another Hugo CLI)" ,dest="prefix", type=str, required=False)
    parser.set_defaults(func=run)
    args=parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()