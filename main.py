import re
# import boto3

class parser():

    # regex pattersn to match dates, workouts, and reps
    isDate = r'[\d]{2}/[\d]{2}/[\d]{2,4}'
    isWorkout = r'[a-zA-Z ]x[ ]{0,1}[\d]'

    def __init__(self, file):
        self.loadData(file)
        self.jsonify(self.data)

    # load the data from file
    def loadData(self, file):
        with open(file) as f:
            self.data = f.readlines()

        for i in range(len(self.data)):
            self.data[i] = self.data[i].rstrip('\r\n')

        print(self.data)

    def jsonify(self, data):
        for line in data:
            try:
                date = re.match(self.isDate, line).group(0)
            except:
                try:
                    workout = re.match(self.isWorkout, line).group(0)
                    print(workout)
                except:
                    print('passed')
                    pass
                # else:
                #     try:
                #         reps = re.match(self.isReps, line).group(0)

if __name__ == '__main__':
    p = parser('sample.txt')
