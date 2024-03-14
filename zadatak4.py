def confidenceFun():
    try:
        fileName = input("Unesi ime datoteke: ")
        file = open(fileName, 'r')
        total = 0.0
        num = 0

        for line in file:
            if line.startswith('X-DSPAM-Confidence:'):
                confidence = float(line.split(':')[1])
                total += confidence
                num += 1

        if num > 1:
            average = total / num
            print('Average X-DSPAM-Confidence: ', average)
        else:
            print('Nema pronadenih linija.')
    except FileNotFoundError:
        print('Datoteka nije pronadena.')

confidenceFun()