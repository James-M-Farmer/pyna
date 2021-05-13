#!/usr/bin/env python3

from napalm import get_network_driver
import pprint as pp
import yaml
import sqlite3

def first_run():
    conn = sqlite3.connect('switches.db')
    print("Opened database successfully")
    try:
        conn.execute("INSERT INTO switches (hostname,ip) VALUES ('sw-1','10.0.41.35')")
        conn.execute("INSERT INTO switches (hostname,ip) VALUES ('sw-2','10.12.190.200')")
        conn.commit()
    except sqlite3.OperationalError as err:
        print(err)
    finally:
        conn.close()

def retrv_config (sw):
    driver = get_network_driver('eos')
    device = driver('admin', 'alta3')
    device.open()
    sw_conf = device.get_config()
    return sw_conf


def update_sw_conf(sw):
    conn = sqlite3.connect("switches.db")
    sw_conf = retrv_conf(sw)
    run_conf = sw_conf['running']
    start_conf = sw_conf ['startup']
    conn.execute(f"UPDATE switches SET running_config = '{sw_conf}' where hostname = '{sw}'")
    conn.execute(f"UPDATE switches SET startup_config = '{sw_conf}' where hostname = '{sw}'")
    conn.commit()

update_sw_conf('sw-1')
