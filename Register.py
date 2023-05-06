import Members

class Register(Members):
    def __init__(self, memberId, memberName, pwd, idNo, checkPwd):
        super().__init__(memberId, memberName, pwd, idNo)
        self.memberId = memberId
        self.memberName = memberName
        self.pwd = pwd
        self.idNo = idNo
        self.checkPwd = checkPwd
    
    
    
    def newMember(self):
        if self.isThisMemberIdNotUsed(self.memberId) and str(self.isPwdValid()) == "" \
            and str(self.isIdNumberValid()) == "" and str(self.checkPwd()) == "":
            newMember = Members(self.memberId, self.memberName, self.pwd, self.idNo)
            newMember.registerMember()
            return "註冊成功"
        else:
            return "註冊失敗"
    
    def isIdNumberValid(self):
        if len(self.idNo) != 10:
            return "身分證字號格式錯誤!"
        else:
            return ""
    
    def isPwdValid(self):
        if len(self.pwd) > 32:
            return "超過密碼長度限制"
        elif len(self.pwd) < 8:
            return "密碼長度不足"
        else:
            if " " in self.pwd:
                return "密碼不可含有空白字元!"
            else:
                return ""
    
    def pwdCheck(self):
        if str(self.pwd) == str(self.checkPwd):
            return ""
        else:
            return "密碼有誤"
        
    @property
    def memberId(self):
        return self.__memberId
    
    @memberId.setter
    def memberId(self, memberId):
        self.__memberId = memberId
    
    @property
    def memberName(self):
        return self.__memberName
    
    @memberName.setter
    def memberName(self, memberName):
        self.__memberName = memberName
    
    @property
    def pwd(self):
        return self.__pwd
    
    @pwd.setter
    def pwd(self, pwd):
        self.__pwd = pwd
    
    @property
    def idNo(self):
        return self.__idNo
    
    @idNo.setter
    def idNo(self, idNo):
        self.__idNo = idNo
    
    @property
    def checkPwd(self):
        return self.__checkPwd
    
    @checkPwd.setter
    def checkPwd(self, checkPwd):
        self.__checkPwd = checkPwd
    