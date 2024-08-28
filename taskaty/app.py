from argparse import ArgumentParser
from .TaskController import TaskController

def main():
    controller = TaskController('tasks.txt')
    parser = ArgumentParser(description='Simple CLI Task Manager')
    subparsers = parser.add_subparsers()
    add_task = subparsers.add_parser('add', help='Add the given task')
    add_task.add_argument('title', help='Title of the task', type=str)
    add_task.add_argument('-d', '--description', help='Short description of the task', type=str, default=None)
    add_task.add_argument('-s', '--start_date', help='Date to begin the task', type=str, default=None)
    add_task.add_argument('-e', '--end_date', help='Date to end the task', type=str, default=None)
    add_task.add_argument('--done', help='Check whether the task is done or not', type=str, default=False)
    add_task.set_defaults(func = controller.add_task)

    list_tasks = subparsers.add_parser('list', help='List unfinished tasks')
    list_tasks.add_argument('-a', '--all', help='List all the tasks', action='store_true')
    list_tasks.set_defaults(func = controller.display)

    check_task = subparsers.add_parser('check', help='Check the given tasks')
    check_task.add_argument('-t', '--task', help='Number of the task to be done. If not specified, last task will be removed.', type=int)
    check_task.set_defaults(func = controller.check_task)

    remove_task = subparsers.add_parser('remove', help='Remove a task')
    remove_task.add_argument('-t', '--task', help='The task to be removed (Number)', type=int)
    remove_task.set_defaults(func = controller.remove)

    reset = subparsers.add_parser('reset', help='Remove all tasks')
    reset.set_defaults(func = controller.reset)

    args = parser.parse_args()
    args.func(args)

if __name__ == '__main__':
    main()