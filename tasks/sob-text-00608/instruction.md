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
List of Sadat Lecture for Peace Speakers: The Sadat Lecture for Peace is a lecture series at the University of Maryland, College Park, which began in 1997 when the Anwar Sadat Chair for Peace and Development was established within The Center for International Development and Conflict Management (which is associated with the Department of Government & Politics).  The Sadat Chair, currently held by Shibley Telhami, was established by Jehan Sadat in memory of her late husband, Anwar Sadat, the former President of Egypt.

Experience &amp; Education: Experience & Education is the second full-length album by rapper Sadat X, of the group Brand Nubian.  The album features production from Diamond D, DJ Spinna, Kleph Dollaz and Ge-ology, and guest appearances from Heltah Skeltah, Edo G, Agallah and the Money Boss Players.  The album's lead single is "What Did I Do?"  b/w "The Great Diamond D."

The State of New York vs. Derek Murphy: The State of New York vs. Derek Murphy is an EP by rapper and member of Brand Nubian, Sadat X, released in September 2000.  The EP is Sadat's second solo effort, following 1996's full-length LP "Wild Cowboys".  "The State of New York vs. Derek Murphy" features production from Diamond D and Minnesota, as well as guest appearances from the Money Boss Players, here credited as Hy Tymes.

Everything Is Everything (Brand Nubian album): Everything is Everything is the third album from Hip Hop group Brand Nubian and the second released by the trio of Sadat X, Lord Jamar, and DJ Sincere.  The album received mixed reviews and mediocre sales at the time of its release, despite a pair of popular singles, "Word Is Bond" and "Hold On."  The album is completely produced by Lord Jamar except the Sadat X solo song "Alladat," which was produced by D.I.T.C. member Buckwild.

Sadat Museum: The Sadat Museum is a cultural museum in Alexandria, Egypt, dedicated to the legacy of Egyptian president Anwar Al Sadat.  It was inaugurated on February 17, 2009 by Suzanne Mubarak and Jehan Al Sadat and is located next to the planetarium of the Bibliotheca Alexandrina, encompassing 200 square meters.  The museum also launched an internet website that contains videos, images and documents about Sadat.  The Museum holds the military uniform Sadat was wearing when he was assassinated, his desk, radio and some of the swords he received from Arab countries.  The web collection contains 14,000 images and 61 hours of video.

In God We Trust (Brand Nubian album): In God We Trust is the second album from hip hop group Brand Nubian.  Lead MC Grand Puba left the group to pursue a solo career in 1991, following the release of their revered debut "One for All".  DJ Alamo also left to work with Puba, leaving MC's Sadat X and Lord Jamar, who enlisted DJ Sincere to join the group.  The album was less successful than the group's debut but still received strong reviews.  The single "Punks Jump Up to Get Beat Down" became a "Billboard" Hot 100 hit, but was met with controversy over allegedly homophobic content, referencing the Sadat X line "Though I can freak, fly, flow, fuck up a faggot/I don't understand their ways, I ain't down with gays."  The single "Love Me or Leave Me Alone" was also a Hot-100 hit.  Lyrically, the album contains extremely militant content that reflects the group's identity as Five Percenters, adhering to the philosophy of the Nation of Gods and Earths.

Black October (album): Black October is the 3rd solo studio album by American rapper Sadat X.  It was released on Female Fun Music in 2006.

Khalid Islambouli: Khalid Ahmed Showky Al-Islambouli (Arabic: خالد أحمد شوقى الإسلامبولى‎ ‎ , ] ) (15 January 1955 – 15 April 1982) was an Egyptian army officer who planned and participated in the assassination of Egypt's third president, Anwar Sadat, during the annual 6th October victory parade on 6 October 1981.  Islambouli stated that his primary motivation for the assassination was Sadat's signing of the Camp David Accords with the State of Israel and Sadat's plan for a more progressive Egypt.  Islambouli was tried by a military tribunal, found guilty, and sentenced to death.  Following his execution, he was declared a martyr by many radicals in the Islamic world, and became an inspirational symbol for radical Islamic movements as one of the first 'modern martyrs' for Islam.

Anwar Sadat: Muhammad Anwar el-Sadat (Arabic: محمد أنور السادات‎ ‎ "Muḥammad Anwar as-Sādāt ", ]; 25 December 1918 – 6 October 1981) was the third President of Egypt, serving from 15 October 1970 until his assassination by fundamentalist army officers on 6 October 1981.  Sadat was a senior member of the Free Officers who overthrew King Farouk in the Egyptian Revolution of 1952, and a close confidant of President Gamal Abdel Nasser, under whom he served as Vice President twice and whom he succeeded as President in 1970.

Sadat X: Sadat X (born Derek Murphy; December 29, 1968) is an American rapper, best known as a member of Alternative hip hop group Brand Nubian.  Originally known as Derek X, Sadat takes his name from former Egyptian president Anwar Sadat.

Question: Rapper Sadat X is named for the third President of Egypt, who was?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "president_name": {
      "type": "string",
      "description": "The name of the president."
    },
    "president_title": {
      "type": "string",
      "description": "The specific title or role of the president mentioned."
    },
    "named_after_entity": {
      "type": "object",
      "properties": {
        "entity_name": {
          "type": "string",
          "description": "The name of the entity named after the president."
        },
        "entity_type": {
          "type": "string",
          "description": "The type of entity (e.g., rapper, album)."
        },
        "original_name": {
          "type": "string",
          "description": "The original name of the entity, if applicable."
        },
        "group_affiliation": {
          "type": "string",
          "description": "The group the entity is affiliated with, if applicable."
        }
      },
      "required": [
        "entity_name",
        "entity_type",
        "original_name",
        "group_affiliation"
      ],
      "additionalProperties": false
    },
    "president_details": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "The full name of the president."
        },
        "term_start_date": {
          "type": "string",
          "format": "date",
          "description": "The start date of the president's term."
        },
        "term_end_date": {
          "type": "string",
          "format": "date",
          "description": "The end date of the president's term."
        },
        "cause_of_death": {
          "type": "string",
          "description": "The cause of the president's death, if mentioned."
        }
      },
      "required": [
        "full_name",
        "term_start_date",
        "term_end_date",
        "cause_of_death"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "president_name",
    "president_title",
    "named_after_entity",
    "president_details"
  ],
  "additionalProperties": false
}
