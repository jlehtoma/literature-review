#!/usr/bin/env python

import os
import re
from git import Repo

BUILD_DIR = "pandoc/build/"

ABSTRACT = "validity_ms_abstract.md"
FIGURES = "validity_ms_figures.md"
FRONT_MATTER = "validity_ms_front_matter.md"
FRONT_MATTER_BUILD = os.path.join(BUILD_DIR,
                                  "validity_ms_front_matter_prep.md")
MAIN_FILE = "validity_ms.md"
MAIN_FILE_BUILD = os.path.join(BUILD_DIR, "validity_ms_prep.md")
TABLES = "validity_ms_tables.md"

GH_ISSUE_URL = "https://github.com/jlehtoma/validityms/issues/"

repo = Repo(".")
current_tag = repo.tags[-1].name


def count_figures():
    figures = 0
    with open(FIGURES, 'r') as f:
        for line in f:
            if line.startswith("__Figure"):
                figures += 1

        return figures


def count_references():
    all_refs = []

    with open(MAIN_FILE, 'r') as f:
        for line in f:
            raw_refs = re.findall(r'\[(@[^]]*)\]', line)
            raw_refs = [ref.split(";") for ref in raw_refs]
            # Flatten the list
            refs = []
            for ref in raw_refs:
                refs = refs + ref
            for ref in refs:
                if ref not in all_refs:
                    all_refs.append(ref)
    return len(all_refs)


def count_tables():
    tables = 0
    with open(TABLES, 'r') as f:
        for line in f:
            if line.startswith("__Table"):
                tables += 1

        return tables


def count_words(fname, include_headers=False, exclude=[]):
    counts = {'num_lines': 0, 'num_words': 0, 'num_chars': 0}

    # Exclude markdown header signs by default
    if not include_headers:
        exclude = exclude + ['#', '##', '###', '####']
    with open(fname, 'r') as f:
        for line in f:
            words = line.split()

            if len(words) == 0 or words[0] in exclude:
                continue

            # Remove known markdown tokens
            for token in ['*', '+', '-']:
                if token in words:
                    words.remove(token)

            counts['num_lines'] += 1
            counts['num_words'] += len(words)
            counts['num_chars'] += len(line)

    return counts


def preprocess_fm_file(input_file, target_file):

    with open(target_file, 'w') as outfile, open(input_file, 'r') as infile:
        for line in infile:
            if "Version" in line:
                line = "{0} {1}\n".format(line, current_tag)

            if "Abstract length" in line:
                abstract_counts = count_words(ABSTRACT, exclude=['Keywords:'])
                # Append two whitespaces for markdown newline
                line = line.replace('xxx', str(abstract_counts['num_words']) +
                                    '  ')
            if "Main text length" in line:
                main_counts = count_words(MAIN_FILE)
                # Append two whitespaces for markdown newline
                line = line.replace('xxx', str(main_counts['num_words']) +
                                    '  ')
            if "Figures" in line:
                line = line.replace("xxx", str(count_figures()) + '  ')
            if "Tables" in line:
                line = line.replace("xxx", str(count_tables()) + '  ')
            if "References" in line:
                line = line.replace("xxx", str(count_references()) + '  ')
            outfile.write(line)


def preprocess_main_file(input_file, target_file):
    with open(target_file, 'w') as outfile, open(input_file, 'r') as infile:
        for line in infile:
            issues = re.findall(r'\[(#[^]]*)\]', line)
            for issue in issues:
                issue_url = GH_ISSUE_URL + issue.replace("#", "")
                link = "([{0}]({1}))".format(issue, issue_url)
                line = line.replace("[" + issue + "]", link)

            outfile.write(line)


preprocess_fm_file(FRONT_MATTER, FRONT_MATTER_BUILD)
preprocess_main_file(MAIN_FILE, MAIN_FILE_BUILD)
