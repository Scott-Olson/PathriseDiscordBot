import requests
import random

"""
Here will be the structures to handle the leetcode API calls and responses.

As of now, the api call returns all the problems.

This uses a similar approach to many other Leetcode API crawlers:
- make a call to get all data
- parse the data into sections
- use that to return desired problems.

"""

all_problems = ['all']
easy_problems = ['easy']
med_problems = ['med']
hard_problems = ['hard']

daily_problem = None

stored_problems_len = 0

class Problem():
	def __init__(self, id: int, slug: str, title: str, difficulty: int):
		self.id = id
		self.slug = slug
		self.title = title
		self.difficulty = difficulty
		self.link = f'https://leetcode.com/problems/{self.slug}'

	def get_link(self):
		return self.link

	def get_title(self):
		return self.title

	def get_slug(self):
		return self.slug


def update_problem_list():

	r = requests.get('https://leetcode.com/api/problems/all')
	r = r.json()
	print(r['num_total'])
	print(len(r['stat_status_pairs']))

	dif_list = []
	# check to see if the number of returned problems is greater than the stored problem list
	# if yes, run the store again
	if stored_problems_len < r['num_total']:

		global all_problems = []
		global easy_problems = []
		global med_problems = []
		global hard_problems = []


		r_set = r['stat_status_pairs']
		for p in r_set:
			print("ID: ", p['stat']['question_id'])
			print("Slug: ", p['stat']['question__title_slug'])
			print("Title: ", p['stat']['question__title'])
			print("Level: ", p['difficulty']['level'])
			dif_list.append(p['difficulty']['level'])
			prob = Problem(p['stat']['question_id'], p['stat']['question__title_slug'], p['stat']['question__title'], p['difficulty']['level'])
			print(prob.get_link())
	

update_problem_list()

# random problem generator, accepts upper bound
def random_index(upper: int):
	return random.randrange(0, upper)

# get random, not specific difficulty
def get_random_problem(diff: str):
	i = random_index(0, len(all_problems))
	return all_problems[i]

# set the daily problem so that anyone can retrieve it
def set_daily(Problem):
	return

# get the daily problem
def get_daily_problem():
	return

# get easy random problem
def get_easy_problem():
	i = random_index(0, len(easy_problems))
	return easy_problems[i]

# get medium random problem
def get_medium_problem():
	i = random_index(0, len(med_problems))
	return med_problems[i]

# get hard random problem
def get_hard_problem():
	i = random_index(0, len(hard_problems))
	return hard_problems[i]



# print(get_random_problem('easy'))





