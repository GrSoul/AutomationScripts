#HTML post creator for any website
#Add you post page website code after the 'DOCTYPE' section. Mind the tags for page title, paragrapf etc.

import textwrap

def generate_html():
    html_content = ""
    while True:
        print("##### Καλωσήρθες στο δημιουργό άρθρων της ιστοσελίδας της Antisel \nΕπίλεξε ένα HTML element για να προσθέσεις στο post σου (ή δώσε 'OK' για ολοκλήρωση):\n")
        print("1. Τίτλος άρθρου")
        print("2. Παράγραφος")
        print("3. Εικόνα")
        print("4. Αριθμημένη λίστα")
        print("5. Bullet λίστα")
        user_input = input("\nΔώσε την επιλογή σου: ")
        if user_input == "OK":
            break
        elif user_input == "1":
            title_text = input("Πρόσθεσε τίτλο: ")
            html_content += f"<h1>{title_text}</h1>"
        elif user_input == "2":
            paragraph_text = input("Πρόσθεσε παράγραφο: ")
            html_content += f"<p>{paragraph_text}</p>"
        elif user_input == "3":
            image_url = input("Enter image URL: ")
            alt_text = input("Enter alternate text: ")
            html_content += f"<img src='{image_url}' alt='{alt_text}'/>\n"
        elif user_input == "4":
            html_content += "<ol>"
            while True:
                list_item = input("Πρόθεσε αντικείμενο λίστας (ή δώσε 'done' για ολοκλήρωση): ")
                if list_item == "done":
                    html_content += "</ol>"
                    break
                else:
                    html_content += f"<li>{list_item}</li>"
        elif user_input == "5":
            html_content += "<ul>\n"
            while True:
                list_item = input("Πρόθεσε αντικείμενο λίστας (ή δώσε 'done' για ολοκλήρωση): ")
                if list_item == "done":
                    html_content += "</ul>\n"
                    break
                else:
                    html_content += f"  <li>{list_item}</li>\n"
        else:
            print("Λάθος επιλογή. Παρακαλώ δοκίμασε ξανά.")
    file_name = input("Δώσε όνομα αρχείου (π.χ. index.html): ")
    with open(file_name, "w") as f:
        f.write(textwrap.dedent(f"""
        <!DOCTYPE html>
            <html>
              <head>
                <title>{file_name}</title>
              </head>
              <body>
                {html_content}
              </body>
            </html>
        """))
    print(f"File saved as {file_name}")

generate_html()
