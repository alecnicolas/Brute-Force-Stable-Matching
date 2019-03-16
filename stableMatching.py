from itertools import permutations
import timeit
import sys

# take preference list input from file
def getPreferenceLists(input):
    with open(input) as f:
        content = f.readlines()[1:]
        content = [x.strip().split(' ') for x in content]
    return content[:len(content)//2],  content[len(content)//2:]

# generate and test each permutation
def getTotalNumberOfStableMatches(input):
    mPref, wPref = getPreferenceLists(input)
    if(len(mPref) < 2):
        return 1
    count = 0

    perm = list(permutations(mPref[0]))
    for matchSet in perm:
        if matchesAreStable(matchSet, mPref, wPref):
            count += 1
    return count

# check each permutation for stability
def matchesAreStable(matchSet, mPref, wPref):
    for husband, wife in enumerate(matchSet):
        if not manIsHappy(mPref[husband], wPref, wife, str(husband + 1), matchSet):
            return False
    return True

# check if man is happy with wife
def manIsHappy(husbandPref, wPref, wife, husband, matchSet):
    for preferredWoman in husbandPref:
        if(preferredWoman != wife):
            if(preferredWomanWantsToSwitch(matchSet, preferredWoman, wPref[int(preferredWoman) - 1], husband)):
                return False
        else:
            return True

# when man is not happy, check to see if his preferred woman would rather switch
def preferredWomanWantsToSwitch(matchSet, woman, wPref, proposer):
    herHusband = matchSet.index(woman) + 1

    # see if the proposer or current husband comes first on her list
    return (max(wPref.index(str(herHusband)), wPref.index(proposer)) == wPref.index(proposer))

# main run
def main():
    start = timeit.default_timer()
    print(getTotalNumberOfStableMatches("./project1_tests_cases/input3.txt"))
    stop = timeit.default_timer()
    print('Time: ', stop - start)

if __name__ == "__main__":
  main()
