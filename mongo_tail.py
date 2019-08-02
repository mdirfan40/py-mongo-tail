import time
import json
import sys
import pymongo
import socket
from pymongo.errors import AutoReconnect


class MongoTail(object):
    MONGOURL = ''
    def __init__(self):

        if not self.MONGOURL:
            raise Exception('Database url should not empty.')

        print(self.MONGOURL)
        client = pymongo.MongoClient(self.MONGOURL)
        self.oplog = client.local.oplog.rs
        self.last_ts = self.oplog.find().sort('$natural', -1)[0]['ts']

    def start(self, all, update, insert, delete):
        while True:

            print("Runnig ..")

            # For a regular capped collection CursorType.TAILABLE_AWAIT is the
            # only option required to create a tailable cursor. When querying the
            # oplog the oplog_replay option enables an optimization to quickly
            # find the 'ts' value we're looking for. The oplog_replay option
            # can only be used when querying the oplog.

            try:
                cursor = self.oplog.find({'ts': {'$gt': self.last_ts}, 'op': {
                    '$in': ['i', 'u', 'd']
                }},
                                         cursor_type=pymongo.CursorType.TAILABLE_AWAIT,
                                         oplog_replay=True)

                try:

                    while cursor.alive:
                        try:
                            # grab a document if available
                            doc = cursor.next()

                            all(doc)

                            if doc["op"] == "u":
                                update(doc)

                            if doc["op"] == "i":
                                insert(doc)

                            if doc["op"] == "d":
                                delete(doc)

                            # do something interesting with "doc"

                        except StopIteration:
                            # thrown when the cursor is out of data, so wait
                            # for a period for some more data
                            time.sleep(2)
                finally:
                    cursor.close()

            except AutoReconnect:
                print("Try to reconnect...")

    def all(self):
        pass

    def update(self):
        pass

    def insert(self):
        pass

    def delete(self):
        pass


