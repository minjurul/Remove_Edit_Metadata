import argparse
import pyexiv2
from termcolor import colored


def Banner():
    print colored("Edit Metadata of you Images or clear All metadata",color='red')
    print colored("    __  __           _ _  __         __  __      _            _       _        ", color='green')
    print colored("   |  \/  |         | (_)/ _|       |  \/  |    | |          | |     | |       ", color='green')
    print colored("   | \  / | ___   __| |_| |_ _   _  | \  / | ___| |_ __ _  __| | __ _| |_ __ _ ", color='green')
    print colored("   | |\/| |/ _ \ / _` | |  _| | | | | |\/| |/ _ \ __/ _` |/ _` |/ _` | __/ _` |", color='green')
    print colored("   | |  | | (_) | (_| | | | | |_| | | |  | |  __/ || (_| | (_| | (_| | || (_| |", color='green')
    print colored("   |_|  |_|\___/ \__,_|_|_|  \__, | |_|  |_|\___|\__\__,_|\__,_|\__,_|\__\__,_|", color='green')
    print colored("                              __/ |                                            ", color='green')
    print colored("                             |___/                                             ", color='green')
    print('{:>70}'.format(colored("Coded by - Minjurul", color='red')))


def ClearAllMatadata(imgname,preserve):
    metadata = pyexiv2.ImageMetadata(imgname)
    metadata.read()
    metadata.clear()
    metadata.write(preserve)
def ModifyMode(imgname,preserve):
    metadata = pyexiv2.ImageMetadata(imgname)
    metadata.read()
    simble = "==>"
    print ('\n\n{:>10}   {:>60}'.format('Key','Data'))
    print("===========================================================================================")
    for key,value in metadata.iteritems():
        print('{:<50} {:<20} {:<70}'.format(colored(key,'green'),simble,colored(value.raw_value,'red')))
    modkey =raw_input("Key to modify (q to quit):")
    while not modkey == 'q':
        print "Editing :" +str(metadata[modkey].raw_value)
        modvalue =raw_input("New value (q to quit):")
        if modvalue == 'q':
            break
        metadata[modkey].raw_value = str(modvalue)
        modkey = raw_input("Key to modify (q to quit):")
    metadata.write(preserve)

def Mian():
    Banner()
    parser = argparse.ArgumentParser()
    parser.add_argument("img",help = "Images file to monipulate")
    parser.add_argument("--clear","-c",help="Clear all metadata from the file",action="store_true")
    parser.add_argument("--preserve","-p",help="Preserve Images modified data",action="store_true")
    args = parser.parse_args()
    if args.img:
        if args.clear:
            ClearAllMatadata(args.img,args.preserve)
        else:
            ModifyMode(args.img,args.preserve)
    else:
        print parser.usage


if __name__ == '__main__':
    Mian()
