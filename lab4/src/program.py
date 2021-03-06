import json
import yaml
import math

dh = {}

pi = 3.14

# we save data from json file to dictionary to change dh notation to coefficients
with open('in.json') as inFile:
    dh = json.load(inFile)
    
# we write to output file (format.yaml) our coefficients
with open('out.yaml', 'w') as outFile:
    for it in dh.keys():
        coeffs = dh[it]
        outFile.write(it + ': \n')
        outFile.write("   " + 'len: ' + str(math.sqrt(math.pow(coeffs[1], 2) + math.pow(coeffs[0], 2))) + '\n')
        outFile.write("   " + 'xyz: ' + ' ' + str(0.5*coeffs[0]) + ' 0.0 ' + str(0.5 * coeffs[1]) + '\n')
       
        outFile.write("   " + 'rpy: ' + ' ' + str(coeffs[2]) + ' 0.0 ' + str(coeffs[3]) + '\n')
        outFile.write("   " + 'limit: ' + str(-1 *math.sqrt(math.pow(coeffs[1], 2) + math.pow(coeffs[0], 2))) + '\n')
        
        
        outFile.write('\n')
