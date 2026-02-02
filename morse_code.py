# Morse Code Dictionary (A-Z and 0-9)
morse_code = {
    # Letters A-Z
    'A': ".-", 'B': "-...", 'C': "-.-.", 
    'D': "-..", 'E': ".", 'F': "..-.",
    'G': "--.", 'H': "....", 'I': "..",
    'J': ".---", 'K': "-.-", 'L': ".-..",
    'M': "--", 'N': "-.", 'O': "---",
    'P': ".--.", 'Q': "--.-", 'R': ".-.",
    'S': "...", 'T': "-", 'U': "..-",
    'V': "...-", 'W': ".--", 'X': "-..-",
    'Y': "-.--", 'Z': "--..",
    
    # Numbers 0-9
    '0': "-----", '1': ".----", '2': "..---",
    '3': "...--", '4': "....-", '5': ".....",
    '6': "-....", '7': "--...", '8': "---..",
    '9': "----."
}

def text_to_morse(text):
    """Convert English text and numbers to Morse code"""
    result = []
    for char in text.upper():
        if char in morse_code:
            result.append(morse_code[char])
        elif char == ' ':
            result.append('/')  # Word separator
        else:
            result.append("?")  # Unknown character
    return ' '.join(result)

def main():
    print("🔤 Text to Morse Code Converter")
    print("=" * 50)
    print("Supports: A-Z letters and 0-9 numbers")
    print("=" * 50)
    
    text_input = input("Enter text or numbers: ")
    morse_result = text_to_morse(text_input)
    
    print("\n" + "=" * 50)
    print("📊 Result:")
    print(f"Input: {text_input.upper()}")
    print(f"Morse Code: {morse_result}")
    print("=" * 50)

if __name__ == "__main__":
    main()