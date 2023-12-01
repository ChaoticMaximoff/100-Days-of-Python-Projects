PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

names = [name.strip("\n") for name in names]

with open("./Input/Letters/starting_letter.txt") as sample_letter:
    letter = sample_letter.read()

    for name in names:
        with open(f"./Output/ReadyToSend/letter_to_{name}.txt", mode="w") as output_letter:
            output_letter.write(letter.replace(PLACEHOLDER, name))

