from napalm import get_network_driver
import pprint as pp

def run_compliance(net_os,net_hostm uname, passw, comp_file):
    driver = get_network_driver(net_os)
    device = driver(net_host, uname, passw)
    device.open()
    pp.pprint(device.compliance_report(comp_file))
    device.close()

if __name__ == "__main__":
    print("Running against Switch 1")
    run_compliance("eos", "sw-1", "admin", "alta3", "/home/student/pyna/sw1_validate01.yml")
    print("Running against Switch 2")
    run_compliance("eos", "sw-1", "admin", "alta3", "/home/student/pyna/sw1_validate01.yml")

