from typing import *
import itertools


class Spell(TypedDict):
    level: int
    learnable_by: List[
        Literal[
            "black mage",
            "white mage",
            "red mage",
            "ninja",
            "knight",
            "black wizard",
            "white wizard",
            "red wizard",
        ]
    ]
    price: int
    name: str
    power: Optional[int]
    hit: Optional[int]
    target: Literal[
        "not usable in battle",
        "one enemy",
        "all enemies",
        "caster",
        "one character",
        "all characters",
    ]
    element: Literal[
        "ice",
        "death",
        "earth",
        "fire",
        "lightning",
        "poison/stone",
        "status",
        "time",
        None,
    ]
    magic_type: Literal["black", "white"]
    status: Optional[str]


spells: List[Spell] = [
    Spell(
        name="ice",
        magic_type="black",
        level=2,
        price=400,
        power=40,
        hit=96,
        target="one enemy",
        status=None,
        element="ice",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="ice2",
        magic_type="black",
        level=4,
        price=4,
        power=80,
        hit=96,
        target="all enemies",
        status=None,
        element="ice",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="ice3",
        magic_type="black",
        level=7,
        price=45,
        power=140,
        hit=96,
        target="all enemies",
        status=None,
        element="ice",
        learnable_by=[
            "black mage",
            "black wizard",
            "red wizard",
        ],
    ),
    Spell(
        name="rub",
        magic_type="black",
        level=6,
        price=20,
        power=None,
        hit=96,
        target="one enemy",
        status="insta-death",
        element="death",
        learnable_by=[
            "black mage",
            "black wizard",
        ],
    ),
    Spell(
        name="xxxx",
        magic_type="black",
        level=8,
        price=60,
        power=None,
        hit=None,
        target="one enemy",
        status="insta-death",
        element="death",
        learnable_by=[
            "black wizard",
        ],
    ),
    Spell(
        name="qake",
        magic_type="black",
        level=6,
        price=20,
        power=None,
        hit=103,
        target="all enemies",
        status="insta-death",
        element="earth",
        learnable_by=[
            "black mage",
            "black wizard",
        ],
    ),
    Spell(
        name="fire",
        magic_type="black",
        level=1,
        price=100,
        power=20,
        hit=96,
        target="one enemy",
        status=None,
        element="fire",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="fir2",
        magic_type="black",
        level=3,
        price=1,
        power=60,
        hit=96,
        target="all enemies",
        status=None,
        element="fire",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="fir3",
        magic_type="black",
        level=5,
        price=8,
        power=100,
        hit=96,
        target="all enemies",
        status=None,
        element="fire",
        learnable_by=[
            "black mage",
            "black wizard",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="lit",
        magic_type="black",
        level=1,
        price=100,
        power=20,
        hit=96,
        target="one enemy",
        status=None,
        element="lightning",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="lit2",
        magic_type="black",
        level=3,
        price=1,
        power=60,
        hit=96,
        target="all enemies",
        status=None,
        element="lightning",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="lit3",
        magic_type="black",
        level=6,
        price=20,
        power=120,
        hit=96,
        target="all enemies",
        status=None,
        element="lightning",
        learnable_by=[
            "black mage",
            "black wizard",
            "red wizard",
        ],
    ),
    Spell(
        name="bane",
        magic_type="black",
        level=5,
        price=8,
        power=None,
        hit=103,
        target="all enemies",
        status="insta-death",
        element="poison/stone",
        learnable_by=[
            "black mage",
            "black wizard",
            "red wizard",
        ],
    ),
    Spell(
        name="brak",
        magic_type="black",
        level=7,
        price=45,
        power=None,
        hit=115,
        target="one enemy",
        status="stone",
        element="poison/stone",
        learnable_by=[
            "black wizard",
        ],
    ),
    Spell(
        name="slep",
        magic_type="black",
        level=1,
        price=100,
        power=None,
        hit=96,
        target="all enemies",
        status="sleep",
        element="status",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="mute",
        magic_type="white",
        level=2,
        price=400,
        power=None,
        hit=115,
        target="all enemies",
        status="silence",
        element="status",
        learnable_by=[
            "knight",
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="dark",
        magic_type="black",
        level=2,
        price=400,
        power=None,
        hit=96,
        target="all enemies",
        status="darkness",
        element="status",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="slow",
        magic_type="black",
        level=2,
        price=400,
        power=None,
        hit=115,
        target="all enemies",
        status=None,
        element="status",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="hold",
        magic_type="black",
        level=3,
        price=1,
        power=None,
        hit=115,
        target="one enemy",
        status="paralysis",
        element="status",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="fear",
        magic_type="white",
        level=4,
        price=4,
        power=None,
        hit=96,
        target="all enemies",
        status=None,
        element="status",
        learnable_by=[
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="conf",
        magic_type="black",
        level=4,
        price=4,
        power=None,
        hit=115,
        target="all enemies",
        status="confusion",
        element="status",
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="stun",
        magic_type="black",
        level=6,
        price=20,
        power=None,
        hit=None,
        target="one enemy",
        status="paralysis",
        element="status",
        learnable_by=[
            "black mage",
            "black wizard",
        ],
    ),
    Spell(
        name="blnd",
        magic_type="black",
        level=7,
        price=45,
        power=None,
        hit=None,
        target="one enemy",
        status="darkness",
        element="status",
        learnable_by=[
            "black mage",
            "black wizard",
        ],
    ),
    Spell(
        name="zap!",
        magic_type="black",
        level=8,
        price=60,
        power=None,
        hit=100,
        target="all enemies",
        status="insta-death",
        element="time",
        learnable_by=[
            "black wizard",
        ],
    ),
    Spell(
        name="stop",
        magic_type="black",
        level=8,
        price=60,
        power=None,
        hit=107,
        target="all enemies",
        status="paralysis",
        element="time",
        learnable_by=[
            "black wizard",
        ],
    ),
    Spell(
        name="ruse",
        magic_type="white",
        level=1,
        price=100,
        power=None,
        hit=None,
        target="caster",
        status=None,
        element=None,
        learnable_by=[
            "knight",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="cure",
        magic_type="white",
        level=1,
        price=100,
        power=16,
        hit=None,
        target="one character",
        status=None,
        element=None,
        learnable_by=[
            "knight",
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="harm",
        magic_type="white",
        level=1,
        price=100,
        power=40,
        hit=96,
        target="all enemies",
        status=None,
        element=None,
        learnable_by=[
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="fog",
        magic_type="white",
        level=1,
        price=100,
        power=None,
        hit=None,
        target="one character",
        status=None,
        element=None,
        learnable_by=[
            "knight",
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="lock",
        magic_type="black",
        level=1,
        price=100,
        power=None,
        hit=115,
        target="one enemy",
        status=None,
        element=None,
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="invs",
        magic_type="white",
        level=2,
        price=400,
        power=None,
        hit=None,
        target="one character",
        status=None,
        element=None,
        learnable_by=[
            "knight",
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="lamp",
        magic_type="white",
        level=2,
        price=400,
        power=None,
        hit=None,
        target="one character",
        status="darkness",
        element=None,
        learnable_by=[
            "knight",
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="alit",
        magic_type="white",
        level=2,
        price=400,
        power=None,
        hit=None,
        target="all characters",
        status=None,
        element=None,
        learnable_by=[
            "knight",
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="tmpr",
        magic_type="black",
        level=2,
        price=400,
        power=None,
        hit=None,
        target="one character",
        status=None,
        element=None,
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="cur2",
        magic_type="white",
        level=3,
        price=1,
        power=33,
        hit=None,
        target="one character",
        status=None,
        element=None,
        learnable_by=[
            "knight",
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="hrm2",
        magic_type="white",
        level=3,
        price=1,
        power=80,
        hit=96,
        target="all enemies",
        status=None,
        element=None,
        learnable_by=[
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="heal",
        magic_type="white",
        level=3,
        price=1,
        power=12,
        hit=None,
        target="all characters",
        status=None,
        element=None,
        learnable_by=[
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="afir",
        magic_type="white",
        level=3,
        price=1,
        power=None,
        hit=None,
        target="all characters",
        status=None,
        element=None,
        learnable_by=[
            "knight",
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="lok2",
        magic_type="black",
        level=3,
        price=1,
        power=None,
        hit=115,
        target="all enemies",
        status=None,
        element=None,
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="pure",
        magic_type="white",
        level=4,
        price=4,
        power=None,
        hit=None,
        target="one character",
        status="poison",
        element=None,
        learnable_by=[
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="aice",
        magic_type="white",
        level=4,
        price=4,
        power=None,
        hit=None,
        target="all characters",
        status=None,
        element=None,
        learnable_by=[
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="amut",
        magic_type="white",
        level=4,
        price=4,
        power=None,
        hit=None,
        target="one character",
        status="silence",
        element=None,
        learnable_by=[
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="fast",
        magic_type="black",
        level=4,
        price=4,
        power=None,
        hit=None,
        target="one character",
        status=None,
        element=None,
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="slp2",
        magic_type="black",
        level=4,
        price=4,
        power=None,
        hit=115,
        target="one enemy",
        status="sleep",
        element=None,
        learnable_by=[
            "black mage",
            "black wizard",
            "ninja",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="cur3",
        magic_type="white",
        level=5,
        price=8,
        power=66,
        hit=None,
        target="one character",
        status=None,
        element=None,
        learnable_by=[
            "red mage",
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="hrm3",
        magic_type="white",
        level=5,
        price=8,
        power=120,
        hit=96,
        target="all enemies",
        status=None,
        element=None,
        learnable_by=[
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="hel2",
        magic_type="white",
        level=5,
        price=8,
        power=48,
        hit=None,
        target="all characters",
        status=None,
        element=None,
        learnable_by=[
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="life",
        magic_type="white",
        level=5,
        price=8,
        power=None,
        hit=None,
        target="one character",
        status="insta-death",
        element=None,
        learnable_by=[
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="slo2",
        magic_type="black",
        level=5,
        price=8,
        power=None,
        hit=115,
        target="one enemy",
        status=None,
        element=None,
        learnable_by=[
            "black mage",
            "black wizard",
            "red mage",
            "red wizard",
        ],
    ),
    Spell(
        name="warp",
        magic_type="black",
        level=5,
        price=8,
        power=None,
        hit=None,
        target="not usable in battle",
        status=None,
        element=None,
        learnable_by=[
            "black wizard",
            "red wizard",
        ],
    ),
    Spell(
        name="inv2",
        magic_type="white",
        level=6,
        price=20,
        power=None,
        hit=None,
        target="all characters",
        status=None,
        element=None,
        learnable_by=[
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="fog2",
        magic_type="white",
        level=6,
        price=20,
        power=None,
        hit=None,
        target="all characters",
        status=None,
        element=None,
        learnable_by=[
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="soft",
        magic_type="white",
        level=6,
        price=20,
        power=None,
        hit=None,
        target="one character",
        status="stone",
        element=None,
        learnable_by=[
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="exit",
        magic_type="white",
        level=6,
        price=20,
        power=None,
        hit=None,
        target="not usable in battle",
        status=None,
        element=None,
        learnable_by=[
            "red wizard",
            "white wizard",
        ],
    ),
    Spell(
        name="cur4",
        magic_type="white",
        level=7,
        price=45,
        power=None,
        hit=None,
        target="one character",
        status="all but death and stone",
        element=None,
        learnable_by=[
            "white wizard",
        ],
    ),
    Spell(
        name="hrm4",
        magic_type="white",
        level=7,
        price=45,
        power=160,
        hit=107,
        target="all enemies",
        status=None,
        element=None,
        learnable_by=[
            "white wizard",
        ],
    ),
    Spell(
        name="hel3",
        magic_type="white",
        level=7,
        price=45,
        power=48,
        hit=None,
        target="all characters",
        status=None,
        element=None,
        learnable_by=[
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="arub",
        magic_type="white",
        level=7,
        price=45,
        power=None,
        hit=None,
        target="all characters",
        status=None,
        element=None,
        learnable_by=[
            "red wizard",
            "white mage",
            "white wizard",
        ],
    ),
    Spell(
        name="sabr",
        magic_type="black",
        level=7,
        price=45,
        power=None,
        hit=None,
        target="caster",
        status=None,
        element=None,
        learnable_by=[
            "black wizard",
        ],
    ),
    Spell(
        name="xfer",
        magic_type="white",
        level=8,
        price=60,
        power=None,
        hit=137,
        target="one enemy",
        status=None,
        element=None,
        learnable_by=[
            "white wizard",
        ],
    ),
    Spell(
        name="fade",
        magic_type="white",
        level=8,
        price=60,
        power=160,
        hit=137,
        target="all enemies",
        status=None,
        element=None,
        learnable_by=[
            "white wizard",
        ],
    ),
    Spell(
        name="lif2",
        magic_type="white",
        level=8,
        price=60,
        power=None,
        hit=None,
        target="one character",
        status="insta-death",
        element=None,
        learnable_by=[
            "white wizard",
        ],
    ),
    Spell(
        name="wall",
        magic_type="white",
        level=8,
        price=60,
        power=None,
        hit=None,
        target="one character",
        status=None,
        element=None,
        learnable_by=[
            "white wizard",
        ],
    ),
    Spell(
        name="nuke",
        magic_type="black",
        level=8,
        price=60,
        power=200,
        hit=137,
        target="all enemies",
        status=None,
        element=None,
        learnable_by=[
            "black wizard",
        ],
    ),
]


def get_spell_names() -> List[str]:
    return [spell["name"] for spell in spells]


def get_spell_elements() -> List[str]:
    return list(
        set(
            [
                spell["element"]
                for spell in spells
                if spell["element"] is not None
            ]
        )
    )


def get_spell_statuses() -> List[str]:
    return list(
        set(
            [spell["status"] for spell in spells if spell["status"] is not None]
        )
    )


def get_learnable_by() -> List[str]:
    return list(
        set(
            itertools.chain.from_iterable(
                [spell["learnable_by"] for spell in spells]
            )
        )
    )


def get_spell_keywords() -> Set[str]:
    keywords: List[str] = []
    keywords.extend(get_spell_names())
    keywords.extend(get_spell_elements())
    keywords.extend(get_spell_statuses())
    keywords.extend(get_learnable_by())
    return set(keywords)


def get_spells() -> List[Spell]:
    return spells


def print_keyword_info(keyword: str) -> None:
    names = get_spell_names()
    elements = get_spell_elements()
    statuses = get_spell_statuses()
    learnable_by = get_learnable_by()

    in_names = keyword in names
    in_elements = keyword in elements
    in_statuses = keyword in statuses
    in_learnable_by = keyword in learnable_by

    if in_names:
        print("Spell info:")
        print([spell for spell in spells if spell["name"] == keyword][0])
        print("\n")

    if in_elements:
        print("Element info:")
        print(
            [spell["name"] for spell in spells if spell["element"] == keyword]
        )
        print("\n")

    if in_statuses:
        print("Status info:")
        print([spell["name"] for spell in spells if spell["status"] == keyword])
        print("\n")

    if in_learnable_by:
        print("Spells learnable info:")
        print(
            [
                spell["name"]
                for spell in spells
                if (keyword in spell["learnable_by"])
            ]
        )
        print("\n")