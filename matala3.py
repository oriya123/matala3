import json
def reader():
    file= open("bonos.txt",encoding="utf8")
    dict1(file)
        
def dict1(file) :
    dict_id=dict()
    message=dict()
    teamNoya=list()
    metadata=dict()
    dictall=dict()
    count=1
    count2=0
    count3=0
    for line in file:
        index = line.find('-')
        if (line[1]=="." or line[2]=="."):
                result = line[index+1::] 
                index2 = result.find(':')
                if(index2>0):
                    name= result[0:index2]
                    if not dict_id.get(name):   
                        dict_id[name]=count
                        count=count+1
                    message['datetime']=line[0:index-1]
                    message['id']=dict_id[name]
                    message['text']=result[index2+1::].strip()
                    teamNoya.append(message.copy())  
        else:
                teamNoya.pop()
                message['text']=(message['text']+" "+line).strip()
                teamNoya.append(message.copy())  
        count2=count2+1
        if(count2==1):
            creationdate=line[0:index-1]
        if(count2==2):
            team=line.index("הקבוצה")
            team1=line.index("נוצרה")
            chat_name=line[team+8:team1-2]
            creator=line[team1+13::].strip()
    num_of_participants=len(dict_id)
    metadata["chat_name:"]=chat_name
    metadata["creationdate:"]=creationdate
    metadata["num_of_participants:"]=num_of_participants
    metadata["creator:"]=creator
    dictall["messages"]=teamNoya
    dictall["metadata"]=metadata
    jsonfile=chat_name+".txt"
    with open (jsonfile,'w',encoding='utf8') as jsonfile:
        json.dump(dictall,jsonfile,ensure_ascii=False,indent=4)

reader()
