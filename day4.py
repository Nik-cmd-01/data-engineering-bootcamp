# Day 4: Read file into a list

languages = []

with open("languages.txt", "r") as file:
    for line in file:
        languages.append(line.strip())  # remove newline characters

print("Languages List:", languages)

language_dict = {lang: len(lang) for lang in languages}
print("Language Dictionary:", language_dict)

# Tuple of top 3
top_3 = tuple(languages[:3])
print("Top 3 Languages:", top_3)

# Set of all letters
letters = set("".join(languages))
print("Unique letters in all languages:", letters)

with open("processed_languages.txt", "w") as file:
    file.write("Language Lengths:\n")
    for lang, length in language_dict.items():
        file.write(f"{lang}: {length}\n")
    
    file.write("\nTop 3 Languages:\n")
    for lang in top_3:
        file.write(lang + "\n")

print("Processed data saved to file!")
