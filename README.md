# Computer
Computer compang

## Finance Build Status
Main Brnach

[![Build Status](https://dev.azure.com/algoautotrader/AlgoAutoTrader-Dev/_apis/build/status/Finance-%20Main?branchName=main)](https://dev.azure.com/algoautotrader/AlgoAutoTrader-Dev/_build/latest?definitionId=1&branchName=main)

India - Prod Build Status



### Notes
#####  To Delete All PyCache

pip3 install pyclean
pyclean .


India URL
[https://api.nserobots.com/api](https://api.nserobots.com/api)

This is vishal's branch

# To deploy and run on server
## Setup Server and clone repos
* Clone repos to desired directories default:`~/repos/`
* Supervisor same uses linux user from which scripts are run, update supervisor `.conf` files on dir `scripts/supervisord/` default: `user=ubuntu`
> NOTE: this user should be allowed to run `root` commands.
* create and update config file on like `scripts/configs/<config-name>.sh`
> This config files contains all required variables which are needed to setup server and deploy application. Create carefully.
* run Setup Script `./scipts/setup_server.sh <config-name> <dns>`, here two DNS should point to this server `api.<dns>` `<dns>`
* Once server setup is completed to deploy application just run deployment scripts, mentioned below:

## To deploy API and Frontend
> NOTE: here frontend are nodejs sites and run using command `node service.js`. To deploy fixed static sites script needs to be modified later.
* deploy api, run: `./scripts/deployapi.sh <config-name>`
* deploy frontend, run: `./scripts/deployfronend.sh <config-name>`

# To run locally
## start django server
* create and update config file on like `scripts/configs/<config-name>.sh`, to run locally we just need environment variables.
* `source scripts/configs/<config-name>.sh`
* start local server `./runserver.sh`, this runs server using `runserver 0.0.0.0:7777` command.

# To run on windows
> This scripts present here are for powershell only.Probably win 10/11 will contain powershell by default, if not present follow this [link](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.2) to install powershell.

> Note the difference b/w backslash`\` and frontslashes`/` used for windows and linux/mac respectively.

* create virtual environment with name `env`
* run script on powershell `.\runserver.ps1`

