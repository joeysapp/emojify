# python/utils
Attempt at submodule-ing, (firstly) for the Console work from axi

## Creation
Create a repo as usual, this should be self explanatory

## Usage
Adding a submodule to an existing git project should be simple - however, the remote origin must contain your username and host.
```shell
$ cd newproject
$ git init --bare
$ mkdir lib; mkdir utils
$ git submodule add zooey@localhost:~/Documents/code/python/utils lib/utils
$ git submodule init
$ git submodule update
```
