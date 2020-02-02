import re
import json
# import boto3

class parser():
    workouts = {}
    date = ''

    def __init__(self, file):
        self.loadData(file)
        self.jsonify(self.data)

    # load the data from file
    def loadData(self, file):
        with open(file) as f:
            self.data = f.readlines()

        for i in range(len(self.data)):
            self.data[i] = self.data[i].rstrip('\r\n')

        # print(self.data)

    # use regex to determine if the line is a date
    def isDate(self, line):
        date = r'[\d]{2}/[\d]{2}/[\d]{2}'
        try:
            returnedDate = re.search(date, line).group(0)
            self.date = returnedDate
            self.workouts[returnedDate] = {}
        except:
            pass

    # use regex to determine if the line is a workout
    def isWorkout(self, line):
        workout = r'[a-zA-Z -]{,}'

        try:
            # regex pattersn to match dates, workouts, and reps
            returnedWorkout = re.search(workout, line).group(0)

            workout = line.split(':')[0]

            # split the workout and reps into separate
            if (returnedWorkout != ''):

                # grab everything in the line after the colon then split by commas
                reps = line.split(':')[-1]
                reps = reps.split(',')

                for i, rep in enumerate(reps):
                    reps[i] = rep.strip(' ')
                self.workouts[self.date][workout] = reps
        except:
            pass

    # turn the text file to json
    def jsonify(self, data):
        for line in data:
            self.isDate(line)
            self.isWorkout(line)
        print(json.dumps(self.workouts, indent=4, sort_keys=True))

if __name__ == '__main__':
    p = parser('sample.txt')
