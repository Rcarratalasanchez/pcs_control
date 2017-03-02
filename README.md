# Pcs Control

Playbooks for control the resources of an Openstack installed in a cluster.

## Overview

When an Openstack is installed and configured in High Availability in the several pieces that is divided (haproxies, controllers, backends, etc) there is a large number of resources that you must to control for perform an upgrade or execute some operations.

For control all the resources (the pacemaker and systemd resources that uses Openstack for the proper execution), you can use the playbook/tasks that allows you to start or stop all the resources and control them.

For example, if you want to perform an upgrade of the controllers, you can stop the controllers, perform the upgrade and started again, one by one, without losing quorum and obviously service.

## Execution

For execute the entire playbook that stops and starts the computes, controllers, cinder_controllers and haproxies execute:

```
ansible-playbook -v -i hosts/<inventory> pcs_control.yml --ask-pass
```

For only execute the playbook for control one specific group like computes or controllers, execute:

```
ansible-playbook -v -i hosts/<inventory> -l compute pcs_control.yml --ask-pass

ansible-playbook -v -i hosts/<inventory> -l controller pcs_control.yml --ask-pass

ansible-playbook -v -i hosts/<inventory> -l haproxy pcs_control.yml --ask-pass
```

NOTE: the groups must to be defined properly into the inventory

## Specifications

Tested with ansible 2.2.1.0 and OSP6 and OSP8.
