import os

class Perceptron:
    def __init__(self, c1=0, c2=0, c3=0):
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.x = []
        self.y = []
        self.truth = []
    
    def loadData(self, filename):
        try: #Added error handling for the file with try/except
            with open(filename, 'r') as f:
                next(f) # This skips the first line of the file because it is a header and was causing file read errors that were giving me nightmares...
                for line in f:
                    data = line.strip().split(',')
                    self.x.append(float(data[0]))
                    self.y.append(float(data[1]))
                    self.truth.append(int(data[2]))
                print(f"Succesfully loaded {len(self.x)} records from {filename}")
        except FileNotFoundError:
            print(f"Error: Could not find file {filename}")
        except: #Covers any other generic errors that might pop up
            print("Error: There was a problem reading the file.")

    def trainPerceptron(self, max_iterations=1000):
        if not self.x or not self.y or not self.truth:
            print("Error: No data loaded")
            return
        
        numCorrect = 0
        dataset_size = len(self.x)
        iteration = 0
        while numCorrect < dataset_size and iteration < max_iterations:
            numCorrect = 0
            for xi, yi, truth in zip(self.x, self.y, self.truth):
                mdl = self.c1 + self.c2 * xi + self.c3 * yi

                if (mdl > 0 and truth > 0) or (mdl < 0 and truth < 0):
                    numCorrect += 1
                else:
                    if truth > 0:
                        self.c1 += 1
                        self.c2 += xi
                        self.c3 += yi
                    else:
                        self.c1 -= 1
                        self.c2 -= xi
                        self.c3 -= yi

                    print(f"Updated coefficients: c1={self.c1}, c2={self.c2}, c3={self.c3}")
            if iteration % 100 == 0:
                print(f"Iteration {iteration}: coefficients: c1={self.c1}, c2={self.c2}, c3={self.c3}")
            iteration += 1

    def printResults(self):
        # Print the final coefficients and the linear equation in y = mx + b form
        print(f"Final coefficients: c1={self.c1}, c2={self.c2}, c3={self.c3}")
        print(f"Raw linear equation: ({self.c3})y + ({self.c2})x + ({self.c1}) = 0")
        # Add error handling for division by zero
        try:
           print(f"Slope-intercept form: y = {-self.c2/self.c3}x + {-self.c1/self.c3}")
        except ZeroDivisionError:
           print("Cannot convert to slope-intercept form (division by zero)")
    def test(self, gradeNumerator, gradeDenominator):
        # uses perceptron object's final c-coefficients to determine a boolean result from the model-equation
        if gradeDenominator == 0:
             return False
             
        x = gradeNumerator
        y = gradeDenominator
             
        mdl = self.c1 + self.c2 * x + self.c3 * y
             
        return mdl > 0
             
def main():
    # Making perceptrons with different initial coefficients
    p1 = Perceptron()
    p2 = Perceptron(0, 1, -2)
    p3 = Perceptron(-2, 1, -2)
    
    perceptrons = [p1, p2, p3]
    names = ["000", "10-2", "-21-2"]
    
    #Testing each
    for p, name in zip(perceptrons, names):
        print(f"\nTesting grades:{name}")
        p.loadData("percepGrades.csv")
        p.trainPerceptron()
        p.printResults()
        
        print("75% (15/20):", p.test(15, 20))
        print("55% (11/20):", p.test(11, 20))
        print("59% (59/100):", p.test(59, 100))
        print("61% (61/100):", p.test(61, 100))
        
if __name__ == "__main__":
    main()
