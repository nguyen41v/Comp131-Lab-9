from scenario import Scenario
from automatic import automatic_decision

def find_difference(manual_file):
    with open(manual_file) as manual_fd:
        for manual_line in manual_fd.readlines():
            if manual_line.strip(" ") == "":
                break
            passengers, pedestrians, manual_decision = manual_line.strip().split('|') #it's broken :'( i tried to fix it but i moved on
            scenario = Scenario.from_string(passengers, pedestrians)
            auto_decision = automatic_decision(scenario)
            if manual_decision != auto_decision:
                print(scenario)
                print()
                print('manual decision: ' + manual_decision)
                print('auto decision: ' + auto_decision)
                print(40 * '-')

def main():
    manual_file = 'manual_decision.20171128222719.log'
    find_difference(manual_file)

if __name__ == '__main__':
    main()
