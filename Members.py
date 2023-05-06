import pymssql

class Members:
    conn = pymssql.connect(
        host = '127.0.0.1\\SQLEXPRESS',
        user = 'sa',
        password = 'b075050',
        database = 'Travel')
    def __init__(self, *args):
        
        
        if len(args) == 4:
            self.memberId = args[0]     #memberId
            self.memberName = args[1]   #memberName
            self.pwd = args[2]          #pwd
            self.idNo = args[3]         #idNo
        else:
            cursor = self.conn.cursor()
            cursor.execute("SELECT member_id, member_name, pwd, id_no from member_data " +
                              "where member_id='" + str(args[0]) + "';")
            
            row = cursor.fetchone()
            
            while row:
                self.memberId = str(row[0])     #memberId
                self.memberName = str(row[1])
                self.pwd = str(row[2])
                self.idNo = str(row[3])
                row = cursor.fetchone()
    
    @staticmethod
    def isThisMemberIdNotUsed(memberId):
        check = True
        cursor = Members.conn.cursor()
        cursor.execute("SELECT member_id, member_name, pwd, id_no from member_data " +
                          "where member_id='" + str(memberId) + "';")
        
        row = cursor.fetchone()
        
        while row:
            check = (memberId != str(row[0]))
            row = cursor.fetchone()
        
        return check
    
    def registerMember(self):
        cursor = Members.conn.cursor()
        cursor.execute("INSERT INTO member_data (member_id, member_name, pwd, id_no) " +
                       "VALUES ('" + str(self.memberId) + "', " + "'" + str(self.memberName) + "', " + "'" + str(self.pwd) + "', " + "'" + str(self.idNo) + "');")
        Members.conn.commit()
        Members.conn.close()
    
    @staticmethod
    def UpdatePwd(memberId, newPwd):
        cursor = Members.conn.cursor()
        cursor.execute("UPDATE member_data " +
                       "SET pwd='" + str(newPwd) + "' " +
                       "where member_id='" + str(memberId) + "';")
        Members.conn.commit()
        Members.conn.close()
    
    @property
    def memberId(self):
        return self.__memberId
    
    @property
    def memberName(self):
        return self.__memberName
    
    @property
    def pwd(self):
        return self.__pwd
    
    @pwd.setter
    def pwd(self, pwd):
        self.__pwd = pwd
    
    @property
    def idNo(self):
        return self.__idNo
    