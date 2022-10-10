""" Mask an email address
Search for email addresses in a string, extract the email addresses, mask them and re-insert them in the string.

Author: Musketeer Computing
Created: 10th October 2022
"""
import re


def main():
    sentence = input("Enter a sentence")
    emails = re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', sentence)
    if not emails:
        print(' No email address to mask')
        exit()
    d_emails = {}
    for email in emails:
        m_email = mask_email(email)
        if m_email == 'error':
            print('There was an error when masking the email. Stopping the program')
            exit()
        d_emails[email] = m_email
    for k_email, v_email in d_emails.items():
        sentence = re.sub(k_email, v_email, sentence)
    print(sentence)


def mask_email(email):
    lo = email.find('@')
    domain_extension = email.rfind('.')
    word_count = len(email)
    if lo > 0:
        return "{0}#####{1}@{2}###{3}".format(email[0],
                                              email[lo-1],
                                              email[lo+1],
                                              email[domain_extension:word_count])
    else:
        return "error"


if __name__ == "__main__":
    main()
