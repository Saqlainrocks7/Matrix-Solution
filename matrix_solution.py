
import json

with open("data.json", "r") as f:
    data = json.load(f)


def build_head_to_head_matrix(data):
    teams = sorted(data.keys())

    # Build header row
    header = ["Tm"] + teams
    table = [header]

    # Build each team row
    for team in teams:
        row = [team]
        for opponent in teams:
            if team == opponent:
                row.append("--")
            else:
                record = data[team][opponent]
                row.append(f"{record['W']}-{record['L']}")
        table.append(row)

    return table

def print_table(table):
    col_widths = [
        max(len(str(row[i])) for row in table)
        for i in range(len(table[0]))
    ]

    for row in table:
        line = "  ".join(
            str(cell).rjust(col_widths[i])
            for i, cell in enumerate(row)
        )
        print(line)

matrix = build_head_to_head_matrix(data)
print_table(matrix)