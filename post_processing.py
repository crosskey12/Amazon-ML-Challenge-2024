import pandas as pd
import re

# Define the cleaning function to apply Post Processing Techniques
def clean_text(text):
    # Remove anything inside parentheses
    text = re.sub(r"\(.*?\)", "", text)

    # Height, Width, Depth replacements
    text = re.sub(r"\bcm\b", "centimetre", text)
    text = re.sub(r"\bmm\b", "millimetre", text)
    text = re.sub(r"\b m \b", " metre ", text)
    text = re.sub(r"\bmeters\b", "meter", text)
    text = re.sub(r"\bmeter\b", "metre", text)
    text = re.sub(r"\bmetres\b", "metre", text)
    text = re.sub(r"centimetre centimetre", "centimetre", text)
    text = re.sub(r"millimetre millimetre", "millimetre", text)
    text = re.sub(r"metre metre", "metre", text)

    # Space ft to foot
    text = re.sub(r"\b ft\b", " foot", text)
    text = re.sub(r"\bfeet\b", "foot", text)
    text = re.sub(r"foot foot", "foot", text)
    text = re.sub(r"\byards\b", "yard", text)
    text = re.sub(r"\binches\b", "inch", text)

    # Weight replacements
    text = re.sub(r" g ", " gram ", text)
    text = re.sub(r" kg ", " kilogram ", text)
    text = re.sub(r" mg ", " milligram ", text)
    text = re.sub(r"\bgrams\b", "gram", text)
    text = re.sub(r"\bkilograms\b", "kilogram", text)
    text = re.sub(r"\bmilligrams\b", "milligram", text)
    text = re.sub(r"gram gram", "gram", text)
    text = re.sub(r"kilogram kilogram", "kilogram", text)
    text = re.sub(r"milligram milligram", "milligram", text)

    # Ounces and pounds replacements
    text = re.sub(r"\bounces\b", "ounce", text)
    text = re.sub(r"oz ounce", "ounce", text)
    text = re.sub(r"ounce oz", "ounce", text)
    text = re.sub(r"\blbs\b", "pound", text)
    text = re.sub(r"\blb\b", "pound", text)
    text = re.sub(r"\bpounds\b", "pound", text)
    text = re.sub(r"pound pound", "pound", text)

    # Remove 'metric'
    text = re.sub(r"\bmetric\b", "", text)

    # Ton replacements
    text = re.sub(r"\btonnes\b", "ton", text)
    text = re.sub(r"\btonne\b", "ton", text)
    text = re.sub(r"\btons\b", "ton", text)
    text = re.sub(r"ton ton", "ton", text)

    # Voltage replacements
    text = re.sub(r" v ", " volt ", text)
    text = re.sub(r"\bvolts\b", "volt", text)
    text = re.sub(r"volt volt", "volt", text)

    # Power replacements
    text = re.sub(r" w ", " watt ", text)
    text = re.sub(r"\bwatts\b", "watt", text)
    text = re.sub(r"watt watt", "watt", text)

    # Volume replacements
    text = re.sub(r"\bml\b", "millilitre", text)
    text = re.sub(r"\bcups\b", "cup", text)
    text = re.sub(r"\bliters\b", "litre", text)
    text = re.sub(r"\bliter\b", "litre", text)
    text = re.sub(r"\blitres\b", "litre", text)
    text = re.sub(r"\bquarts\b", "quart", text)
    text = re.sub(r"\bgallons\b", "gallon", text)

    return text

# Load the CSV file into a DataFrame
df = pd.read_csv('./final_sumbission.csv')

# Apply the cleaning function specifically to the 'prediction' column
df['prediction'] = df['prediction'].apply(lambda x: clean_text(x) if isinstance(x, str) else x)

# Save the cleaned data back to a CSV file
df.to_csv('submission.csv', index=False)

print("CSV cleaned and saved as 'submission.csv'.")
