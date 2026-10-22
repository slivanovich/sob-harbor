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
Kane (comics): Kane is a comic book series created, written and drawn by Paul Grist.  Grist also self-published it through his company, Dancing Elephant Press.  It concerns a police detective who works in the 39th precinct of the fictional American city of New Eden, which seems to be located on the west coast.  Despite being a UK citizen, Grist appears to have modeled New Eden and its police force in the style of American Cop shows such as Hill Street Blues and NYPD Blue.  Another clear influence is the work of Frank Miller, particularly his Sin City comics.  Cerebus was another formative influence, particularly because it proved to Grist that self-published comics were a viable proposition; the first issue of Cerebus that Grist read was #39, hence the designation of Kane's precinct.

Cop Hater (film): Cop Hater is a 1958 American police procedural film, based on the 1956 novel "Cop Hater" by Ed McBain, the first in a series of books about the 87th Precinct in New York City.  The film was produced and directed by William Berke, written by Henry Kane, and stars Robert Loggia and Gerald S. O'Loughlin.

The Mugger (novel): The Mugger is a (1956) novel by Ed McBain, the second in his 87th Precinct series.  It was adapted for a film of the same name in 1958.  In 2002 the author wrote an introduction to this and to his earlier novel "Cop Hater" when both were published in an omnibus edition.

Nick Amaro: Nicolas "Nick" Amaro is a fictional character on the NBC police procedural drama "", portrayed by Danny Pino.  Amaro is a detective with the Manhattan SVU at the 16th Precinct of the New York City Police Department.

Mariska Hargitay: Mariska Magdolna Hargitay ( ; born January 23, 1964) is an American actress best known for her role as NYPD Special Victims Unit Detective/Sergeant/Lieutenant Olivia Benson on the NBC drama series "", for which she has earned multiple awards and nominations, including an Emmy and Golden Globe.

Cop Hater: Cop Hater (1956) is the first 87th Precinct police procedural novel by Ed McBain.  The murder of three detectives in quick succession in the 87th Precinct leads Detective Steve Carella on a search that takes him into the city's underworld and ultimately to a .45 automatic aimed straight at his head.

Olivia Benson: Olivia Margaret Benson is a fictional character on the NBC police procedural drama "", portrayed by Mariska Hargitay.  Benson holds the rank of Lieutenant and is the Commanding Officer of the Manhattan Special Victims Unit of the New York City Police Department, which operates out of the 16th precinct.

Amanda Rollins: Amanda Rollins is a fictional character on the NBC police procedural drama "", portrayed by Kelli Giddish.  Rollins is a detective with the Manhattan Special Victims Unit at the 16th Precinct of the New York Police Department.

The Policeman of the 16th Precinct: The Policeman of the 16th Precinct (Greek: Ο Ηλίας του 16ου ) is a 1959 Greek comedy film directed by Alekos Sakellarios.

Mad Bull 34: Mad Bull 34 (マッド★ブル34 , Maddo Buru Sanjūyon ) is a manga series written by Kazuo Koike and illustrated by Noriyoshi Inoue, serialized in Shueisha's "Young Jump" between 1986 and 1990, and collected in 27 volumes.  The series follows the toughest cop in the NYPD's 34th precinct, Mad Bull, and his often-violent exploits when dealing the city's criminals.

Question: Which actress has won multiple awards and nominations for playing a cop out of the 16th precinct?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress."
    },
    "character_played": {
      "type": "string",
      "description": "The name of the character played by the actress."
    },
    "precinct_number": {
      "type": "integer",
      "description": "The number of the precinct the character works out of."
    },
    "awards_information": {
      "type": "object",
      "properties": {
        "has_won_multiple_awards": {
          "type": "boolean",
          "description": "Indicates if the actress has won multiple awards for the role."
        },
        "specific_awards": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of specific awards mentioned."
        }
      },
      "required": [
        "has_won_multiple_awards",
        "specific_awards"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actress_name",
    "character_played",
    "precinct_number",
    "awards_information"
  ],
  "additionalProperties": false
}
