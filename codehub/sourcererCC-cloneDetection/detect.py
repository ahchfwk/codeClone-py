import os
import MySQLdb
import PairToClass

def getPathFromId(release_id):
    dbconn = MySQLdb.connect('10.141.221.73', 'root', 'root', 'codehub')
    dbcursor = dbconn.cursor()
    sql = "select local_addr from releases where id=%s" % release_id
    dbcursor.execute(sql)
    result = dbcursor.fetchone()
    path = "/home/fdse/data/releases"+str(release_id/10000+1)+"_unzip"+result[0][8:-4]
    dbcursor.close()
    dbconn.close()
    return path


def detect(dirPath):
    # return (location, cloneGroup)
    os.popen("cp -rf "+dirPath+" /home/fdse/fwk/SourcererCC/clone-detector/input/dataset/")
    os.popen("./SourCC.sh")
    locate = []
    with open("input/bookkeping/headers.file", "r") as f:
        for i in f.readlines():
            headers = i.strip().split(",")
            locate.append(dirPath + headers[1][71:]+","+headers[2]+","+headers[3])
    
    result = []
    with open("output9.0/tokensclones_index_WITH_FILTER.txt", "r") as g:
        data = []
        for i in g.readlines():
            data.append(set(i.strip().split(",")))
        PairToClass.pairToGroup(data, result)
        print data
    result = [list(x) for x in result]
    return locate, result


if __name__ == "__main__":
    print detect(getPathFromId(1))