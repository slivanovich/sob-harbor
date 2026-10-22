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
Thomas-McJunkin-Love House: Thomas-McJunkin-Love House is a historic home located at Charleston, West Virginia.  It was built for James R. Thomas, president of the Carbon Fuel Company, a coal mining business in the Kanawha Valley.  Known originally as "The Maples," it was built for him and his family around 1921.  It is in the English Tudor style and features half timbering in some of the gables and brick in others, but the exterior is predominantly in stucco.

Elgin Schoolhouse State Historic Site: Elgin Schoolhouse State Historic Site is a state park property in Nevada, United States, preserving a historic one-room schoolhouse that operated from 1922 to 1967.  In 1998, the building was restored at private expense to its original appearance.  In July 2005, it became a state historic site.  Later that year, floods damaged Nevada State Route 317, restricting access to the site.  The park features half of the school's original furnishings and other items authentic to the time period.  It is open for tours by appointment.

All Is Dream: All Is Dream is the fifth studio album by American rock band Mercury Rev.  It was released in the United Kingdom on August 27, 2001, in France on August 28, 2001, and in the United States on September 11, 2001.  The album's front cover features half of the 1991 painting "Breakthrough Dreaming" by artist and mystic Jennifer Hathaway.

Belgrade Marathon: The Belgrade Marathon is a marathon race held annually in Belgrade since 1988.  It is typically held in mid-April and also features half marathon and fun run for the public.

Nancy Argenta: Nancy Maureen Argenta (born Nancy Maureen Herbison on January 17, 1957) is a Canadian soprano singer, best known for performing music from the pre-classical era.  She has won international acclaim, and is considered by many as the leading Handel soprano of her time.

Manuela Kraller: Manuela Kraller (born 1 August 1981) is a German soprano singer from Ainring.  She is best known as the former lead singer of German symphonic metal band Xandria from late 2010, until late 2013.  Manuela was formerly one of the soprano vocalists in German symphonic metal band Haggard.

Zulma Bouffar: Zulma Madeleine Boufflar, known as Zulma Bouffar, (24 May 1841 – 20 January 1909), was a French actress and soprano singer, associated with the opéra-bouffe of Paris in the second half of the 19th century who enjoyed a successful career around Europe.

Mezzo-soprano: A mezzo-soprano or mezzo ( , ; ] meaning "half soprano") is a type of classical female singing voice whose vocal range lies between the soprano and the contralto voice types.  The mezzo-soprano's vocal range usually extends from the A below middle C to the A two octaves above (i.e. A–A in scientific pitch notation, where middle C = C).  In the lower and upper extremes, some mezzo-sopranos may extend down to the F below middle C (F) and as high as "high C" (C).

Keys to Ascension: Keys to Ascension is the fourth live and fifteenth studio album by the English rock band Yes.  It was released as a double album in October 1996 on Essential Records.  After guitarist Steve Howe and keyboardist Rick Wakeman returned to the band in mid-1995, the group relocated to Anderson's hometown of San Luis Obispo, California and started writing and rehearsing for a studio new album.  The reunion of this particular line-up was promoted with three shows at the city's Fremont Theater in March 1996, the five's first live performance together since 1979.  The album features half of the live set from the 1996 shows and two studio tracks which marked a return to producing long-form pieces.

Virpi Moskari: Virpi Moskari is a Mezzo-soprano, and a founder member of the Finnish a cappella group, Rajaton.

Question: What group features half soprano singer Virpi Moskari?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "group_name": {
      "type": "string",
      "description": "The name of the group."
    },
    "group_type": {
      "type": "string",
      "description": "The type or genre of the group."
    },
    "singer_information": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the singer."
        },
        "vocal_type": {
          "type": "string",
          "description": "The classical vocal type of the singer."
        },
        "vocal_type_alias": {
          "type": "string",
          "description": "The common alias or meaning for the vocal type, as mentioned in the context."
        },
        "role_in_group": {
          "type": "string",
          "description": "The role of the singer within the group."
        }
      },
      "required": [
        "name",
        "vocal_type",
        "vocal_type_alias",
        "role_in_group"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "group_name",
    "group_type",
    "singer_information"
  ],
  "additionalProperties": false
}
