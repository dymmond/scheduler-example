# Esmerald application running with a Scheduler

This serves as a simple application using Esmerald and running the default
scheduler with some simple tasks as described in the [documentation](https://esmerald.dev/scheduler/scheduler/#tasks).

With some minor alterations for the frequency of the tasks for example purposes of course.

## Requirements

* Python 3.8+
* A Python Virtual environment (optional) at your choice.

## Installation

You will need to clone the repo.

```shell
$ git clone https://github.com/dymmond/scheduler-example 
```

And then:

```shell
$ cd scheduler-example
$ pip install -r requirements/development.txt
```

## Run the local

To run the project locally, after the [installation](#installation), simply run:

```shell
$ esmerald runserver
```

Or alternatively

```shell
$ make run
```

There is a default API that you can access via `http://localhost:8000/docs/swagger` and play along but
the most important thing is that you will be able to see in the console the default tasks running as per
schedule.

Something like this:

```shell
2024-06-04 11:28:23.494 | ERROR    | accounts.tasks:collect_market_data:14 - Collecting market data
2024-06-04 11:28:23.494 | INFO     | asyncz.executors.base:run_task:163 - Task 'collect_data (trigger: interval[0:00:01], next run at: 2024-06-04 11:28:24 BST)' executed successfully.
2024-06-04 11:28:24.492 | DEBUG    | asyncz.schedulers.base:process_tasks:934 - Looking for tasks to run.
2024-06-04 11:28:24.493 | DEBUG    | asyncz.schedulers.base:process_tasks:1017 - Next wakeup is due at 2024-06-04 10:28:25.492278+00:00 (in 0.999287 seconds).
2024-06-04 11:28:24.493 | INFO     | asyncz.executors.base:run_task:135 - Running task "collect_data (trigger: interval[0:00:01], next run at: 2024-06-04 11:28:25 BST)" (scheduled at 2024-06-04 11:28:24.492278+01:00)
2024-06-04 11:28:24.493 | ERROR    | accounts.tasks:collect_market_data:14 - Collecting market data
2024-06-04 11:28:24.493 | INFO     | asyncz.executors.base:run_task:163 - Task 'collect_data (trigger: interval[0:00:01], next run at: 2024-06-04 11:28:25 BST)' executed successfully.
2024-06-04 11:28:25.492 | DEBUG    | asyncz.schedulers.base:process_tasks:934 - Looking for tasks to run.
2024-06-04 11:28:25.493 | DEBUG    | asyncz.schedulers.base:process_tasks:1017 - Next wakeup is due at 2024-06-04 10:28:26.492278+00:00 (in 0.999268 seconds).
2024-06-04 11:28:25.493 | INFO     | asyncz.executors.base:run_task:135 - Running task "collect_data (trigger: interval[0:00:01], next run at: 2024-06-04 11:28:26 BST)" (scheduled at 2024-06-04 11:28:25.492278+01:00)
2024-06-04 11:28:25.493 | INFO     | asyncz.executors.base:run_task:135 - Running task "send_email_newsletter (trigger: interval[0:00:03], next run at: 2024-06-04 11:28:28 BST)" (scheduled at 2024-06-04 11:28:25.492333+01:00)
2024-06-04 11:28:25.493 | ERROR    | accounts.tasks:collect_market_data:14 - Collecting market data
2024-06-04 11:28:25.493 | WARNING  | accounts.tasks:send_newsletter:24 - sending email newsletter!
2024-06-04 11:28:25.493 | INFO     | asyncz.executors.base:run_task:163 - Task 'collect_data (trigger: interval[0:00:01], next run at: 2024-06-04 11:28:26 BST)' executed successfully.
2024-06-04 11:28:25.494 | INFO     | asyncz.executors.base:run_task:163 - Task 'send_email_newsletter (trigger: interval[0:00:03], next run at: 2024-06-04 11:28:28 BST)' executed successfully.
2024-06-04 11:28:26.493 | DEBUG    | asyncz.schedulers.base:process_tasks:934 - Looking for tasks to run.
2024-06-04 11:28:26.493 | DEBUG    | asyncz.schedulers.base:process_tasks:1017 - Next wakeup is due at 2024-06-04 10:28:27.492278+00:00 (in 0.998851 seconds).
2024-06-04 11:28:26.493 | INFO     | asyncz.executors.base:run_task:135 - Running task "collect_data (trigger: interval[0:00:01], next run at: 2024-06-04 11:28:27 BST)" (scheduled at 2024-06-04 11:28:26.492278+01:00)
2024-06-04 11:28:26.494 | ERROR    | accounts.tasks:collect_market_data:14 - Collecting market data
```
