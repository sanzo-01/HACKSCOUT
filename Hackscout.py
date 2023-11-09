import os
import time
import sys
import instaloader
import requests
import whois
import phonenumbers
import subprocess
from bs4 import BeautifulSoup
from phonenumbers import carrier, geocoder, timezone

bot = instaloader.Instaloader()

R = '\033[31m'  # red
G = '\033[32m'  # green
C = '\033[36m'  # cyan
W = '\033[0m'   # white
Y = '\033[33m'  # yellow

os.system('cls' if os.name =='nt' else 'clear')

banner = f'''   
{G}───────█████████████████████
{G}────████▀─────────────────▀████
{G}──███▀───────────────────────▀███
{G}─██▀───────────────────────────▀██
{G}█▀───────────────────────────────▀█ 
{G}█─────────────────────────────────█   {Y}Program : Your ultimate companion{Y}
{G}█───█████─────────────────█████───█   {Y}HackScout 1.0.47{Y}      
{G}█──██▓▓▓███─────────────███▓▓▓██──█   {Y}Please use this tools only{Y} 
{G}█──██▓▓▓▓▓██───────────██▓▓▓▓▓██──█   {Y}for educational purpose{Y}
{G}█──██▓▓▓▓▓▓██─────────██▓▓▓▓▓▓██──█
{G}█▄──████▓▓▓▓██───────██▓▓▓▓████──▄█   {Y}More tools adding soon in{Y}
{G}▀█▄───▀███▓▓▓██─────██▓▓▓███▀───▄█▀   {Y}1.1.0 update stay tuned{Y}
{G}──█▄────▀█████▀─────▀█████▀────▄█
{G}─▄██───────────▄█─█▄───────────██▄
{G}─███───────────██─██───────────███
{G}─███───────────────────────────███
{G}──▀██──██▀██──█──█──█──██▀██──██▀
{G}───▀████▀─██──█──█──█──██─▀████▀
{G}────▀██▀──██──█──█──█──██──▀██▀
{G}──────────██──█──█──█──██
{G}───────────█▄▄█▄▄█▄▄█▄▄█
{G}
'''

class extra:
    @staticmethod
    def write(text):
        for char in text:
            time.sleep(0.08)
            sys.stdout.write(char)
            sys.stdout.flush()

class x:
    @staticmethod
    def write(text):
        for Y in text:
            time.sleep(0.02)
            sys.stdout.write(Y)
            sys.stdout.flush()

extra.write(f"{R}[ X ] Starting tool please wait ....\n")
time.sleep(5)

x.write("████████████████████████████████████████")
time.sleep(2)


def menu():
    print("[ 1 ] instascrape                             [ 2 ] IP lookup")
    print("[ 3 ] Webcrawl                                [ 4 ] Phone number")
    print("[ 5 ] Domain lookup")

os.system('cls' if os.name == 'nt' else 'clear')

print(banner)
menu()
print("")
option = int(input("Choose your option: "))

while option != 0:
    if option == 1:
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(banner)
            username = input("Enter account username: ")
            print("")
            extra.write("[ X ] Extracting info. Please wait...\n")
            time.sleep(2)
            extra.write("[ X ] Getting profile ...\n")
            
            profile = instaloader.Profile.from_username(bot.context, username)
            
            username1 = profile.username
            userid = profile.userid
            mediacount = profile.mediacount
            igtv = profile.igtvcount
            following = profile.followees
            follower = profile.followers
            bio = profile.biography
            hashtag = profile.biography_hashtags
            mentions = profile.biography_mentions
            pfp = profile.profile_pic_url
            story = profile.has_public_story
            private = profile.is_private
            external_url = profile.external_url
            verified = profile.is_verified
            print("Scraping done...")
            print("")
            print(f"{R}Username: {username1}")
            print(f"{R}User id: {userid}")
            print(f"{R}No of posts: {mediacount}")
            print(f"{R}Igtv count: {igtv}")
            print(f"{R}Following: {following}")
            print(f"{R}Followers: {follower}")
            print(f"{R}User bio: {bio}")
            print(f"{R}Hashtag in bio: {hashtag}")
            print(f"{R}Mentions in bio: {mentions}")
            print(f"{R}Pfp: {pfp}")
            print(f"{R}Has story: {story}")
            print(f"{R}Private account: {private}")
            print(f"{R}External urls: {external_url}")
            print(f"{R}Is verified: {verified}")
            back = input("Press enter to exit: ")
            break

        except Exception as e:
            print("Error!! Please try again later"+e)
            break

    elif option==2:
        try:
           os.system('cls' if os.name =='nt' else 'clear')
           print(banner)
           ip_address = input(f"{G}Enter the ip you want to lookup: ")
           response = requests.get(f"https://ipinfo.io/{ip_address}/json")
           data = response.json()
           extra.write(f"{G}Getting info ...\n")
           print(f"{R}IP Address: " + data.get("ip", "N/A"))
           print(f"{R}City: " + data.get("city", "N/A"))
           print(f"{R}Region: " + data.get("region", "N/A"))
           print(f"{R}Country: " + data.get("country", "N/A"))
           print(f"{R}Location: " + data.get("loc", "N/A"))
           print(f"{R}Organization: " + data.get("org", "N/A"))
           print("")
   
           back = input(f"{G}Press enter to exit: ")
           break

        except Exception as e:
            print("Error!! please try again later")
            break

    elif option==3:
        try:
            os.system('cls' if os.name =='nt' else 'clear')
            print(banner)
            webname = input(f"{G}Enter website link you want to crawl: ")
            soup = BeautifulSoup(webname, 'html.parser')
            links = [link.get('href') for link in soup.find_all('a')]
            for link in links:
                print(links)
                print("")
                back = input(f"{G}Press enter to exit: ")
                break
        except Exception as e:
            print("Unable to crawl!!")     
            break
    
    elif option==4:
        try:
           os.system('cls' if os.name =='nt' else 'clear')
           print(banner)
           number = input(f"{G}Enter phone number you want to trace: ")
           parsed_number = phonenumbers.parse(number, None)
           country = geocoder.description_for_number(parsed_number, "en")
           location = geocoder.description_for_valid_number(parsed_number, "en")
           carrier_name = carrier.name_for_number(parsed_number, 'en')
           timezones = timezone.time_zones_for_number(parsed_number)
           validity = phonenumbers.is_valid_number(parsed_number) 
           possible = phonenumbers.is_possible_number(parsed_number) 
           national_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
           international_format = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
           normalized_number = phonenumbers.normalize_digits_only(number)
           country_code = parsed_number.country_code
           region_code = phonenumbers.region_code_for_country_code(country_code)
           line_type = carrier.number_type(parsed_number)
           valid_length = phonenumbers.is_possible_number(parsed_number) 

           extra.write(f"{G}Getting info...\n")
           print("")
           print(f"{R}Country: {country}")
           print(f"{R}Location: {location}")
           print(f"{R}Carrier: {carrier_name}")
           print(f"{R}Timezones: {', '.join(timezones)}")
           print(f"{R}Validity: {validity}")
           print(f"{R}Possible: {possible}")
           print(f"{R}National Format: {national_format}")
           print(f"{R}International Format: {international_format}")
           print(f"{R}Normalized Number: {normalized_number}")
           print(f"{R}Country Code: {country_code}")
           print(f"{R}Region Code: {region_code}")
           print(f"{R}Line Type: {line_type}")
           print(f"{R}Valid Length: {valid_length}")
           print("")
           
           back = input(f"{G}Press enter to exit: ")
           break

        except number.NumberParseException as e:
           print("Error: Invalid phone number. Please try again.")
           break
  
        except Exception as e:
            print("Error")
            break
    elif option==5:
        try:
           os.system('cls' if os.name =='nt' else 'clear')
           print(banner)

           domain = input(f"{G}Enter your domain to lookup: ")
           w = whois.whois(domain)
           w.text
           print(f"{R}{w}")

           back = input(f"{G}Press enter to exit: ")
           break

        except Exception as e:
            print("Error!! please try later")
            break
