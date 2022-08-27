import os
import os.path
import sys
import datetime
import time
import random
import multiprocessing
from types import SimpleNamespace


from util.ssh_util import *
from util.ec2_util import *
from util.prop_util import *


def run():
    props = loadPropertyFile("test_ec2_config.json")
    ec_props = SimpleNamespace(**props["ec2"])
    client_conn = startConnection(ec_props.client_region, aws_key="", aws_secret="")
    tag = "test"
    startEc2Instance(
        client_conn,
        ec_props.client_ami,
        client_key,
        ec_props.client_inst_type,
        [client_secret],
        ec_props.client_availability,
        tag,
        spot=ec_props.usespot,
    )


if __name__ == "__main__":
    run()
