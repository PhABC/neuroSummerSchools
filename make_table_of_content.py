import re
import string
from collections import Counter


if __name__ == '__main__':
    # run make_table_of_content.py to generate proper table of content
    with open('README.md') as f:
        lines = f.readlines()
    intro_index = [i for i, l in enumerate(lines) if '# Table of Content' in l][0]
    content_index = [i for i, l in enumerate(lines) if '# Neuroscience\n' in l][0]
    punct_list = string.punctuation.replace('&', '').replace('?', '')

    table_of_contents = []
    for line in lines[content_index::]:
        n_pound = Counter(line).get('#', 0)
        header = re.findall("\[(.*?)\]", line)
        if n_pound == 1 and len(header) == 0:
            header = [line.replace('#', '').strip()]
        if n_pound > 0 and len(header) > 0:
            header = header[0]
            line_rm_punct = ''.join([c for c in header if c not in punct_list])
            tag = '(#' + '-'.join(line_rm_punct.lower().split()) + ')'
            tag = tag.replace('&', '').replace('???', '')
            if n_pound == 1:
                pre = '- '
            elif n_pound == 2:
                pre = '  * '
            else:
                pre = '  * '
            table_of_contents.append(pre + '[' + header + ']' + tag + '\n')

    f_added = lines[0:intro_index] + ['\n'] + ['# Table of Contents'] + table_of_contents + ['\n'] + lines[content_index-1::]
    output_file = open('new_readme.md', 'w')
    output_file.write("".join(f_added))
