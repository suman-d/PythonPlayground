#/usr/bin/python
import os
import socket

###### All config parameters(Edit the configuration) ########
file_size = [20, 40, 80, 160, 320, 640, 1280, 2560, 5120, 10240, 20480, 40960]
buffer_size = [512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576]
thread_per_target = 6
thread_cpu_affinity = "1-32"
max_queue_depth = 40
access_profile_weight = "-%f100"
test_duration = 30
sample_output_interval = 60
timeout_interval = 0
test_type = [" -n -u -r -o ", " -n -u -o ", " -n -u -w -o "] # [read, mixed, write] test
target_file = "/root/targets.dat"

#e.g:  maim 20KB -b512B -t6 -T:1-32 -Q40 -n -u -r -o -%f100 -d30 -Y60 -M0 --perf-mode -f/root/LPe16002B_Test/targets.dat

###### Nothing to modify below this point ######


file_size = [str(i)+"KB" for i in file_size]
buffer_size = [str(i)+"B" for i in buffer_size]

# This function will create the Medusa test commands based on the configuration provided by the user
def maim_test():
    test_list = []
    for i in test_type:
        for j in range(len(file_size)):
            test_list.append("maim " + str(file_size[j]) + \
            " -b" + str(buffer_size[j]) + \
            " -t" + str(thread_per_target) + \
            " -T:" + thread_cpu_affinity + \
            " -Q" + str(max_queue_depth) + \
            str(i) + \
            access_profile_weight + \
            " --perf-mode " + \
            " -d" + str(test_duration) + \
            " -Y" + str(sample_output_interval) + \
            " -M" + str(timeout_interval) + \
            " -f" + target_file)

    return test_list

# This function will run all the test
def run_test():
    cmd = "rm -rf " + os.getcwd() + "/" + socket.gethostname() + ".*"
    os.system(cmd)
    for test in maim_test():
        os.system(test)

run_test()