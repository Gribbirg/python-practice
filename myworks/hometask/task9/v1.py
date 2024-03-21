def main(s: str):
    return [
        (el.split("'")[1],
         int(el.split("#")[1].split("->")[0]))
        for el in s.replace("\n", "").split("<section>")[1:]
    ]
