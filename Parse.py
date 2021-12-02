import json
import re
class Parse:
        def Parse(GMcourses):
            GMcourses.pop(0)
            teacher = "TBA"
            crn=-9999
            startTime = "TBA"
            endTime = "TBA"
            days = "none"
            courseCode = "NONE 0000"
            teacherRating = 3.8

            #Split string by double empty lines
            splitGMcourses = []
            temp = []

            for line in range(len(GMcourses)-1):
                temp.append(GMcourses[line])
                if (GMcourses[line] == "\n" and GMcourses[line+1]=="\n") \
                    or (GMcourses[line] == "" and GMcourses[line+1]==""):
                    splitGMcourses.append(temp)
                    temp=[]

            #add split courses to txt
            file2 = open('/Users/aldo/PycharmProjects/scriptGM/SplitClasses.txt', 'w')
            for course in splitGMcourses:
                for line in course:
                    file2.write(line)
                file2.write('////////////////////////////////////')
            print(len(splitGMcourses))
            print()

            #turn string to object
            file = open('/Users/aldo/PycharmProjects/scriptGM/Parsed.txt', 'w')
            listjsonObjects = []
            for course in splitGMcourses:
                if len(course)>2:
                    i=0
                    usefulLine=""
                    while usefulLine == "" or usefulLine =="\n":
                        usefulLine=course[i]
                        i+=1
                    i=0

                    print(usefulLine)
                    # find crn and courseCode
                    x = re.findall("[0-9]{5}", usefulLine)
                    crn = x[0]
                    print(crn)
                    y = re.findall("[A-Z]{1,4}\s[A-Z0-9]{3,5}", usefulLine)
                    courseCode = y[0]
                    print(courseCode)


                    #find teacher
                    i=0
                    while '(P)' not in course[i]:
                        i+=1
                        if i==len(course):
                            teacher ="TBA"
                            break
                    if i!=len(course):
                        x = re.findall(":[a-zA-Z\s\-]+", course[i])
                        teacher=x[0][2:]
                    print(teacher)

                    #find times
                    i = 0
                    while ' am ' not in course[i] and ' pm ' not in course[i]:
                        i += 1
                        if i == len(course):
                            startTime = "TBA"
                            endTime = "TBA"
                            print('no times')
                            break
                    if i != len(course):
                        print('times found')
                        print(course[i])
                        x = re.findall("[0-9]+[0-9\:\-\sa-z]{17,19}", course[i])
                        startTime = x[0].split('-')[0]
                        endTime = x[0].split('-')[1]
                    print(startTime)
                    print(endTime)

                    #Find Days
                    i = 0
                    while 'Class' not in course[i] or i<10:
                        i += 1
                        if i == len(course):
                            days = "TBA"
                            break
                    if i != len(course):
                        print('days found')
                        print(course[i])
                        x = re.findall("\s[MTWRFSU]{0,7}\s", course[i])
                        days = x[0]
                    print(days)

                    print('building object-')
                    temp = {
                        "teacher": teacher,
                        "crn": crn,
                        "courseCode": courseCode,
                        "days": days,
                        "startTime": startTime,
                        "endTime": endTime,
                        "teacherRating" : teacherRating
                        }
                    jsonObject = json.dumps(temp)
                    listjsonObjects.append(jsonObject)
                    file.write(jsonObject)
                    file.write('\n')
                    print(jsonObject)
                    print()
            return listjsonObjects

#Turn HTML TO JSON strings and put on txt file
file = open('/Users/aldo/PycharmProjects/scriptGM/HTML_no-tags.txt','r')
HTML_no_tags = file.readlines()
print('DONE reading HTML no tags')
parsed= Parse.Parse(HTML_no_tags)
file.close()
print('DONE JSON txt file')
