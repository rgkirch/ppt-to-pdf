import dropbox
import subprocess
import os

app_key = "frfr1xbptzoc2da"
app_secret = "t0sf2zywhutrcg9"
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

if 1:
	authorize_url = flow.start()
	print '1. Go to: ' + authorize_url
	print '2. Click "Allow" (you might have to log in first)'
	print '3. Copy the authorization code.'
	code = raw_input("Enter the authorization code here: ").strip()
	access_token, user_id = flow.finish(code)
	print access_token, user_id
	with open("token", "w") as f:
		f.write(access_token)
if 0:
	with open("token", "r") as f:
		access_token = f.readline().strip()
	client = dropbox.client.DropboxClient(access_token)
	#print 'linked account: ', client.account_info()
	# find all ppts without pdfs and convert
	ppt_data = client.search( '/', 'ppt', file_limit=10 )
	for ppt in ppt_data:
		print ppt
	# use delta to maintain pdf copies
	#print client.delta()
#for current_dir, dirs_in_current_dir, files_in_current_dir in os.walk("/home/dog/Dropbox"):
	#dirs_in_current_dir[:] = [x for x in dirs_in_current_dir if not x[0] == "."]
