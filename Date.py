class datemodify:
    def __init__(self,date=0):
        if date==0:
            date=input("Enter the date : ")
        self.date=date
    def nextdate(self):
        a=self.date
        d = a[0:2]
        m = a[3:5]
        y = a[6:10]
        if (int(a[3:5]) == 1 or int(a[3:5]) == 3 or int(a[3:5]) == 5 or int(a[3:5]) == 7 or int(a[3:5]) == 8 or int(
                a[3:5]) == 10 or int(a[3:5]) == 12):
            if (int(a[0:2]) == 31):
                if (int(a[3:5]) == 12):
                    m = "01"
                    y = str(int(a[6:10]) + 1)
                else:
                    m = str(int(m) + 1)
                d = "01"
            else:
                d = str(int(a[0:2]) + 1)
        elif (int(a[3:5]) == 4 or int(a[3:5]) == 6 or int(a[3:5]) == 9 or int(a[3:5]) == 11):
            if (int(a[0:2]) == 30):
                m = str(int(m) + 1)
                d = "01"
            else:
                d = str(int(a[0:2]) + 1)
        elif (int(a[3:5]) == 2):
            if (int(y) % 4 == 0):
                if (int(a[0:2]) == 29):
                    m = str(int(m) + 1)
                    d = "01"
                else:
                    d = str(int(d) + 1)
            else:
                if (int(d) == 28):
                    m = str(int(m) + 1)
                    d = "01"
                else:
                    d = str(int(d) + 1)
        p = ["1", '2', '3', '4', '5', '6', '7', '8', '9']
        if d in p:
            d = "0" + d
        if m in p:
            m = "0" + m

        b = d + "-" + m + "-" + y
        return (b)
    def previousdate(self):
        a=self.date
        d = a[0:2]
        m = a[3:5]
        y = a[6:10]
        if (int(m) == 1 or int(m) == 3 or int(m) == 5 or int(m) == 7 or int(m) == 8 or int(m) == 10 or int(m) == 12):
            if (int(a[0:2]) == 1):
                if (int(a[3:5]) == 1):
                    m = "12"
                    y = str(int(a[6:10]) - 1)
                else:
                    m = str(int(m) - 1)
                if (int(m) == 1 or int(m) == 3 or int(m) == 5 or int(m) == 7 or int(m) == 8 or int(m) == 10 or int(
                        m) == 12):
                    d = "31"
                elif (int(m) == 4 or int(m) == 6 or int(m) == 9 or int(m) == 11):
                    d = "30"
                elif (int(m) == 2):
                    if (int(y) % 4 == 0):
                        d = "29"
                    else:
                        d = "28"
            else:
                d = str(int(a[0:2]) - 1)
        elif (int(a[3:5]) == 4 or int(a[3:5]) == 6 or int(a[3:5]) == 9 or int(a[3:5]) == 11):
            if (int(a[0:2]) == 1):
                m = str(int(m) - 1)
                if (int(m) == 1 or int(m) == 3 or int(m) == 5 or int(m) == 7 or int(m) == 8 or int(m) == 10 or int(
                        m) == 12):
                    d = "31"
                elif (int(m) == 4 or int(m) == 6 or int(m) == 9 or int(m) == 11):
                    d = "30"
                elif (int(m) == 2):
                    if (int(y) % 4 == 0):
                        d = "29"
                    else:
                        d = "28"
            else:
                    d = str(int(a[0:2]) - 1)
        elif (int(a[3:5]) == 2):
            if (int(d)==1):
                m="01"
                d="31"
            else:
                d=str(int(d)-1)
        p = ["1", '2', '3', '4', '5', '6', '7', '8', '9']
        if d in p:
            d = "0" + d
        if m in p:
            m = "0" + m

        b = d + "-" + m + "-" + y
        return (b)
