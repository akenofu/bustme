# bustme
  During my venture to conquer another vulnerable web application OWASP Juice Shop. I aimed to brute force the scoreboard page. However, when running go buster on the site it hit me. The website always servers me to a certain page when the requested url is invalid while sending out a 200 status code, this is also implemented by many web apps specifically single page web apps ( Yes, I am looking at you angular and node devs out there), So here we are a a directory busting tool that checks the response body for strings. If found, the script dooms this as a redirect by the web app. Ifnot then ding ding we have a winner.
## In other words
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
