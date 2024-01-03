import os
import json


from divided_solution_manager import apply_all_transformation_for_steps_str, apply_transformation, find_next_steps_from_board_str_hash2action
from divided_solution_manager import get_all_step_str2action, normalize_steps_str, steps2board_str, board_str_hash, move2position

board_str_hash2action = get_all_step_str2action()


def get_next_black_move(step_str):
    """

    :param step_str: d5_d4_e4_e5_d3
    :return:
    """
    board_str = steps2board_str(step_str)
    if board_str in board_str_hash2action:
        return board_str_hash2action[board_str]
    else:
        cmd = 'export LD_LIBRARY_PATH=/usr/local/clang_9.0.0/lib:$LD_LIBRARY_PATH&&%s/web_search %s' % (os.getcwd(), step_str)
        print(cmd)
        res = json.loads(os.popen(cmd).read().strip("\n"))
        next_move = chr(res['x'] + ord('a')) + str(res['y'] + 1)
        return next_move

if __name__ == '__main__':
    # 1. start with 4 board,2 possible position
    # d5B_d4W_e4B_e5W
    five_positions = ["d5b_d4b_e4b_e5w_c4b",
    "d5b_d4b_e4b_e5w_d3b"]
    # "d5_d4_e4_e5_f5",
    # "d5_d4_e4_e5_e6"]


    # 2. find each black step by web_search
    six_position = []
    for step_str in five_positions:
        next_move = get_next_black_move(step_str)
        six_position.append("%s_%s" % (step_str, next_move))
    print(six_position)

    # 3. loop all white possible move, 2 * 2xx four position
    seven_position = []
    for step_str in six_position:
        for i in range(8):
            for j in range(8):
                positions = step_str.split("_")
                possible_white_move = chr(i + ord('a')) + str(j + 1)
                if possible_white_move not in positions:
                    seven_position.append("%s_%s" % (step_str, possible_white_move))

    # 4. find each black step by web_search, 35 * 2xx four position + guided black step
    # generate problem_comb four_position + guilded black step

    with open("../../third_move_all_solutions_all.sh", "w") as f:
        for step_str in sorted(seven_position):
            next_move = get_next_black_move(step_str)
            cmd = "./problem_comb.sh %s %s" % (step_str, next_move)
            print(cmd)
            f.write(cmd + "\n")

