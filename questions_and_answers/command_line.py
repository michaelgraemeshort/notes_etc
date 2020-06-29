import random

questions_and_answers = [
    ("What does > do? How about >>?",
    "Redirects (writes a better word?) the output of the command on the left to whatever's on the right e.g. ls > output.txt. Be careful - will overwrite. >>, on the other hand, appends."),
    ("What does cat do?",
    "Lots of things. For now: use to look at file contents (cat <file>)."),
    ("What does echo do and how is this useful?",
    "Prints out its own arguments. Combine with a redirect (>) to create a file, e.g. echo 'argle bargle' > test.txt"),
    ("What does ? do?",
    "Matches any single character. For example, ?rgh.txt matches argh.txt and urgh.txt."),
    ("What does * do?",
    "'Wildcard' character. Matches zero or more characters, i.e. anything."),
    ("What if a document is so large it won't all fit in the terminal at once when you use cat do display it?",
    "Use less instead of cat. Not more, more is rubbish."),
    ("What does .. represent?",
    "The parent directory."),
    ("What does . represent?",
    "The current working directory."),
    ("What does apt stand for?",
    "Advanced Packaging Tool."),
    ("How do you hide a file or or folder?",
    "Begin its name with a dot."),
    ("Where does an absolute pathname begin? What about a relative pathname?",
    "The root directory and working directory, respectively."),
    ("What does cd - do?",
    "Changes the working directory to the previous one."),
    ("What does the file command do?",
    "file <file> tells you the type of the file and whether it is viewable as text."),
    ("What does /etc contain?",
    "System configuration files."),
    ("What does g* match?",
    "Names that begin with g."),
    ("What does b*.txt match?",
    "Names that begin with b and end with .txt."),
    ("What does Data??? match?",
    "Names that begin with Data followed by exactly 3 more characters."),
    ("What does [abc]* match?",
    "Names that begin with a or b or c."),
    ("What does [[:upper:]]* match?",
    "Names that begin with an uppercase letter."),
    ("What does BACKUP.[[:digit:]][[:digit:]] match?",
    "Names that begin with BACKUP. followed by exactly 2 numerals."),
    ("What does *![[:lower:]] match?",
    "Any filename that does not end with a lowercase letter."),
    ("What should you do before using rm with wildcards?",
    "Run the command with ls first, so you can see exactly what you would remove."),
    ("What does mv my_dir ../*.bak my_new_dir do?",
    "moves the directory my_dir and all files ending in .bak from the parent folder into the directory my_new_dir."),
    ("How to find the location of an executable program?",
    "Using which <program name>."),
    ("How to embed newlines in a command line command?",
    "Escape the newlines with \, so the shell ignores them. Can be used to improve readability."),
    ("What does which <command> do?",
    "Locates the command."),
    ("What does su do? How to undo it?",
    "Gives you superuser privileges. Type exit."),
    ("What does chmod <file or directory> do?",
    "Changes the permissions of a file or directory."),
    ("What does chown do? What about chgrp?",
    "Changes the ownership (file or group, respectively) of a file or directory."),
    ("What is PATH?",
    "A list of files where executable files (programs) are kept."),
    ("What is ~.bashrc?",
    "User configuration file."),
]

print(f"There are currently {len(questions_and_answers)} questions.")

while True:
    random.shuffle(questions_and_answers)
    for i, j in questions_and_answers:
        print('Q.', i)
        input()
        print('A.', j)
        print()
    print('All questions asked. Restarting:')