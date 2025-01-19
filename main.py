from calender import MonthlyCalender
from exercises import ExerciseTracker

def cal_update(user_visit, cal: MonthlyCalender):
    """
    Updates the calender based on if the user visited the gym or not

    time complexity: O(1) all operations are done in constant time
    space complexity: O(1) does not generate any new data only updates existing data
    """
    cal.visit(user_visit)
    print(cal)

def exercise_update(exercises, tracker: ExerciseTracker):
    """
    Adds user exercises to the exercise tracker

    time complexity: O(n) where n is the number of exercises to be added
    space complexity: O(1) does not generate any new data only updates existing data or adds to the tracker
    """
    for i in exercises:
        try:
            tracker.update(i[0], i[1], i[2], i[3])
        except:
            tracker.add_exercise(i[0], i[1], i[2], i[3])


if __name__ == '__main__':
    # update the calender
    cal = MonthlyCalender()
    user_visit = input("Did you visit the gym today (yes/no)? ")
    print()
    cal_update(user_visit, cal)
    # update the exercises
    tracker = ExerciseTracker()
    if user_visit == 'yes':
        more_exercises = 1
        exercises = []
        # keep adding exercises until the user is done
        # runs in O(m) where m is the number of exercises to be added
        # space complexity is also O(m) where m is the number of exercises to be added
        while more_exercises == 1:
            exercise_name = input("Enter the name of the exercise: ")
            muscle_groups = input("Enter the main muscle group worked: ")
            last_session = input("Enter the set, reps and weight of the last session (?x?x?): ")
            pb = int(input("Enter your one rep max if applicable else enter 0: "))
            exercises.append([exercise_name, muscle_groups, last_session, pb])
            more_exercises = int(input("Do you have more exercises to add (1/0)? "))
        
        exercise_update(exercises, tracker)
        print()

    view = input("Would you like to view any exercises (yes/no)? ")  
    
    # keep looking up exercises or muscle groups until the user is done
    # runs in O(m * n) where m is the number of exercises to be looked up and n is number of exercises in the tracker
    # space complexity is O(1) as no new data is generated
    while view == 'yes':
        lookup = input("Would you like to lookup by exercise or muscle group (exercise/muscle)? ")
        if lookup == 'exercise':
            exercise = input("Enter the name of the exercise: ")
            print(tracker.lookup_exercise(exercise))
        else:
            muscle_group = input("Enter the muscle group: ")
            print(tracker.lookup_muscle_group(muscle_group))
        
        view = input("Would you like to view any more exercises (yes/no)? ")
    
    print("Goodbye!")
        



    
    