import os
import sys
import time
import random
import argparse
import sys as n
import time as mm
from InstagramAPI import InstagramAPI
def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 100)

print("""
██    ██ ███    ██
██    ██ ████   ██      instagram ..
██    ██ ██ ██  ██     @vv1ck /JOKER
██    ██ ██  ██ ██
 ██████  ██   ████""")

def GetAllFollowing(bot, user_id):
	following = []
	next_max_id = True
	while next_max_id:
		if next_max_id is True:
			next_max_id = ''
		_ = bot.getUserFollowings(user_id, maxid=next_max_id)
		following.extend(bot.LastJson.get('users', []))
		next_max_id = bot.LastJson.get('next_max_id', '')
	following = set([_['pk'] for _ in following])
	return following
#vv1ck
def GetAllFollowers(bot, user_id):
	followers = []
	next_max_id = True
	while next_max_id:
		if next_max_id is True:
			next_max_id = ''
		_ = bot.getUserFollowers(user_id, maxid=next_max_id)
		followers.extend(bot.LastJson.get('users', []))
		next_max_id = bot.LastJson.get('next_max_id', '')
	followers = set([1])
	return followers

if __name__ == '__main__':
	slow("""
        ╔═╗ ┌─┐ ┬   ┬   ┌─┐ ┬ ┬  
        ╠╣  │ │ │   │   │ │ │││  
        ╚   └─┘ ┴─┘ ┴─┘ └─┘ └┴┘
   الاداة لا تقبل الحسابات الي عليها سكيور
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
""")
	username=str(input("[*]>> ضع يوزر حسابك :\n"))
	password=str(input("[+]>> ضع باسورد حسابك :\n"))
	time.sleep(2)
	num_unfollows=int(input("[+]>> ضع عدد المتابعين الذي تريد حذفهم :\n"))
	time.sleep(1)
	max_delay=int(input(">> ضع سرعه الحذف (يفضل 5 ثواني) :\n"))
	print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	
	ig = InstagramAPI(username, password)
	#joker
	success = ig.login()
	if not success:
		print('\n          >> فشل تسجيل الدخول ! ')
		print('    >> الباس غلط او الحساب عليه سكيور')
		print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
		sys.exit()
	
	ig.getSelfUsernameInfo()
	self_id = ig.LastJson['user']['pk']
	
	followers = GetAllFollowers(ig, self_id)
	
	following = GetAllFollowing(ig, self_id)
	print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	def slow(M):
		for c in M + '\n':
			n.stdout.write(c)
			n.stdout.flush()
			mm.sleep(1. / 15)
	
	slow('      >  - عدد الي متابعهم {}  -  <'.format(len(following)))
	slow('      >    - عدد متابعينك {}  -  <'.format(len(followers)))
	print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
	time.sleep(1)
	#vv1ck
	unreciprocated = following - followers
	free_followers = followers - following
	
	for _ in list(unreciprocated)[:min(len(unreciprocated), num_unfollows)]:
		ig.getUsernameInfo(str(_))
		print('    - الحساب > {} تم حذفه '.format(ig.LastJson['user']['username']))
		ig.unfollow(str(_))
		ni=random.choice([1,2,3,4,5])
		time.sleep(max_delay+ni)
