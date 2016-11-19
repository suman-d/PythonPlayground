#/usr/bin/python
import os
import socket
import argparse
import subprocess


def create_target_file():
    #create the file name based on the LUNs available
    #and return the file name, if no LUN is visible return exception
    pass

def get_cpu_affinity()
    #return the no. of CPU that can be used for the test, default all the CPU in Numa Node 0, if NUMA
    #is available
    pass

def test_config():
    pass

def gen_numa():
    """Generate NUMA info"""
    cpunodes = {}
    numacores = {}
    out = subprocess.Popen('numactl --hardware | grep cpus', shell=True,
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    errtxt = out.stderr.readline()
    if errtxt:
        print errtxt + '\r\n'
        print "Is numactl installed?\r"
        exit(1)
    for line in out.stdout.readlines():
        arr = line.split()
        if arr[0] == "node" and arr[2] == "cpus:" and len(arr) > 3:
            node = arr[1]
            numacores[node] = arr[3:]
            for core in arr[3:]:
                cpunodes[core] = node
    return numacores, cpunodes





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

def main():

    parser = argparse.ArgumentParser(description='Medusa Performance Testing')
    parser.add_argument("-t", "--threads", action='store', )

    args = parser.parse_args()
    print args.accumulate(args.integers)

    run_test()