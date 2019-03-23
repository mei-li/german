
import click

with open('german/german.dic', encoding='latin-1') as fp:
    german_words = fp.read().splitlines()


@click.command()
@click.option('--ending', required=True, help='Ending to find')
def find_similar_ending_words(ending): 
    ending = ending.strip().lower()

    for word in german_words:
        if word.strip().lower().endswith(ending):
            print(word)


if __name__ == '__main__':
    find_similar_ending_words()