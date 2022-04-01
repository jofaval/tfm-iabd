[« Docs](../README.md)

# Tools #

All the tools used to make the dev team work faster and more comfortable.

## Table of Contents

1. [Infra](#infra)
    1. [infrastructure](#infrastructure)
    1. [start](#start)
    1. [stop](#stop)
1. [Git](#git)
    1. [pull](#pull)
    1. [push](#push)
    1. [fetch upstream](#fetch-upstream)

## Infra
[↑ Back to top](#table-of-contents)

The project's infraestructure utilities

### infrastructure
[↑ To the section](#infra)

Moves to the desired directory

#### Execute on Windows

From the cmd or powershell

```bash
tools/windows/infra/infrastructure.bat
```

#### Execute on Linux

From the bash or shell

```bash
./tools/linux/infra/infrastructure.sh
```

### start
[↑ To the section](#infra)

Starts the Docker-Compose

#### Execute on Windows

From the cmd or powershell

```bash
tools/windows/infra/start.bat
```

#### Execute on Linux

From the bash or shell

```bash
./tools/linux/infra/start.sh
```

### stop
[↑ To the section](#infra)

Shuts down the Docker-Compose

#### Execute on Windows

From the cmd or powershell

```bash
tools/windows/infra/stop.bat
```

#### Execute on Linux

From the bash or shell

```bash
./tools/linux/infra/stop.sh
```

## Git
[↑ Back to top](#table-of-contents)

Some git utilities. The descriptions will ignore the merge conflicts as for now

### pull
[↑ To the section](#git)

Updates the local files with the changes in remote

#### Execute on Windows

From the cmd or powershell

```bash
tools/windows/git/pull.bat
```

#### Execute on Linux

From the bash or shell

```bash
./tools/linux/pull.sh
```

### push
[↑ To the section](#git)

Updates the remote files with the changes in local

#### Execute on Windows

From the cmd or powershell

```bash
tools/windows/git/push.bat
```

#### Execute on Linux

From the bash or shell

```bash
./tools/linux/push.sh
```

### fetch upstream
[↑ To the section](#git)

Updates both the local and remote files in the local, remote and fork's origin

#### Execute on Windows

From the cmd or powershell

```bash
tools/windows/git/fetch upstream.bat
```

#### Execute on Linux

From the bash or shell

```bash
./tools/linux/fetch upstream.sh
```