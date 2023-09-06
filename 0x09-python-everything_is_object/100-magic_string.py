#!/usr/bin/python3
def magic_string(data={"count": 0}):
    data["count"] += 1
    return (", ".join(["BestSchool"] * data["count"]))
