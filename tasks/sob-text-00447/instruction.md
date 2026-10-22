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
Johnny Budd: John Walter Budd (January 14, 1899 - December 26, 1963) was a professional football player from Newton, New Jersey.  He was an offensive lineman and also served as a place kicker.  Budd played college football for Lafayette College before making his National Football League debut in 1926 with the Frankford Yellow Jackets.  After helping the Yellow Jackets win the 1926 NFL Championship, he later joined the Pottsville Maroons for the 1927 and 1928 seasons.  Budd was a first team All-Pro in 1926.

Jersey Budd: Jersey Budd is an English singer-songwriter from Leicester, England.

Budd Lake, New Jersey: Budd Lake is an unincorporated community and census-designated place (CDP) located within Mount Olive Township, in Morris County, New Jersey, United States.  As of the 2010 United States Census, the CDP's population was 8,968.  Budd Lake was named for John Budd.  Prior to that, it was called Hattacawanna Lake.

Vasa Park, New Jersey: Vasa Park is a small unincorporated community, built in the 1920s, near Budd Lake, in Mount Olive Township in Morris County, New Jersey, United States.

On the Waterfront: On the Waterfront is a 1954 American crime drama film directed by Elia Kazan and written by Budd Schulberg.  It stars Marlon Brando and features Karl Malden, Lee J. Cobb, Rod Steiger, Pat Henning, and, in her film debut, Eva Marie Saint.  The soundtrack score was composed by Leonard Bernstein.  The film was suggested by "Crime on the Waterfront" by Malcolm Johnson, a series of articles published in November–December 1948 in the "New York Sun" which won the 1949 Pulitzer Prize for Local Reporting, but the screenplay by Budd Schulberg is directly based on his own original story.  The film focuses on union violence and corruption amongst longshoremen while detailing widespread corruption, extortion, and racketeering on the waterfronts of Hoboken, New Jersey.

Buddtown, New Jersey: Buddtown is an unincorporated community located within Southampton Township in Burlington County, New Jersey, United States.  Located between Vincentown and Pemberton, it is named for Thomas Budd who owned farmland in the area in the 18th century.  The area itself contains houses and churches in the community itself and farmland surrounding the settlement.  The stream that runs through Buddtown is named Stop the Jade Run supposedly named for the cry made by the owners of a runaway horse, "jade" being an old name for a horse.

The Go-Betweens: The Go-Betweens were an indie rock band formed in Brisbane, Queensland, Australia in 1977 by singer-songwriters and guitarists Robert Forster and Grant McLennan.  They were later joined by Lindy Morrison on drums, Robert Vickers on bass guitar, and Amanda Brown on violin, oboe, guitar, and backing vocals, before disbanding in late 1989.  Forster and McLennan reformed the band in 2000 with a new line-up.  McLennan died on 6 May 2006 of a heart attack and The Go-Betweens disbanded again.

Pax Amicus Theatre: The Pax Amicus Theater is located in Budd Lake, New Jersey, United States, and was founded in 1970.  This community theater produces a full year-round season of Broadway and off-Broadway revivals, professional productions of works by Shakespeare and Edgar Allan Poe, a program devoted to children's theater, and special events throughout the year.

Question: Who has had more bandmates, Jersey Budd or The Go-Betweens?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_1": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the first entity"
        },
        "type": {
          "type": "string",
          "description": "Type of entity (e.g., solo artist, band)"
        },
        "bandmate_count": {
          "type": "integer",
          "description": "Number of bandmates for this entity"
        }
      },
      "required": [
        "name",
        "type",
        "bandmate_count"
      ],
      "additionalProperties": false
    },
    "entity_2": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "Name of the second entity"
        },
        "type": {
          "type": "string",
          "description": "Type of entity (e.g., solo artist, band)"
        },
        "bandmate_count": {
          "type": "integer",
          "description": "Number of distinct band members mentioned for this entity"
        },
        "bandmate_names": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Names of the band members for this entity"
        }
      },
      "required": [
        "name",
        "type",
        "bandmate_count",
        "bandmate_names"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "string",
      "description": "Statement comparing the number of bandmates between the two entities"
    },
    "entity_with_more_bandmates": {
      "type": "string",
      "description": "The name of the entity that had more bandmates"
    }
  },
  "required": [
    "entity_1",
    "entity_2",
    "comparison_result",
    "entity_with_more_bandmates"
  ],
  "additionalProperties": false
}
