import pandas as pd


def build_vocab():
    return set(pd.read_csv(
            '../metallica-words.csv', 
            sep=',', 
            encoding='latin-1')['Word'].tolist())

def raw_text_to_csv(filename, vocab):
    # read
    with open(filename) as rf:
        words = [ w for w in rf.read().lower().replace('\n', '').replace(',','').split(' ') if w and not '[' in w ]
    # write
    with open(filename + '.csv', 'w') as wf:
        wf.write('id,word')
        for i,w in enumerate(words):
            if w in vocab:
                wf.write('\n{},{}'.format(i, w))


if __name__ == '__main__':
    vocab = build_vocab()
    #filenames = [ 'deathmagnetic', 'reload' ]
    filenames = [ 'killemall' ]
    [ raw_text_to_csv(filename, vocab) for filename in filenames ]
