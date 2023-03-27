from pylgnt.constants.mappings.codepoint.greek import MAPPING


def fix(string):
    return "".join(
        map(
            chr,
            map(lambda codepoint: MAPPING.get(codepoint, codepoint), map(ord, string)),
        )
    )
