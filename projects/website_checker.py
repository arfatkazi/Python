def website_checker():
        while True:
            
            url_input = input("Enter a website URL (or type 'exit' to quit): ")

            if url_input.lower() == 'exit':
                print("👋 Exiting...  Goodbye!")
                break

            if url_input.startswith('https://'):
                print("✅ This website uses HTTPS (secure)")
            elif url_input.startswith('http://'):
                print("💀 This website uses HTTP (not secure)")
            else:
                print("❌ This doesn't look like a complete URL.")

def main():
    print("🔎  WEBSITE URL CHECKER  🔎")

    website_checker()






if __name__ == '__main__':
    main()