
def analyze_string(input_str):
   
    consonants = "bcdfghjklmnpqrstvwxyz"
    lower_str = input_str.lower()
    filtered = sorted([char for char in lower_str if char in consonants])
    consonant_str = ''.join(filtered)
     has_multiple_spaces = input_str.count(' ') > 1
    
    
    return (consonant_str, has_multiple_spaces)


  # Приклад використання функції
   if name == "main":
    example_input = input("Введіть рядок для аналізу: ")
       result = analyze_string(example_input)
       print("\nРезультат аналізу:")
       print(f"Приголосні (за алфавітом): {result[0]}")
       print(f"Більше одного пробілу: {result[1]}")
