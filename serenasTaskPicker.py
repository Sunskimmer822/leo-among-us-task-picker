import random, yaml, sys

def main():
    with open("./taskList.yml") as f:
        taskListPool = yaml.safe_load(f)
    try:
        times = int(sys.argv[1])
    except:
        times = 1
    pick(times, taskListPool)

def pick(times,list):
    for i in range(times):
        choice = random.choice(list)
        print(choice)

# holy shit Serena actually using good python coding practices?!?!?!?!?!?!?!?!?!?!
if __name__ == "__main__":
    main()