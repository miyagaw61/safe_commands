# safe_commands - safe rm/mv/cp

間違って削除しても大丈夫！  
safe_cmmandsならすぐ元通り！  

## Install

```
pip install git+https://github.com/miyagaw61/safe_commands --process-dependency-links
```

## Usage

- rm -> remove

```
Usage: remove [-g(--grave) <grave_directory>] [-l(--list)] [-u(--unbury) <dead_file>] [file]
```

```
remove file01 # KILL file01
remove -l #/tmp/grave/path/to/file01
remove -u /tmp/grave/path/to/file01 # RESCURED to ./file01
```

- mv -> move

```
Usage: move [-g(--grave) <grave_directory>] [src] [dst]
```

- cp -> copy

```
Usage: copy [-g(--grave) <grave_directory>] [src] [dst]
```

