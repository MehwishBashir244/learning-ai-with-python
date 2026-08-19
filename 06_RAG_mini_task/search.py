def search_notes(question):
    with open("notes.txt", "r", encoding="utf-8") as file:
        notes = file.read()

    relevant_lines = []

    for section in notes.split("\n\n"):
        for word in question.split():
            if word.lower() in section.lower():
                relevant_lines.append(section)
                break

    return "\n".join(relevant_lines)