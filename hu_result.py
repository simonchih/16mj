class hu_result():
    def __init__(self, mj, dmj, hnum, first_turn, hmj, circle, getmj = None, first_hear = 0, drophu = None, hhu = False):
        self.mj = mj
        self.dj = dmj
        self.hnum = hnum
        self.ft = first_turn
        self.hj = hmj
        self.circle = circle
        self.gethu = getmj
        self.first_hear = first_hear
        self.drophu = drophu
        self.hhu = hhu
        
        self.fmj = self.mj[:]
        if None == getmj:
            self.fmj.append(drophu)
            self.fmj.sort()
        else:
            self.fmj.append(getmj)
            self.fmj.sort()
            
        self.table = {
            "莊家": self.hosthu(),
            ("連%d拉%d" % (hnum, hnum)): 2 * hnum,
            "自摸": self.selfhu(),
            "門清": self.dmjclear(),
            "三元台": self.dragons(2),
            "圈風台": 0,
            "門風台": 0,
            "花牌": 0,
            "獨聽": 0,
            "搶槓": 0,
            "槓上開花": 0,
            "半求人": 0,
            "海底撈月": 0,
            "河底撈魚": 0,
            "花槓": 0,
            "全求人": 0,
            "平胡": 0,
            "三暗刻": self.same_color_bundle(3),
            "門清自摸": 0,
            "對對胡": 0,
            "混一色": 0,
            "小三元": self.dragons(1),
            "四暗刻": self.same_color_bundle(4),
            "五暗刻": self.same_color_bundle(5),
            "清一色": 0,
            "小四喜": 0,
            "大三元": self.dragons(0),
            "七搶一": 0,
            "八仙過海": 0,
            "天聽": 0,
            "地聽": 0,
            "字一色": 0,
            "大四喜": 0,
            "地胡": 0,
            "天胡": 0,
            "人胡": 0,
            "見花見台": 0,
            "見風見台": 0,
            "槓牌": 0,
            "暗槓": 0
        }
        
    def hosthu(self):
        if self.hnum > 0:
            return 1
        else:
            return 0
            
    def selfhu(self):
        if None == self.drophu:
            return 1
        else:
            return 0
            
    def dmjclear(self):
        if 0 == len(self.dj):
            return 1
        else:
            for tv in self.dj:
                type = tv[0]
                if type != 2: # dmj type is not dark kong
                    return 0
                    
            return 1
    
    def cal_same_color(self):
        bundle_number = 0
        
        # Calculate dark kong
        for tv in self.dj:
            type = tv[0]
            if 2 == type: #dmj type is dark kong
                bundle_number += 1
        
        i = 0
        while(i+2 < len(self.fmj)):
            if self.fmj[i] == self.fmj[i+1] == self.fmj[i+2]:
                i += 3
                bundle_number += 1
                continue
            i += 1
                
        return bundle_number
        
    def same_color_bundle(self, n):
        if n == self.cal_same_color():
            if 3 == n:
                return 2
            elif 4 == n:
                return 5
            elif 5 == n:
                return 8
            else:
                return 0
        else:
            return 0
            
    def cal_dragons(self):
        dpair = 0
        dseq = 0
        
        for tv in self.dj:
            t = tv[0]
            v = tv[1][0]
            if 1 == t or 2 == t or 3 == t:
                if 31 == v or 32 == v or 33 == v:
                    dseq += 1
                    
        i = 0
        while i+1 < len(self.fmj):
            if i+2 < len(self.fmj):
                if self.fmj[i] == self.fmj[i+1] == self.fmj[i+2] and (31 == self.fmj[i] or 32 == self.fmj[i] or 33 == self.fmj[i]):
                    dseq += 1
                    i += 3
                    continue
                elif self.fmj[i] == self.fmj[i+1] and (31 == self.fmj[i] or 32 == self.fmj[i] or 33 == self.fmj[i]):
                    dpair += 1
                    i += 2
                    continue
            else:
                if self.fmj[i] == self.fmj[i+1] and (31 == self.fmj[i] or 32 == self.fmj[i] or 33 == self.fmj[i]):
                    dpair += 1
                    i += 2
                    continue
            i += 1
        
        return dseq, dpair
        
    # t = 0, big dragons. t = 1, little dragons. t = 2, dragons.
    def dragons(self, t):
        dseq, dpair = self.cal_dragons()
        if 0 == t:
            if 3 == dseq:
                return 1
            else:
                return 0
        elif 1 == t:
            if 2 == dseq and 1 == dpair:
                return 1
            else:
                return 0
        elif 2 == t:
            if 1 == dseq:
                return 1
            elif 2 == dseq and 0 == dpair:
                return 2
            else:
                return 0