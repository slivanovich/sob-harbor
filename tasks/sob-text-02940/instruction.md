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
Raffaele Mirate: Raffaele Mirate (3 September 1815 – November 1895) was a celebrated Italian operatic tenor who had an active career from the 1830s through the 1860s.  Known for his intelligent phrasing and bright and powerful vocal timbre, he was regarded as an outstanding interpreter of the tenor roles in the early and middle period operas of Giuseppe Verdi.  He notably created the role of the Duke of Mantua in the world premiere of Verdi's "Rigoletto" in 1851.  He was also a highly regaurded interpreter of bel canto roles, excelling in the operas of Vincenzo Bellini, Gaetano Donizetti, and Gioachino Rossini.

Vaga luna, che inargenti: "Vaga luna, che inargenti " (Beautiful moon, dappling with silver) is an arietta composed by Vincenzo Bellini to an anonymous Italian text and dedicated to Giulietta Pezzi.  It was published in 1838 by Casa Ricordi in "Tre ariette inedite " along with two other Bellini songs, "Il fervido desiderio " and "Dolente immagine di Fille mia ".  It was also amongst the fifteen Bellini songs published by Ricordi under the title "Composizioni da Camera " in 1935, the centenary of the composer's death.  Composed in the bel canto style, it is a frequent recital piece, and has often been recorded.  Its original key is in A-flat major with a tempo of andante cantabile.

Catania–Fontanarossa Airport: Catania–Fontanarossa Airport (Italian: "aeroporto internazionale Vincenzo Bellini di Catania-Fontanarossa" , English: Catania International Airport) (IATA: CTA, ICAO: LICC) also named as Vincenzo Bellini Airport, is an international airport 2.3 NM southwest of Catania, the second largest city on the Italian island of Sicily.  It is named after the opera composer Vincenzo Bellini who was born in Catania.

Giacomo Tritto: Giacomo Domenico Mario Antonio Pasquale Giuseppe Tritto (2 April 1733 – 16 September 1824) was an Italian composer, known primarily for his 54 operas.  He was born in Altamura, and studied in Naples; among his teachers were Nicola Fago, Girolamo Abos, and Pasquale Cafaro.  Amongst his pupils were the young Vincenzo Bellini around 1821, plus Ferdinando Orlandi.  He died in Naples.

Gregorio Babbi: Gregorio Babbi (16 November 1708, Cesena - 2 January 1768) was an Italian operatic tenor.  He performed in the premieres of numerous operas, including works by Girolamo Abos, Pietro Auletta, Andrea Bernasconi, Giuseppe de Majo, Giuseppe Ferdinando Brivio, Pasquale Cafaro, Gioacchino Cocchi, Nicola Conforto, Pasquale Errichelli, Baldassarre Galuppi, Giuseppe Gazzaniga, Geminiano Giacomelli, Giovanni Antonio Giay, Johann Adolph Hasse, Niccolò Jommelli, Gaetano Latilla, Leonardo Leo, Gennaro Manna, Antonio Maria Mazzoni, Davide Perez, Niccolò Piccinni, Nicola Sabatino, Giuseppe Scarlatti, Tommaso Traetta and Antonio Vivaldi among others.

Gaetano Donizetti: Domenico Gaetano Maria Donizetti (] ; 29 November 1797 – 8 April 1848) was an Italian composer.  Along with Gioachino Rossini and Vincenzo Bellini, Donizetti was a leading composer of the "bel canto" opera style during the first half of the nineteenth century.  Donizetti's close association with the bel canto style was undoubtedly an influence on other composers such as Giuseppe Verdi (1813–1901).

Casa Ricordi: Casa Ricordi is a publisher of primarily classical music and opera.  Its classical repertoire represents one of the important sources in the world through its publishing of the work of the major 19th-century Italian composers such as Gioachino Rossini, Gaetano Donizetti, Vincenzo Bellini, Giuseppe Verdi, and, later in the century, Giacomo Puccini, composers with whom one or another of the Ricordi family came into close contact.

Vincenzo Bellini: Vincenzo Salvatore Carmelo Francesco Bellini (] ; 3 November 1801 – 23 September 1835) was an Italian opera composer, who was known for his long-flowing melodic lines for which he was named "the Swan of Catania".

Vincenzo La Scola: Vincenzo La Scola (25 January 1958 – 15 April 2011) was an Italian tenor who had a successful international opera career for more than 25 years.  He was particularly admired for his portrayals in operas by Giuseppe Verdi, Giacomo Puccini, Gaetano Donizetti, and Vincenzo Bellini.  He also achieved success as a crossover artist, particularly in his many collaborations with singer-songwriter Cliff Richard and for his solo crossover album for EMI, "Vita Mia" (1999).  In 2000 he was made a UNICEF Goodwill Ambassador, and from 2004 until his sudden death in 2011 he served as principal teacher and artistic director of the Accademia Verdi Toscanini in Parma.

Bellini (Italian band): Bellini is an international indie rock/math rock band, composed of members from Girls Against Boys, Soulside and Uzeda.  This band was named after the Italian composer, Vincenzo Bellini.

Question: Giacomo Domenico Mario Antonio Pasquale Giuseppe Tritto, was an Italian composer, known primarily for his 54 operas, amongst his pupils were Vincenzo Bellini, around which year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "teacher": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the teacher."
        },
        "occupation": {
          "type": "string",
          "description": "The primary occupation of the teacher."
        },
        "number_of_operas": {
          "type": "integer",
          "description": "The number of operas composed by the teacher."
        }
      },
      "required": [
        "name",
        "occupation",
        "number_of_operas"
      ],
      "additionalProperties": false
    },
    "pupil_name": {
      "type": "string",
      "description": "The name of the pupil."
    },
    "year_of_study": {
      "type": "integer",
      "description": "The approximate year the pupil studied with the teacher."
    }
  },
  "required": [
    "teacher",
    "pupil_name",
    "year_of_study"
  ],
  "additionalProperties": false
}
