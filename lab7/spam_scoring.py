import re


def sender_domain(email):
    """Return the lower-case domain, or an empty string for invalid input."""
    if not isinstance(email, str):
        return ""

    email = email.strip()
    if email.count("@") != 1 or any(character.isspace() for character in email):
        return ""

    local, domain = email.split("@")
    if not local or not domain:
        return ""
    return domain.lower()


def first_link(text):
    """Return the first HTTP(S) URL, or an empty string if none is present."""
    if not isinstance(text, str):
        return ""

    match = re.search(r"https?://\S+", text)
    return match.group(0) if match else ""


def shout_ratio(text):
    """Return the fraction of alphabetic characters that are uppercase."""
    if not isinstance(text, str):
        return 0.0

    letters = [c for c in text if c.isalpha()]
    if not letters:
        return 0.0
    upper = [c for c in letters if c.isupper()]
    return len(upper) / len(letters)

def main():
    print("==== Running sender_domain ====")
    user_input = input("Enter a sender email (e.g. offers@Deals.com): ")
    result = sender_domain(user_input)
    print("Sender Domain:", result)

    print("\n==== Running first_link ====")
    user_input = input("Enter a message containing a link: ")
    result = first_link(user_input)
    print("First Link:", result)

    print("\n==== Running shout_ratio ====")
    user_input = input("Enter a message (e.g. FREE prize NOW): ")
    result = shout_ratio(user_input)
    print("Uppercase Ratio:", result)

if __name__ == "__main__":
    main()
