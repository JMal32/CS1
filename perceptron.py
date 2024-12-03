

class perceptron:
    def __init__(self, x, y):
        self.c1 = 0
        self.c2 = 0
        self.c2 = 0
        self.x = []
        self.y = []
        self.truth = []
    
    def loadData(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                data = line.strip().split(',')
                self.x.append(float(data[0]))
                self.y.append(float(data[1]))
                self.truth.append(int(data[2]))

    def trainPerceptron(self):
        numCorrect = 0
        dataset_size = len(self.x)
        
        while numCorrect < dataset_size:
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
                
