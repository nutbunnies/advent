from collections import defaultdict, namedtuple
import queue
import threading

with open("input.txt") as file:
    input = file.read().strip().split("\n")

# input = """set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2"""

def get_value(registers, v):
    try:
        return int(v)
    except:
        return registers[v]

def process_instructions(instructions, thread_id, send_queue, recv_queue):
    registers = defaultdict(int)
    registers['p'] = thread_id
    send_count = 0
    n = 0
    while n < len(instructions):
        command = instructions[n].split(" ")
        # snd X plays a sound with a frequency equal to the value of X.
        if command[0] == "snd":
            registers['lp'] = (command[1], registers[command[1]])
            send_queue.put_nowait((command[1], get_value(registers, command[1])))
            send_count += 1
        # set X Y sets register X to the value of Y.
        elif command[0] == "set":
            registers[command[1]] = get_value(registers, command[2])
        # add X Y increases register X by the value of Y.
        elif command[0] == "add":
            registers[command[1]] += get_value(registers, command[2])
        # mul X Y sets register X to the result of multiplying the value contained in register X by the value of Y.
        elif command[0] == "mul":
            registers[command[1]] *= get_value(registers, command[2])
        # mod X Y sets register X to the remainder of dividing the value contained in register X by the value of Y (that is, it sets X to the result of X modulo Y).
        elif command[0] == "mod":
            registers[command[1]] %= get_value(registers, command[2])
        # rcv X recovers the frequency of the last sound played, but only when the value of X is not zero. (If it is zero, the command does nothing.)
        elif command[0] == "rcv":
            # if get_value(registers, command[1]) != 0:
            #     print("LAST PLAYED: ", registers['lp'])
            #     exit()
            try:
                next_val = recv_queue.get(timeout=5)
                registers[command[1]] = next_val[1]
            except:
                print("Thread {} locked.  Sent {} times".format(thread_id, send_count))
                break
        # jgz X Y jumps with an offset of the value of Y, but only if the value of X is greater than zero. (An offset of 2 skips the next instruction, an offset of -1 jumps to the previous instruction, and so on.)
        elif command[0] == "jgz":
            if get_value(registers, command[1]) > 0:
                n += get_value(registers, command[2])
            else:
                n += 1
        else:
            print("UNKNOWN command: ", command[0])

        if command[0] != "jgz":
            n += 1

        # print("command: {}, registers: {}, next: {}, sendcount: {}".format(command, registers, n, send_count))

thread_0_queue = queue.Queue()
thread_1_queue = queue.Queue()

t0 = threading.Thread(target=process_instructions, args=(input, 0, thread_1_queue, thread_0_queue))
t0.start()

t1 = threading.Thread(target=process_instructions, args=(input, 1, thread_0_queue, thread_1_queue))
t1.start()

t0.join()
t1.join()
