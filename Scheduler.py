#import libraries---------------------------------------------------------------------------
import math 
import pandas as pd

    #file locations
course_file = ".\MockClasses.csv"
faculty_file = ".\MockFaculty.csv"
manager_file = ".\MockManagers.csv"

    #constants
manager_weight: float = 0.5

#main function----------------------------------------------------------------------------
def main() -> None:
    #MICHAEL create code here to read in courses and campuses before building the dictionary
    
    #read in course as data dataframe
    extract = pd.read_csv(course_file)
    Courses = list(extract["Course"].unique())
    Campus = list(extract["Campus"].unique())
    Modality =list(extract["Modality"].unique())
    del extract
    
    #create a merged database of faculy and manager preferences
    faculty_extract: pd = pd.read_csv(faculty_file)
    manager_extract: pd = pd.read_csv(manager_file)
    merged_extract = pd.merge(manager_extract, faculty_extract, how = "left", on = ["ID","ID"], suffixes = ["m", "f"], validate = "1:1")
    merged_extract = merged_extract.drop(columns = ["FirstNamem", "LastNamem"])
    merged_extract = merged_extract.rename(columns = {"LastNamef": "Last", "FirstNamef": "First"})
    print(merged_extract.head())
    merged_extract.to_csv("SCRATCH.csv")
    del merged_extract
    del faculty_extract
    del manager_extract
    
    #create dictionaries 
    global Course_dictionary
    Course_dictionary = {}
    for i, course in enumerate(Courses):
        Course_dictionary[course] = i
        
    # global Campus_dictionary
    global Campus_dictionary
    Campus_dictionary = {}
    for i, campus in enumerate(Campus):
        Campus_dictionary[campus] = i        

    # global Modality_dictionary
    global Modality_dictionary
    Modality_dictionary = {}
    for i, mode in enumerate(Modality):
        Campus_dictionary[mode] = i   

    #build faculty list
    # faculty_list = []
    # with open(course_file, 'r') as file:
    #     reader = csv.reader(file, delimiter = ",")
    #     for i, line in enumerate(reader):
    #         if i > 0: #skips header row
    #             faculty_list.append(faculty(f"{line[4]} {line[5]}", get_id(line[1]), float(line[6]), line[4], line[5], line[6], line[7])) #make sure this is correct
                
    #build courses
    # course_list = []
    # with open(course_file, 'r') as file:
    #     reader = csv.reader(file, delimiter = ",")
    #     for i, line in enumerate(reader):
    #         if i > 0: #skips header row
    #             if line[9] == "ON":
    #                 LecTime = []
    #                 LecDOW = []
    #                 LabTime = []
    #                 LabDOW = []
    #             if line[9] == "HY":
    #                 LecTime = []
    #                 LecDOW = []
    #                 LabTime = Course_time_to_array(line[4], line[5])
    #                 LabDOW = Days_of_week_to_list(line[3])
    #             elif line[9] == "IN":
    #                 LecTime = Course_time_to_array(line[7], line[8])
    #                 LecDOW = Days_of_week_to_list(line[6])
    #                 LabTime = Course_time_to_array(line[4], line[5])
    #                 LabDOW = Days_of_week_to_list(line[3]) 
    #             course_list.append(CourseMaker(line[0], line[1], LecTime, LecDOW, LabTime, LabDOW, int(line[10]), line[2], line[9]))
    
    
    #build manager preferences
    
    
    
    
    
    
    #match courses
    
    
    #check to see if campus and course match up
        #one cond for instructor, one cond for manager
            #log mismatches
            #report score as 0
        #else calculate overlap
    
    #sort for the strongest match by row
        #add to instructor's hours
        #check to see instructor's hours
        #
            #drop if at max
        #drop course
        #check courses and instructors
        #repeat until instructors or courses are used up
    
    
    
    #incorporate managerial overlaps
    
    
    
    #incorporate documentation
    
    return


#defined functions----------------------------------------------------------------------------------------------------------------------
    #builds up faculty, course, and manager classes--------------------------------------
    
    #generates a faculty matrix
def generate_faculty_schedule(weight: float, d_pref: list, t_pref: list) -> list:
    schedule: list = []
    max: float = 100
    for i in range(0, 4):
        schedule.append([])
        for j in range(9, 17):
            schedule[i].append(probability(weight, d_pref, t_pref, i, j))
            if max < schedule[i][j - 9]:
                max = schedule[i][j - 9]
    for i in range(0, 4):
        for j in range(0, 8):
            schedule[i][j] = schedule[i][j] / max
    return schedule 
    
    #generate course matrix
def generate_course_schedule(LaTimes: list, Labs: list, LeTimes: list, Lecture: list, modality: str) -> list:
    base: list = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    if modality == "ON":
        return base
    if modality == "HY":
        Lecture: list = [0, 0, 0, 0, 0]
        LeTimes: list = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    else:
        LeTimes = Times_to_list(LeTimes)
    LaTimes = Times_to_list(LaTimes)
    for i in range(0, 4):
        for j in range(0, 8):
            base[j][i] = second_binary_output(LaTimes[j] * Labs[i] + LeTimes[j] * Lecture[i])
    return base 

    
    #helper functions----------------------------------------------
     
    #punch out the faculty member
def punch_faculty() -> list:
    updated_matrix: list = []
    for i in range(0, 5):
        updated_matrix.append([])
        for j in range(0,9):
            updated_matrix[i].append(0)
    return updated_matrix
    
    #punch out the course and update matrix
def punch_course(faculty: list, course: list) -> list:
    updated_matrix: list = []
    for i in range(0, 5):
        updated_matrix.append([])
        for j in range(0,9):
            updated_matrix[i].append(faculty[i][j] * (1 - course[i][j]))
    return updated_matrix
    
    #extracts user ID from email
def get_id(email: str) -> str:
    end = email.find("@")
    user_id = end[0:end - 1]
    return user_id
    
    #converts course times to a list
def Course_time_to_array(Lower: str, Upper: str) -> list:
    Lower = Lower[0:2].replace(":", "")
    Upper = Upper[0:2].replace(":", "")
    return [int(Lower), int(Upper)]
            
    #probability function
def probability(weight: float, d_pref: list, t_pref: list, i: int, j: int) -> float:
    a = (0.01 + weight) * math.exp(-(i - d_pref[i])^2) #day weight
    b = (1.01 - weight) * (0.01 + t_pref[0]) * math.exp(-(9 - j)^2)
    c = (1.01 - weight) * (0.01 + t_pref[1]) * math.exp(-(12 - j)^2)
    d = (1.01 - weight) * (0.01 + t_pref[2]) * math.exp(-(15 - j)^2)
    return a + b + c + d
    
    #convert days of week to list
def Days_of_week_to_list(value: str) -> list:
    list = [0, 0, 0, 0, 0]
    if value.find("M") > -1:
        list[0] = 1
    if value.find("W") > -1:
        list[2] = 1
    if value.find("F") > -1:
        list[4] = 1
    if value.find("T") > -1:
        if value.find("TT") > -1 or value.find("Th") > -1:
            list[3] = 1
        if value.find("TW")  > -1 or value.find("TT")  > -1 or value.find("TF")  > -1:
            list[1] = 1
    return list

    #convert to times of day
def Times_of_day_to_list(value: str) -> list:
    list = [binary_output(value.find("Morning")), binary_output(value.find("Midday")), binary_output(value.find("Afternoon"))]
    return list
    
    #return 1 or 0 for values
def binary_output(number: int) -> int:
    if number > -1:
        return 1
    return 0

    #return 1 or 0 for values
def second_binary_output(number: int) -> int:
    if number > 0:
        return 1
    return 0

#convert times to a list
def Times_to_list(times : list) -> list:
    listtimes = []
    for i in range(0, 9):
        if int(times[0]) >= i + 8 and int(times[1]) > i + 8:
            listtimes.append(1)
        else:
            listtimes.append(0)
    return listtimes

    #convert campus to matrix
def course_to_list(faculty_pref: str, manager_pref: str) -> list:
    faculty_list: list = [0]* len(Course_dictionary)
    manager_list: list = [0]* len(Course_dictionary)
    for i, v in enumerate(manager_pref.split(",")):
        manager_list[Course_dictionary[v]] = 1
    if len(faculty_pref) != 0:
        for i, v in enumerate(faculty_list.split(",")):
            faculty_list[Course_dictionary[v]] = 1
    return final_weights(faculty_list, manager_list)   

    #convert campus to matrix
def campus_to_list(faculty_pref: str, manager_pref: str) -> list:
    faculty_list: list = [0]* len(Campus_dictionary)
    manager_list: list = [0]* len(Campus_dictionary)
    for i, v in enumerate(manager_pref.split(",")):
        manager_list[Campus_dictionary[v]] = 1
    if len(faculty_pref) != 0:
        for i, v in enumerate(faculty_list.split(",")):
            faculty_list[Campus_dictionary[v]] = 1
    return final_weights(faculty_list, manager_list)    
    
    #convert moality to matrix
def campus_to_list(faculty_pref: str, manager_pref: str) -> list:
    faculty_list: list = [0]* len(Modality_dictionary)
    manager_list: list = [0]* len(Modality_dictionary)
    for i, v in enumerate(manager_pref.split(",")):
        manager_list[Modality_dictionary[v]] = 1
    if len(faculty_pref) != 0:
        for i, v in enumerate(faculty_list.split(",")):
            faculty_list[Modality_dictionary[v]] = 1
    return final_weights(faculty_list, manager_list)    

    #create the weights for the faculty and managers prefernces****************
def final_weights(pref_faculty: str, pref_manager: str) -> list:
    weights = [pref_faculty, pref_manager, []]
    for i, v in enumerate(pref_faculty):
        weights[2].append(v * (1 - manager_weight) + pref_manager[i] * manager_weight)
    return weights

#classes-------------------------------------------------------------------------------------------------------------------------------------
    #faculty class
class faculty:
    def __init__(self, name: str, id: str, weight: float, d_pref: str, t_pref: str, c_preff: str, camp_preff: str,  c_prefm: str, camp_prefm: str) -> None:
        self.faculty = name 
        self.faculty_id = id
        self.dp = d_pref
        self.tp = t_pref
        self.cp = c_preff
        self.campus = camp_preff
        self.campus_preferences = campus_to_list(camp_preff, camp_prefm)
        self.course_preferences = course_to_list(c_preff, c_prefm)
        self.hours = 0
        self.courses = []
        self.matrix = generate_faculty_schedule(weight, Days_of_week_to_list(d_pref), Times_of_day_to_list(t_pref))
        
    def __str__(self) -> str:
        return f"the schedule preference for {self.faculty}"
    
    def __repr__(self) -> str:
       return "this class is used to keep faculty preferences along with their names and IDs"
    
    def overlap(self, course) -> float:
        overlap = 0
        for i in range(0, 4):
            for j in range(0, 8):
                overlap += self.matrix[i][j] * course.matrix[i][j] * self.campus_preferences[2][Campus_dictionary[course.campuse]] * self.course_preferences[2][Course_dictionary[course.course_name]]
        overlap = overlap * self.cp[Course_dictionary(course.course_name)]
        return overlap
                
    #course class-----------------------
class CourseMaker:
    def __init__(self, course: str, section: int, Lectime: list, LecDOW: list, Labtime: list, LaDOW: list, hours: int, campus: str, modality: str) -> None:
        self.course_name = course
        self.campus = campus
        self.sec = section
        self.hours = hours
        self.modality = modality
        self.matrix = generate_course_schedule(Labtime, LaDOW, Lectime, LecDOW, modality)

    def __str__(self) -> str:
        return f"the schedule for {self.matrix}"
    
    def __repr__(self) -> str:
       return "this class is used to create courses"
   
#execute main
if __name__ == "__main__":
  main()
  