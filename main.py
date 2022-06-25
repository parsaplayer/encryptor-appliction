from colorama import Fore
import sys
from colorama import init
from termcolor import cprint
from pyfiglet import figlet_format
from time import sleep
import os
import progressbar
import glob
file_dir = os.getcwd()
print(file_dir)
init(strip=not sys.stdout.isatty())
def fast_scandir(dirname):
    try:
        subfolders= [f.path for f in os.scandir(dirname) if f.is_dir()]
        for dirname in list(subfolders):
            subfolders.extend(fast_scandir(dirname))
        return subfolders
    except:
        return ""
def reader(directory):
    files = []
    dirs = fast_scandir(directory)
    bar = progressbar.ProgressBar(maxval=20, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
    bar.start()
    i = 0
    dirs.append(directory)
    for directory in dirs:
        try:
            os.chdir(directory)
            glb = glob.glob("*.*")
            for j in range(len(glb)):
                files.append(directory+"/"+glb[j])
            bar.update(((20*i)/len(dirs)))
            i=i+1
        except :
            bar.update(((20*i)/len(dirs)))
            i=i+1
    bar.finish()
    return files 
def ascii_art(text):
    cprint(figlet_format(text),'yellow', 'on_red', attrs=['bold'])
ascii_art("encryptor")
print("welcome!!!\nuse command 'help'for Help")
run_time = True
while run_time:
    command = str(input(">"))
    if command == "help":
        print("encrypt     encrypt mode\n1.add your directory which you want to encrypt/hide\n2.add your jpg format image which you want your files hide in it\n3.wait!!!")
    if command == "encrypt":
        print(Fore.RED+"encryptor")
        dir_ok_to_pass = False
        jpg_ok_to_pass = False
        while not dir_ok_to_pass:
            ok = False
            dir = str(input("directory address>"))
            try:
                os.chdir(dir)
                ok = True
            except:
                print(Fore.RED+"error:this directory do not exicte!!!")
                ok = False
            if ok:
                dir_ok_to_pass = True
        while not jpg_ok_to_pass:
            print(Fore.YELLOW+"warning:Images with more details works better for this program")
            img_dir = str(input("jpg image address>"))
            if ".jpg" in img_dir or ".jpeg" in img_dir:
                try:
                    os.chdir(file_dir)
                    if open(img_dir,"rb"):
                        jpg_ok_to_pass = True
                except:
                    print("err here")
            else:
                print(Fore.RED+"error:can not access this jpg file or this file do not exicte!!!")
        img_dir = file_dir+"/"+img_dir
        print(Fore.BLUE+"collecting files from folder")
        print(Fore.YELLOW+"warning:some files can't be collected becuse of adminestor access")
        files = reader(dir)
        for addrs in files:
            print(Fore.GREEN+addrs+" collected")
        print(Fore.BLUE+"processing:")
        os.chdir(file_dir)
        bar = progressbar.ProgressBar(maxval=20, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
        bar.start()
        for i in range(len(files)):
            bar.update((i*20)/len(files))
            wsrc1 = open(img_dir,"rb").read()+bytes("\n#","utf8")+bytes(files[i],"utf8")
            open(img_dir,"wb").write(wsrc1)
            #try:
            for line in open(files[i],"rb"):
                wsrc2 = open(img_dir,"rb").read()+bytes("\n***","utf8")+line
                open(img_dir,"wb").write(wsrc2)
            #except:
                #pass
        bar.finish()