import os
import sys


def possible_white(step_list):
    steps = set()
    dirs = []
    # support white move at all position
    for i in range(-7, 8):
        for j in range(-7, 8):
            dirs.append([i, j])
    for s in step_list:
        x = ord(s[0]) - ord('a')
        y = int(s[1:]) - 1
        for d in dirs:
            xn = x + d[0]
            yn = y + d[1]
            if 0 <= xn < 8 and 0 <= yn < 8:
                next_step = "%s%s" % (chr(xn + ord('a')), str(yn+1))
                steps.add(next_step)
    for s in step_list:
        if s in steps:
            steps.remove(s)
    return list(steps)


if __name__ == '__main__':
    # part_board_name = sys.argv[1]
    # next_black_name = sys.argv[2]

    print("Python interpreter path:", sys.executable)

    script_dir = "/Users/lemonshark/PycharmProjects/Reversi"
    print("Script directory:", script_dir)

    # Construct full paths for your files
    part_board_name = os.path.join(script_dir, "reversi/divided/d5b_d4b_e4b_e5w_d3b/d5b_d4b_e4b_e5w_d3b_c4b.txt")
    next_black_name = os.path.join(script_dir, "black_steps.txt")
    print("Part board name:", part_board_name)
    print("Next black name:", next_black_name)


    step_list = []
    step_list_plus_black = []
    for line in open(part_board_name, "r"):
        step_list.append((line.strip()))

    for line in open(next_black_name, "r"):
        new_list = step_list[:]
        new_list.append(line.strip())
        step_list_plus_black.append(new_list)

    for item in step_list_plus_black:
        top_dir_name = "divided/"
        if not os.path.isdir(top_dir_name):
            os.mkdir(top_dir_name)
        dir_name = top_dir_name + "_".join(item)
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
        for white in possible_white(item):
            new_item_list = item[:]
            new_item_list.append(white)
            filename = "./%s/%s%s" % (dir_name, "_".join(new_item_list), ".txt")
            print(filename)
            with open(filename, "w") as f:
                for step in new_item_list:
                    f.write(step + '\n')