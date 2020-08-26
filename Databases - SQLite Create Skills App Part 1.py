import sqlite3

#  connect data base file
db = sqlite3.connect("skill.db")

# setting up cursor
cr = db.cursor()


def commit_and_close():
    db.commit()
    db.close()
    print("Data commit and close")


# user id global
user_id = int(input(" input user id "))
# Beg input massge
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option:
"""

# Input Option Choose
user_input = input(input_message).strip().lower()

# list commands
list_commands = ["s", "a", "d", "u", "q"]

# Define The Methods


def show_skills():
    cr.execute(f"select * from skills where user_id = {user_id}")
    resalte = cr.fetchall()
    print(f"you have {len(resalte)} .skills ")
    for counter, skills in enumerate(resalte):
        print(f"{counter+1} skills name => {skills[0]}  ", end=" ")
        print(f"=> progress {skills[1]}% => user_id  {skills[2]} ")

    print()
    commit_and_close()


def add_skill():
    sk = input("writ skills name ").strip().capitalize()
    cr.execute(f"select name from skills where name = '{sk}' and user_id = {user_id}")
    resalte = cr.fetchone()
    print(resalte)
    if resalte == None :
        prog = input("writ progerss ").strip()
        cr.execute(f"insert into skills(name , progress , user_id )values ('{sk}', '{prog}', {user_id}) ")
        commit_and_close()
    else :
        var = input("These skills are already there. Do you want to change to progress? y or n").strip()
        if var == "y" :
            update_skill()
        
        if var == "n":
            print("close app ")
            

           
            


   
    


def delete_skill():
    sk = input("writ skills name ").strip().capitalize()
    cr.execute(
        f"delete from skills where name  = {sk} and user_id = {user_id} ")
    commit_and_close()


def update_skill():

    sk = input("Write Skill Name: ").strip().capitalize()

    prog = input("Write The New Skill Progress ").strip()

    cr.execute(f"update skills set progress = {prog} where name = '{sk}' and user_id = {user_id}")

    commit_and_close()

    print("Update Skill Progress")


# chack if command is Exists
if user_input in list_commands:
    if user_input == "s":
        show_skills()

    elif user_input == "a":
        add_skill()

    elif user_input == "d":
        delete_skill()

    elif user_input == "u":
        update_skill()

    else:
        print("App Is Close ")


else:
    print("Comand Not found ")
