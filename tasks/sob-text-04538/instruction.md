{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nMadeline Lee: Madeline Lee is a one act opera, composed by John Haddock to a libretto written jointly by the composer and Michael Campbell.  It premiered at the Sydney Opera House on 8 October 2004 in an Opera Australia production directed by Michael Campbell and conducted by Tom Woods.\n\nGustavo primo, re di Svezia: Gustavo primo, re di Svezia (\"Gustavus the First, King of Sweden\") is a three act opera seria by Baldassare Galuppi, with a libretto by Carlo Goldoni, fictionalising events in the life of Gustav I of Sweden.  Composed in honour of the Genoese nobleman marchese Giovanni Giacomo Grimaldi, it premiered on 25 May 1740 at Venice's Teatro San Samuele.  It was first recorded in 2003 by Karoly, Gonzalez, Cecchetti and the Capella Savaria Baroque Orchestra, conducted by Fabio Pirona.\n\nGloriana: Gloriana, Op. 53, is an opera in three acts by Benjamin Britten to an English libretto by William Plomer, based on Lytton Strachey's 1928 \"Elizabeth and Essex: A Tragic History\".\n\nWilliam McAlpine (tenor): William McAlpine (3 December 1922 – 2 February 2004) was leading British tenor during the 1950s and 60s.  He created roles in two operas by Benjamin Britten— A Novice in \"Billy Budd\" and The Spirit of the Masque in \"Gloriana\".  He also sang Andres in the UK premiere of Berg's \"Wozzeck\".\n\nSafié: Safié is a one act opera by American composer Henry Kimball Hadley.  The opera's libretto was written in English by Edward Oxenford, but its premiere, on April 4, 1909 in Mainz, Germany, was given in a German translation by Otto Neitzel.  Hadley conducted the premiere, and the title role was sung by American soprano Marguerite Lemon.\n\nSapho (Gounod): Sapho is a 3-act opera by Charles Gounod to a libretto by Émile Augier which was premiered by the Paris Opera at the Salle Le Peletier on 16 April 1851.  It was presented only 9 times in its initial production, but was a \"succès d'estime\" for the young composer, with the critics praising Act 3 in particular.  It was later revived in 2-act (1858) and 4-act (1884) versions, achieving a total of 48 performances.\n\nGallantry (opera): Gallantry is a one act opera by composer Douglas Moore.  The work is a parody of soap opera, complete with sung commercial interruptions.  The work uses an English language libretto by Arnold Sundgaard.  The opera premiered in a double bill with Dominick Argento's \"The Boor\" on March 19, 1958, in New York City at the now-destroyed Brander Matthews Theater on 117th Street, between Amsterdam Avenue and Morningside Drive.  It was presented by the Columbia University School of Music with a student cast.  It has subsequently been staged by several other university opera theatre programs in the United States and Canada, including UCLA (1958, 1974, and 1994), Immaculate Heart College (1968), Goucher College (1969), the University of Michigan (1978), the University of Toronto (1988), San Diego State University (1989), Pepperdine University (1990), Wilfrid Laurier University (1992), the University of Arizona (1995), George Washington University (1999), and the University of Wisconsin (2003) among others.  The University of Southern California toured the opera to the Netherlands in 1968.\n\nBianca (opera): Bianca is a one act opera by American composer Henry Kimball Hadley.  The opera's libretto was an English-language adaptation of Carlo Goldoni's comedy \"The Mistress of the Inn\" by Grant Stewart.  Hadley finished the score in January, 1917, and entered it in a competition for the best American opera without chorus, for which William Wade Hinshaw offered a $1000 prize and a promise to produce the opera in New York City by the American Society of Singers.  It won, and was produced on October 19, 1918, at the Park Theater in Manhattan, with the composer conducting, and soprano Maggie Teyte in the title role.\n\nMaritana: Maritana is a three act opera including both spoken dialogue and some recitatives, composed by William Vincent Wallace, with a libretto by Edward Fitzball (1792–1873).  The opera is based on the 1844 French play \"Don César de Bazan\" by Adolphe d'Ennery and Philippe François Pinel Dumanoir, which was also the source material for Jules Massenet's opéra comique \"Don César de Bazan\" (the character of Don César de Bazan first appeared in Victor Hugo's \"Ruy Blas\").  The opera premiered at the Theatre Royal, Drury Lane on 15 November 1845.\n\nLetters, Riddles and Writs: Letters, Riddles and Writs is a one act opera for television by Michael Nyman.  The story is devised by Nyman, with a libretto by Jeremy Newson and Pat Gavin that incorporates Emily Anderson's English translations of correspondence and other texts by Wolfgang Amadeus Mozart, the subject of the opera.\n\nQuestion: What is the name of the three act opera that had a role created by William McAlpine ?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"opera_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the opera.\"\n    },\n    \"number_of_acts\": {\n      \"type\": \"integer\",\n      \"description\": \"The number of acts in the opera.\"\n    },\n    \"role_creator\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the person who created a role in the opera.\"\n    },\n    \"role_name\": {\n      \"type\": \"string\",\n      \"description\": \"The name of the specific role created by the person.\"\n    }\n  },\n  \"required\": [\n    \"opera_title\",\n    \"number_of_acts\",\n    \"role_creator\",\n    \"role_name\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "opera_title": {
        "type": "string",
        "description": "The title of the opera."
      },
      "number_of_acts": {
        "type": "integer",
        "description": "The number of acts in the opera."
      },
      "role_creator": {
        "type": "string",
        "description": "The name of the person who created a role in the opera."
      },
      "role_name": {
        "type": "string",
        "description": "The name of the specific role created by the person."
      }
    },
    "required": [
      "opera_title",
      "number_of_acts",
      "role_creator",
      "role_name"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
