"""
Usage: python cli-utility-count-words.py --string "Hi there, I am participating in Hacktoberfest"
"""
import click

@click.command()
@click.option('--string', help='Counts number of words in the entered string')


def count_words(string):
    """Simple program that counts number of words in the entered string"""
    if string is None:
        print('Please pass --string with your sentence. Usage: python cli-utility-count-words.py --string "Hi there, I am participating in Hacktoberfest"')
    else: 
        print(f'Words: {len(string.split(" "))}')

if __name__ == '__main__':
    count_words()