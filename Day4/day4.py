import re

byr = re.compile("^\d{4}$")
iyr = re.compile("^\d{4}$")
eyr = re.compile("^\d{4}$")
hgt = re.compile("^\d{1,3}in|\d{1,3}cm$")
hcl = re.compile("^#[0-9a-fA-F]{6}$")
ecl = re.compile("^(amb|blu|brn|gry|grn|hzl|oth)$")
pid = re.compile("^\d{9}$")


def create_passport(p_input: str) -> dict:
    passport = {}
    pairs = p_input.split(" ")
    for pair in pairs:
        kv = pair.split(":")
        passport[kv[0]] = kv[1]

    return passport


def valid_number_of_keys(passport: dict, keys: set):
    valid = True
    current_passport_keys = list(passport.keys())
    for key in keys:
        if key not in current_passport_keys:
            valid = False
            break
    return valid


def keys_range_validation(passport: dict, keys: set):
    valid = True
    validation = {
        "byr": {"min": 1920, "max": 2002, "regex": byr},
        "iyr": {"min": 2010, "max": 2020, "regex": iyr},
        "eyr": {"min": 2020, "max": 2030, "regex": eyr},
        "hgt": {
            "cm": {"min": 150, "max": 193},
            "in": {"min": 59, "max": 76},
            "regex": hgt,
        },
        "hcl": {"regex": hcl},
        "ecl": {"regex": ecl},
        "pid": {"regex": pid},
    }
    for key in keys:
        try:
            kvalue = passport[key]
        except:
            valid = False
            break
        key_validator = validation[key]
        found = re.findall(key_validator["regex"], kvalue)

        if found:
            if key in ["byr", "iyr", "eyr"]:
                year = int(kvalue)
                if not (key_validator["min"] <= year <= key_validator["max"]):
                    valid = False
                    break
            if key in ["hgt"]:
                if "cm" in kvalue:
                    height = int(kvalue.replace("cm", ""))
                    if not (
                        key_validator["cm"]["min"]
                        <= height
                        <= key_validator["cm"]["max"]
                    ):
                        valid = False
                        break
                if "in" in kvalue:
                    height = int(kvalue.replace("in", ""))
                    if not (
                        key_validator["in"]["min"]
                        <= height
                        <= key_validator["in"]["max"]
                    ):
                        valid = False
                        break

        else:
            valid = False
            break

    return valid


def result() -> int:
    with open("./Day4/input.txt", "rt") as f:
        input_text = f.read()

    split_array = input_text.split("\n")

    passports = []
    acc = ""
    for entry in split_array:
        acc += f" {entry}"
        if entry == "":
            passports.append(acc.strip())
            acc = ""
    passports.append(acc.strip())

    valid_passports = 0
    v_p = []
    valid_keys_no_cid = set(
        (
            "byr",
            "iyr",
            "eyr",
            "hgt",
            "hcl",
            "ecl",
            "pid",
        )
    )
    for pp in passports:
        passport = create_passport(pp)

        are_keys_present = valid_number_of_keys(passport, valid_keys_no_cid)

        are_values_valid = keys_range_validation(passport, valid_keys_no_cid)
        valid = are_keys_present and are_values_valid
        if valid:
            valid_passports += 1
        v_p.append(valid)

    return v_p.count(True)


r = result()