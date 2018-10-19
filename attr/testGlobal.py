class global_var():
    mydict=['mm', 'qq']

    @classmethod
    def setdict(cls,dict):
        global_var.mydict=dict

    @classmethod
    def getdict(cls):
        return global_var.mydict

# if __name__== '__main__':
#     print(getdict())
#     setdict(['kk','qq'])
#     print(getdict())