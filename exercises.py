import pandas as pd

class ExerciseTracker():
    
    def __init__(self):
        """
        Initialises the exercise tracker with the existing exercises or creates a new one if it does not exist.

        time complexity: O(1) all operations are done in constant time
        space complexity: O(n) if it reads from a csv file where n is the number of exercises in the tracker
        """
        #try to read the exercises from a csv file
        try:
            self.exercises = pd.read_csv('exercises.csv')
        except:
            # create a data frame to store the exercises
            exercise_dict = {'Exercise': [], 'Muscle Groups': [], 'Last Session': [], 'Personal Best': []}
            self.exercises = pd.DataFrame(exercise_dict)
        
        self.exercises.to_csv('exercises.csv', index=False)

    def __str__(self): 
        """
        Prints the exercises as a string

        time complexity: O(1) all operations are done in constant time
        space complexity: O(1) does not generate any new data
        """
        return self.exercises.to_string(index=False)
    
    def add_exercise(self, exercise, muscle_groups, last_session, pb):
        """
        Adds an exercise to the exercise tracker

        time complexity: O(1) all operations are done in constant time
        space complexity: O(1) does not generate any new data only updates exiuisting data
        """
        self.exercises.loc[len(self.exercises)] = [exercise, muscle_groups, last_session, pb]
        self.exercises.to_csv('exercises.csv', index=False)

    def lookup_exercise(self, exercise):
        """
        Looks up an exercise in the exercise tracker

        time complexity: O(n) where n is the number of exercises in the tracker
        space complexity: O(1) does not generate any new data only updates exiuisting data
        """
        return self.exercises[self.exercises['Exercise'] == exercise].reset_index(drop=True)
    
    def lookup_muscle_group(self, muscle_group):
        """
        Looks up an exercise by muscle group in the exercise tracker

        time complexity: O(n) where n is the number of exercises in the tracker
        space complexity: O(1) does not generate any new data only updates exiuisting data
        """
        return self.exercises[self.exercises['Muscle Groups'] == muscle_group].reset_index(drop=True)
    
    
    def update(self, exercise, muscle_groups, last_session, pb):
        """
        Updates an exercise in the exercise tracker

        time complexity: O(n) where n is the number of exercises in the tracker
        space complexity: O(1) does not generate any new data only updates existing data
        """
        current_pb = self.exercises.loc[self.exercises['Exercise'] == exercise, 'Personal Best'].values[0]
        if pb > current_pb:
            self.exercises.loc[self.exercises['Exercise'] == exercise] = [exercise, muscle_groups, last_session, pb]
        self.exercises.loc[self.exercises['Exercise'] == exercise] = [exercise, muscle_groups, last_session, pb]
        self.exercises.to_csv('exercises.csv', index=False)