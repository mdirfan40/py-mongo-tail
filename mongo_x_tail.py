from mongo_tail import MongoTail


class MongoXTail(MongoTail):

    MONGOURL = 'mongodb://localhost:27017'


    def all(self, doc):
        pass

    def update(self, doc):
        print(doc, 'u')

    def insert(self, doc):
        print(doc, 'i')

    def delete(self, doc):
        print(doc, 'd')


#
# def sendmsg(msg):
#     try:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     except socket.error as msg:
#         sys.stderr.write("[ERROR] %s\n" % msg[1])
#         sys.exit(1)
#
#     try:
#         sock.connect((HOST, PORT))
#     except socket.error as msg:
#         sys.stderr.write("[ERROR] %s\n" % msg[1])
#         sys.exit(2)
#
#     sock.send(str(json.dumps(msg)).encode('utf-8'))
#
#     sock.close()


if __name__ == "__main__":

    tail = MongoXTail()
    tail.start(tail.all, tail.update, tail.insert, tail.delete)
