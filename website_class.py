from hsk_profiler import profile
import string
from textstat import textstat
class Website:
    def __init__(self, st):
        self.st = st
        self.title = "Language Analysis"
        self.description = "Analyze text in Chinese, English, and other languages, using Streamlit."
        self.keywords = "HSK, Chinese, Profiler, Text, Analysis, Linguistics"
        self.author = "Ancastal"

    def show_hsk_profiler(self):
        self.st.title("HSK Profiler")
        self.st.subheader("Analyze the HSK level of Chinese text")

        # Add text area and button
        txt = self.st.text_area("Enter Chinese text here:")
        if self.st.button('Profile', key="profile", help="Analyze the text and display the results."):
            # Analyze text and display results
            total_chars, hsk_counts, avg_hsk_level = profile(txt)
            self.st.write("Total characters:", total_chars)
            self.st.write("HSK level counts:", hsk_counts)
            self.st.write("Average HSK level:", avg_hsk_level)

            # Create bar chart of HSK level distribution
            hsk_data = {"HSK Level " + str(i): hsk_counts[i-1] for i in range(1, 7)}
            self.st.bar_chart(hsk_data)

        # Define CSS styles
        STYLE = """
        <style>
        body {
            background-color: #f9f9f9;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 18px;
        }
        button:hover {
            background-color: #3e8e41;
        }
        textarea {
            height: 300px;
            border-radius: 4px;
            border: 1px solid #ccc;
            padding: 12px 20px;
            box-sizing: border-box;
            font-size: 18px;
            resize: vertical;
        }
        </style>
        """

        # Add CSS styles to page
        self.st.markdown(STYLE, unsafe_allow_html=True)
    def show_readability(self):
        def get_readability_description(score, formula):
                ranges = {
                    "Flesch Reading Ease": [(0, 30, "very difficult"), (30, 50, "difficult"), (50, 60, "fairly easy"), (60, 70, "easy"), (70, 100, "very easy")],
                    "Flesch-Kincaid Grade Level": [(0, 7, "easy"), (7, 10, "fairly easy"), (10, 13, "difficult"), (13, 100, "very difficult")],
                    "Gunning Fog Index": [(0, 12, "easy"), (12, 14, "fairly easy"), (14, 17, "difficult"), (17, 100, "very difficult")],
                    "Coleman-Liau Index": [(0, 8, "easy"), (8, 10, "fairly easy"), (10, 12, "difficult"), (12, 100, "very difficult")],
                    "SMOG Index": [(0, 8, "easy"), (8, 10, "fairly easy"), (10, 12, "difficult"), (12, 100, "very difficult")],
                    "Automated Readability Index": [(0, 8, "easy"), (8, 10, "fairly easy"), (10, 12, "difficult"), (12, 100, "very difficult")],
                    "Linsear Write Formula": [(0, 8, "easy"), (8, 10, "fairly easy"), (10, 12, "difficult"), (12, 100, "very difficult")]
                }
                for r in ranges[formula]:
                    if score >= r[0] and score < r[1]:
                        return f"The text is {r[2]} to read. It is suitable for audiences with {formula} levels ranging from {r[0]} to {r[1]}."

                return f"The readability score of {score} is outside the expected range for {formula}."

        self.st.title("Readability")
        self.st.subheader("Analyze the readability of English text")

        # Add text area and button
        txt = self.st.text_area("Enter English text here:")
        if self.st.button('Analyze', key="analyze", help="Analyze the text and display the results."):
            print(txt)
            fre = textstat.flesch_reading_ease(txt)
            fkg = textstat.flesch_kincaid_grade(txt)
            gf = textstat.gunning_fog(txt)
            cli = textstat.coleman_liau_index(txt)
            lwf = textstat.linsear_write_formula(txt)
            ari = textstat.automated_readability_index(txt)
            smog = textstat.smog_index(txt)

            # Automated Readability Index
            ari = 4.71 * (sum([len(word.strip(string.punctuation)) for word in txt.split()]) / len(txt.split())) + 0.5 * (len(txt.split()) / len(txt.split("."))) - 21.43

            with self.st.expander(f"Flesch Reading Ease: {fre}"):
                self.st.write(get_readability_description(fre, "Flesch Reading Ease"))
            with self.st.expander(f"Flesch-Kincaid Grade Level: {fkg}"):
                self.st.write(get_readability_description(fkg, "Flesch-Kincaid Grade Level"))
            with self.st.expander(f"Gunning Fog Index: {gf}"):
                self.st.write(get_readability_description(gf, "Gunning Fog Index"))
            with self.st.expander(f"Coleman-Liau Index: {cli}"):
                self.st.write(get_readability_description(cli, "Coleman-Liau Index"))
            with self.st.expander(f"Linsear Write Formula: {lwf}"):
                self.st.write(get_readability_description(lwf, "Linsear Write Formula"))
            with self.st.expander(f"Automated Readability Index: {ari}"):
                self.st.write(get_readability_description(ari, "Automated Readability Index"))
    def show_home(self):
        # Set page title and subtitle
        self.st.title("Welcome to Linguistic Analysis")
        self.st.subheader("A website for advanced text analysis in multiple languages")

        # Add a description of the website
        self.st.write("Linguistic Analysis is a website that provides advanced text analysis tools for multiple languages. From readability analysis to BLEU scores, our features are designed to give you a more in-depth understanding of your text data. Whether you're a language student, researcher, or data analyst, Linguistic Analysis can help you gain valuable insights from your text.")

        # Add a section about the features
        ciau.st.header("Our Features")
        ciau.st.write("At Linguistic Analysis, we offer a range of features for advanced text analysis, including:")
        ciau.st.write("- HSK Profiling for Chinese language learners")
        ciau.st.write("- Readability analysis for English texts")
        ciau.st.write("- BLEU scores for machine translation evaluation")
        ciau.st.write("And more! We're constantly updating our features to provide the most useful tools for our users.")

        # Add a section about the creator
        self.st.header("About the Creator")
        self.st.write("Linguistic Analysis was created by Ancastal, a Computational Linguist and Data Scientist with a passion for language and data analysis. If you have any questions or feedback, feel free to reach out to me on LinkedIn.")

        # Add a call to action
        self.st.header("Get Started")
        self.st.write("Ready to start analyzing text? Use the navigation menu at the top of the page to explore our different features and tools. If you have any questions or need help getting started, don't hesitate to reach out to us for support.")
