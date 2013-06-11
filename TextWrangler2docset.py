import sqlite3 as lite
import glob
import os
import subprocess
from bs4 import BeautifulSoup
import shutil

base_path = os.path.dirname(os.path.abspath(__file__))+'/TextWrangler2docset.docset/Contents/Resources'

source_dir = '/Applications/TextWrangler.app/Contents/Resources/TextWrangler Help/'

doc_path =  base_path+'Documents/'
db_path  =  base_path+'/docSet.dsidx'

shutil.rmtree(doc_path)

shutil.copytree(source_dir, doc_path) 

deletelist =[ "grep.htm","searching.htm","index.htm"]
for f in deletelist:
    os.remove(doc_path+f)


# 2 directory level down listed
filelist = glob.glob(doc_path+'*.htm*')+glob.glob(doc_path+'*/*.htm*')
 
# print filelist

#connect to the sqlite db
con = lite.connect(db_path)
cur = con.cursor()    
#erase all
cur.execute('DELETE FROM searchIndex')

#insert the file in the filelist and beautify the html file
for file in filelist:
    print '--------------------------------------------------------'
    print 'FILENAME : '+file
    #set the name for the DB
    filename_ext = file[len(doc_path):]
    name = os.path.split(file)[1].split('.')[0]
    # if the file exist (in else we delete some file,hence possibly modifying the list)
    if os.path.exists(file):
        #get the soup ready...
        soup = BeautifulSoup(open(file))
        # if there are no <frame> then...
        if len(soup.findAll('frame')) == 0 :
            title = soup.title.string
#             print "Title : "+title.title(),"  |  Filename  : "+name+' Filename_ext : '+filename_ext
            cur.execute("INSERT INTO searchIndex (path,type,name) VALUES (?,'Guide',?)",(filename_ext,name))
            print('Insert in DB : ',filename_ext,name)
        else :
            # if there are <frame> delete the file and the first frame reference
            frame_file = str(soup.frame['src'])
#             print " >>>  Found <frame> : "+os.path.split(frame_file)[1]
            os.remove(file)
            try:
                os.remove(doc_path+frame_file)
            except OSError:
                 print " >>>  Nested  <frame> src deleted : "+os.path.split(frame_file)[1]
  
#commit the DB changes
con.commit()


# add the tabel of contents
b = os.system('sh table_of_contents.sh')

b = os.system("tar --exclude='.DS_Store' -czf TextWrangler2docset.tgz TextWrangler2docset.docset")
print 'compress to '+os.path.dirname(os.path.abspath(__file__))+'/TextWrangler2docset.tgz'
