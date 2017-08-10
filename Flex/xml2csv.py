import re

file_xml = open("Teststand_201706271014.xml")
rawfile_string = file_xml.readlines()
file_string = "".join(rawfile_string)
#file_string = '''<GROUP NAME="TestInit" STEPGROUP="Main" GROUPINDEX="1" LOOPINDEX="-1" TYPE="PassFailTest" RESOURCE="" MODULETIME="0.033384" TOTALTIME="0.033444" TIMESTAMP="2015-06-11T09:30:33.475+08:00" STATUS="Passed">'''
print(file_string)
print("\n")

#m = re.findall(r'(?=<\<GROUP NAME=\").*?', file_string)
#m = re.findall(r'G.*?N', file_string)
#m = re.findall(r'(?<=<GROUP\sNAME=").*?(?="\s.*?TOTALTIME)', file_string)

m_list = re.findall(r'<GROUP\sNAME=".*?>', file_string)
#m = re.findall(r'(?<=TOTALTIME=").*', file_string)
all_the_text = ""

for m in m_list:
    m1 = re.findall(r'(?<=<GROUP\sNAME=").*?(?=")', m) #Why re.match cannot found anything
    m2 = re.findall(r'(?<=TOTALTIME=").*?(?=")', m)
#    string_result = m1 + "," + m2 + "\n"
    print(m1[0] + ","+ m2[0])
    all_the_text += m1[0] + ","+ m2[0] + "\n"
    
file_object = open('result.csv', 'w')
file_object.write(all_the_text)
file_object.close()
