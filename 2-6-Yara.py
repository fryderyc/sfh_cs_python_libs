import yara

# Compile and match YARA rules
def scan_with_yara(file_path, rule_path):
    rules = yara.compile(rule_path)
    matches = rules.match(file_path)

    if matches:
        for match in matches:
            print("Matched rule:", match.rule)
            print("Matched strings:")
            for string in match.strings:
                print(f"  - Offset: {string[0]}, String: {string[2].decode()}")

    else:
        print("No matches found.")

def main():
    file_path = input("Enter the path to the file to scan: ")
    rule_path = input("Enter the path to the YARA rule file: ")
    scan_with_yara(file_path, rule_path)

if __name__ == '__main__':
    main()