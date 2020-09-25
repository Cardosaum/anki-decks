#!/usr/bin/env python3

from pathlib import Path
import csv
import sys

# print(us[0])

def clean_borders(borders: list):
    s = list()
    for f in borders:
        s.append(f.strip().lower())
    return s

def get_n_bordering(borders: str):
    b = clean_borders(borders.split(","))
    if b[0] == "":
        return 0
    return len(b)

def find_states(states: list, borders: list):
    s = list()
    borders = clean_borders(borders)
    for f in states:
        if f[0].lower() in borders:
            s.append(f)
    return(s)


def format_borders(borders: str):
    return clean_borders(borders.split(","))


def find_states_codes(states: list, borders: list):
    m = find_states(states, borders)
    s = [i[2] for i in m]
    return s


def read_svg_template(svg='us_template.svg'):
    return Path(svg).open().readlines()

def svg_color_state(state: str):
    return "#{} {}".format(state, "{fill:#bd93f9}\n")

def svg_color_bordering(bordering: list):
    s = list()
    for f in sorted(bordering):
        t = "#{} {}".format(f, "{fill:#50fa7b;opacity:0.8}\n")
        s.append(t)
    return s

def svg_create_state_borders(filename: str, state: str, borders: list, svg='us_template.svg'):
    s = read_svg_template(svg)
    s[11] = svg_color_state(state)
    s[12:12] = svg_color_bordering(borders)
    Path(filename).open("w").writelines(s)

def svg_create_state_only(filename: str, state: str, svg='us_template.svg'):
    s = read_svg_template(svg)
    s[11] = svg_color_state(state)
    Path(filename).open("w").writelines(s)


def main():
    us_header = ["name", "abbreviation", "largest_city", "capital", "bordering", "flag", "state_nickname", "nickname_reverse", "blankmap", "location", "n_bordering", "Tags"]
    us = [f[:-1] for f in csv.reader(Path("us.txt").open(), delimiter='\t')]
    svgf = Path("us_template.svg").open().readlines()
    flags = Path("flags.txt").open().readlines()
    f = Path("us_states.csv").open("w")
    c = csv.writer(f)
    c.writerow(us_header)

    for u in range(len(us)):
        i = us[u]
        i.append(f'<img src="us_state_{i[2]}.svg">')
        del i[1]
        del i[7]
        i.insert(-1, '<img src="us_base.svg">')
        i[5] = flags[u].strip()
        if i[4] == "None":
            i[4] = str()
        i.append(get_n_bordering(i[4]))
        i.append("mcs::subjects::geography::political::countries::united_states::states")
        svg_create_state_only(f'us_stateOnly_{i[1]}.svg', i[1])
        # svg_create_state_borders(f'us_stateBorders_{i[1]}.svg', i[1], find_states_codes(us, format_borders(i[4])))
        print(i)
        # if i[1] == "CA":
        #     print(i)
        # else:
        #     continue
        # # sys.exit()

        # s = svgf
        # s[11] = "#{} {}\n".format(i[1], "{fill:#bd93f9}")
        # us_svg = Path(f'us_state_{i[1]}.svg').open("w")

        # write data to final file
        c.writerow(i)


if __name__ == "__main__":
    us = [f[:-1] for f in csv.reader(Path("us.txt").open(), delimiter='\t')]
    # a = find_states_codes(us, format_borders('Oregon, Nevada, Arizona'))
    # print(a)
    # print(svg_color_bordering(a))
    # print(find_states_codes(us, format_borders('Oregon, Nevada, Arizona')))
    print(svg_color_bordering(find_states_codes(us, format_borders("Oregon, Nevada, Arizona"))))
    # sys.exit()

    main()

#
# print(find_states_codes(us, us[0][5].split(",")))
# print(find_states(us, us[0][5].split(",")))
# print(us)
sys.exit()



def n_bordering(border: str):
    border = border.split(",")
    if border[0] == str():
        return str()
    else:
        return len(border)


for u in range(len(us)):
    i = us[u]
    i = i.split("\t")[:-1]
    i.append(f'<img src="us_state_{i[2]}.svg">')
    del i[1]
    del i[7]
    i.insert(-1, '<img src="us_base.svg">')
    i[5] = flags[u].strip()
    if i[4] == "None":
        i[4] = str()
    i.append(n_bordering(i[4]))
    i.append("mcs::subjects::geography::political::countries::united_states::states")

    s = svgf
    s[11] = "#{} {}\n".format(i[1], "{fill:#bd93f9}")
    us_svg = Path(f'us_state_{i[1]}.svg').open("w")

    # write data to final file
    us_svg.writelines(s)
    c.writerow(i)
