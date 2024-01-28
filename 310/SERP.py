import threading
import requests
import json
import webbrowser
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import tkinter as tk
from tkinter import scrolledtext, font
 

class WebScannerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Web Scanner")
        
        # Create a StringVar to hold the query
        self.query_var = tk.StringVar()

        # Create a custom font
        custom_font = font.Font(family="Helvetica", size=12)
        
        # Header label
        self.header = tk.Label(self.master, text="CSC 310 Group 3's SERP", font= font.Font(family="Helvetica", size=16, weight="bold"))

        self.header.pack(pady=10)
        
        # Create a Label, Entry, and Button
        self.label = tk.Label(self.master, text="Enter Query:", font=custom_font)
        self.entry = tk.Entry(self.master, textvariable=self.query_var, font=font.Font(family="Helvetica", size=14))
        self.button = tk.Button(self.master, text="Search", command=self.start_search, font=custom_font)

        # Create a ScrolledText widget for displaying results
        self.text_area = scrolledtext.ScrolledText(self.master, wrap=tk.WORD, font=custom_font)

        # Use pack to place components
        self.label.pack(padx=20)
        self.entry.pack(fill=tk.X, padx=100, pady=20)
        self.button.pack(padx=20, pady=20)
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

    def start_search(self):
        self.text_area.delete('1.0', tk.END)  # Clear previous results
        query = self.query_var.get()

        api_key = "AIzaSyB5oLlt7mIO63taSYmQK5ATzClYnQnZrf0"
        cx = "d625ccdc0906f4f30"

        if not query:
            self.text_area.insert(tk.END, "Please enter a search query.\n")
            return

        url = f"https://www.googleapis.com/customsearch/v1?key={api_key}&cx={cx}&q={query}"
        response = requests.get(url)
        data = json.loads(response.text)

        # Check for errors or empty search results
        if 'error' in data:
            self.text_area.insert(tk.END, f"Error: {data['error']['message']}\n")
        elif 'items' not in data:
            self.text_area.insert(tk.END, "No search results found.\n")
        else:
            # Extract search results
            search_results = data['items']

            threads = []
            results = []

            for result in search_results:
                link = result['link']
                thread = threading.Thread(target=self.process_url, args=(link, query, results), name=f"Thread-{len(threads)+1}")
                threads.append(thread)
                thread.start()

            # Wait for all threads to finish
            self.master.after(100, self.check_threads, threads, results)

    def check_threads(self, threads, results):
        for thread in threads:
            if thread.is_alive():
                self.master.after(100, self.check_threads, threads, results)
                return

        # All threads have finished
        self.display_results(results)

    def display_results(self, results):
        self.text_area.insert(tk.END, "\nAll threads have finished. Ranking summaries by relevance:\n\n")

        # Sort results based on the third element of the tuple (the relevance score)
        sorted_results = sorted(results, key=lambda x: x[2], reverse=True)

        link_tag = "link_placeholder"  # Placeholder tag for the link

        for index, (full_url, relevant_paragraph, score) in enumerate(sorted_results, start=1):
            self.text_area.insert(tk.END, f"\nRank {index} - Relevant Paragraph:\n")
            self.text_area.insert(tk.END, f"{relevant_paragraph}\n")
           
            self.text_area.insert(tk.END, f"Relevance Score: {score}\n")
            # Make only the link in this line clickable
            self.text_area.tag_add(link_tag, f"{self.text_area.index(tk.END)}-2c", tk.END)
            self.text_area.tag_config(link_tag, foreground="blue", underline=True)
            self.text_area.tag_bind(link_tag, "<Button-1>", lambda e, url=full_url: self.open_link(url))
            self.text_area.insert(tk.END, f"Direct link to the relevant paragraph: {full_url}\n")
            

            # Remove the old placeholder tag
            self.text_area.tag_remove(link_tag, f"{self.text_area.index(tk.END)}-2c", tk.END)
            # Update the link tag to a new placeholder for the next iteration
            link_tag = f"link_{index}"
            

    def process_url(self, link, search_query, results):
        relevant_paragraph, paragraph_index, score = self.find_relevant_paragraph(link, search_query)

        if paragraph_index != -1:
            fragment_identifier = f"#paragraph-{paragraph_index}"
            full_url = link + fragment_identifier
            result = (full_url, relevant_paragraph, score)
            results.append(result)
        else:
            self.text_area.insert(tk.END, f"Thread {threading.current_thread().name} - No relevant paragraph found.\n")

    def find_relevant_paragraph(self, url, query):
        website_text = self.get_website_text(url)
        paragraphs = website_text.split('\n')

        best_paragraph = None
        best_score = 0
        paragraph_index = -1  # Default value

        for index, paragraph in enumerate(paragraphs, start=1):
            score = self.bag_of_words(query, paragraph)

            if score > best_score:
                best_score = score
                best_paragraph = paragraph
                paragraph_index = index

        return best_paragraph, paragraph_index, best_score

    def get_website_text(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        paragraphs = soup.find_all('p')
        text = ' '.join([paragraph.get_text() for paragraph in paragraphs])
        return text

    def clean_and_tokenize(self, text):
        tokenizer = RegexpTokenizer(r'\w+')
        words = tokenizer.tokenize(text)
        stop_words = {'a', 'an', 'the', 'and', 'or', 'in', 'on', 'of', 'with', 'by', 'for', 'to', 'at'}  # Add more stopwords as needed
        filtered_words = [word.lower() for word in words if word.lower() not in stop_words]
        return filtered_words


    def bag_of_words(self, query, text):
        query_words = self.clean_and_tokenize(query)
        text_words = self.clean_and_tokenize(text)

        query_freqdist = FreqDist(query_words)
        text_freqdist = FreqDist(text_words)

        intersection = set(query_freqdist.keys()) & set(text_freqdist.keys())

        result = 0
        for word in intersection:
            result += query_freqdist[word] * text_freqdist[word]

        return result

    def open_link(self, url):
         self.master.after(100, lambda u=url: webbrowser.open(u))

if __name__ == "__main__":
    if __name__ == "__main__":
        root = tk.Tk()

    # Create an instance of WebScannerApp
    app = WebScannerApp(root)

    # Configure window to expand and fill
    root.geometry("800x600")
    root.minsize(400, 300)

    # Run the Tkinter event loop
    root.mainloop()
