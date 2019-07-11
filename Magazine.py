import os
import csv

##################-Skrypt do odczytywania wszystkich plików w folderze i zapisywania ich w jednym pliku-##############

files = os.listdir(r'C:\Users\DELL\Desktop\Big_Data\Movies_review\aclImdb\train\neg')
Database = []
for file in files:
    if file.endswith('.txt'):

        with open(r'C:\Users\DELL\Desktop\Big_Data\Movies_review\aclImdb\train\neg/'+ file,'r', encoding="utf8") as afile:
            data = afile.read()
            Database.append(data)
print("----------------First_part_done--------------")
with open ('neg_rev.csv', 'a+', encoding="utf8") as neg_rev:
    wr = csv.writer(neg_rev, delimiter = "^", quoting=csv.QUOTE_ALL)
    wr.writerow(Database)
print("-----------------Done----------------")

files = os.listdir(r'C:\Users\DELL\Desktop\Big_Data\Movies_review\aclImdb\train\pos')
Database = []
for file in files:
    if file.endswith('.txt'):

        with open(r'C:\Users\DELL\Desktop\Big_Data\Movies_review\aclImdb\train\pos/'+ file,'r', encoding="utf8") as afile:
            data = afile.read()
            Database.append(data)
print("----------------First_part_done--------------")
with open ('pos_rev.csv', 'a+', encoding="utf8") as pos_rev:
    wr = csv.writer(pos_rev, delimiter = "^", quoting=csv.QUOTE_ALL)
    wr.writerow(Database)
print("-----------------Done----------------")

#############################-Skrypt to testowania skryptu mierzenia sentymentu-####################################

print("-----------Go to Hell----------------")
start = time.time()
csv.field_size_limit(100000000)
stop_words = stopwords.words('english')
print("---Starting-poz---------")
print(start-time.time())
pos_count = 0
pos_correct = 0
data = pd.read_csv(r"pos_rev.csv", engine='python', quotechar='"', sep="^", error_bad_lines=False, quoting=csv.QUOTE_NONE)
demodata = [0]
num= 0
print("---------Anal------")
print(start-time.time())
'''for x in data:
    print("Number before stopwords")
    print(len(x))
for x in data:
    y = [word for word in x if word not in stop_words]
    print("Number after stopwords")
    print(len(y))'''
for x in data:
    #y = [word for word in x if word not in stop_words]
    if num <= 10:
        demodata.append(str(x))
        num+=1

print("---------Anal2------")
print(start-time.time())

for rev in demodata:
    analysis = TextBlob(str(rev))
    if analysis.sentiment.polarity > 0.1:
        print("Sentyment pozytyw")
        print(analysis.sentiment.polarity)
        pos_correct += 1
    pos_count += 1
print("---Ending-poz---------")
print("---Starting-neg---------")
print(start-time.time())

neg_count = 0
neg_correct = 0
data = pd.read_csv(r"neg_rev.csv", engine='python', quotechar='"', sep="^", error_bad_lines=False, quoting=csv.QUOTE_NONE)
demodata = [0]
num= 0
print("---------Anal------")
print(start-time.time())
for x in data:
    #y = [word for word in x if word not in stop_words]
    if num <= 10:
        demodata.append(str(x))
        num+=1
print("---------Anal2------")
print(start-time.time())

for rev in demodata:
    analysis = TextBlob(str(rev))
    print(analysis)
    if analysis.sentiment.polarity <=0:
        print("Sentyment negatyw")
        print(analysis.sentiment.polarity)
        neg_correct += 1
    neg_count += 1
print("---Ending-neg---------")
print(start-time.time())

print("Positive accuracy = {}% via {} samples".format(pos_correct/pos_count*100.0, pos_count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/neg_count*100.0, neg_count))



#######################################-Skrypt do mierzenia sentymentu-###########################################

print("-----------Go to Hell----------------")
start = time.time()
csv.field_size_limit(100000000)
stop_words = stopwords.words('english')
count = 0
pos_correct = 0
neg_correct = 0


print("---Starting-poz---------")
print(start-time.time())

data = pd.read_csv(r"pos_rev.csv", engine='python', quotechar='"', sep="^", error_bad_lines=False, quoting=csv.QUOTE_NONE)
demodata = [0]
num = 0

print("---------Anal------")
print(start-time.time())

for x in data:
    #y = [word for word in x if word not in stop_words]
    if num <= 10:
        demodata.append(str(x))
        num+=1

print("---------Anal2------")
print(start-time.time())

for rev in demodata:
    analysis = TextBlob(str(rev))
    if analysis.sentiment.polarity > 0.1:
        print("Sentyment pozytyw")
        print(analysis.sentiment.polarity)
        pos_correct += 1
    if analysis.sentiment.polarity <=0:
        print("Sentyment negatyw")
        print(analysis.sentiment.polarity)
        neg_correct += 1
    count += 1

print("---Ending-poz---------")
print("---Starting-neg---------")
print(start-time.time())

print("Positive accuracy = {}% via {} samples".format(pos_correct/count*100.0, count))
print("Negative accuracy = {}% via {} samples".format(neg_correct/count*100.0, count))
