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
Konstantin Vakulovsky: Captain Konstantin Konstantinovich Vakulovsky (born 28 October 1894, died Summer 1918) was a World War I flying ace credited with six aerial victories.  A major general's son, he volunteered for aviation duty on 8 August 1914, six days after graduating from university.  He taught himself to fly, and became one of Russia's first military pilots on 13 June 1915.  After escaping the fall of the Novogeorgievsk Fortress in a hazardous flight, Vakylovsky flew reconnaissance missions, some through heavy ground fire.  Given command of the newly formed First Fighter Detachment, he became a flying ace credited with six aerial victories.  He died in a flying accident during Summer 1918.

Japp–Maitland condensation: The Japp–Maitland condensation is an organic reaction and a type of Aldol reaction and a tandem reaction.  In a reaction between the ketone 2-pentanone and the aldehyde benzaldehyde catalyzed by base the bis Aldol adduct is formed first.  The second step is a ring-closing reaction when one hydroxyl group displaces the other in a nucleophilic substitution forming an oxo-tetrahydropyran.

West Bengal Legislative Assembly election, 1967: The West Bengal Legislative Assembly election, 1967 was held in Indian state of West Bengal in 1967 to elect 280 members to the West Bengal Legislative Assembly.  United Front led by Ajoy Mukherjee won majority of seats in the election, and formed first non-Congress government of the state.

Liberty Baptist Church (Grooverville, Georgia): Liberty Baptist Church is a historic church built about 1858 in Grooverville, Georgia.  It was added to the National Register of Historic Places on August 20, 2013.  It is located on Liberty Church Road.  There is a Georgia Historical Commission historical marker at the site.  According to the marker: "In 1841 the Ocklochnee anti-Missionary Baptist Association passed a ruling to dismiss members believing in the 'new fangled institutions of the day.'"  One of the excommunicated sisters joined with others in forming the Liberty Baptist Church.  The church includes a slave gallery.  Freed slaves from the area formed First Elizabeth Church in Grooverville.

The Sounds: The Sounds are a Swedish indie rock band.  Formed in Helsingborg in 1998 the group's musical style has been compared to new wave acts such as Blondie, The Cars, the Epoxies and Missing Persons.

SV St. Georg: SV St. Georg Hamburg is a German association football club playing in Hamburg.  The club was established 3 June 1895 and shares a common origin with "FC Hammonia Hamburg": both sides arose out of the students group Seminarvereinigung Frisch-Auf with "St. Georg" being formed first on the left bank of the Alster River, and "Hammonia" appearing later on the right bank.  Like their brother side, "St. Georg" was a founding member of the German Football Association (Deutscher Fussball Bund or German Football Association) at Leipzig in 1900.  However, while "Hammonia" folded after only a short existence, "St. Georg" still plays today.

Primary rock: Primary rock is an early term in geology that refers to crystalline rock formed first in geologic time, containing no organic remains, such as granite, gneiss and schist as well as igneous and magmatic formations from all ages.  Webster's Revised Unabridged Dictionary published in 1913 provides the following term as used in geology:

Tad (band): Tad (often styled as TAD) was an American grunge band from Seattle, Washington, formed in 1988 by Tad Doyle.  Among the first of the many bands which came out of Seattle in the grunge era, Tad was notable for the fact that its music was inspired far more by 1970s metal (much like Alice in Chains and Soundgarden) than the punk which influenced many other grunge bands.  Although their commercial success was limited, their music is still highly regarded amongst grunge fans.

Bloodbound: Bloodbound is a Swedish power metal band formed in 2004.  They released their first album, Nosferatu, in 2005 and their second, Book of the Dead, in May 2007.  The brainchild of former Street Talk members Fredrik Bergh and Tomas Olsson, the band has also included Michael Bormann (Jaded Heart), Urban breed (Tad Morose) and Pelle Åkerlind (Morgana Lefay).  Their debut album Nosferatu featured former Tad Morose singer Urban breed on vocals.  Released on 16 December 2005 (in Japan; European release date 24 February 2006), "Nosferatu" features artwork by Mark Wilkinson (Iron Maiden, Judas Priest, Marillion) and received an early rave review from the Swedish rock magazine Power Play.  Based solely on the strength of their debut album, the band opened for Evergrey and headlined day one of the Gothenburg Metal Festival.

Harris, Forbes &amp; Co.: Harris, Forbes & Co. was an investment banking affiliate of Harris Bank incorporated in 1911.  Harris, Forbes firm was acquired by Chase Manhattan Bank in 1930 to form Chase Harris, Forbes.  Just two years later, in 1932, the firm was dissolved after the passage of the Glass–Steagall Act in 1932.  Chase transferred what remained of its securities business to the Bank of Boston's newly formed First Boston Corporation, buttressing that firm's early municipal bond department.

Question: Which was formed first, The Sounds or Tad?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "first_formed_entity_name": {
      "type": "string",
      "description": "The name of the entity that was formed first."
    },
    "first_formed_year": {
      "type": "integer",
      "description": "The year the first formed entity was established."
    },
    "compared_entities": {
      "type": "array",
      "description": "Details of the entities being compared, including their formation years.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the entity."
          },
          "formation_year": {
            "type": "integer",
            "description": "The year the entity was formed."
          }
        },
        "required": [
          "name",
          "formation_year"
        ],
        "additionalProperties": false
      }
    }
  },
  "required": [
    "first_formed_entity_name",
    "first_formed_year",
    "compared_entities"
  ],
  "additionalProperties": false
}
