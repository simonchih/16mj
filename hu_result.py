class hu_result():
    def __init__(self, mj, dmj, hnum, first_turn, hmj, getmj = None, first_hear = 0, drophu = None, hhu = False):
        self.mj = mj
        self.dj = dmj
        self.hnum = hnum
        self.ft = first_turn
        self.hj = hmj
        self.gethu = getmj
        self.first_hear = first_hear
        self.drophu = drophu
        self.hhu = hhu
        self.table = {
            "莊家": 0,
            ("連%d拉%d" % (hnum, hnum)): 0,
            "自摸": 0,
            "門清": 0,
            "三元台": 0,
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
            "三暗刻": 0,
            "門清自摸": 0,
            "對對胡": 0,
            "混一色": 0,
            "小三元": 0,
            "四暗刻": 0,
            "五暗刻": 0,
            "清一色": 0,
            "小四喜": 0,
            "大三元": 0,
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