Use the following extraction rules and source material. Write your final JSON object to `/tmp/answer.json`. The verifier reads that file, not your final chat message.

Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.

Rules:
- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.
- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.
- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.
- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.
- Include all required fields: Every field listed as required in the schema must appear in the JSON.
- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing.

Context:
Yan Liben: Yan Liben () ("c." 600–673), formally Baron Wenzhen of Boling (博陵文貞男), was a Chinese painter and official of the early Tang Dynasty.  His most renowned work is the "Thirteen Emperors Scroll".  He also painted the Portraits at Lingyan Pavilion, under Emperor Taizong of Tang, commissioned in 643 to commemorate 24 of the greatest contributors to Emperor Taizong's reign, as well as 18 portraits commemorating the 18 great scholars who served Emperor Taizong when he was the Prince of Qin.  Yan's paintings included painted portraits of various Chinese emperors from the Han Dynasty (202 BC–220 AD) up until the Sui Dynasty (581–618) period.  His works were highly regarded by the Tang writers Zhu Jingxuan and Zhang Yanyuan, who noted his paintings were "works among the glories of all times".

Kir Ianulea: Kir Ianulea or Kyr Ianulea (] ) is a fantasy and historical fiction novella or short story, published by Romanian author Ion Luca Caragiale in 1909.  Borrowing the elements of a fairy tale, satire and frame story, it has become recognized as one of Caragiale's leading contributions to short prose, and is often described as one of the seminal works written by him during the last decade of his life.  While its narrative structure is largely based on "Belfagor arcidiavolo", a story by 16th century writer and political thinker Niccolò Machiavelli, "Kir Ianulea" employs additional elements such as anecdotes to evolve into a social fresco of late 18th-century Wallachia and the Ottoman-ruled Balkans as a whole.  Caragiale primarily adapts Machiavelli's theme, which is a fable about the innate unreliability of women, to the realities of the Phanariote epoch, focusing his attention on the interactions between Greeks and Romanians while offering additional insight into the process of acculturation.

Belfagor arcidiavolo: Belfagor arcidiavolo is a novella by Niccolò Machiavelli.  It was written between 1518 and 1527 and published with Machiavelli's collected works in 1549.  It is also known under the titles La favola di Belfagor Arcidiavolo and Il demonio che prese moglie.

Wheelers (novel): Wheelers is a science fiction novel written by English mathematician Ian Stewart and reproductive biologist Jack Cohen, figures notable for both their personal scholarly work and numerous individual and collaborative contributions to the world of science fiction.  The book was originally released in hardcover form in the year 2000, and a more common paperback printing was begun in 2001.  It has enjoyed modest commercial success and is perhaps best known for its intriguing conceptions of alien zoology and intelligence—hallmarks of Cohen's renowned work as a consultant on exobiology for books, movies, and television.

Niccolò Machiavelli: Niccolò di Bernardo dei Machiavelli (] ; 3 May 1469 – 21 June 1527) was an Italian diplomat, politician, historian, philosopher, humanist, and writer of the Renaissance period.  He has often been called the father of modern political science.  He was for many years a senior official in the Florentine Republic, with responsibilities in diplomatic and military affairs.  He also wrote comedies, carnival songs, and poetry.  His personal correspondence is renowned in the Italian language.  He was secretary to the Second Chancery of the Republic of Florence from 1498 to 1512, when the Medici were out of power.  He wrote his most renowned work "The Prince" ("Il Principe") in 1513.

Belfagor: Belfagor (premiere 26 April 1923) is an Italian-language opera by the composer Ottorino Respighi to a libretto by Claudio Guastalla (1880-1948) based on the comedy "Belfagor" of Ercole Luigi Morselli (1882-1921), itself loosely based on the novella "Belfagor arcidiavolo" by Niccolò Machiavelli.  It was premiered in 1923 at La Scala in Milan, under the baton of Antonio Guarnieri, since Toscanini was unavailable.  The cast featured Irish soprano Margaret Burke Sheridan as Candida, tenor Mariano Stabile as her lover Baldo, and baritone Francesco Merli as the titular Belfagor, a "arcidiavolo" who tries to marry a human maiden while in disguise as a nobleman, using gifts of money to her father.

Leslie Fiedler: Leslie Aaron Fiedler (March 8, 1917 – January 29, 2003) was an American literary critic, known for his interest in mythography and his championing of genre fiction.  His work also involves application of psychological theories to American literature.  His most renowned work is "Love and Death in the American Novel" (1960).

Santa Maria de Ripoll: The Monastery of Santa Maria de Ripoll is a Benedictine monastery, built in the Romanesque style, located in the town of Ripoll in Catalonia, Spain.  Although much of the present church is 19th century rebuilding, the sculptured portico is a renowned work of Romanesque art.

The Return of the Prodigal Son (Rembrandt): The Return of the Prodigal Son is an oil painting by Rembrandt.  It is among the Dutch master's final works, likely completed within two years of his death in 1669.  Depicting the moment of the prodigal son's return to his father in the Biblical parable, it is a renowned work described by art historian Kenneth Clark as "a picture which those who have seen the original in St. Petersburg may be forgiven for claiming as the greatest picture ever painted".

Stephen A. Shapiro: Stephen A. Shapiro was an American author, psychotherapist, management consultant and founding executive of the Volunteer Counselling Service of Rockland County.  His most famous book is "Manhood, a new definition," in which inspiring himself from real life cases, personal experience and recent feminist literature, he analyses behavioural patterns of contemporary men and their relationship with women, and suggests solutions to their limits and dissatisfactions.  "Manhood" is quoted by Canadian psychoanalyst Guy Corneau in his renowned work "Absent fathers, lost sons" as a landmark in the new movement of masculinity analysis which started in the late 1970s.

Question: What is the most renowned work of the author of "Belfagor arcidiavolo"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "initial_work_title": {
      "type": "string",
      "description": "The title of the work mentioned in the question."
    },
    "author_name": {
      "type": "string",
      "description": "The name of the author of the initial work."
    },
    "author_most_renowned_work": {
      "type": "string",
      "description": "The title of the author's most renowned work."
    },
    "author_birth_year": {
      "type": "integer",
      "description": "The birth year of the author."
    },
    "author_death_year": {
      "type": "integer",
      "description": "The death year of the author."
    }
  },
  "required": [
    "initial_work_title",
    "author_name",
    "author_most_renowned_work",
    "author_birth_year",
    "author_death_year"
  ],
  "additionalProperties": false
}
