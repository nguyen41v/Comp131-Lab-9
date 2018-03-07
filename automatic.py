from audit import audit, log_scenario
import random
save_passengers = "passengers"
save_pedestrians = "pedestrians"

def count_people(people):
    num_people = 0
    for person in people:
        if person.charType == "human":
            if person.pregnant:
                num_people += 2
            else:
                num_people += 1
    return num_people

def count_jobs(people, characteristic):
    num_people_w_char = 0
    for person in people:
        if person.profession == characteristic:
            num_people_w_char += 1
    return num_people_w_char

def count_ages(people, age):
    num_people_of_age = 0
    for person in people:
        if person.age == age:
            num_people_of_age += 1
    return num_people_of_age

def automatic_decision(scenario):
    #gets rid of people who are similar, gender doesn't matter
    i = 0
    while i < len(scenario.pedestrians):
        ii = 0
        while ii < len(scenario.passengers):

            #all pets are treated the same
            if scenario.pedestrians[i].charType == scenario.passengers[ii].charType != "human":
                scenario.pedestrians.pop(i)
                scenario.passengers.pop(ii)
                i -= 1
                break

            elif scenario.pedestrians[i].charType == scenario.passengers[ii].charType == "human":
                if scenario.pedestrians[i].age == scenario.passengers[ii].age == "adult":
                    if scenario.pedestrians[i].profession == scenario.passengers[ii].profession:
                        if scenario.pedestrians[i].gender == scenario.passengers[ii].gender == "female":
                            if scenario.pedestrians[i].pregnant == scenario.pedestrians[ii].pregnant:
                                scenario.pedestrians.pop(i)
                                scenario.passengers.pop(ii)
                                i -= 1
                                break
                        else:
                            scenario.pedestrians.pop(i)
                            scenario.passengers.pop(ii)
                            i -= 1
                            break
                elif scenario.pedestrians[i].age == scenario.passengers[ii].age:
                    scenario.pedestrians.pop(i)
                    scenario.passengers.pop(ii)
                    i -= 1
                    break
            ii += 1
        i += 1

    # sees which one has more people and saves the one with more people; pets not counted
    num_passengers = count_people(scenario.passengers)
    num_pedestrians = count_people(scenario.pedestrians)
    if num_passengers > num_pedestrians:
        return save_passengers
    if num_pedestrians > num_passengers:
        return save_pedestrians

    # elderly are worth less
    num_ped_elderly = count_ages(scenario.pedestrians, "elderly")
    num_pas_elderly = count_ages(scenario.passengers, "elderly")
    if num_ped_elderly > num_pas_elderly:
        return save_passengers
    if num_pas_elderly > num_ped_elderly:
        return save_pedestrians

    #children are worth more
    num_ped_child = count_ages(scenario.pedestrians, "child") + count_ages(scenario.pedestrians, "baby")
    num_pas_child = count_ages(scenario.passengers, "child") + count_ages(scenario.passengers, "baby")
    if num_pas_child > num_ped_child:
        return save_passengers
    if num_ped_child > num_pas_child:
        return save_pedestrians

    #docs save people
    num_ped_docs = count_jobs(scenario.pedestrians, "doctor")
    num_pas_docs = count_jobs(scenario.passengers, "doctor")
    if num_pas_docs > num_ped_docs:
        return save_passengers

    ped_rng = random.randint(0, 1)
    pas_rng = random.randint(0, 1)
    while ped_rng == pas_rng:
        ped_rng = random.randint(0, 1)
        pas_rng = random.randint(0, 1)
    if ped_rng > pas_rng:
        return save_passengers
    return save_pedestrians

if __name__ == '__main__':
    audit(automatic_decision, 100000, seed=8675309)
