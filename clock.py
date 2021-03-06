from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from automate import send

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send, 'interval', seconds=20)

sched.start()