from prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(ProgrammingLanguage.__str__(ruby))
    print(ProgrammingLanguage.__str__(python))
    print(ProgrammingLanguage.__str__(visual_basic))


main()
