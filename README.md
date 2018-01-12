# WebAgency
Use Python and Splinter to auto-exe tasks in browsers.

## Environment: ##

Windows:

Chrome Driver: 
> Download from `https://chromedriver.storage.googleapis.com/index.html?path=2.35/`
> 
> Put it in C disk

Python: only Python 2.7+ is supported

Splinter: `pip install splinter`

Selenium: `pip install selenium`

## Document: ##

Splinter: `https://splinter.readthedocs.io/en/latest/`


Steps:
1. Set up above environment

2. Set up selenium and use chrome.
	
>     from splinter import Browser
>     
>     executable_path = {'executable_path':'C:\Google\chromedriver.exe'}
>     
>     browser = Browser('chrome', **executable_path)
    

3. 

