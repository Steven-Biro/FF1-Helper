from typing import *
from .data.spells import (
    get_spells,
    Spell,
    get_spell_keywords,
    print_keyword_info,
)
from fuzzywuzzy import fuzz, process
import sys

spells = get_spells()
MIN_SCORE = 70
first_args = ["spells", "skills", "weapons", "gear", "enemies"]


def main() -> None:
    args = sys.argv
    first = args[1]
    second: Optional[str]
    try:
        second = args[2]
    except IndexError:
        second = None

    first_res: Tuple[str, int] = process.extractOne(first, first_args)
    if first_res[1] >= MIN_SCORE:
        if first_res[0] == "spells":
            if second is None:
                print(spells)
            else:
                spell_keywords = get_spell_keywords()
                second_res: List[Tuple[str, int]] = process.extractBests(
                    second, spell_keywords, score_cutoff=MIN_SCORE
                )
                potential_matches = [second_res[0][0]]
                potential_matches.extend(
                    [
                        x[0]
                        for x in second_res[1:]
                        if second_res[0][1] - x[1] <= 5
                        and second_res[0][1] != 100
                    ]
                )

                if len(potential_matches) > 1:
                    string = "Multiple potential matches found:"
                    for match in potential_matches:
                        string += f"\n{match}"
                    print(string)

                elif len(potential_matches) == 1:
                    print_keyword_info(potential_matches[0])
                else:
                    print(second_res)
