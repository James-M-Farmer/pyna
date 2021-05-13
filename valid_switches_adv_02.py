from napalm import get_network_driver
import pprint as pp

def run_compliance(net_os,net_host, uname, passw, comp_file):
    driver = get_network_driver(net_os)
    device = driver(net_host, uname, passw)
    device.open()
    pp.pprint(device.compliance_report(comp_file))
    device.close()

if __name__ == "__main__":
    with open("switches.csv") as f:
        txt = f.readlines()
        for line in txt:
            switch_data = line.split(",")
            print(switch_data)
            run_compliance(switch_data[3], switch_data[0], switch_data[1], switch_data[2], switch_data[4].strip())
