#--------------Step 1------------
import os.path

# Step 1
def fileToList(filename):
    if not os.path.isfile(filename):
        return []
    new_lst = []
    with open(filename) as file:
        for line in file:
            new_lst.append(line.strip())
    return new_lst

# Step 2
def getTargetStrand(filename):
    return returnFirstString(fileToList(filename))

def getCandidateStrands(filename):
    return fileToList(filename)

def returnFirstString(new_lst):
    if new_lst:
        return new_lst[0]
    else:
        return ""

# Step 3
def strandsAreNotEmpty(strand1, strand2):
    return bool(strand1 and strand2)

# Step 4
def strandsAreEqualLengths(strand1, strand2):
    return len(strand1) == len(strand2)

# Step 5
def candidateOverlapsTarget(target, candidate, overlap):
    if len(target) < overlap or len(candidate) < overlap:
        return False
    return target[-overlap:] == candidate[:overlap]

# Step 6
def findLargestOverlap(target, candidate):
    if not strandsAreNotEmpty(target, candidate) or not strandsAreEqualLengths(target, candidate):
        return -1
    
    largestOverlap = 0
    for i in range(1, len(target)+1):
        if candidateOverlapsTarget(target, candidate, i):
            largestOverlap = i
    return largestOverlap

#Step 7
def findBestCandidate(target, candidates):
    largestOverlap = 0
    bestCandidate = ""
    for candidate in candidates:
        overlap = findLargestOverlap(target, candidate)
        if overlap > largestOverlap:
            largestOverlap = overlap
            bestCandidate = candidate
    return (bestCandidate, largestOverlap)

#Step 8
def joinTwoStrands(target, candidate, overlap):
    if overlap == 0:
        return target + candidate
    else:
        return target + candidate[overlap:]


def main():
    target_filename = input("Target strand filename: ")
    candidates_filename = input("Candidate strands filename: ")

    target_strand = getTargetStrand(target_filename)
    candidate_strands = getCandidateStrands(candidates_filename)
    
    best_candidate, overlap_size = findBestCandidate(target_strand, candidate_strands)
    if overlap_size > 0:
        joined_strand = joinTwoStrands(target_strand, best_candidate, overlap_size)
    else:
        joined_strand = target_strand
    print(joined_strand)

if __name__ == '__main__':
    main()
