<h1 align="center">My Public IP API</h1>


Use gh-pages as an API for the public IP (typically for dynamic IPs) of your home network, this repo is deployed without any real IP so what you'll see in [gh-pages](https://msramalho.github.io/my-public-ip-api/) is `{}`

### Instructions
1. Fork this repo/ use it as a template
2. `git clone <YOUR-NEW-REPO>` to a machine in the network whose IP you want to have always accessible
3. Ensure you have python and git
4. Deploy the script with one of the following (or other parallel alternatives you like): 
   1. `python update-ip.py` to update once
   2. `nohup python update-ip.py &` this will send the output to `nohup.out`
   3. `nohup python update-ip.py > logs.txt &` this will send the output to `logs.txt`
   4. you can also use [bg](https://linux.die.net/man/1/bg) or [tmux](https://linux.die.net/man/1/tmux) see [this SO question](https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session) for more ways
5. Enable GH-pages
   1. Go to your repository settings 
   2. Scroll to "GitHub Pages"
   3. Select source: "master branch /docs folder"
6. (you can have your own custom domain) if not check [https://YOUR-USER-NAME.github.io/my-public-ip-api/](https://YOUR-USER-NAME.github.io/my-public-ip-api/) to see something like `{"ipv4": "<YOUR-IPv4>", "ipv6": "<YOUR-IPv6>"}`
7. That is now an endpoint with your public IPs


### Applications
Access servers and services in your home (or wherever) network even though they have dynamic IPs simply by querying your gh-pages endpoint and then use the IP to access them as if you had a static one.

### Customize
By default, the script will check if your IP has changed every 10 seconds and update your gh-pages endpoint **only** if it has, if you want to increase this value, simply update the `UPDATE_INTERVAL` in the [update-ip.py](update-ip.py) in your own copy. 

### Privacy
If you have privacy concerns, you can always make your copy private and change its name to a long and random sequence of chars like `my-public-ip-api-nanananananananananananbatman`
