import os
from time import sleep
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

def test_restic_version(host):
    command_output = host.run("restic version")
    assert command_output.rc == 0
    assert "restic 0.15.1" in command_output.stdout

def test_autorestic_version(host):
    command_output = host.run("autorestic --version")
    assert command_output.rc == 0
    assert "autorestic version" in command_output.stdout
