#this is the file for reading a writing to the ini file

def getSetting(field):
    with open('settings.ini', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if (field in line):
            pos = line.find('=')
            value = line[pos+1:]
    return value
    f.close()

def getConnection(field):
    with open('settingspw.ini', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if (field in line):
            pos = line.find('=')
            value = line[pos+1:]
    return value
    f.close()

def writeSettings(field, newline):
    with open('settings.ini', 'r') as f:
            lines = f.readlines()
    #iterate through the lines
    i = 0
    for line in lines:
        if (field in line):
            lines[i] = str(newline) + '\n'
            break
        i += 1
    #now write all lines back
    with open('settings.ini', 'w') as f:
        f.writelines(lines)
    f.close()

def createLogFile(today):
    log_path = getSetting('log_path').rstrip('\n')
    file_name = '\ADM_API_' + str(today) + '.txt'
    file_path = log_path + file_name
    with open(file_path, "w") as lf:
        lf.write("Admobilize API Device Status\n")

def writeToLog(today, data):
    log_path = getSetting('log_path').rstrip('\n')
    file_name = '\ADM_API_' + str(today) + '.txt'
    file_path = log_path + file_name
    with open(file_path, "a") as lf:
        lf.write(data)