class Console:

    WIDTH = 60

    @classmethod
    def line(cls):
        print("=" * cls.WIDTH)

    @classmethod
    def separator(cls):
        print("-" * cls.WIDTH)

    @classmethod
    def title(cls, text):

        print()

        cls.line()

        print(text)

        cls.line()

    @staticmethod
    def info(text):

        print(text)

    @staticmethod
    def success(text):

        print(f"✅ {text}")

    @staticmethod
    def warning(text):

        print(f"⚠ {text}")

    @staticmethod
    def error(text):

        print(f"❌ {text}")

    @staticmethod
    def lesson(name):

        print()

        print(f"📚 {name}")

    @staticmethod
    def generated(file):

        print(f"   🎤 {file}")

    @staticmethod
    def skipped(file):

        print(f"   ✔ {file}")