from scenario import Scenario
from automatic import automatic_decision

def find_difference(manual_file):
    print
    with open(manual_file) as manual_fd:
        for manual_line in manual_fd.readlines():
            print(manual_line)
            passengers, pedestrians, manual_decision = manual_line.strip().split('|')
            print(passengers + "\n" + pedestrians + "\n" + manual_decision + "\n")

def main():
    manual_file = 'manual_decision.20171128222719.log'
    find_difference(manual_file)

if __name__ == '__main__':
    main()
