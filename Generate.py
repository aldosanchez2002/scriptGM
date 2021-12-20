import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#THIS GETS THE BEST SCHEDULE AFTER GOLDMINE AND RATE MY PROFESSOR HAVE BEEN SCRAPED
#IT TAKES ABOUT 90 MINUTES TO RUN AND IT IS NOT IN USE

#NOT IN USE BECAUSE IT WAS MOVED TO JAVASCRIPT

class Generate:

    def makeListOptions(self,ccList):
        # make list of lists of options from list of course codes using goldmine data text file (no rmp data)
        # returns a list of lists of OBJECTS for all crns that belong to one of the course codes inputted
        # returns empty list if there is an invalid course code input
        # EXAMPLE INPUT:
        #   ["MATH 2300","CS 2302"]
        # EXAMPLE OUTPUT:
        # {""teacher": "Julio Cesar Urenda ", "crn": "20967", "courseCode": "MATH 2300", "days": " MW ", "startTime": "1:30 pm ", "endTime": " 2:50 pm ", "teacherRating": 3.8",
        #   ""teacher": "Julio Cesar Urenda ", "crn": "24594", "courseCode": "MATH 2300", "days": " TR ", "startTime": "12:00 pm ", "endTime": " 1:20 pm ", "teacherRating": 3.8",
        #   ""teacher": "Emil Schwab ", "crn": "20968", "courseCode": "MATH 2300", "days": "  ", "startTime": "TBA", "endTime": "TBA", "teacherRating": 3.8",
        #   ""teacher": "Angel Fernando Garcia Contreras ", "crn": "21736", "courseCode": "CS 2302", "days": " MW ", "startTime": "1:30 pm ", "endTime": " 2:50 pm ", "teacherRating": 3.8",
        #   ""teacher": "Olac Fuentes ", "crn": "25686", "courseCode": "CS 2302", "days": " TR ", "startTime": "12:00 pm ", "endTime": " 1:20 pm ", "teacherRating": 3.8",
        #   ""teacher": "Olac Fuentes ", "crn": "27090", "courseCode": "CS 2302", "days": " TR ", "startTime": "1:30 pm ", "endTime": " 2:50 pm ", "teacherRating": 3.8"}
        if len(ccList)<1:
            print('invalid')
            return []
        GM = open('/Users/aldo/PycharmProjects/scriptGM/Parsed.txt', 'r')
        courses = GM.readlines()
        possibleCrns=[]
        for cc in ccList:
            temp = []
            found = False
            for course in courses:
                if cc in course.split("\""):
                    found=True
                    try:
                        temp.append(json.loads(course))
                    except:
                        print('failed to load')
                        print(course)
                        temp.append(json.loads(course))

            possibleCrns.append(temp)
            if not found:
                print('invalid course: '+str(cc))
                return []
        return possibleCrns

    def sortByNumOptions(self, allOptions):
        # sort list by amount of options for each course
        # Example input:
        #   [['A1','A2','A3','A4'],['B1','B2'],['C1']]
        # Example output:
        #   [['C1'],['B1','B2'],['A1','A2','A3','A4']]
        newList = []
        numofcourses=len(allOptions)
        while len(allOptions)>0:
            temparr=[]
            for y in range(len(allOptions)):
                if len(allOptions[y])>len(temparr):
                    temparr=allOptions[y]
            newList.append(temparr)
            allOptions.remove(temparr)
        return newList

    def addRMPData (self,sOptions):
        #  add rmp data to each course in sorted list of lists of Objects using selenium

        #dictionary to speed up lookup
        seenteachers={'teacher':'2.8'}
        newList=[]
        for course in sOptions:
            subject=[]
            for option in course:
                t = option['teacher']
                if t in seenteachers:
                    teacherRating = seenteachers[t]
                elif t == 'TBA':
                    teacherRating=3.8
                else:
                    #build url from teacher name
                    splitTeacherName = t.split(" ")
                    splitTeacherName.pop(len(splitTeacherName) - 1)

                    url = 'https://www.ratemyprofessors.com/search/teachers?query='
                    for part in range(len(splitTeacherName)):
                        url += splitTeacherName[part] + '%20'
                    url = url[:-3]
                    url += '&sid=U2Nob29sLTQwNTg='
                    print(url)
                    # Get score via safari webdriver
                    driver = webdriver.Safari()
                    driver.minimize_window()
                    driver.get(url)

                    # Accept Cookies if popup
                    try:
                        driver.find_element(By.XPATH, '/ html / body / div[5] / div / div / button').click()
                        time.sleep(0.1)
                    except:
                        time.sleep(0.1)

                    # Find score via xpath
                    try:
                        Number = driver.find_element(By.XPATH,
                                                     '//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                        splitnum = Number.text.split('>')
                        teacherRating = splitnum[0]
                    except:
                        #default teacher rating if none are found (utep average)
                        teacherRating=3.8
                    driver.close()
                    seenteachers[t]=teacherRating
                print(teacherRating)
                option['teacherRating']=teacherRating
                subject.append(option)
            newList.append(subject)
        return newList

    def getValidCombinations(self,list):
        #goes through list of courses and returns a list of lists of objects that make us a valid combination
        # a valid combination of coruses contains one of each type where no course times overlap
        # Example input:f
        #   [[A1,A2,A3,A4],[B1,B2],[C1]]
        # Example output:
        #   [[A1,B1,C1],[A1,B2,C1],[A2,B2,C1]]
        temp=[]
        validCombos = []
        for c in list[0]:
            a=[]
            a.append(c)
            validCombos.append(a)

        for x in range(1,len(list)):
            for course in list[x]:
                for combo   in validCombos:
                    a = Generate.noOverlapHelper(Generate,course,combo)
                    if len(a)>0:
                        temp.append(a)
            validCombos = temp
            temp = []
        print('Number of Valid Combinations: '+str(len(validCombos)))
        return validCombos

    def noOverlapHelper(self,course,combo):
        #this is a helper method for getValidCombinations
        #this returns an array of courses if they dont overlap
        #returns [] is there is overlap (not viable)
        # Example 1 input:  (B1,[A1])
        # Example 1 output: [A1,B1]

        # Example 2 input:  (C1,[B1,A1])
        # Example 2 output: [A1,B1,C1]

        for crn in combo:
            if 'TBA' not in str(course['days']) and 'TBA' not in str(course['days']):
                usedDays = crn['days'].split()
                newDays= course['days'].split()
                for day in newDays:
                    if day!="" and day in usedDays:
                        usedstart = int(crn['startTime'].split(":")[0])*100+int(crn['startTime'].split(":")[1][:2])
                        if usedstart!=1200 and 'pm' in crn['startTime'].split(" "):
                            usedstart += 1200

                        usedend = int(crn['endTime'].split(":")[0])*100+int(crn['endTime'].split(":")[1][:2])
                        if usedend!=1200 and 'pm' in crn['endTime'].split(" ")[2]:
                            usedend+=1200

                        newstart = int(course['startTime'].split(":")[0])*100+int(course['startTime'].split(":")[1][:2])
                        if newstart!=1200 and 'pm' in course['startTime'].split(" "):
                            newstart += 1200

                        newend = int(course['endTime'].split(":")[0])*100+int(course['endTime'].split(":")[1][:2])
                        if newend!=1200 and 'pm' in course['endTime'].split(" "):
                            newend += 1200

                        if(newstart <= usedstart and newend>usedstart)or(newstart<usedend and newend<=usedend):
                            return []
        temp=[]
        for c in combo:
            temp.append(c)
        temp.append(course)
        return temp

    def RMPSort(self,list):
        #Sorts list of viable options from best RMP score to worst via bubblesort
        #Example input:
        #   [[A1,B1,C1],[A1,B2,C1],[A2,B2,C1],[A3,B3,C2]]
        # Example output:
        #   [[A2,B2,C1],[A3,B3,C2],[A1,B1,C1],[A1,B2,C1]]
        print(len(list))
        scores=[]
        for x in range(len(list)):
            temp=0.0
            for crn in list[x]:
                temp+=float(crn['teacherRating'])
            scores.append(temp)
        endPos=len(scores)
        curPos=0
        while endPos!=0:
            while curPos < endPos:
                if curPos<len(list)-1 and scores[curPos]<scores[curPos+1]:
                    temp=scores[curPos]
                    scores[curPos]=scores[curPos+1]
                    scores[curPos+1]=temp

                    temp2=list[curPos]
                    list[curPos]=list[curPos+1]
                    list[curPos+1]=temp2
                curPos+=1
            endPos-=1
            curPos=0
        print('THE BEST OPTION IS')
        for a in list[0]:
            print(a)
        print('RMP SCORES:')
        print(scores)
        return list


if __name__ == "__main__":
    courseList=['MATH 3323','CS 2302','EE 2369','EE 2169'] # example list
    options = Generate.makeListOptions(Generate,courseList)
    if len(options) > 0:
        sortedOptions = Generate.sortByNumOptions(Generate,options)
        sortedOptionsWithRMP = Generate.addRMPData(Generate,sortedOptions)
        validCombinations = Generate.getValidCombinations(Generate,sortedOptionsWithRMP)
        final = Generate.RMPSort(Generate,validCombinations)
        a=""
        index=1
        while(a!='done'):
            a= input('type \'next\' for next best option or \'done\'')
            if a == 'next':
                if index == len(final):
                    print('no more viable options')
                    a='done'
                else:
                    print('OPTION: ' + str(index+1)+' IS')
                    for a in final[index]:
                        print(a)
                    index+=1


