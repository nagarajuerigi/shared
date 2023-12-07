import re

def cal_waysTo_win(race_last_time,race_duration):
    
    ways_to_win=0

    for hold_button_time in range(1,race_duration):
        total_distance=(race_duration - hold_button_time)*hold_button_time

        if total_distance > race_last_time:
            ways_to_win=ways_to_win+1
    
    return ways_to_win

def main():
    with open("input.txt", "r") as file:
        race_duration_line = file.readline().strip()
        record_distance_line = file.readline().strip()
        race_duration = [int(match.group()) for match in re.finditer(r'\b\d+\b', race_duration_line)]
        record_distance = [int(match.group()) for match in re.finditer(r'\b\d+\b', record_distance_line)]
        #print(race_duration[1])
        #print(record_distance[2])
    
    no_of_ways=1
    
    for time,distance in zip(race_duration,record_distance):
        
        #print(time,distance,"no_of_ways",no_of_ways)
        
        no_of_ways=no_of_ways*cal_waysTo_win(distance,time)

    print(no_of_ways)

    
if __name__ == "__main__":
    main()
