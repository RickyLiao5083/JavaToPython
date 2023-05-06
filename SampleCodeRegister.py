import Register

if __name__ == '__main__':
    memberId = "Ricky1120506"
    memberName = "廖威騏"
    pwd = "abc0123456"
    idNo = "A112233449"
    checkPwd = "abc0123456"
    newMember = Register(memberId, memberName, pwd, idNo, checkPwd)
    newMember.newMember()
