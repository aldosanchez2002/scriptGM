import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
class RMP:
#THIS ADDS THE RATE MY PROFFESSOR DATA TO ALL OF GOLDMINE DATA
#IT TAKES ABOUT 90 MINUTES TO RUN AND IT IS NOT IN USE

#NOT IN USE

    ########## 0-1000 ###############################
    def run1(self,courses,knownScores):
        RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP1.txt', 'w')
        driver = webdriver.Safari()
        driver.minimize_window()
        for x in range(1000):
            print()
            course = courses[x]
            courseSplit=course.split('\"')
            teacher=courseSplit[3]
            crn=courseSplit[7]
            subject=courseSplit[11]
            coursenumber= courseSplit[15]
            days=courseSplit[19]
            startTime=courseSplit[23]
            endTime=courseSplit[27]
            teacherRating=0.0

            if teacher not in knownScores:
                splitTeacherName = teacher.split(" ")
                splitTeacherName.pop(len(splitTeacherName)-1)

                url='https://www.ratemyprofessors.com/search/teachers?query='
                for part in range(len(splitTeacherName)):
                    url += splitTeacherName[part]+'%20'
                url=url[:-3]
                url+='&sid=U2Nob29sLTQwNTg='
                print(url)

                # Get safari
                driver.get(url)

                #Accept Cookies
                try:
                    driver.find_element(By.XPATH,'/ html / body / div[5] / div / div / button').click()
                    time.sleep(0.1)
                except:
                    time.sleep(0.1)

                # Find score
                try:
                    Number = driver.find_element(By.XPATH,'//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                    splitnum=Number.text.split('>')
                    teacherRating = splitnum[0]
                    time.sleep(0.1)
                except:
                    teacherRating=0.0
            else:
                teacherRating = knownScores.get(teacher)
                print('found in dict')

            #Build Object
            if teacherRating==0.0 or teacherRating=='0.0':
                teacherRating=3.8

            knownScores[teacher]=teacherRating
            print(str(knownScores.get(teacher))+' '+str(teacher))


            temp = {
                "teacher": teacher,
                "crn": crn,
                "subject": subject,
                "coursenumber": coursenumber,
                "days": days,
                "startTime": startTime,
                "endTime": endTime,
                "teacherRating": teacherRating
            }
            #Add new object to ParsedWithRMP.txt
            jsonObject = json.dumps(temp)
            RMP.write(jsonObject)
            RMP.write('\n')
            print(str(x) + '/'+str(len(courses)))
        driver.close()
        return 1

    ########## 1000-2000 ###############################
    def run2(self, courses, knownScores):
        RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP2.txt', 'w')
        driver = webdriver.Safari()
        for x in range(1000,2000):
            print()
            course = courses[x]
            courseSplit = course.split('\"')
            teacher = courseSplit[3]
            crn = courseSplit[7]
            subject = courseSplit[11]
            coursenumber = courseSplit[15]
            days = courseSplit[19]
            startTime = courseSplit[23]
            endTime = courseSplit[27]
            teacherRating = 0.0

            if teacher not in knownScores:
                splitTeacherName = teacher.split(" ")
                splitTeacherName.pop(len(splitTeacherName) - 1)

                url = 'https://www.ratemyprofessors.com/search/teachers?query='
                for part in range(len(splitTeacherName)):
                    url += splitTeacherName[part] + '%20'
                url = url[:-3]
                url += '&sid=U2Nob29sLTQwNTg='
                print(url)

                # Get safari
                driver.get(url)

                # Accept Cookies
                try:
                    driver.find_element(By.XPATH, '/ html / body / div[5] / div / div / button').click()
                    time.sleep(0.1)
                except:
                    time.sleep(0.1)

                # Find score
                try:
                    Number = driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                    splitnum = Number.text.split('>')
                    teacherRating = splitnum[0]
                    time.sleep(0.1)
                except:
                    teacherRating = 0.0
            else:
                teacherRating = knownScores.get(teacher)
                print('found in dict')

            # Build Object
            if teacherRating == 0.0 or teacherRating == '0.0':
                teacherRating = 3.8

            knownScores[teacher] = teacherRating
            print(str(knownScores.get(teacher)) + ' ' + str(teacher))

            temp = {
                "teacher": teacher,
                "crn": crn,
                "subject": subject,
                "coursenumber": coursenumber,
                "days": days,
                "startTime": startTime,
                "endTime": endTime,
                "teacherRating": teacherRating
            }
            # Add new object to ParsedWithRMP.txt
            jsonObject = json.dumps(temp)
            RMP.write(jsonObject)
            RMP.write('\n')
            print(str(x) + '/' + str(len(courses)))
        driver.close()
        return 1

    ########## 2000-3000 ###############################
    def run3(self, courses, knownScores):
        RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP3.txt', 'w')
        driver = webdriver.Safari()
        for x in range(2000,3000):
            print()
            course = courses[x]
            courseSplit = course.split('\"')
            teacher = courseSplit[3]
            crn = courseSplit[7]
            subject = courseSplit[11]
            coursenumber = courseSplit[15]
            days = courseSplit[19]
            startTime = courseSplit[23]
            endTime = courseSplit[27]
            teacherRating = 0.0

            if teacher not in knownScores:
                splitTeacherName = teacher.split(" ")
                splitTeacherName.pop(len(splitTeacherName) - 1)

                url = 'https://www.ratemyprofessors.com/search/teachers?query='
                for part in range(len(splitTeacherName)):
                    url += splitTeacherName[part] + '%20'
                url = url[:-3]
                url += '&sid=U2Nob29sLTQwNTg='
                print(url)

                # Get safari
                driver.get(url)

                # Accept Cookies
                try:
                    driver.find_element(By.XPATH, '/ html / body / div[5] / div / div / button').click()
                    time.sleep(0.1)
                except:
                    time.sleep(0.1)

                # Find score
                try:
                    Number = driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                    splitnum = Number.text.split('>')
                    teacherRating = splitnum[0]
                    time.sleep(0.1)
                except:
                    teacherRating = 0.0
            else:
                teacherRating = knownScores.get(teacher)
                print('found in dict')

            # Build Object
            if teacherRating == 0.0 or teacherRating == '0.0':
                teacherRating = 3.8

            knownScores[teacher] = teacherRating
            print(str(knownScores.get(teacher)) + ' ' + str(teacher))

            temp = {
                "teacher": teacher,
                "crn": crn,
                "subject": subject,
                "coursenumber": coursenumber,
                "days": days,
                "startTime": startTime,
                "endTime": endTime,
                "teacherRating": teacherRating
            }
            # Add new object to ParsedWithRMP.txt
            jsonObject = json.dumps(temp)
            RMP.write(jsonObject)
            RMP.write('\n')
            print(str(x) + '/' + str(len(courses)))
        driver.close()
        return 1

    ########## 3000-4000 ###############################
    def run4(self, courses, knownScores):
        RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP4.txt', 'w')
        driver = webdriver.Safari()
        for x in range(3000,4000):
            print()
            course = courses[x]
            courseSplit = course.split('\"')
            teacher = courseSplit[3]
            crn = courseSplit[7]
            subject = courseSplit[11]
            coursenumber = courseSplit[15]
            days = courseSplit[19]
            startTime = courseSplit[23]
            endTime = courseSplit[27]
            teacherRating = 0.0

            if teacher not in knownScores:
                splitTeacherName = teacher.split(" ")
                splitTeacherName.pop(len(splitTeacherName) - 1)

                url = 'https://www.ratemyprofessors.com/search/teachers?query='
                for part in range(len(splitTeacherName)):
                    url += splitTeacherName[part] + '%20'
                url = url[:-3]
                url += '&sid=U2Nob29sLTQwNTg='
                print(url)

                # Get safari
                driver.get(url)

                # Accept Cookies
                try:
                    driver.find_element(By.XPATH, '/ html / body / div[5] / div / div / button').click()
                    time.sleep(0.1)
                except:
                    time.sleep(0.1)

                # Find score
                try:
                    Number = driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                    splitnum = Number.text.split('>')
                    teacherRating = splitnum[0]
                    time.sleep(0.1)
                except:
                    teacherRating = 0.0
            else:
                teacherRating = knownScores.get(teacher)
                print('found in dict')

            # Build Object
            if teacherRating == 0.0 or teacherRating == '0.0':
                teacherRating = 3.8

            knownScores[teacher] = teacherRating
            print(str(knownScores.get(teacher)) + ' ' + str(teacher))

            temp = {
                "teacher": teacher,
                "crn": crn,
                "subject": subject,
                "coursenumber": coursenumber,
                "days": days,
                "startTime": startTime,
                "endTime": endTime,
                "teacherRating": teacherRating
            }
            # Add new object to ParsedWithRMP.txt
            jsonObject = json.dumps(temp)
            RMP.write(jsonObject)
            RMP.write('\n')
            print(str(x) + '/' + str(len(courses)))
        driver.close()
        return 1

    ########## 4000-5000 ###############################
    def run5(self, courses, knownScores):
        RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP5.txt', 'w')
        driver = webdriver.Safari()
        for x in range(4000,5000):
            print()
            course = courses[x]
            courseSplit = course.split('\"')
            teacher = courseSplit[3]
            crn = courseSplit[7]
            subject = courseSplit[11]
            coursenumber = courseSplit[15]
            days = courseSplit[19]
            startTime = courseSplit[23]
            endTime = courseSplit[27]
            teacherRating = 0.0

            if teacher not in knownScores:
                splitTeacherName = teacher.split(" ")
                splitTeacherName.pop(len(splitTeacherName) - 1)

                url = 'https://www.ratemyprofessors.com/search/teachers?query='
                for part in range(len(splitTeacherName)):
                    url += splitTeacherName[part] + '%20'
                url = url[:-3]
                url += '&sid=U2Nob29sLTQwNTg='
                print(url)

                # Get safari
                driver.get(url)

                # Accept Cookies
                try:
                    driver.find_element(By.XPATH, '/ html / body / div[5] / div / div / button').click()
                    time.sleep(0.1)
                except:
                    time.sleep(0.1)

                # Find score
                try:
                    Number = driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                    splitnum = Number.text.split('>')
                    teacherRating = splitnum[0]
                    time.sleep(0.1)
                except:
                    teacherRating = 0.0
            else:
                teacherRating = knownScores.get(teacher)
                print('found in dict')

            # Build Object
            if teacherRating == 0.0 or teacherRating == '0.0':
                teacherRating = 3.8

            knownScores[teacher] = teacherRating
            print(str(knownScores.get(teacher)) + ' ' + str(teacher))

            temp = {
                "teacher": teacher,
                "crn": crn,
                "subject": subject,
                "coursenumber": coursenumber,
                "days": days,
                "startTime": startTime,
                "endTime": endTime,
                "teacherRating": teacherRating
            }
            # Add new object to ParsedWithRMP.txt
            jsonObject = json.dumps(temp)
            RMP.write(jsonObject)
            RMP.write('\n')
            print(str(x) + '/' + str(len(courses)))
        driver.close()
        return 1

    ########## 5000-6000 ###############################
    def run6(self, courses, knownScores):
        RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP6.txt', 'w')
        driver = webdriver.Safari()
        for x in range(5000,6000):
            print()
            course = courses[x]
            courseSplit = course.split('\"')
            teacher = courseSplit[3]
            crn = courseSplit[7]
            subject = courseSplit[11]
            coursenumber = courseSplit[15]
            days = courseSplit[19]
            startTime = courseSplit[23]
            endTime = courseSplit[27]
            teacherRating = 0.0

            if teacher not in knownScores:
                splitTeacherName = teacher.split(" ")
                splitTeacherName.pop(len(splitTeacherName) - 1)

                url = 'https://www.ratemyprofessors.com/search/teachers?query='
                for part in range(len(splitTeacherName)):
                    url += splitTeacherName[part] + '%20'
                url = url[:-3]
                url += '&sid=U2Nob29sLTQwNTg='
                print(url)

                # Get safari
                driver.get(url)

                # Accept Cookies
                try:
                    driver.find_element(By.XPATH, '/ html / body / div[5] / div / div / button').click()
                    time.sleep(0.1)
                except:
                    time.sleep(0.1)

                # Find score
                try:
                    Number = driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                    splitnum = Number.text.split('>')
                    teacherRating = splitnum[0]
                    time.sleep(0.1)
                except:
                    teacherRating = 0.0
            else:
                teacherRating = knownScores.get(teacher)
                print('found in dict')

            # Build Object
            if teacherRating == 0.0 or teacherRating == '0.0':
                teacherRating = 3.8

            knownScores[teacher] = teacherRating
            print(str(knownScores.get(teacher)) + ' ' + str(teacher))

            temp = {
                "teacher": teacher,
                "crn": crn,
                "subject": subject,
                "coursenumber": coursenumber,
                "days": days,
                "startTime": startTime,
                "endTime": endTime,
                "teacherRating": teacherRating
            }
            # Add new object to ParsedWithRMP.txt
            jsonObject = json.dumps(temp)
            RMP.write(jsonObject)
            RMP.write('\n')
            print(str(x) + '/' + str(len(courses)))
        driver.close()
        return 1

    ########## 6000 - 7000 ###############################
    def run7(self, courses, knownScores):
        RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP7.txt', 'w')
        driver = webdriver.Safari()
        for x in range(6000,7000):
            print()
            course = courses[x]
            courseSplit = course.split('\"')
            teacher = courseSplit[3]
            crn = courseSplit[7]
            subject = courseSplit[11]
            coursenumber = courseSplit[15]
            days = courseSplit[19]
            startTime = courseSplit[23]
            endTime = courseSplit[27]
            teacherRating = 0.0

            if teacher not in knownScores:
                splitTeacherName = teacher.split(" ")
                splitTeacherName.pop(len(splitTeacherName) - 1)

                url = 'https://www.ratemyprofessors.com/search/teachers?query='
                for part in range(len(splitTeacherName)):
                    url += splitTeacherName[part] + '%20'
                url = url[:-3]
                url += '&sid=U2Nob29sLTQwNTg='
                print(url)

                # Get safari
                driver.get(url)

                # Accept Cookies
                try:
                    driver.find_element(By.XPATH, '/ html / body / div[5] / div / div / button').click()
                    time.sleep(0.1)
                except:
                    time.sleep(0.1)

                # Find score
                try:
                    Number = driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                    splitnum = Number.text.split('>')
                    teacherRating = splitnum[0]
                    time.sleep(0.1)
                except:
                    teacherRating = 0.0
            else:
                teacherRating = knownScores.get(teacher)
                print('found in dict')

            # Build Object
            if teacherRating == 0.0 or teacherRating == '0.0':
                teacherRating = 3.8

            knownScores[teacher] = teacherRating
            print(str(knownScores.get(teacher)) + ' ' + str(teacher))

            temp = {
                "teacher": teacher,
                "crn": crn,
                "subject": subject,
                "coursenumber": coursenumber,
                "days": days,
                "startTime": startTime,
                "endTime": endTime,
                "teacherRating": teacherRating
            }
            # Add new object to ParsedWithRMP.txt
            jsonObject = json.dumps(temp)
            RMP.write(jsonObject)
            RMP.write('\n')
            print(str(x) + '/' + str(len(courses)))
        driver.close()
        return 1

    ########## 7000 - 7500 ###############################
    def run8(self, courses, knownScores):
        RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP8.txt', 'w')
        driver = webdriver.Safari()
        for x in range(7000, 7500):
            print()
            course = courses[x]
            courseSplit = course.split('\"')
            teacher = courseSplit[3]
            crn = courseSplit[7]
            subject = courseSplit[11]
            coursenumber = courseSplit[15]
            days = courseSplit[19]
            startTime = courseSplit[23]
            endTime = courseSplit[27]
            teacherRating = 0.0

            if teacher not in knownScores:
                splitTeacherName = teacher.split(" ")
                splitTeacherName.pop(len(splitTeacherName) - 1)

                url = 'https://www.ratemyprofessors.com/search/teachers?query='
                for part in range(len(splitTeacherName)):
                    url += splitTeacherName[part] + '%20'
                url = url[:-3]
                url += '&sid=U2Nob29sLTQwNTg='
                print(url)

                # Get safari
                driver.get(url)

                # Accept Cookies
                try:
                    driver.find_element(By.XPATH, '/ html / body / div[5] / div / div / button').click()
                    time.sleep(0.1)
                except:
                    time.sleep(0.1)

                # Find score
                try:
                    Number = driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                    splitnum = Number.text.split('>')
                    teacherRating = splitnum[0]
                    time.sleep(0.1)
                except:
                    teacherRating = 0.0
            else:
                teacherRating = knownScores.get(teacher)
                print('found in dict')

            # Build Object
            if teacherRating == 0.0 or teacherRating == '0.0':
                teacherRating = 3.8

            knownScores[teacher] = teacherRating
            print(str(knownScores.get(teacher)) + ' ' + str(teacher))

            temp = {
                "teacher": teacher,
                "crn": crn,
                "subject": subject,
                "coursenumber": coursenumber,
                "days": days,
                "startTime": startTime,
                "endTime": endTime,
                "teacherRating": teacherRating
            }
            # Add new object to ParsedWithRMP.txt
            jsonObject = json.dumps(temp)
            RMP.write(jsonObject)
            RMP.write('\n')
            print(str(x) + '/' + str(len(courses)))
        driver.close()
        return 1

    ########## 7500 - 8282(end) ###############################
    def run9(self, courses, knownScores):
        RMP = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP9.txt', 'w')
        driver = webdriver.Safari()
        for x in range(7500, len(courses)):
            print()
            course = courses[x]
            courseSplit = course.split('\"')
            teacher = courseSplit[3]
            crn = courseSplit[7]
            subject = courseSplit[11]
            coursenumber = courseSplit[15]
            days = courseSplit[19]
            startTime = courseSplit[23]
            endTime = courseSplit[27]
            teacherRating = 0.0

            if teacher not in knownScores:
                splitTeacherName = teacher.split(" ")
                splitTeacherName.pop(len(splitTeacherName) - 1)

                url = 'https://www.ratemyprofessors.com/search/teachers?query='
                for part in range(len(splitTeacherName)):
                    url += splitTeacherName[part] + '%20'
                url = url[:-3]
                url += '&sid=U2Nob29sLTQwNTg='
                print(url)

                # Get safari
                driver.get(url)

                # Accept Cookies
                try:
                    driver.find_element(By.XPATH, '/ html / body / div[5] / div / div / button').click()
                    time.sleep(0.1)
                except:
                    time.sleep(0.1)

                # Find score
                try:
                    Number = driver.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/div/div[4]/div[1]/div[3]/a/div/div[1]/div/div[2]')
                    splitnum = Number.text.split('>')
                    teacherRating = splitnum[0]
                    time.sleep(0.1)
                except:
                    teacherRating = 0.0
            else:
                teacherRating = knownScores.get(teacher)
                print('found in dict')

            # Build Object
            if teacherRating == 0.0 or teacherRating == '0.0':
                teacherRating = 3.8

            knownScores[teacher] = teacherRating
            print(str(knownScores.get(teacher)) + ' ' + str(teacher))

            temp = {
                "teacher": teacher,
                "crn": crn,
                "subject": subject,
                "coursenumber": coursenumber,
                "days": days,
                "startTime": startTime,
                "endTime": endTime,
                "teacherRating": teacherRating
            }
            # Add new object to ParsedWithRMP.txt
            jsonObject = json.dumps(temp)
            RMP.write(jsonObject)
            RMP.write('\n')
            print(str(x) + '/' + str(len(courses)))
        driver.close()
        return 1

    def merge(self):
        print('merging')
        RMP1 = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP1.txt', 'r').readlines()
        RMP2 = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP2.txt', 'r').readlines()
        RMP3 = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP3.txt', 'r').readlines()
        RMP4 = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP4.txt', 'r').readlines()
        RMP5 = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP5.txt', 'r').readlines()
        RMP6 = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP6.txt', 'r').readlines()
        RMP7 = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP4.txt', 'r').readlines()
        RMP8 = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP5.txt', 'r').readlines()
        RMP9 = open('/Users/aldo/PycharmProjects/scriptGM/ParsedWithRMP6.txt', 'r').readlines()
        FINAL = open('/Users/aldo/PycharmProjects/scriptGM/GMandRMP.txt', 'w')

        list = [RMP1,RMP2,RMP3,RMP4,RMP5,RMP6,RMP7,RMP8,RMP9]
        for file in list:
            for line in file:
                FINAL.write(line)

    def main(self):
        GM = open('/Users/aldo/PycharmProjects/scriptGM/Parsed.txt', 'r')
        courses = GM.readlines()
        knownScores = {"EXAMPLE TEACHER": '3.8'}
        # RMP.run1(RMP, courses, knownScores)
        # RMP.run2(RMP, courses, knownScores)
        # RMP.run3(RMP, courses, knownScores)
        # RMP.run4(RMP, courses, knownScores)
        # RMP.run5(RMP, courses, knownScores)
        # RMP.run6(RMP, courses, knownScores)
        # RMP.run7(RMP, courses, knownScores)
        # RMP.run8(RMP, courses, knownScores)
        # RMP.run9(RMP, courses, knownScores)
        RMP.merge(RMP)

if __name__ == "__main__":
        RMP.main(RMP)
