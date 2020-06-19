## bustme
  bustme is A Directory brute forcing tool that assesses if pages exist according to the returned response body. If it contains a strings defined in the page of redirection then the request was redirected. If the text doesnot exist then this is most likely a new page.


## Installation:
> git clone https://github.com/akenofu/bustme.git

> cd bustme

## Usage
> python3 bustme.py -u http://localhost:3000 -s '<title>OWASP Juice Shop</title>' -w /root/wordlist.txt

> python3 bustme.py -u http://localhost:3000 -s '<title>OWASP Juice Shop</title>' -w /root/wordlist.txt -o ok.txt -v  -p http://127.0.0.1:8080 -c 'language=en; welcomebanner_status=dismiss' -t 20

## Preview

![output](https://raw.githubusercontent.com/akenofu/bustme/master/screenshots/Screenshot%20at%202020-01-29%2005-34-55.png)

![help](https://raw.githubusercontent.com/akenofu/bustme/master/screenshots/Screenshot%20at%202020-01-29%2005-36-25.png)
