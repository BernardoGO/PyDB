__author__ = 'Bernardo'




class general:
    def func():
        print ("here")

    def writePage(self, pageId):
        file_ = open(str(pageId) + 'page.dat', 'w')
        file_.write('whatever')
        file_.close()