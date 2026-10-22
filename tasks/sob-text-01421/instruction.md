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
The Bold Fisherman: The Bold Fisherman (Roud 291, Laws O24) is an English folk song popular with traditional singers and widely collected in the early and mid 20th century CE.  It has been frequently performed and recorded by contemporary folk singers and groups.

Cecil Sharp: Cecil James Sharp (22 November 1859 – 23 June 1924) was the founding father of the folk-song revival in England in the early 20th century.

Roud Folk Song Index: The Roud Folk Song Index is a database of nearly 200,000 references to nearly 25,000 songs that have been collected from oral tradition in the English language from all over the world.  It is compiled by Steve Roud, a former librarian in the London Borough of Croydon.  Roud's Index is a combination of the Broadside Index (printed sources before 1900) and a "field-recording index" compiled by Roud.  It subsumes all the previous well-known printed sources known to Francis James Child (the Child Ballads) and includes recordings from 1900 to 1975.  Until early 2006 the index was available only by a CD subscription; it can now be found online on a website maintained by the English Folk Dance and Song Society (EFDSS).  A partial list is also available at List of folk songs by Roud number.

Fred Jordan (singer): Fred Jordan (5 January 1922 – 30 July 2002) was a farm worker from Ludlow, Shropshire, and is noted as one of the great musically untutored traditional English singers.  He was first recorded in the 1940s by folk music researcher Alan Lomax and, over subsequent decades endeared himself to the English folk-song revival movement.  Jordan was awarded the English Folk Dance and Song Society's highest honour, the Gold Badge, "for distinguished and unique contributions to the folk performing arts" in 1995.

Master Kilby: Master Kilby (Roud 1434) is a traditional English folk song.  It was collected by Cecil Sharp and Maud Karpeles in 1909.  It has been arranged by Benjamin Britten

The Full English (folk music archive): The Full English launched in 2013 and is an ongoing English Folk Dance and Song Society (EFDSS) project to create a searchable digital archive of English folk song collections from the early 20th century, thereby preserving and improving the accessibility of these resources.  The project is supported by the Heritage Lottery Fund, The Folklore Society, the National Folk Music Fund and the English Miscellany Folk Dance Group.  An offshoot of the archive, also in 2013, was an album and concert tour under The Full English name by a collective of UK folk singers.

The Butcher's Boy (folk song): "The Butcher’s Boy" or "The Butcher Boy" (Laws P24, Roud 409) is an American folk song derived from traditional English ballads. Folklorists of the early 20th century considered it to be a conglomeration of several English broadside ballads, tracing its stanzas to "Sheffield Park", "The Squire's Daughter", "A Brisk Young Soldier", "A Brisk Young Sailor" and "Sweet William (The Sailor Boy)".

Billy Boy: "Billy Boy" is a traditional folk song and nursery rhyme found in the United States.  It has a Roud Folk Song Index number of 326.  It is a variant of the traditional English folk song "My Boy Billy", collected by Ralph Vaughan Williams and published by him in 1912 as number 232 in "Novello's School Songs".  The song is very popular with the Orange Order.

Somerset Carol: Come all you worthy gentlemen, sometimes referred to as the Somerset Carol, is an English folk carol of unknown authorship.  It was collected from a Mr. Rapsey, of Bridgwater during the English Folk-song revival at the turn of the 20th century by Cecil Sharp.  It was first published in 1905 in Sharp and Marson's "Folk songs from Somerset".

Lucy Broadwood: Lucy Etheldred Broadwood (9 August 1858 – 22 August 1929) was an English folksong collector and researcher during the late 19th and early 20th centuries.  As one of the founder members of the Folk-Song Society and Editor of the Folk Song Journal, she was one of the main influences of the English folk revival of that period.  She was an accomplished singer, composer, piano accompanist, and amateur poet.  She was much sought after as a song and choral singing adjudicator at music festivals throughout England, and was also one of the founders of the Leith Hill Music Festival in Surrey.

Question: Master Kilby (Roud 1434) is a traditional English folk song, it was collected by Maud Karpeles, and which person, who was the founding father of the folk-song revival in England in the early 20th century?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_name": {
      "type": "string",
      "description": "The name of the folk song."
    },
    "roud_number": {
      "type": "integer",
      "description": "The Roud Folk Song Index number for the song."
    },
    "collection_details": {
      "type": "object",
      "properties": {
        "collectors": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of individuals who collected the song."
        },
        "collection_year": {
          "type": "integer",
          "description": "The year the song was collected."
        }
      },
      "required": [
        "collectors",
        "collection_year"
      ],
      "additionalProperties": false
    },
    "founding_father_of_folk_revival": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the person identified as the founding father of the folk-song revival."
        },
        "role_description": {
          "type": "string",
          "description": "The specific role or title of the person in the folk-song revival."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the person."
        },
        "death_year": {
          "type": "integer",
          "description": "The death year of the person."
        }
      },
      "required": [
        "name",
        "role_description",
        "birth_year",
        "death_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_name",
    "roud_number",
    "collection_details",
    "founding_father_of_folk_revival"
  ],
  "additionalProperties": false
}
