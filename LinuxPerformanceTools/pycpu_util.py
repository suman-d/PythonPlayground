import time
import json

last_worktime=0
last_idletime=0

def get_cpu():
        global last_worktime, last_idletime
        f=open("/proc/stat","r")
        line=f.readline()
        f.close()
        spl=line.split(" ")
        worktime=int(spl[2])+int(spl[3])+int(spl[4])
        idletime=int(spl[5])
        dworktime=(worktime-last_worktime)
        didletime=(idletime-last_idletime)
        rate=float(dworktime)/(didletime+dworktime) * 100
        last_worktime=worktime
        last_idletime=idletime
        if(last_worktime==0): return 0
        return round(rate, 2)

def get_started():
    block_size = ["512B", "1KB", "2KB", "4KB", "8KB", "16KB", "32KB", "64KB", "128KB", "256KB", "512KB", "1MB"]
    read_test = [i + "_Read" for i in block_size]
    write_test = [i + "_Write" for i in block_size]
    rw_test = [i + "_RW" for i in block_size]
    all_test_list = read_test + write_test + rw_test
    all_test_dict = dict.fromkeys(all_test_list, 0)
    for test in all_test_list:
        print "Test : {} is started".format(test)
        timeout = time.time() + 30  # 30 sec from now
        cpu_time = []
        while time.time() < timeout:
            g_cpu = get_cpu()
            cpu_time.append(g_cpu)
            time.sleep(1)
        all_test_dict[test] = (max(cpu_time), cpu_time)
        print "Test : {} got over with the cpu utilization of {}".format(test, max(cpu_time))
    print "All test got over !!"
    with open('cpu_raw_stat_iometer_test.json', 'w') as fp:
        json.dump(all_test_dict, fp)

    with open('cpu_stat_iometer_test', 'w') as fp:
        for i in all_test_list:
            tmp = i, str(all_test_dict[i][0]), "\n"
            fp.write(" ".join(tmp))

time.sleep(5)
get_started()







