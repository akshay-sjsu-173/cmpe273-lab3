import json

def listOfStudents(_,info):
    students = json.loads(open('students.json','r').read())["students"]
    return students

def listOfCourses(_,info):
    courses = json.loads(open('courses.json','r').read())["courses"]
    return courses

def newStudent(_,info,id,name):
    students = json.loads(open('students.json','r').read())
    last_id = students["students"][-1]["id"]
    students["students"].append({"id":id, "name":name})
    open('students.json','w').write(json.dumps(students))
    return {"id": id, "name": name}

def newCourse(_,info,id,name):
    courses = json.loads(open('courses.json','r').read())
    courses["courses"].append({"id":id, "name":name, "students": []})
    open('courses.json','w').write(json.dumps(courses))
    return {"id": id, "name": name, "students": []}

def updateCourse(_,info,course_id,student_id):
    students = json.loads(open('students.json','r').read())
    if student_id not in [item["id"] for item in students["students"]]:
        return {"error": "Invalid student_id"}

    courses = json.loads(open('courses.json','r').read())
    if course_id not in [item["id"] for item in courses["courses"]]:
        return {"error": "Invalid course_id"}
    
    for student in students["students"]:
        if student["id"] == student_id:
            for course in courses["courses"]:
                if course["id"] == course_id:
                    course["students"].append(student)
                    open('courses.json','w').write(json.dumps(courses))
                    return course

    #students["students"].append({"id":id, "name":name})
    #open('students.json','w').write(json.dumps(students))
    #return {"id":id, "name":id}
