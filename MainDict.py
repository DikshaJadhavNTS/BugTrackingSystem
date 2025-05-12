
bugs = {
    "BUG001": {"title": "Login button unresponsive", "severity": "High", "status": "Open", "tags": {"frontend", "authentication", "UI"}, "reported_date": (2025, 5, 1), "assigned_to": None},
    "BUG002": {"title": "Crash on profile update", "severity": "Critical", "status": "In Progress", "tags": {"backend", "database"}, "reported_date": (2025, 4, 25), "assigned_to": None},
    "BUG003": {"title": "Typo in welcome message", "severity": "Low", "status": "Closed", "tags": {"frontend", "content"}, "reported_date": (2025, 3, 15), "assigned_to": None},
    "BUG004": {"title": "Password reset email not sent", "severity": "High", "status": "Open", "tags": {"backend", "email", "authentication"}, "reported_date": (2025, 5, 2), "assigned_to": None},
    "BUG005": {"title": "Image upload fails on mobile", "severity": "Medium", "status": "Open", "tags": {"frontend", "mobile", "upload"}, "reported_date": (2025, 5, 3), "assigned_to": None},
    "BUG006": {"title": "Notifications not showing in dashboard", "severity": "Medium", "status": "Open", "tags": {"frontend", "backend", "notifications"}, "reported_date": (2025, 5, 4), "assigned_to": None},
    "BUG007": {"title": "Database deadlock on heavy traffic", "severity": "Critical", "status": "Open", "tags": {"backend", "database", "performance"}, "reported_date": (2025, 5, 5), "assigned_to": None},
    "BUG008": {"title": "App crashes on logout", "severity": "High", "status": "Open", "tags": {"frontend", "authentication", "logout"}, "reported_date": (2025, 5, 6), "assigned_to": None},
    "BUG009": {"title": "Broken link in footer", "severity": "Low", "status": "Open", "tags": {"frontend", "UI", "content"}, "reported_date": (2025, 5, 7), "assigned_to": None},
    "BUG010": {"title": "Session timeout too short", "severity": "Medium", "status": "Open", "tags": {"backend", "authentication", "session"}, "reported_date": (2025, 5, 8), "assigned_to": None},
}

developers = {
    "DEV001": {"name": "Alice", "skills": {"frontend", "UI", "React"}, "assigned_bugs": [], "bugs_resolved": 5},
    "DEV002": {"name": "Bob", "skills": {"backend", "database", "Python"}, "assigned_bugs": [], "bugs_resolved": 3},
    "DEV003": {"name": "Charlie", "skills": {"authentication", "security", "frontend"}, "assigned_bugs": [], "bugs_resolved": 4},
    "DEV004": {"name": "Diana", "skills": {"mobile", "React Native", "UI"}, "assigned_bugs": [], "bugs_resolved": 2},
    "DEV005": {"name": "Evan", "skills": {"API", "backend", "integration"}, "assigned_bugs": [], "bugs_resolved": 6},
    "DEV006": {"name": "Fiona", "skills": {"CSS", "frontend", "theme"}, "assigned_bugs": [], "bugs_resolved": 4},
    "DEV007": {"name": "George", "skills": {"database", "performance", "backend"}, "assigned_bugs": [], "bugs_resolved": 5},
    "DEV008": {"name": "Hannah", "skills": {"email", "notifications", "backend"}, "assigned_bugs": [], "bugs_resolved": 3},
    "DEV009": {"name": "Ivan", "skills": {"logs", "data", "reporting"}, "assigned_bugs": [], "bugs_resolved": 4},
    "DEV010": {"name": "Julia", "skills": {"browser compatibility", "UI", "testing"}, "assigned_bugs": [], "bugs_resolved": 2},
}
########################################################################################################################
#task 1

def Display():
    print("**************************List of Bugs:******************************\n")
    for bug_id, bug_info in bugs.items():
        print(f"Bug ID: {bug_id}")
        print(f"  Title: {bug_info['title']}")
        print(f"  Severity: {bug_info['severity']}")
        print(f"  Status: {bug_info['status']}")
        print(f"  Tags: {', '.join(bug_info['tags'])}")
        print(f"  Reported Date: {bug_info['reported_date']}")
        print(f"  Assigned To: {bug_info['assigned_to'] if bug_info['assigned_to'] else 'Not assigned'}")
    print("\nList of Developers:\n")
    for dev_id, dev_info in developers.items():
        print(f"Developer ID: {dev_id}")
        print(f"  Name: {dev_info['name']}")
        print(f"  Skills: {', '.join(dev_info['skills'])}")
        print(f"  Assigned Bugs: {', '.join(dev_info['assigned_bugs']) if dev_info['assigned_bugs'] else 'None'}")
        print(f"  Bugs Resolved: {dev_info['bugs_resolved']}")
    print("******************************************************************************************")

######################################################################################################
# task 2

def add_new_bug(bugs):
    bug_id = input("Bug ID: ")
    title = input("Title: ")
    severity = input("Severity: ")
    status = input("Status: ")
    tags = input("Tags (comma separated): ").split(',')
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))
    bugs = {}
    print("your bug is :",bugs)
    bugs[bug_id] = {
        "title": title,
        "severity": severity,
        "status": status,
        "tags": set(tags),
        "reported_date": (f"{year}/ {month}/ {day}"),
        "assigned_to": None
    }
    print("******************************************************************************************")
    

######################################################################################################
# task 3

def bug_assigner():
     for bug_id, bug_info in bugs.items():
          if bug_info["assigned_to"] is None:
               for dev_id, dev_info in developers.items():
                    if bug_info["tags"] & dev_info["skills"]:
                        bug_info["assigned_to"] = dev_id
                        dev_info["assigned_bugs"].append(bug_id)
                        break  
    
                    print("******************************List of Bugs:******************************\n")
                    for bug_id, bug_info in bugs.items():
                     print(f"Bug ID: {bug_id}")
                     print(f"  Title: {bug_info['title']}")
                     print(f"  Severity: {bug_info['severity']}")
                     print(f"  Status: {bug_info['status']}")
                     print(f"  Tags: {', '.join(bug_info['tags'])}")
                     print(f"  Reported Date: {bug_info['reported_date']}")
                     print(f"  Assigned To: {bug_info['assigned_to']}")
    print("******************************************************************************************")
#########################################################################################
# task 4

def UpdateStatus():
    
    confirm = input("Do you want to update the status? (yes/no): ").lower()
    for bug_id, bug_info in bugs.items():
        if confirm == "yes":
            if bug_info["status"] == "Open":
                bug_info["status"] = "In Progress"
                print("Status is open but now it is updated to In Progress.")
            elif bug_info["status"] == "In Progress":
                bug_info["status"] = "Closed"
                print("Status is In Progress but now it is updated to Closed.")
            else:
                print("Bug is already Closed.")
    print("******************************************************************************************")



##############################################################################################
#task 5

def filter_bugs():
    print("1. Filter by Severity")
    print("2. Filter by Status")
    choice = input("Enter choice (1 or 2): ")

    if choice == "1":
        severity = input("Enter severity (Low / Medium / High / Critical): ")
        for bug_id, bug_info in bugs.items():
            if bug_info["severity"].lower() == severity.lower():
                print(bug_id, "-", bug_info["title"])
    elif choice == "2":
        status = input("Enter status (Open / In Progress / Closed): ")
        for bug_id, bug_info in bugs.items():
            if bug_info["status"].lower() == status.lower():
                print(bug_id, "-", bug_info["title"])
    else:
        print("Invalid choice.")
    print("******************************************************************************************")

#################################################################################################################3
# task 6

def developer_dashboard():
    print("\n Developer Dashboard ")

    top_bugs = 0
    top_name = ""

    for dev in developers.values():
        if dev["bugs_resolved"] > top_bugs:
            top_bugs = dev["bugs_resolved"]
            top_name = dev["name"]

    print("Top Performer :", top_name)
    print(top_bugs, "bugs resolved")

    total_bugs = 0
    for dev in developers.values():
        total_bugs += dev["bugs_resolved"]
    average = total_bugs / len(developers)
    print("Average Bugs Resolved :", round(average, 2))

    print("Available Developers :")
    for dev in developers.values():
        if len(dev["assigned_bugs"]) == 0:
            print("-", dev["name"])
    print("******************************************************************************************")

#############################################################################################################
#task 7

def SimilarBugs():

    bug_id=input("Enter Bug Id :")
    if bug_id not in bugs:
        print("Bug not found")
        return

    for other_id, other_bug in bugs.items():
        if other_id == bug_id:
            continue
        
        if bugs[bug_id]["tags"] & other_bug["tags"]: 
            print(f"{other_id}: {other_bug['title']}")

    print("******************************************************************************************")

##################################################################################################################
#task 8

import datetime

def DetectBugs():
    today = datetime.date.today()

    print("\n This Bugs are Open for more than 7 days:\n")
    found = False

    for bug_id, bug in bugs.items():
        if bug["status"] == "Open":
            r_date = datetime.date(*bug["reported_date"])  
            if (today - r_date).days > 7:
                print(f"- {bug_id}: {bug['title']}")
                found = True

    if not found:
        print(" No stale bugs found")
    print("******************************************************************************************")
