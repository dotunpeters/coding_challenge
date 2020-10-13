
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        #people = sorted(people, key=lambda n: n[2], reverse=True)
        people.sort(key=lambda n:n[2])
        print(people)
        return f(people)
        #people.sort(lambda n: n[2])
    return inner

@person_lister
def name_format(people):
    return [("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1] + " " + person[2] for person in people]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
