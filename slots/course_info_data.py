def get_substring_label_truple(intent, label_indicator, label):
    start = intent.find(label_indicator)
    end = start + len(label_indicator)
    return (start, end, label)


def get_data():
    CS_COURSES = [
        # "C S 110",
        # "C S 111",
        # "C S 117",
        # "C S 150",
        # "C S 151",
        # "C S 152",
        # "C S 153",
        # "C S 154",
        # "C S 155",
        # "C S 156",
        # "C S 157",
        # "C S 158",
        # "C S 159",
        # "C S 171G",
        # "C S 172",
        # "C S 209",
        # "C S 271",
        # "C S 272",
        # "C S 273",
        # "C S 278",
        # "C S 343",
        # "C S 370",
        # "C S 371",
        # "C S 372",
        # "C S 375",
        # "C S 409",
        # "C S 419",
        # "C S 448",
        # "C S 449",
        # "C S 450",
        # "C S 451",
        # "C S 452",
        # "C S 453",
        # "C S 454",
        # "C S 455",
        # "C S 456",
        # "C S 457",
        # "C S 458",
        # "C S 459",
        # "C S 460",
        # "C S 462",
        # "C S 463",
        # "C S 464",
        # "C S 465",
        # "C S 466",
        # "C S 468",
        # "C S 469",
        # "C S 471",
        # "C S 473",
        # "C S 474",
        # "C S 475",
        # "C S 476",
        # "C S 477",
        # "C S 478",
        # "C S 479",
        # "C S 480",
        # "C S 481",
        # "C S 482",
        # "C S 483",
        # "C S 484",
        # "C S 485",
        # "C S 486",
        # "C S 487",
        # "C S 488",
        # "C S 489",
        # "C S 491",
        # "C S 493",
        # "C S 494",
        # "C S 496",
        # "C S 502",
        # "C S 503",
        # "C S 504",
        # "C S 505",
        # "C S 506",
        # "C S 508",
        # "C S 509",
        # "C S 510",
        # "C S 513",
        # "C S 514",
        # "C S 515",
        # "C S 516",
        # "C S 517",
        # "C S 518",
        # "C S 519",
        # "C S 521",
        # "C S 522",
        # "C S 570",
        # "C S 571",
        # "C S 573",
        # "C S 574",
        # "C S 575",
        # "C S 579",
        # "C S 581",
        # "C S 582",
        # "C S 583",
        # "C S 584",
        # "C S 586",
        # "C S 587",
        # "C S 589",
        # "C S 598",
        # "C S 599",
        # "C S 600",
        # "C S 700",
        "Computer Literacy",
        "Computer Science Principles",
        "Introduction to Computer Animation",
        "C Programming",
        "C++ Programming",
        "Java Programming",
        "Python Programming I",
        "Python Programming II",
        "Internet Programming I",
        "Internet Programming II",
        "Topics in Software Programming and Applications",
        "R Programming I",
        "R Programming II",
        "Computer Science I Transition",
        "Object Oriented Programming Transition",
        "Introduction to Data Structures Transition",
        "Machine Programming and Organization Transition",
        "Discrete Math for Computer Science Transition",
        "Compilers and Automata Transition",
        "Software Development Transition",
        "Data Structure and Algorithms Transition",
        "Programming Language Structure I",
        "Architectural Concepts I",
        "Operating Systems I",
        "Computer Graphics I",
        "Digital Game Design",
        "Computer Security",
        "Special Topics",
        "Linux System Administration",
        "User Interface Design",
        "Introduction to Data Mining",
        "Algorithm Design and Implementation",
        "Database Management Systems I",
        "Introduction to Robotics",
        "Computer Networks I",
        "Artificial Intelligence I",
        "Computer Graphics I",
        "Bioinformatics Programming",
        "Automata, Languages, Computability",
        "Computer Security",
        "Introduction to Smart Grids",
        "Human-Centered Computing",
        "Bioinformatics",
        "Digital Game Design",
        "Visual Programming",
        "Applied Machine Learning I",
        "Parallel Programming",
        "Cloud and Edge Computing",
        "Analysis of Algorithms",
        "Programming Language Structure II",
        "Architectural Concepts II",
        "Operating Systems II",
        "Artificial Intelligence II",
        "Special Topics",
        "Advanced Software Engineering",
        "Database Management Systems II",
        "Advanced Cryptography",
        "Computer Networks II",
        "Algorithms in Systems Biology",
        "Advanced Human-Centered Computing",
        "Special Research Problems",
        "Master's Project",
        "Master's Thesis",
        "Pre-dissertation Research",
        "Doctoral Dissertation",
    ]

    COURSE_INFO_TRAIN_DATA = []
    COURSE_TIME_LABEL = "COURSE_TIME"
    COURSE_CRED_LABEL = "COURSE_CRED"
    COURSE_ROOM_LABEL = "COURSE_ROOM"
    COURSE_PROFESSOR_LABEL = "COURSE_PROFESSOR"

    for course in CS_COURSES:
        text = "What are the meeting times for " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "meeting times", COURSE_TIME_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        print('("' + text + '","course","meeting times","' + COURSE_TIME_LABEL + '"),')

        text = "What days are " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "What days", COURSE_TIME_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        print('("' + text + '","course","What days","' + COURSE_TIME_LABEL + '"),')

        text = "When is " + course + " class?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "When is", COURSE_TIME_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        print('("' + text + '","course","When is","' + COURSE_TIME_LABEL + '"),')

        text = "How many credits is " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "credits", COURSE_CRED_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        print('("' + text + '","course","credits","' + COURSE_CRED_LABEL + '"),')

        text = "Who is teaching " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "teaching", COURSE_PROFESSOR_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        print('("' + text + '","course","teaching","' + COURSE_PROFESSOR_LABEL + '"),')

        text = "Who is the professor for " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(
                        text, "professor", COURSE_PROFESSOR_LABEL
                    )
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        print('("' + text + '","course","professor","' + COURSE_PROFESSOR_LABEL + '"),')

        text = "What room is " + course + " in?"

        my_tuple = (
            text,
            {"entities": [get_substring_label_truple(text, "room", COURSE_ROOM_LABEL)]},
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        print('("' + text + '","course","room","' + COURSE_ROOM_LABEL + '"),')

        text = "Where is " + course + "?"

        my_tuple = (
            text,
            {
                "entities": [
                    get_substring_label_truple(text, "Where", COURSE_ROOM_LABEL)
                ]
            },
        )
        COURSE_INFO_TRAIN_DATA.append(my_tuple)
        print('("' + text + '","course","Where","' + COURSE_ROOM_LABEL + '"),')

    COURSE_INFO_LABELS = []
    COURSE_INFO_LABELS.append(COURSE_CRED_LABEL)
    COURSE_INFO_LABELS.append(COURSE_PROFESSOR_LABEL)
    COURSE_INFO_LABELS.append(COURSE_ROOM_LABEL)
    COURSE_INFO_LABELS.append(COURSE_TIME_LABEL)

    return COURSE_INFO_TRAIN_DATA, COURSE_INFO_LABELS