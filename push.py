import subprocess

bashCommand = "git add ."
bashCommand2 = "git commit -m 'python'"
bashCommand3 = "git push -u origin master"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
process = subprocess.Popen(bashCommand2.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
process = subprocess.Popen(bashCommand3.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
