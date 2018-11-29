#import os
import json

def Demo():
    data = {}
    data['ENV_FILE_DETAILS'] = []
    
    file_open = open("/Users/sankar.biswas/Desktop/input_file.txt","r")
    
    file_read = file_open.readlines()
    
    heading = file_read[0].strip().split(":")[:-1]
    
    length = len(heading)
    
    dummy_data = {"EVENT_NAME":"STM_MZ_PLI_LITE_COMPUTE","PROCESS_NAME":"STM_MZ_PLI_LITE","SLEEP_TIME":"60","MAX_SLA_WAIT_SECS_CNT":"300"}
    for each_line in file_read[1:]:
        values = each_line.strip().split("|")
        for a in range(length):
            dummy_data[heading[a].strip()[1:][:-1]] = values[a]
        data['ENV_FILE_DETAILS'].append(dummy_data)
        dummy_data = {"EVENT_NAME":"STM_MZ_PLI_LITE_COMPUTE","PROCESS_NAME":"STM_MZ_PLI_LITE","SLEEP_TIME":"60","MAX_SLA_WAIT_SECS_CNT":"300"}
    
    with open('/Users/sankar.biswas/Desktop/data.json', 'w') as outfile:
        json.dump(data, outfile)

Demo()

