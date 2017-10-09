import os
import bz2

def split_xml(filename):
    ''' The function gets the filename of wiktionary.xml.bz2 file as  input and creates
    smallers chunks of it in a the diretory chunks
    '''
    # Check and create chunk diretory
    if not os.path.exists("chunks"):
        os.mkdir("chunks")
    # Counters
    pagecount = 0
    filecount = 1
    #open chunkfile in write mode
    chunkname = lambda filecount: os.path.join("chunks","chunk-"+str(filecount)+".xml.bz2")
    chunkfile = bz2.BZ2File(chunkname(filecount), 'w')
    chunkfile.write("<mediawiki>\n")    
    # Read line by line
    bzfile = bz2.BZ2File(filename)
    for _ in xrange(1):
        next(bzfile)
    for line in bzfile:
        chunkfile.write(line)
        # the </page> determines new wiki page
        if '</page>' in line:
            pagecount += 1
            if pagecount % 5000 == 0:
                print pagecount
        if pagecount > 199999:
            #print chunkname() # For Debugging
            chunkfile.write("</mediawiki>")
            chunkfile.close()
            pagecount = 0 # RESET pagecount
            filecount += 1 # increment filename           
            chunkfile = bz2.BZ2File(chunkname(filecount), 'w')
            chunkfile.write("<mediawiki>\n")

    try:
        chunkfile.close()
    except:
        print 'Files already close'

if __name__ == '__main__':
    # When the script is self run
    split_xml('enwiki-20170820-pages-articles.xml.bz2')