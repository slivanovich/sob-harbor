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
Téa Leoni: Elizabeth Téa Pantaleoni ( ; born February 25, 1966), better known by her stage name Téa Leoni, is an American actress and producer.

The Smell of Success: The Smell of Success is an Initiate Productions film directed by Michael Polish, starring Billy Bob Thornton, Téa Leoni, Kyle MacLachlan, and Ed Helms.  The film’s original title was "Manure".

Yumiko Nogawa: Yumiko Nogawa (野川由美子 , Nogawa Yumiko ) (born August 30, 1944) is a Japanese actress born in Kyoto, Japan.  She has starred in several movies, notably "Gate of Flesh" (1964), a Japanese erotic film, part of a trilogy of films she made with director Seijun Suzuki.  Including "Story of a Prostitute" (1965) and "Carmen from Kawachi" (1966), these films are known as Nogawa's "Flesh Trilogy".  Nogawa has appeared in numerous films in Japan, including director Nagisa Oshima's "The Pleasures of the Flesh" (1965) and "Zatoichi and the Fugitives" (1968), the eighteenth film in the "Zatoichi" series.  She has also appeared in television series on Nippon Television, TV Tokyo, Fuji TV, and NHK.

Suet Nei: Hung Suet-nei (Chinese: 熊雪妮), known as Suet Nei or Suet Nay (Chinese: 雪妮) is a Hong Kong actress born in 1945, Hong Kong.  She is a veteran actress, having acted for many years.  She has starred in martial arts Cantonese operas, due to her skill in martial arts.  She signed with TVB in 1988.

Mayu Gamō: Mayu Gamō (蒲生 麻由 , Gamō Mayu , born March 16, 1982) is a Japanese actress born in Saitama Prefecture, Japan.  She has starred in many films, most notably in Tokusou Sentai Dekaranger as Succubus Hells/ Human Fatale Camille.  She reprised her role in Tokusou Sentai Dekaranger vs. Abaranger for a brief appearance.  She also starred in Kamen Rider Hibiki as Kasumi Tachibana.  Gamō is an active amateur marathon competitor and triathlete, having competed both in the Tokyo Marathon and in Hawaii, Paris, and Australia.  She completed the 2011 Lavaman Triathlon in Anaehoomalu Bay, Hawaii.

Rachel Devirys: Rachel Devirys (28 February 1890 - 16 May 1983) was a French film actress born in the Crimea, Russian Empire (now Ukraine).  She starred in some 50 films between 1916 and 1956.

Soher Al Bably: Soheir Al Bably (Arabic: ‎ ‎ ; born 14 February 1935) is an Egyptian actress born in Damietta.  After completing secondary school, she attended the Institute of Theatrical Arts.  ٍShe starred in the play "Madrast Al-Mushaghebeen" in 1973, and also in a stage version of the life of Raya and Sakina in 1985.  She married four times, and her second husband was Mounir Mourad.

Kara Zediker: Kara Zediker is an American actress born in Kankakee, Illinois.  She guest starred on "" as the young T'Pau in the fourth-season episodes "Awakening" and "Kir'Shara".  She has also guest-starred on such shows as "Charmed", "The King of Queens", "Becker", "Joan of Arcadia" and "24".

Irene Montalà: Irene Montalà is a Spanish actress born in the district of Nou Barris of Barcelona.  She is the daughter of Mercè Montalà.  She studied interpretation with Txiki Berrando and Manuel Lillo.  She has also studied dancing and singing.  Her mother tongues are Spanish and catalan, although she has also studied English and french.  She started as an actress in series "Poblenou" (TV3).  In 2001, she starred in the film "Fausto 5.0".  In 2002, she participated in the series <nowiki>"Por Palabras"</nowiki> like Barbara which in the end it wasn't finished.  In 2004 she appeared in an episodic way in the series "Cuéntame como pasó" (La 1), where she played the role of Mila.

Maggie Moore: Maggie Moore (10 April 1851 - March 15, 1926) was an American-Australian actress born as Margaret Virginia Sullivan.  She met and married producer J. C. Williamson in the U.S. and became popular as an actress in their production of "Struck Oil", which premiered in 1873 and was revived many times.  Soon after their marriage, they took the play on a tour of Australia.  It was such a success that they stayed there, where he founded the most successful theatrical company in Australia, and she became a leading actress.

Question: What actress born February 25,1966 starred in The Smell of Success?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The full name of the actress."
    },
    "birth_details": {
      "type": "object",
      "properties": {
        "year": {
          "type": "integer",
          "description": "The birth year of the actress."
        },
        "month": {
          "type": "string",
          "description": "The birth month of the actress."
        },
        "day": {
          "type": "integer",
          "description": "The birth day of the actress."
        }
      },
      "required": [
        "year",
        "month",
        "day"
      ],
      "additionalProperties": false
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the actress."
    },
    "film_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the film the actress starred in."
        },
        "director": {
          "type": "string",
          "description": "The director of the film."
        },
        "original_title": {
          "type": "string",
          "description": "The original title of the film, if different."
        }
      },
      "required": [
        "title",
        "director",
        "original_title"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "birth_details",
    "nationality",
    "film_details"
  ],
  "additionalProperties": false
}
