import customtkinter as ctk
from tkinter import filedialog
from textblob import TextBlob
import matplotlib.pyplot as plt
from collections import Counter

# --- Core Logic ---

# A simple list to store the results of each analysis for visualization
analysis_history = []

def analyze_sentiment(text):
    """
    Analyzes the sentiment of a given text using TextBlob.
    Returns the sentiment category, polarity score, and subjectivity score.
    """
    if not text.strip():
        return "Enter Text", 0.0, 0.0

    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity > 0.05:
        sentiment = "Positive"
    elif polarity < -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    
    # Add the result to our history for the chart
    analysis_history.append(sentiment)
    
    return sentiment, polarity, subjectivity

def show_history_chart():
    """
    Displays a pie chart of the sentiment analysis history.
    """
    if not analysis_history:
        print("No analysis history to show.")
        return

    # Count the occurrences of each sentiment
    counts = Counter(analysis_history)
    labels = list(counts.keys())
    sizes = list(counts.values())
    colors = {'Positive': 'lightgreen', 'Negative': 'lightcoral', 'Neutral': 'lightskyblue'}
    pie_colors = [colors[label] for label in labels]

    # Create and display the pie chart
    plt.figure(figsize=(6, 6))
    plt.pie(sizes, labels=labels, colors=pie_colors, autopct='%1.1f%%', startangle=140, shadow=True)
    plt.title('Sentiment Analysis History')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()


# --- GUI Application ---

class SentimentAnalyzerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # --- Window Setup ---
        self.title("Sentiment Analyzer")
        self.geometry("700x550")
        ctk.set_appearance_mode("System")  # Can be "System", "Dark", "Light"
        ctk.set_default_color_theme("blue")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Widgets ---

        # Main Text Input Box
        self.textbox = ctk.CTkTextbox(self, wrap="word", font=("Arial", 14))
        self.textbox.grid(row=0, column=0, columnspan=2, padx=20, pady=(20, 10), sticky="nsew")

        # Frame for buttons
        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row=1, column=0, columnspan=2, padx=20, pady=10, sticky="ew")
        self.button_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.analyze_button = ctk.CTkButton(self.button_frame, text="Analyze Text", command=self.analyze_text_command)
        self.analyze_button.grid(row=0, column=0, padx=10, pady=10)

        self.load_file_button = ctk.CTkButton(self.button_frame, text="Load from File", command=self.load_file_command)
        self.load_file_button.grid(row=0, column=1, padx=10, pady=10)
        
        self.chart_button = ctk.CTkButton(self.button_frame, text="Show History Chart", command=show_history_chart)
        self.chart_button.grid(row=0, column=2, padx=10, pady=10)

        # Frame for results display
        self.results_frame = ctk.CTkFrame(self, height=150)
        self.results_frame.grid(row=2, column=0, columnspan=2, padx=20, pady=(10, 20), sticky="nsew")
        self.results_frame.grid_columnconfigure(0, weight=1)

        # Labels for results
        self.sentiment_label = ctk.CTkLabel(self.results_frame, text="Sentiment: -", font=ctk.CTkFont(size=20, weight="bold"))
        self.sentiment_label.pack(pady=(20, 10))

        self.polarity_label = ctk.CTkLabel(self.results_frame, text="Polarity: -", font=ctk.CTkFont(size=16))
        self.polarity_label.pack(pady=5)

        self.subjectivity_label = ctk.CTkLabel(self.results_frame, text="Subjectivity: -", font=ctk.CTkFont(size=16))
        self.subjectivity_label.pack(pady=(5, 20))


    # --- Widget Commands ---

    def analyze_text_command(self):
        """Callback for the 'Analyze Text' button."""
        text_to_analyze = self.textbox.get("1.0", "end-1c")
        sentiment, polarity, subjectivity = analyze_sentiment(text_to_analyze)

        # Update the result labels
        self.sentiment_label.configure(text=f"Sentiment: {sentiment}")
        self.polarity_label.configure(text=f"Polarity: {polarity:.2f}")
        self.subjectivity_label.configure(text=f"Subjectivity: {subjectivity:.2f}")

    def load_file_command(self):
        """Callback for the 'Load from File' button."""
        filepath = filedialog.askopenfilename(
            title="Open a Text File",
            filetypes=(("Text Files", "*.txt"), ("All files", "*.*"))
        )
        if not filepath:
            return
        
        with open(filepath, 'r', encoding='utf-8') as f:
            file_content = f.read()
            self.textbox.delete("1.0", "end")
            self.textbox.insert("1.0", file_content)

# --- Run the Application ---
if __name__ == "__main__":
    app = SentimentAnalyzerApp()
    app.mainloop()


    
