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
Bride of the Century: Bride of the Century () is a 2014 South Korean television series starring Lee Hong-gi and Yang Jin-sung.  It aired on cable channel TV Chosun from February 22 to April 12, 2014 for 16 episodes.  The story of the fantasy/romance drama revolves around a family curse that causes the first wife of the first born son to die.

Firstborn: A firstborn (also known as an eldest child or sometimes firstling) is the first child born to in the birth order of a couple through childbirth.  Historically, the role of the first born child has been socially significant, particularly for a first born son in patriarchal societies.  In law, many systems have incorporated the concept of primogeniture, wherein the first-born child inherits their parent's property.  The firstborn in Judaism, the "bechor", is also accorded a special position.

Milton S. Eisenhower: Milton Stover Eisenhower (September 15, 1899 – May 2, 1985) was an American educational administrator.  He served as president of three major American universities: Kansas State University, the Pennsylvania State University, and the Johns Hopkins University.  He was the younger brother of U.S. President Dwight D. Eisenhower.

Ida Stover Eisenhower: Ida Elizabeth Stover Eisenhower (May 1, 1862 – September 11, 1946) was the mother of U.S. President Dwight David Eisenhower (1890–1969), university president Milton Stover Eisenhower (1899–1985), Edgar N. Eisenhower (1889–1971), and Earl D. Eisenhower (1898–1968).

Edgar N. Eisenhower: Edgar N. Eisenhower (19 January 1889 – 12 July 1971) was a lawyer, and an older brother of President Dwight D. Eisenhower.  He was born in Hope, Kansas and graduated from the University of Michigan in 1914.  He began practicing law in 1915 in Tacoma, Washington and was known as a “shoot from the hip ultraconservative.”

Duryodhana: Duryodhana (Devanāgari: दुर्योधन ; lit.  "unconquerable warrior"), originally named "Suyodhana" (Devanāgari: सुयोधन ; lit.  "great warrior") is a major character in the Hindu epic "Mahabharata" and was the eldest of the Kauravas, the hundred sons of blind king Dhritarashtra and Queen Gandhari.  Despite being the first born son of the incumbent king, he becomes disqualified as heir to the throne of Hastinapura upon the return of his cousins, the Pandavas, who left their rural forest dwelling upon the death of their father Pandu, the preceding king of Hastinapura and younger brother to Dhrithrashtra.  His resultant animosity towards his cousins renders Duryodhana the chief antagonist of the epic.  Karna was the closest friend of Duryodhana.  Notably, Duryodhana, with significant assistance from Karna, performs Digvijaya Yatra when the Pandavas are in exile, conquering all kings in every direction of the world, establishing himself as the emperor of the world.

Eisenhower Home: The Eisenhower Home in Abilene, Kansas at the Eisenhower Presidential Center, was the house where U.S. President Dwight D. Eisenhower lived with his five brothers from 1898 to 1911, when he entered the U.S. Military Academy at West Point at age 20.  In 1898 Eisenhower's father, David Jacob Eisenhower, and his wife Ida Elizabeth Stover Eisenhower, bought the house from David's uncle Abraham.  David and Ida lived in the house until their deaths in 1942 and 1946.

Kalaimanokahoʻowaha: Kalaimanokahoʻowaha (also known as Kanaʻina) was an aliʻi high chief of the island of Hawai'i who lived during the period of Captain James Cook's visit and western naming of the Sandwich Islands.  He was the chief said to have struck the first blow to Cook when he attempted to kidnap Kalaniʻōpuʻu, the king of the island.  He was called Kanaʻina nui ( an aliʻi title) as a birthright from his father, Keaweʻopala, first born son of Alapainui.  After his father was killed by Kalaniʻōpuʻu, he would serve the new king as a kaukau aliʻi, a service class of Hawaiian nobility that his mother, Moana Wahine had descended from.  This aliʻi service line would continue throughout the Kingdom of Hawaii.

Utoni Nujoma: Utoni Daniel Nujoma (born 8 September 1952) is a Namibian politician who has served in the government of Namibia as Minister of Land Reform since 2015.  Previously he was Deputy Minister of Justice from 2005 to 2010, Minister of Foreign Affairs from 2010 to 2012, and Minister of Justice from 2012 to 2015.  Nujoma is also a member of the Central Committee and Politburo of SWAPO.  Nujoma is the first born son of Namibia's founding President Sam Nujoma, who was in office from 1990 to 2005, and Kovambo Nujoma, the former First Lady of Namibia.

Laodice III: Laodice III (in Greek Λαοδικη) also known as Laodika, was a Princess of Pontus and a Seleucid Queen.  She was regent for her first born son, Antiochus, during the Anabase expedition of her husband, Antiochus III the Great, between 212 and 206 BC.  Antiochus created a royal cult dedicated to her in 193 BC.  In 192 BC she was pushed out of political life due to her husband's remarriage.  Her last known activities are documented in 177–176 BC and relate to the court of her son, Seleucus IV.

Question: Where was the first born son of Ida Stover Eisenhower born?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the firstborn son."
    },
    "parent_name": {
      "type": "string",
      "description": "The name of the parent whose firstborn son is being identified."
    },
    "birth_location": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the person was born."
        },
        "state": {
          "type": "string",
          "description": "The state where the person was born."
        }
      },
      "required": [
        "city",
        "state"
      ],
      "additionalProperties": false
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the firstborn son."
    },
    "relationship_to_president": {
      "type": "string",
      "description": "The relationship of the firstborn son to a US President mentioned in the context."
    }
  },
  "required": [
    "person_name",
    "parent_name",
    "birth_location",
    "birth_year",
    "relationship_to_president"
  ],
  "additionalProperties": false
}
