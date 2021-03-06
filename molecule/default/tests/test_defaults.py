import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_redmine_running(host):
    out = host.check_output('curl -sf localhost:3000')
    assert '<title>Redmine</title>' in out
