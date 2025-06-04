from deep_translator import GoogleTranslator

class SimpleTranslator:
    def __init__(self):
        self.languages = {
            "English"  : "en",
            "Japanese" : "ja",
            "Burmese"  : "my",
            "Korean"   : "ko",
            "Chinese"  : "zh-CN",
            "French"   : "fr",
            "German"   : "de",
            "Spanish"  : "es",
            "Russian"  : "ru",
            "Thai"     : "th"
        }

    def show_menu(self):
        print("-" * 25)
        print("Available Languages\n")
        for index, lang in enumerate(self.languages, 1):
            print(f"{index}. {lang}")
        print("-" * 25)

    def exit_message(self):
        print("Exiting...Bye!")

    def failed_message(self):
        print("Translation Failed!")

    def from_translate(self):
        while True:
            try:
                text = input("Enter text to translate: ").strip()
            except ValueError:
                print("Invalid input. Please enter valid input.")
                
                if text.lower() == "exit":
                    return None
                if text:
                    return text
                print("Please enter some text.")

    def to_translate(self):
        while True:
            try:
                to_lang = input("To translate: ").strip()
            except ValueError:
                print("Invalid input. Please enter valid input.")

                if to_lang.lower() == "exit":
                    return None
                if not to_lang.isdigit():
                    print("Invalid input. Please enter a number.")
                    continue

                dest_choice = int(to_lang) - 1
                if dest_choice not in range(len(self.languages)):
                    print("Invalid choice. Please enter valid number.")
                    continue

            return dest_choice
                
    def translate(self):

        print("\nWelcome to Simple Translator!")
        print("Type 'exit' to quit.")
        self.show_menu()

        while True:
            try:
                text = self.from_translate()
                if text is None:
                    self.exit_message()
                    break

                dest_choice = self.to_translate()
                if dest_choice is None:
                    self.exit_message()
                    break

                dest_lang, dest_code = list(self.languages.items())[dest_choice]
                
                translated = GoogleTranslator(source="auto", target=dest_code).translate(text)
                if translated:
                    print(f"Translation to {dest_lang}: {translated}")
                else:
                    self.failed_message()

                again = input("Translate another sentence? (y/n): ").strip().lower()
                if again in ["n","no"]:
                    print("Thanks for using simple translator!")
                    break
            
            except ValueError:
                print("Invalid input. Please enter valid input.")

            except Exception as e:
                self.failed_message()
                print("Error", e)


if __name__ == "__main__":
    translation = SimpleTranslator()
    try:
        translation.translate()
    except KeyboardInterrupt:
        print("\nExit...Bye!")