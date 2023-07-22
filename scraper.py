from decouple import config, Csv
from boards import indeed

indeed_url = config('INDEED_URL')
disgard_list = config('DESCRIPTION_DOESNT_CONTAIN', cast=Csv())

print('Getting jobs from indeed.com')
indeed = indeed.IndeedJobs(indeed_url)
indeed_jobs = indeed.get()
print(f'Found {len(indeed_jobs)} job listings within the specified criteria')

unfiltered_jobs =  indeed_jobs
filtered_jobs = []

for job in unfiltered_jobs:
    contains_bad_string = any(dis in job["description_text"].lower() for dis in disgard_list)
    if not contains_bad_string:
        print(f'Title: {job["title"]}')
        print(f'Company: {job["company"]}')
        print(f'Url: {job["href"]}')
        print('------------------------------------------------------------------------------')

# todo: send on email
