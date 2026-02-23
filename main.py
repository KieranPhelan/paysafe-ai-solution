"""File to analyse mock customer enquiries with AI assistant."""

from dotenv import load_dotenv
from openai import OpenAI

from mock_enquiries import ENQUIRIES
from request import analyse_enquiry


if __name__ == "__main__":

    load_dotenv()

    client = OpenAI()

    # for enquiry in ENQUIRIES:
    #     result = analyse_enquiry(client, enquiry["message"])
    #     print(result)

    enquiry = """Hey I just logged in to my account 
    and suddenly the application shows 'Your account 
    is restricted and I can't make any transactions. 
    It says contact us to remove restrictions. I don't 
    know what happened suddenly. I didn't even do anything 
    I had some funds in the account and just went to 
    withdrew them from there but I suddenly see this. 
    What's the quickest solution to solve this. I don't 
    know what's the issue really is so I am choosing a 
    random issue. Kindly tell me what happened to my 
    account and how can I prevent it. And why don't you 
    guys send an email or a push notification before 
    doing this?? I needed to withdraw funds right now and 
    I am stuck because of this random action by your team. 
    Kindly resolve this ASAP!!"""

    result = analyse_enquiry(client, enquiry)

    print(result)
