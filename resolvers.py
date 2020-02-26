import json

def listOfStudents(_,info):
    students = json.loads(open('students.json','r').read())["students"]
    return students

def listOfCourses(_,info):
    courses = json.loads(open('courses.json','r').read())["courses"]
    return courses

def newStudent(_,info,name,age):
    students = json.loads(open('students.json','r').read())
    if len(students["students"])>0:
        next_id = students["students"][-1]["id"]+1
    else:
        next_id = 0 #For the first student
    students["students"].append({"id":next_id, "name":name, "age":age})
    open('students.json','w').write(json.dumps(students))
    return students["students"][-1] #{"id": next_id, "name": name, "age": age}

def newCourse(_,info,name):
    courses = json.loads(open('courses.json','r').read())
    if len(courses["courses"])>0:
        next_id = courses["courses"][-1]["id"]+1
    else:
        next_id = 0 #For the first course
    courses["courses"].append({"id":next_id, "name":name, "students": []})
    open('courses.json','w').write(json.dumps(courses))
    return courses["courses"][-1] #{"id": next_id, "name": name, "students": []}

def updateCourse(_,info,course_id,student_id):
    students = json.loads(open('students.json','r').read())
    if int(student_id) not in [item["id"] for item in students["students"]]:
        return {"error": "Invalid student_id"}
        #return {"id": 0, "name": "00", "age": 0}

    courses = json.loads(open('courses.json','r').read())
    if int(course_id) not in [item["id"] for item in courses["courses"]]:
        return {"error": "Invalid course_id"}
        #return {"id": 1, "name": "00", "age": 0}
    
    for student in students["students"]:
        if student["id"] == int(student_id):
            for course in courses["courses"]:
                if course["id"] == int(course_id):
                    if student not in course["students"]:
                        course["students"].append(student)
                    open('courses.json','w').write(json.dumps(courses))
                    return course
                    #return {"id": 3, "name": "00", "age": 0}

    #students["students"].append({"id":id, "name":name})
    #open('students.json','w').write(json.dumps(students))
    #return {"id":id, "name":id}
