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

	# check to see if the number of returned problems is greater than the stored problem list
	# if yes, run the store again
	if stored_problems_len < r['num_total']:
		r_set = r['stat_status_pairs']
		for p in r_set:
			print("ID: ", p['stat']['question_id'])
			print("Slug: ", p['stat']['question__title_slug'])
			print("Title: ", p['stat']['question__title'])
			print("Level: ", p['difficulty']['level'])
			prob = Problem(p['stat']['question_id'], p['stat']['question__title_slug'], p['stat']['question__title'], p['difficulty']['level'])
			print(prob.get_link())

update_problem_list()

def get_random_problem(diff: str):
	choices = {
		'all': 'all_problems',
		'easy': 'easy_problems',
		'med': 'med_problems',
		'hard': 'hard_problems',
	}

	random.choice(choices[diff])

# print(get_random_problem('easy'))





