
getAllMachinesByPowerState
==========================

Contents
========

* [Overview](#overview)
	* [Id:](#id)
	* [Fqn](#fqn)
	* [Input Parameters](#input-parameters)
	* [Script](#script)

# Overview


Get All Machines By Power State Filter


## Id:
  
d0a5b782-f963-40b6-a5f7-ed852178cdf1
## Fqn
  
com.vmware.library.vra.infrastructure.machine/getAllMachinesByPowerState


## Input Parameters

|name|type|description|
| :--- | :--- | :--- |
|host|VRA:Host|VMware Aria Automation Host Object|
|state|string|Power State e.g. ON, OFF etc.|
||||

## Script


```javascript
return VraEntitiesFinder.getMachines(host, "powerState eq '" + state + "'");
```