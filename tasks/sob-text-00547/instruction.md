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
Chris Doig (opera singer): Christopher Keith Doig, CNZM, OBE (4 April 1948 – 13 October 2011) was a New Zealand opera singer and sports administrator.  In 1972 he won New Zealand's Mobil Song Quest and subsequently became principal tenor at the Vienna State Opera.  Later in his career he was appointed chief executive of New Zealand Cricket and was a member of the New Zealand Rugby Union board.

Kiri – The Best Of: Kiri is a greatest hits album released by New Zealand opera diva, Kiri Te Kanawa in 2001.

Michael F. Williams: Michael F. Williams (born 1962, New Zealand) is a composer of contemporary classical music.  He has received commissions from many of New Zealand's major musical institutions such as the New Zealand Symphony Orchestra, NBR New Zealand Opera and Chamber Music New Zealand and his work is regularly broadcast on Radio New Zealand Concert.  A lecturer in composition at the University of Waikato, Williams has received recognition in the NZSO-SOUNZ Readings on three occasions and in the SOUNZ Contemporary Award in 2012 for his multimedia World War II opera, The Juniper Passion.

Kiri Te Kanawa: Dame Kiri Janette Te Kanawa {'1': ", '2': ", '3': ", '4': "} {'1': ", '2': ", '3': ", '4': "} (pronounced ; born Claire Mary Teresa Rawstron, March 6, 1944) is a New Zealand soprano.  She has a full lyric soprano voice, which has been described as "mellow yet vibrant, warm, ample and unforced".

Maori Songs: Maori Songs is a traditional album released by New Zealand opera diva, Kiri Te Kanawa in 1999 to celebrate the new millennium.

The Very Best Of (Kiri Te Kanawa album): The Very Best Of is a greatest hits album released by New Zealand opera diva, Kiri Te Kanawa in 2003.

Auckland Philharmonia Orchestra: The Auckland Philharmonia Orchestra (APO) is a symphony orchestra based in Auckland, New Zealand.  Its principal concert venue is the Auckland Town Hall.  The APO is the accompanying ensemble for performances by the NBR New Zealand Opera and the Royal New Zealand Ballet in Auckland.  The APO's patrons are Dame Catherine Tizard, Dame Kiri Te Kanawa, Sir James Wallace, Dame Rosanne Meo and Vice Patron Dame Jenny Gibbs.

Kiri Sings Karl: Kiri Sings Karl is a 2006 classical album by New Zealand opera singer Kiri Te Kanawa, conducted by Karl Jenkins.  All but one of the pieces are composed by the acclaimed Argentine classical composer Carlos Guastavino.  ("Misa Criolla" is by the Argentine composer Ariel Ramirez).

French Songs and Arias: French Songs and Arias is an album released by New Zealand opera diva Kiri Te Kanawa in 1997.

Iosefa Enari: Iosefa Enari (1954 – 22 October 2000) was a New Zealand opera singer who was born in Samoa.  The Iosefa Enari Memorial Award, presented annually by Creative New Zealand, recognises Enari's pioneering contribution to Pacific Islands opera.  Enari was the Artistic Director of "Classical Polynesia", the first New Zealand opera combining traditional Samoan words and music with classical opera.  "Classical Polynesia" premiered at the New Zealand International Festival of the Arts 1998 in Wellington, and featured Jonathan Lemalu.

Question: When was the New Zealand opera singer born who's album is Kiri Sings Karl?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "opera_singer": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the New Zealand opera singer."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the opera singer."
        },
        "birth_date": {
          "type": "string",
          "description": "The full birth date of the opera singer."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the opera singer."
        }
      },
      "required": [
        "name",
        "nationality",
        "birth_date",
        "birth_year"
      ],
      "additionalProperties": false
    },
    "album_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the album associated with the singer."
        }
      },
      "required": [
        "title"
      ],
      "additionalProperties": false
    },
    "question_answer": {
      "type": "string",
      "description": "The direct answer to the question about the birth date."
    }
  },
  "required": [
    "opera_singer",
    "album_details",
    "question_answer"
  ],
  "additionalProperties": false
}
