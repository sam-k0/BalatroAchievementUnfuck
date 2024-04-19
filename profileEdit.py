import os
import zlib 
def GetCurrentDirectory():
    return os.getcwd()

def ReadBinary(path):
    with open(path, "rb") as f:
        data = f.read()
        return data

def ReadText(path):
    with open(path, "r") as f:
        data = f.read()
        return data

def Decompress(bindata):
    return zlib.decompress(bindata, wbits=-zlib.MAX_WBITS)

def Compress(save_file_data):
        return zlib.compress(save_file_data, level=1, wbits=-zlib.MAX_WBITS)


def GetLocalDirectory(dirname):
    GetCurrentDirectory() + os.sep + dirname



def dump(fpath):
    text = str(Decompress(ReadBinary(fpath)), encoding='ascii')
    # save this to a file
    with open(GetCurrentDirectory()+os.sep+"dumped" +os.sep+ "dumped.txt", "w") as f:
        f.write(text)

def recompress(fpath): # reads a dumped file and recompresses it
    text = ReadText(fpath)
    savdata = Compress(bytes(text, encoding='ascii'))
    savepath = GetCurrentDirectory()+os.sep+"output"+os.sep+"profile.jkr"
    with open(savepath, "wb") as f:
        f.write(savdata)
    return savepath

if __name__ == "__main__":
    exit()
    #dump("profile.jkr")
    #recompress("profile.txt")