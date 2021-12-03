import json
import requests
from lxml import html
from bs4 import BeautifulSoup

class GMPmerger:
    RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP.txt', 'w')
    GM = open('/Users/aldo/PycharmProjects/scriptGM/Parsed.txt','r')
    courses=GM.readlines()

    for course in courses:
        courseSplit=course.split('\"')
        teacher=courseSplit[3]
        crn =courseSplit[7]
        courseCode = courseSplit[11]
        days=courseSplit[15]
        startTime=courseSplit[19]
        endTime=courseSplit[23]
        teacherRating=3.8

        splitTeacherName=teacher.split(" ")
        splitTeacherName.pop(len(splitTeacherName)-1)
        print(splitTeacherName)
        url='https://www.ratemyprofessors.com/search/teachers?query='
        for part in range(len(splitTeacherName)-1):
            url += splitTeacherName[part]+'%20'
        url+=splitTeacherName[len(splitTeacherName)-1]
        url+='&sid=U2Nob29sLTQwNTg='
        print(url)

        searchResultpage = requests.get(url).text
        #print(searchResultpage)

        index = searchResultpage.find("CardName")
        if index == -1:  # find return position of string if found else -1
            print('not on RMP')
        else:
            teacherRating=searchResultpage[index+60:index+65]
            print(teacherRating)

        temp = {
            "teacher": teacher,
            "crn": crn,
            "courseCode": courseCode,
            "days": days,
            "startTime": startTime,
            "endTime": endTime,
            "teacherRating": teacherRating
        }
        jsonObject = json.dumps(temp)
        RMP.write(jsonObject)
        RMP.write('\n')




