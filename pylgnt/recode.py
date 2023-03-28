from pylgnt.constants.mappings.codepoint.greek import MAPPING


def recode(string):
    return "".join(
        map(
            chr,
            map(lambda codepoint: MAPPING.get(codepoint, codepoint), map(ord, string)),
        )
    )
