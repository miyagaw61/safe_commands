from enert import *

GRAVE_ROOT = '/tmp/grave'
if 'GRAVE_ROOT' in os.environ:
    GRAVE_ROOT = os.environ['GRAVE_ROOT']

def remove(victim, grave=GRAVE_ROOT):
    victim = File(victim)
    dst = File(f'{grave}{victim.abspath}')
    if not victim.exist():
        return -1
    if dst.exist():
        dst = create_dst(dst, 1)
    dst_base = dst.basename
    dirs_lst = dst.name.split('/')[:-1]
    dirs = '/'.join(dirs_lst)
    File(dirs).mkdir()
    victim.mv(dst)
    return 0

def create_dst(old, idx):
    f = File(f'{old.name}~{idx}')
    if f.exist():
        idx = idx + 1
        f = create_dst(old, idx)
        return f
    else:
        return f

def console_remove():
    usage = 'Usage: remove [-g(--grave) <grave_directory>] [-l(--list)] [-u(--unbury) <dead_file>] [file]'
    parser = mkparser(usage)
    parser.add_argument('-u', '--unbury')
    parser.add_argument('-g', '--grave')
    parser.add_argument('-l', '--list', action='store_true')
    grave = GRAVE_ROOT
    if argc < 2:
        print(usage)
        exit(0)
    args = parser.parse_args(argv[1:])
    if args.help:
        print(usage)
        exit(0)
    if args.grave:
        grave = args.grave
    if args.list:
        for root, dirs, files in os.walk(grave):
            for i in range(len(files)):
                print(f'{root}/{files[i]}')
        exit(0)
    if args.unbury:
        f = File(args.unbury)
        move(f.name, f.basename)
        exit(0)
    for i in range(len(args.args)):
        if remove(args.args[i], grave=grave) == -1:
            print(usage)
            exit(0)

def save_dst(src, dst, grave=GRAVE_ROOT):
    src = File(src)
    dst = File(dst)
    if dst.isdir():
        dst = File(f'{dst.name}/{src.name}')
    if dst.exist():
        remove(dst.name, grave=grave)
    return [src, dst]

def move(src, dst, grave=GRAVE_ROOT):
    if not File(src).exist() or src == dst:
        return -1
    src, dst = save_dst(src, dst, grave=grave)
    src.mv(dst)

def console_move():
    usage = 'Usage: move [-g(--grave) <grave_directory>] [src] [dst]'
    if argc < 3:
        print(usage)
        exit(0)
    parser = mkparser(usage)
    parser.add_argument('-g', '--grave')
    args = parser.parse_args(argv[1:])
    grave = GRAVE_ROOT
    if args.grave:
        grave = args.grave
    if move(args.args[0], args.args[1], grave=grave) == -1:
        print(usage)
        exit(0)

def copy(src, dst, grave=GRAVE_ROOT):
    if not File(src).exist() or src == dst:
        return -1
    src, dst = save_dst(src, dst, grave=grave)
    src.cp(dst)

def console_copy():
    usage = 'Usage: copy [-g(--grave) <grave_directory>] [src] [dst]'
    if argc < 3:
        print(usage)
        exit(0)
    parser = mkparser(usage)
    parser.add_argument('-g', '--grave')
    args = parser.parse_args(argv[1:])
    grave = GRAVE_ROOT
    if args.grave:
        grave = args.grave
    if copy(args.args[0], args.args[1], grave=grave) == -1:
        print(usage)
        exit(0)
