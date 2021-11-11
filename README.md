# safe_commands - safe rm/mv/cp

間違って削除しても大丈夫！  
safe_commandsならすぐ元通り！  

## Install

```
pip install git+https://github.com/miyase256/safe_commands
```

## Usage

- rm -> remove

```
Usage: remove [-g(--grave) <grave_directory>] [-l(--list)] [-u(--unbury) <dead_file>] [file]
```

```
$ ls
file01
$ remove file01 # remove and backup file01
$ ls
$ remove -l
/tmp/grave/path/to/file01
$ remove -u /tmp/grave/path/to/file01 # rescure file01 to ./file01
$ ls
file01
```

- mv -> move

```
Usage: move [-g(--grave) <grave_directory>] [src] [dst]
```

- cp -> copy

```
Usage: copy [-g(--grave) <grave_directory>] [src] [dst]
```

## Recommended aliases

```
$ alias rm=remove
$ alias mv=move
$ alias cp=copy
```
