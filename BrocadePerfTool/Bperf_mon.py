import paramiko
import configuration as config
from time import sleep as sleep
import csv
import json


s = paramiko.SSHClient()
s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

hostname = config.HOSTNAME
uname = config.UNAME
passwd = config.PASSWORD
sshport = config.SSHPORT

fcport = config.FCPORT
duration = config.DURATION

s.connect(hostname, username=uname, password=passwd, port=sshport)


def switch_show():
    cmd_to_execute = "switchshow"
    stdin, stdout, strerr = s.exec_command(cmd_to_execute)
    switch_show_all = [line.strip() for line in stdout.readlines() if line]
    switch_details = {}
    for item in switch_show_all:
        if item.startswith("switch"):
            k, v = item.split(":", 1)
            switch_details[k.strip()] = v.strip()

    return switch_details


def switch_perfmon(port, duration):
    port_tput = {}
    mode = "-tx -rx"
    cmd_to_execute = "portperfshow {} {}".format(port, mode)
    print("Collecting the performance stats for port {} for next {} mins".format(port, duration))
    stdin, stdout, strerr = s.exec_command(cmd_to_execute)
    sleep(int(duration)*60)
    stdout.channel.shutdown(2)
    sleep(5)
    print("Calculating the Throughput")
    tput_raw = [i.strip() for i in stdout.readlines() ]
    tput_raw = [i for i in tput_raw if not i.startswith("==")]
    tput = [i.split() for i in tput_raw[2::3]]
    port_tput[str(port)] = tput
    # This dump is only for debugging
    with open('result.json', 'w') as fp:
        json.dump(port_tput, fp)
    print("Throughput Calculation is over")
    return port_tput

def tput_parse(tput):
    port_num = tput.keys()[0]
    t_tput = tput[port_num]
    rx = []
    tx = []
    for t in t_tput:
        tx.append(t[0])
        rx.append(t[1])
    rx = [t_convert_to_mbps(i) for i in rx]
    tx = [t_convert_to_mbps(i) for i in tx]
    return rx, tx

def t_convert_to_mbps(t):
    if t.endswith("g"):
        t = float(t.split("g")[0]) * 1024
    elif t.endswith("m"):
        t = float(t.split("m")[0])
    elif t.endswith("k"):
        t = float(t.split("k")[0]) / 1024
    elif t.endswith("b"):
        t = float(t.split("b")[0]) / 1024 / 1024
    else: t = float(t)
    return round(t, 3)

def generate_csv(t):
    tp_final = []
    for tp in zip(range(1, len(t[0])+1), t[0], t[1]):
        tp_final.append(tp)
    with open('Tput.csv', 'w') as out:
        csv_out = csv.writer(out)
        csv_out.writerow(['Time(seconds)', 'Read Throughput(MBps)', 'Write Throughput(MBps)'])
        for row in tp_final:
            csv_out.writerow(row)


tput = switch_perfmon(fcport, duration)
rx_tx = tput_parse(tput)
generate_csv(rx_tx)













