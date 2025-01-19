<<<<<<< HEAD
# Analysis and Cleanup of lotr_scripts.csv

## 1. Data Fields Description

### The dataset contains the following columns:

1. **char**: Character Name.

2. **dialog**: A phrase that a character says.

3. **movie**: In which film he says that.

## 2. Dirty Data Identification and Cleanup

### Issues Identified:

1. The first column that has no header.

    Removing the first column because it looked redundant: this is an index that is automatically created when exporting data from Pandas to CSV.

    To do this, `cleaner.py` has the following line:
    ```
    lotr_data_cleaned = lotr_data.drop(columns=['Unnamed: 0'])
    ```

2. Extra spaces and characters in columns.

    For example: 
    - The second line in the `dialog` column in the original csv file has an empty space:

        *"Oh Smeagol Ive got one! , Ive got a fish Smeagol, Smeagol!    "*

    - Third, fifth, eighth... line in the `dialog` column in the original csv file has the letter `B` after the punctuation mark.

        *"Pull it in! Go on, go on, go on, pull it in! В "*

        *Deagol! В*

        *Give us that! Deagol my love В*

    To solve this problem `cleaner.py` has the following line of code :
    ```
    lotr_data_cleaned = lotr_data_cleaned.apply(lambda col: col.str.strip() if col.dtypes == 'object' else col)
    ```

3. Missing values in **dialog**.

    For example:
    - line `1011` the dialogue column in the original csv file.

    - line `1403` the dialogue column in the original csv file.

    - line `1571` the dialogue column in the original csv file.

    - line `2082` the dialogue column in the original csv file.

    To solve this problem I used the **Notepad++** application

    I deleted lines with missing values. I found them using the search function on `,,`

## Data Analysis

### The following analyses were performed:

1. The dataset contains 2385 lines of dialogue.

    ```
    wc -l lotr_scripts_cleaned.csv
    ```

2. There are 4591 unique words used across all dialogues.

    ```
    cut -d',' -f2 lotr_scripts_cleaned.csv | tr ' ' '\n' | sort | uniq -i | wc -l
    ```

3. The number of lines of dialogue in each movie:
- The Two Towers: 1008 lines
- The Return of the King: 872 lines
- The Fellowship of the Ring: 504 lines

    ```
    grep -c "The Two Towers" lotr_scripts_cleaned.csv
    grep -c "The Return of the King" lotr_scripts_cleaned.csv
    grep -c "The Fellowship of the Ring" lotr_scripts_cleaned.csv
    ```

4. Top 5 Characters by Line Count
- Frodo: 226 lines
- Sam: 217 lines
- Gandalf: 205 lines
- Aragorn: 187 lines
- Pippin: 163 lines

    ```
    cut -d',' -f1 lotr_scripts_cleaned.csv | sort | uniq -c | sort -nr | head -5
    ```

5. Top 5 Characters by Dialogue Word Count
- Gandalf: 1747 words
- Frodo: 1262 words
- Sam: 1222 words
- Aragorn: 1104 words
- Theoden: 890 words

    ```
    $ awk -F',' '
    {
    if (NR > 1) {
        # The first column is character, the second column is dialogue
        char = $1;
        dialog = $2;

        # Remove inverted commas from character and dialogue names
        gsub(/"/, "", char);
        gsub(/"/, "", dialog);

        # Count the number of words in the dialogue
        split(dialog, words, " ");
        count[char] += length(words);
    }
    }
    END {
        for (char in count) print count[char], char
    }' lotr_scripts_cleaned.csv | sort -nr | head -5

    ```
=======
# Analysis and Cleanup of lotr_scripts.csv

## 1. Data Fields Description

### The dataset contains the following columns:

1. **char**: Character Name.

2. **dialog**: A phrase that a character says.

3. **movie**: In which film he says that.

## 2. Dirty Data Identification and Cleanup

### Issues Identified:

1. The first column that has no header.

    Removing the first column because it looked redundant: this is an index that is automatically created when exporting data from Pandas to CSV.

    To do this, `cleaner.py` has the following line:
    ```
    lotr_data_cleaned = lotr_data.drop(columns=['Unnamed: 0'])
    ```

2. Extra spaces and characters in columns.

    For example: 
    - The second line in the `dialog` column in the original csv file has an empty space:

        *"Oh Smeagol Ive got one! , Ive got a fish Smeagol, Smeagol!    "*

    - Third, fifth, eighth... line in the `dialog` column in the original csv file has the letter `B` after the punctuation mark.

        *"Pull it in! Go on, go on, go on, pull it in! В "*

        *Deagol! В*

        *Give us that! Deagol my love В*

    To solve this problem `cleaner.py` has the following line of code :
    ```
    lotr_data_cleaned = lotr_data_cleaned.apply(lambda col: col.str.strip() if col.dtypes == 'object' else col)
    ```

3. Missing values in **dialog**.

    For example:
    - line `1011` the dialogue column in the original csv file.

    - line `1403` the dialogue column in the original csv file.

    - line `1571` the dialogue column in the original csv file.

    - line `2082` the dialogue column in the original csv file.

    To solve this problem I used the **Notepad++** application

    I deleted lines with missing values. I found them using the search function on `,,`

## Data Analysis

### The following analyses were performed:

1. The dataset contains 2385 lines of dialogue.

    ```
    wc -l lotr_scripts_cleaned.csv
    ```

2. There are 4591 unique words used across all dialogues.

    ```
    cut -d',' -f2 lotr_scripts_cleaned.csv | tr ' ' '\n' | sort | uniq -i | wc -l
    ```

3. The number of lines of dialogue in each movie:
- The Two Towers: 1008 lines
- The Return of the King: 872 lines
- The Fellowship of the Ring: 504 lines

    ```
    grep -c "The Two Towers" lotr_scripts_cleaned.csv
    grep -c "The Return of the King" lotr_scripts_cleaned.csv
    grep -c "The Fellowship of the Ring" lotr_scripts_cleaned.csv
    ```

4. Top 5 Characters by Line Count
- Frodo: 226 lines
- Sam: 217 lines
- Gandalf: 205 lines
- Aragorn: 187 lines
- Pippin: 163 lines

    ```
    cut -d',' -f1 lotr_scripts_cleaned.csv | sort | uniq -c | sort -nr | head -5
    ```

5. Top 5 Characters by Dialogue Word Count
- Gandalf: 1747 words
- Frodo: 1262 words
- Sam: 1222 words
- Aragorn: 1104 words
- Theoden: 890 words

    ```
    $ awk -F',' '
    {
    if (NR > 1) {
        # The first column is character, the second column is dialogue
        char = $1;
        dialog = $2;

        # Remove inverted commas from character and dialogue names
        gsub(/"/, "", char);
        gsub(/"/, "", dialog);

        # Count the number of words in the dialogue
        split(dialog, words, " ");
        count[char] += length(words);
    }
    }
    END {
        for (char in count) print count[char], char
    }' lotr_scripts_cleaned.csv | sort -nr | head -5

    ```
>>>>>>> 0f26296dd6f69840c7ad8a791607f77772c7fcf2
