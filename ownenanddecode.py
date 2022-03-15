class Encodess():
    def Encodes(data):
        encodestr=""
        enco = {
             'a':"46cd", 'b':"32gb", 'c':"45ef", 'd':"89ef", 'e':"75wf", 'f':"56rt", 'g':"78rt", 'h':"76ty", 'i':"35er", 'j':"26et",
             'k':'55eg', 'l':"89zx", 'm':"78we", 'n':"95df", 'o':"56qr", 'p':"45qn", 'q':'89tr', 'r':'35wx', 's':'21eb', 't':'85gh',
             'u':"63dg", 'v':'54dl', 'w':"56ev", 'x':'23df', 'y':'12dg', 'z':"13df",
             'A':"95ef", 'B':"64cd", 'C':"23uv", 'D':'46lk', 'E':'36rs', 'F':'27uc', 'G':'98kv', 'H':'81pr', 'I':'83sv', 'J':'81su',
             'K':'86jk', 'L':'89ji', 'M':'99GK', 'N':'99gh', 'O':'93ln', 'P':'95nm', 'Q':'22gh', 'R':'34hy', 'S':'12he', 'T':'34su',
             "U":'12ra', 'V':'67rt', 'W':'32er', 'X':'55ra', 'Y':'33cv', 'Z':'32ep',
             '1':'12As', '2':'45We', '3':'44Sr', '4':'89Sd', '5':'99We', '6':'66Ft', '7':'22Et', '8':'88Er', '9':"44De", '0':"44Ww",
             '.':'AD45', ' ':'DF45', '-':'SB56'} 

        data=list(str(data))
        for i in data:
            for j in enco:
                if i==j:
                    encodestr=encodestr+enco[j]+"0"
        return encodestr

class Decodess():
    def Decodes(data):
        decodestr=""
        decodelist=[]
        enco = {
             'a':"46cd", 'b':"32gb", 'c':"45ef", 'd':"89ef", 'e':"75wf", 'f':"56rt", 'g':"78rt", 'h':"76ty", 'i':"35er", 'j':"26et",
             'k':'55eg', 'l':"89zx", 'm':"78we", 'n':"95df", 'o':"56qr", 'p':"45qn", 'q':'89tr', 'r':'35wx', 's':'21eb', 't':'85gh',
             'u':"63dg", 'v':'54dl', 'w':"56ev", 'x':'23df', 'y':'12dg', 'z':"13df",
             'A':"95ef", 'B':"64cd", 'C':"23uv", 'D':'46lk', 'E':'36rs', 'F':'27uc', 'G':'98kv', 'H':'81pr', 'I':'83sv', 'J':'81su',
             'K':'86jk', 'L':'89ji', 'M':'99GK', 'N':'99gh', 'O':'93ln', 'P':'95nm', 'Q':'22gh', 'R':'34hy', 'S':'12he', 'T':'34su',
             "U":'12ra', 'V':'67rt', 'W':'32er', 'X':'55ra', 'Y':'33cv', 'Z':'32ep',
             '1':'12As', '2':'45We', '3':'44Sr', '4':'89Sd', '5':'99We', '6':'66Ft', '7':'22Et', '8':'88Er', '9':"44De", '0':"44Ww",
             '.':'AD45', ' ':'DF45', '-':'SB56' }
        data=data.split("0")
        for i in data:
            key=[k for k, v in enco.items() if v==i]
            decodelist=decodelist+key
        for i in decodelist:
            decodestr=decodestr+i
        return decodestr

#en=Encodess.Encodes("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLNMOPQRSTUVWXYZ0123456789 .-")
#print(en,'encode')   
#print(Decodess.Decodes(en),'decode')