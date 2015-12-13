__author__ = 'Bernardo Augusto Godinho de Oliveira - @bernardogo'

__PAGE_SIZE__ = 1024
__MAX_SIZE_SEQ__ = 64
__PAGE_SUFFIX__ = 'page.dat'

__PAGE_SIZE__ += int(__PAGE_SIZE__/__MAX_SIZE_SEQ__)


class general:
    def func(self):
        print ("here")

    def readPage(self, pageId):
        file_ = open(str(pageId) + __PAGE_SUFFIX__, 'rb')
        byt = bytearray(file_.read())
        file_.close()
        return byt

    def initPage(self, pageId):
        file_ = open(str(pageId) + __PAGE_SUFFIX__, 'wb')

        toBeWritten = bytearray([])  #'\0' *__PAGE_SIZE__
        for i in range(__PAGE_SIZE__):
            toBeWritten.append(0)

        for x in range(int(__PAGE_SIZE__/ __MAX_SIZE_SEQ__)):
            toBeWritten[x*-1 -1] = 255#ord('d')

        file_.write(toBeWritten )
        file_.close()
        print("all written")
        print(self.readPage(pageId))

    def writeValue(self, rid, bytes, pageId):
        toBeWritten = self.readPage(pageId)  #'\0' *__PAGE_SIZE__
        file_ = open(str(pageId) + __PAGE_SUFFIX__, 'wb')
        print(self.readPage(pageId))

        print(toBeWritten)
        position = 255
        for x in range(int(__PAGE_SIZE__/ __MAX_SIZE_SEQ__)):

            if toBeWritten[x*-1 -1] == 255:
                toBeWritten[x*-1-1] = rid
                position = x
                break

        for x in range(len(bytes)):
            toBeWritten[x+(position*__MAX_SIZE_SEQ__)] = ord(bytes[x])

        file_.write(toBeWritten )
        file_.close()
        print("all written")
        print(self.readPage(pageId))

    def readValue(self, rid, pageid):
        page = self.readPage(pageid)
        position = 255
        for x in range(int(__PAGE_SIZE__/ __MAX_SIZE_SEQ__)):
            if page[x*-1 -1] == rid:
                position = x
                break
        print(position)
        value = bytearray([])
        for x in range(__MAX_SIZE_SEQ__):
            value.append(page[x+(position*__MAX_SIZE_SEQ__)])
        print(value.decode("utf-8") )




    def write(self):
        self.initPage(2)
        print(self.readPage(2))
        self.writeValue(40, "test1running", 2)
        self.writeValue(41, "test2running", 2)
        self.writeValue(43, "test23running", 2)
        self.readValue(43,2)