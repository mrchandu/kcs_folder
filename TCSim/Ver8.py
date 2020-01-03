exe_list = []
for root, dirs, files in os.walk("."):
 #print (dirs)
 for j in dirs:
  for i in files:
   if i.endswith('.exe'):
     #p=os.getcwd()+'/'+j+'/'+i
     p=root+'/'+j+'/'+i
     #print(p)
     exe_list.append(p)