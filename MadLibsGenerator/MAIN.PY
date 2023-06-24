def mad_libs_generator():
    # User inputs
    adjective = input("Enter an adjective: ")
    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adverb = input("Enter an adverb: ")

    # Generate the story
    story = f"Once upon a time, there was a {adjective} {noun} who loved to {verb} {adverb}."

    # Print the story
    print("\nHere's your Mad Libs story:\n")
    print(story)

# Generate a Mad Libs story when the program runs
mad_libs_generator()
