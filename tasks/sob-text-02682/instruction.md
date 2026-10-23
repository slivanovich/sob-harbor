{
  "messages": [
    {
      "role": "system",
      "content": "Answer the question using only the provided context. Return a valid JSON object that strictly follows the given JSON schema. Do not output anything except the JSON object.\n\nRules:\n- No explanations: Do not include reasoning, analysis, or any sentences outside the JSON.\n- No markdown: Do not wrap the JSON in code blocks or add formatting like ``` or 'json'.\n- No extra text: Do not add prefixes or suffixes such as 'Answer:' or 'Output:'.\n- Follow the schema exactly: Use only the keys defined in the schema and ensure correct data types.\n- Include all required fields: Every field listed as required in the schema must appear in the JSON.\n- If unknown, return null: If the context does not contain the answer, set the field value to null instead of guessing."
    },
    {
      "role": "user",
      "content": "Context:\nCocker (album): Cocker is the tenth studio album by Joe Cocker, released in April 1986, his second on Capitol label.  It features hit singles \"You Can Leave Your Hat On\" and \"Don't You Love Me Anymore\", the first made popular after its use in the famous striptease scene in the film \"9 1/2 Weeks\".  Released as a single, Cocker's version of the song peaked at No. 35 on Billboard Hot Mainstream Rock Tracks.  The album also features rendition of Marvin Gaye's \"Inner City Blues\", a Motown legend's classic lament to urban decay.\n\nFire It Up (Joe Cocker album): Fire It Up is the twenty-second and final studio album by Joe Cocker, released on 6 November 2012 by Sony/Columbia in Europe.  It was recorded at Emblem Studios Calabasas, California and like Cocker's previous album, \"Hard Knocks\", it was produced by Matt Serletic.  The album was released as a regular jewel case edition as well as a premium edition with additional DVD.\n\nHeart &amp; Soul (Joe Cocker album): Heart & Soul is the nineteenth studio album by Joe Cocker, released in the UK on 12 October 2004, and in the US on 1 February 2005.  The album is composed solely of cover songs, including a live version of the U2 song \"One\" taken from Cocker's 2004 Night of the Proms performance in Antwerp, Belgium.\n\nHard Knocks (album): Hard Knocks is the twenty-first studio album by Joe Cocker, released on 1 October 2010 by Columbia Records in Europe.  It features nine new songs produced by Matt Serletic plus Cocker's version of the Dixie Chicks number \"I Hope\", which was produced by Tony Brown.  Apart from a regular CD release, the album was also released on vinyl.\n\nHymn for My Soul: Hymn for My Soul is the twentieth studio album by Joe Cocker, released in 2007.  It was produced by Ethan Johns.  Musicians on these special sessions included Tom Petty & The Heartbreakers' Benmont Tench, legendary drummer Jim Keltner, Mike Finnigan, ace guitarist Albert Lee, Dave Palmer, Greg Leisz, James Gadson, Bob Babbitt and Johns.  The songs include Cocker's signatures on George Harrison's \"Beware of Darkness\", Bob Dylan's \"Ring Them Bells\", John Fogerty's \"Long As I Can See The Light\" and Stevie Wonder's \"You Haven't Done Nothin'\".\n\nJim Keltner: James Lee Keltner (born April 27, 1942) is an American drummer known primarily for his session work.  He was characterized by Bob Dylan biographer Howard Sounes as \"the leading session drummer in America\".\n\nJoe Cocker!: Joe Cocker!  is Joe Cocker's second studio album, released in November 1969.  Following the template of his first LP, this album features numerous covers of songs originally performed by Bob Dylan (\"Dear Landlord\"), The Beatles (\"She Came in Through the Bathroom Window\" and \"Something\" - both released almost simultaneously with original versions; \"Let It Be\" was also recorded and released as a B-side), Leonard Cohen (\"Bird on the Wire\"), and future touring partner Leon Russell (\"Delta Lady\").  Cocker also co-wrote one song, \"That's Your Business Now\", Chris Stainton, who was also his writing partner in later years.\n\nJoe Cocker Live: Joe Cocker Live is a live album by Joe Cocker, released in 1990 (see 1990 in music).  It was recorded live 5 October 1989 at Memorial Auditorium in Lowell, Massachusetts with the exception of the last two tracks which were recorded in the studio.  The album was re-released in 2011 under the title \"Joe Cocker's Greatest Hits Live\".\n\nJoe Cocker (album): Joe Cocker is the third studio album by Joe Cocker, released in 1972 in Europe as Something to Say on Cube Records, and in the USA as \"Joe Cocker\" on A&M Records.  It contains the hit single \"High Time We Went\", that was released in the summer of 1971.  \"Joe Cocker\" signalled Cocker's change of direction into a more jazzy, blues style.  The album reached no. 30 in the US album charts.  However, although it received a positive response from the press, it made no impression on the British and European charts.\n\nMad Dogs &amp; Englishmen (album): Mad Dogs & Englishmen is a live album by Joe Cocker, released in 1970.  The album's title is drawn from the 1931 Noël Coward song of the same name.  Only four songs of the 16 on the original album were drawn from his first two studio albums.  Besides the contributions of bandmate and musical director Leon Russell, it draws equally from rock (the Rolling Stones, Traffic, Bob Dylan, the Beatles) and soul (Ray Charles, Sam and Dave, Otis Redding).  Accompanying Cocker is a choir, a three-piece horn section and several drummers.\n\nQuestion: When was the legendary drummer born who was part of \"Hymn for My Soul\", the twentieth studio album by Joe Cocker, released in 2007?\n\nRespond with JSON matching this schema:\n{\n  \"type\": \"object\",\n  \"properties\": {\n    \"album_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"title\": {\n          \"type\": \"string\"\n        },\n        \"release_year\": {\n          \"type\": \"integer\"\n        },\n        \"studio_album_number\": {\n          \"type\": \"integer\"\n        }\n      },\n      \"required\": [\n        \"title\",\n        \"release_year\",\n        \"studio_album_number\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"musician_details\": {\n      \"type\": \"object\",\n      \"properties\": {\n        \"role\": {\n          \"type\": \"string\"\n        },\n        \"name\": {\n          \"type\": \"string\"\n        },\n        \"birth_date\": {\n          \"type\": \"string\"\n        }\n      },\n      \"required\": [\n        \"role\",\n        \"name\",\n        \"birth_date\"\n      ],\n      \"additionalProperties\": false\n    },\n    \"question_answer\": {\n      \"type\": \"string\",\n      \"description\": \"The birth date of the legendary drummer.\"\n    }\n  },\n  \"required\": [\n    \"album_details\",\n    \"musician_details\",\n    \"question_answer\"\n  ],\n  \"additionalProperties\": false\n}"
    }
  ],
  "json_schema": {
    "type": "object",
    "properties": {
      "album_details": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string"
          },
          "release_year": {
            "type": "integer"
          },
          "studio_album_number": {
            "type": "integer"
          }
        },
        "required": [
          "title",
          "release_year",
          "studio_album_number"
        ],
        "additionalProperties": false
      },
      "musician_details": {
        "type": "object",
        "properties": {
          "role": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "birth_date": {
            "type": "string"
          }
        },
        "required": [
          "role",
          "name",
          "birth_date"
        ],
        "additionalProperties": false
      },
      "question_answer": {
        "type": "string",
        "description": "The birth date of the legendary drummer."
      }
    },
    "required": [
      "album_details",
      "musician_details",
      "question_answer"
    ],
    "additionalProperties": false
  },
  "answer_path": "/tmp/answer.json"
}
