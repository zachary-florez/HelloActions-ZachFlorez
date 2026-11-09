import os


def main():
	name = os.getenv("WHO_TO_GREET", "GitHub Actions Student")
	print(f"Hello {name}!")
	print("This program is running inside GitHub Actions.")


if __name__ == "__main__":
	main()
