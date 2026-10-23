{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nBlah Blah Blah (Gershwin song): \"Blah, Blah, Blah\" is a 1931 song with music by George Gershwin, to lyrics by Ira Gershwin.  Originally written for the abortive \"East is West\" it was taken \"out of the trunk\" by the Gershwins for Delicious (1931 film).  It was later used in the 2012 Broadway production of \"Nice Work if You Can Get it\", a compilation of Gershwin nice lyrics not songs.\n\nEmbraceable You: \"Embraceable You\" is a popular jazz song, with music by George Gershwin and lyrics by Ira Gershwin.  The song was originally written in 1928 for an unpublished operetta named \"East Is West\".  It was eventually published in 1930 and included in the Broadway musical \"Girl Crazy\" where it was performed by Ginger Rogers in a song and dance routine choreographed by Fred Astaire.\n\nSomeone to Watch Over Me (song): \"Someone to Watch Over Me\" is a song composed by George Gershwin with lyrics by Ira Gershwin from the musical \"Oh, Kay! \" (1926), where it was introduced by Gertrude Lawrence.  Gershwin originally approached the song as an uptempo jazz tune, but his brother Ira suggested that it might work much better as a ballad, and George ultimately agreed.  It has been performed by many artists since its debut and is a jazz standard as well as a key work in the Great American Songbook.  It is also referenced in the Frank McGuinness play \"Someone Who'll Watch Over Me\".\n\nIra, George and Joe: Ira, George and Joe is a live album by American jazz guitarist Joe Pass, released in 1981 (see 1981 in music).  It was re-issued in 1994 on CD by Original Jazz Classics.  It is a tribute album to the songs of George Gershwin and Ira Gershwin.\n\nThey Can't Take That Away from Me: \"They Can't Take That Away from Me\" is a 1937 jazz song (see 1937 in music) written by George Gershwin and Ira Gershwin and introduced by Fred Astaire in the 1937 film \"Shall We Dance\".\n\nShall We Dance (1937 film): Shall We Dance, released in 1937, is the seventh of the ten Astaire-Rogers musical comedy films.  The idea for the film originated in the studio's desire to exploit the successful formula created by Richard Rodgers and Lorenz Hart with their 1936 Broadway hit \"On Your Toes\".  The musical featured an American dancer getting involved with a touring Russian ballet company.  In a major coup for RKO, Pan Berman managed to attract the Gershwins – George Gershwin who wrote the symphonic underscore and Ira Gershwin the lyrics – to score this, their second Hollywood musical after \"Delicious\" in 1931.\n\nThe Man I Love (song): \"The Man I Love\" is a popular standard, with music by George Gershwin and lyrics by his brother Ira Gershwin.  Originally part of the 1924 score for the Gershwin government satire \"Lady, Be Good\" as \"The Girl I Love\", the song was deleted from the show as well as from both the 1927 anti-war satire \"Strike Up the Band\" (where it first appeared as \"The Man I Love\") and 1928 Ziegfeld hit \"Rosalie\" after tryouts.  It is the basis for the 1947 film \"The Man I Love\" starring Ida Lupino and Bruce Bennett and featured prominently throughout.\n\nLiza (All the Clouds'll Roll Away): \"Liza (All the Clouds'll Roll Away)\" is a song composed by George Gershwin with lyrics by Ira Gershwin and Gus Kahn.  It was introduced in 1929 by Ruby Keeler (as Dixie Dugan) in Florenz Ziegfeld's musical \"Show Girl\".  The stage performances were accompanied by the Duke Ellington Orchestra.  On the show's opening night in Boston on June 25, 1929, Keeler's husband and popular singer Al Jolson suddenly stood up from his seat in the third row and sang a chorus of the song, much to the surprise of the audience and Gershwin himself.  Jolson recorded the song a few days later on July 6, 1929, and his rendition rose to number nine on the charts of the day.\n\nOscar Peterson Plays George Gershwin: Oscar Peterson Plays George Gershwin is a 1952 album by pianist Oscar Peterson of popular songs written by George Gershwin and Ira Gershwin.  Several tracks were included on the 1959 album \"Oscar Peterson Plays the George Gershwin Songbook\".\n\nI Got Rhythm: \"I Got Rhythm\" is a piece composed by George Gershwin with lyrics by Ira Gershwin and published in 1930, which became a jazz standard.  Its chord progression, known as the \"rhythm changes\", is the foundation for many other popular jazz tunes such as Charlie Parker's and Dizzy Gillespie's bebop standard \"Anthropology (Thrivin' on a Riff)\".\n\nQuestion: Which film did George Gershwin and Ira Gershwin write the famous jazz song for?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"film_title\": {\n      \"type\": \"string\",\n      \"description\": \"The title of the film for which the song was written.\"\n    },\n    \"song_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"song_title\": {\n          \"type\": \"string\",\n          \"description\": \"The title of the famous jazz song.\"\n        },\n        \"song_genre\": {\n          \"type\": \"string\",\n          \"description\": \"The genre of the song.\"\n        },\n        \"year_introduced\": {\n          \"type\": \"integer\",\n          \"description\": \"The year the song was introduced.\"\n        }\n      },\n      \"required\": [\n        \"song_title\",\n        \"song_genre\",\n        \"year_introduced\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"composers\": {\n      \"type\": \"array\",\n      \"description\": \"A list of composers who wrote the song.\",\n      \"items\": {\n        \"type\": \"object\",\n        \"properties\": {\n          \"first_name\": {\n            \"type\": \"string\",\n            \"description\": \"The first name of the composer.\"\n          },\n          \"last_name\": {\n            \"type\": \"string\",\n            \"description\": \"The last name of the composer.\"\n          }\n        },\n        \"required\": [\n          \"first_name\",\n          \"last_name\"\n        ],\n        \"additionalProperties\": false\n      }\n    }\n  },\n  \"required\": [\n    \"film_title\",\n    \"song_details\",\n    \"composers\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "film_title": {
        "type": "string",
        "description": "The title of the film for which the song was written."
      },
      "song_details": {
        "type": "object",
        "properties": {
          "song_title": {
            "type": "string",
            "description": "The title of the famous jazz song."
          },
          "song_genre": {
            "type": "string",
            "description": "The genre of the song."
          },
          "year_introduced": {
            "type": "integer",
            "description": "The year the song was introduced."
          }
        },
        "required": [
          "song_title",
          "song_genre",
          "year_introduced"
        ],
        "additionalProperties": false
      },
      "composers": {
        "type": "array",
        "description": "A list of composers who wrote the song.",
        "items": {
          "type": "object",
          "properties": {
            "first_name": {
              "type": "string",
              "description": "The first name of the composer."
            },
            "last_name": {
              "type": "string",
              "description": "The last name of the composer."
            }
          },
          "required": [
            "first_name",
            "last_name"
          ],
          "additionalProperties": false
        }
      }
    },
    "required": [
      "film_title",
      "song_details",
      "composers"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
