def CountDNA(sequence):
    proofread_sequence = sequence.upper() #to proofread in case there's nucleotide written in lowercase
    print ('A: {} '.format(proofread_sequence.count('A')))
    print ('T: {} '.format(proofread_sequence.count('T')))
    print ('G: {} '.format(proofread_sequence.count('G')))
    print ('C: {} '.format(proofread_sequence.count('C')))
    print ('X: {} '.format(proofread_sequence.count('X')))

def CountRNA(sequence):
    proofread_sequence = sequence.upper() #to proofread in case there's nucleotide written in lowercase
    print ('A: {} '.format(proofread_sequence.count('A')))
    print ('G: {} '.format(proofread_sequence.count('G')))
    print ('C: {} '.format(proofread_sequence.count('C')))
    print ('U: {} '.format(proofread_sequence.count('U')))
    print ('X: {} '.format(proofread_sequence.count('X')))

print('Is your sequence DNA or RNA?')
print('1. DNA')
print('2. RNA')

choice = input('1 or 2? ')
if int(choice) == 1:
    sequenceinput = input('Input your sequence:')
    CountDNA(sequenceinput)
elif int(choice) == 2:
    sequenceinput = input('Input your sequence:')
    CountRNA(sequenceinput)
else:
    print('Wrong options. Please try again.')