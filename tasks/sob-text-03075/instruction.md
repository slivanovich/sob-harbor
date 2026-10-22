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
Three Comrades (novel): Three Comrades (German: "Drei Kameraden" ) is a novel first published in 1936 by the German author Erich Maria Remarque.  It is written in first person by the main character Robert Lohkamp, whose somewhat disillusioned outlook on life is due to his horrifying experiences in the trenches of the First World War's French-German front.  He shares these experiences with Otto Köster and Gottfried Lenz, his two comrades with whom he runs an auto-repair shop in late 1920s Berlin (probably).  Remarque wrote the novel in exile and it was first published in Dutch translation as "Drie kameraden", with English translation following soon in "Good Housekeeping" from January to March 1937 and in the book form in the same year.  First German language edition was published in 1938 by exile publisher "Querido" in Amsterdam, but the novel was published in Germany only in 1951.

Tony Judt: Tony Robert Judt, FBA ( ; 2 January 1948 – 6 August 2010) was a British historian, essayist, and university professor who specialized in European history.  Judt moved to New York and served as the Erich Maria Remarque Professor in European Studies at New York University, and Director of NYU's Erich Maria Remarque Institute.  He was a frequent contributor to the "New York Review of Books".  In 1996 Judt was elected a Fellow of the American Academy of Arts and Sciences and in 2007 a corresponding Fellow of the British Academy.

Robert Shvarc: Robert Shvarc (10 December 1932 – 25 April 2003) born in Sarajevo of Bosnia, 10 December 1932, is a Hebrew and Albanian, recognized as one of the best translators from German of the 20th century and beginning of new millennium, writer and poet.  His parents were respectively mother from Elbasan and father an Hebrew from Austria and lived in Shkodra, Albania.  There Robert Shvarc grew up as a lover of Albanian mother's language and is the first who brought for the Albanian reader some masterpieces of literature as the novels of Gabriel García Márquez, Erich Maria Remarque, Lion Feuchtwanger, dramas of Bertolt Brecht; books of poetry from Goethe, Schiller and Heine.  Also Shvarc translated in German best books of many Albanian poets and writers.

Ragnar Kvam: Ragnar Kvam (18 November 1917 – 15 February 2006) was a Norwegian journalist, novelist, translator and literary critic.  He was born in Tønsberg and grew up in Drammen.  After the Second World War he was journalist in the newspaper "Fremtiden", and the Norwegian News Agency.  He made his literary debut in 1950 with the novel "Alle vil hjem".  Among his other novels are "De herjede menn" from 1953, "Den store stillheten" from 1964, and "Krystallnatten" from 1970.  He translated many books into Norwegian language, including works by George Orwell, Virginia Woolf, Graham Greene, Oscar Wilde, C. P. Snow and Erich Maria Remarque.

Erich Maria Remarque: Erich Maria Remarque (born Erich Paul Remark; 22 June 1898 – 25 September 1970) was a German

Gerina Dunwich: Gerina Dunwich (born December 27, 1959, Illinois, United States) is a professional astrologer, occult historian, and New Age author, best known for her books on Wicca and various occult subjects.  She is also involved in paranormal research and is the founder of the Paranormal Animal Research Group, which investigates cases of alleged hauntings by animal spirits.

Mary Carruthers: Mary J. Carruthers (born January 15, 1941) is the Erich Maria Remarque Professor of Literature and Professor of English, emerita, at New York University.  She also teaches at New York University Abu Dhabi.

The Night in Lisbon: The Night in Lisbon (German: "Die Nacht von Lissabon" ) is a novel by Erich Maria Remarque published in 1962.  It revolves around the plight of two German refugees in the opening months of World War II.  One of the refugees relates their story during the course of a single night in Lisbon in 1942.  The story he recounts is mainly a romantic one, and also contains a lot of action with arrests, escapes and near-misses.  The novel is realistic, Remarque was himself a German refugee (although the novel is fictional and only loosely based on the experience of Remarque 's friend, novelist Hans Habe), and provides insight into refugee life in Europe during the early days of the war.  The book completed what was known as Remarque’s "emigre trilogy" along with "Flotsam" and "Arch of Triumph".  It was Remarque's last completed work.

Principe di Savoia: Hotel Principe di Savoia, or simply referred to as The Principe, is a five-star hotel in Milan, Italy.  The hotel has long become one of Milan's Landmarks.  Founded by the name of "Principe e Savoia" in 1927, a time when Milan had already established its position as financial center of the country, it soon became a home for businessmen.  With time, celebrities of all kinds chose The Principe for their Italian stays: Edward VIII, Erich Maria Remarque, Aristotle Onassis, Evita Peron, Maria Callas; and in recent years Madonna, David Beckham and George Clooney, among others.

August Perk: August Perk (October 25, 1897, Lohne / Lingen, Germany; – May 12, 1945, Braunschweig, Germany) was a German Resistance fighter against the National Socialism.  His brief friendship with Erich Maria Remarque influenced Remarque's novel "All Quiet on the Western Front".

Question: Who was born earlier, Gerina Dunwich or Erich Maria Remarque?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "person_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string"
        },
        "birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "name",
        "birth_date"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "object",
      "properties": {
        "earlier_born_person_name": {
          "type": "string"
        },
        "earlier_birth_date": {
          "type": "string",
          "format": "date"
        },
        "later_born_person_name": {
          "type": "string"
        },
        "later_birth_date": {
          "type": "string",
          "format": "date"
        }
      },
      "required": [
        "earlier_born_person_name",
        "earlier_birth_date",
        "later_born_person_name",
        "later_birth_date"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string"
    }
  },
  "required": [
    "person_1",
    "person_2",
    "comparison_result",
    "final_answer"
  ],
  "additionalProperties": false
}
