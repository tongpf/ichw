"""wcount.py: count words from an Internet file.

__author__ = "tongpf"
__pkuid__  = "1600013237"
__email__  = "tongpf@pku.edu.cn"
"""

import sys
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    for i in ["'",'"',',','.','?','!',';',':','*','(',')','/','\n','\r','[',']','-']:
        lines=lines.replace(i,' ')
    lines=lines.lower()
    lines=lines.split(' ')
    chardir={}
    for i in lines:
        if i == '':
            pass
        elif i in chardir:
            chardir[i]=chardir[i]+1
        else:
            chardir[i]=1
    num=list(chardir.values())
    for i in range(topn):
        namelist=[]
        knum = max(num)
        for key, value in chardir.items():
            if value == knum:
                namelist.append(key)
            char=' '.join(namelist)
        print('%-20s%-20s' % (char,knum))
        num.remove(knum)
    return

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
