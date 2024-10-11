from spellchecker import SpellChecker

def spell_check_resume(resume_text):
    spell = SpellChecker()

    # Tokenize the resume text
    words = resume_text.split()

    # Find misspelled words
    misspelled = spell.unknown(words)

    # Collect corrections
    corrections = {}
    for word in misspelled:
        corrections[word] = spell.correction(word)

    return corrections

if __name__ == "__main__":
    resume_text = """
    John Doe
    123 Main Street
    Anytown, USA
    johndoe@email.com

    Objective:
    Seeking a challenging position as a software engineer.

    Education:
    Bachelor of Science in Computer Science
    XYZ University, Anytown, USA
    Graduated: May 2022

    Experience:
    Software Developer Intern
    ABC Company, Anytown, USA
    June 2021 - August 2021
    - Developed web applications using Python and Django framework.
    - Collaborated with the team to design and implement new features.

    Skills:
    - Programming languages: Python, Java, JavaScript
    - Web development: HTML, CSS, JavaScript, Django
    - Version control: Git

    References:
    Available upon request
    """

    corrections = spell_check_resume(resume_text)
    if corrections:
        print("Mistakes found in the resume:")
        for mistake, correction in corrections.items():
            print(f"- '{mistake}' should be corrected to '{correction}'")
    else:
        print("No spelling mistakes found in the resume.")
