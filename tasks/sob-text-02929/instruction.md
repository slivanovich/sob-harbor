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
I've Gotta Be Me: "I've Gotta Be Me" is a popular song that appeared in the Broadway musical "Golden Rainbow", which starred Steve Lawrence and Eydie Gormé.  The musical opened in New York City at the Shubert Theatre on February 4, 1968, and closed less than a year later, on January 11, 1969.  The music and lyrics for the musical were by Walter Marks and were composed in 1967; the production featured a book by Ernest Kinoy.  This song was listed in the musical as "I've Got to Be Me", and it was sung by Lawrence's character Larry Davis at the end of the first act.  Lawrence released the song as a single in 1967, and the following year it hit number six on the "Billboard" Easy Listening chart, with little or no support from traditional Top 40 radio.

Steve and Eydie: Steve and Eydie is the name of an American pop vocal duet, consisting of Steve Lawrence and Eydie Gormé.  They were a husband and wife team from their wedding in 1957 until Eydie's death in 2013.  Both have also had separate careers as solo singers.  The performer name on their duet releases was denoted as "Steve and Eydie", without the last names.  Eydie was born as Edith Gormezano, while Steve's birth name was Sidney Leibowitz.

Eydie Gormé: Eydie Gormé (also spelled Gorme; August 16, 1928 – August 10, 2013) was an American singer who performed solo as well as with her husband, Steve Lawrence, in popular ballads and swing.  She earned numerous awards, including a Grammy and an Emmy.  She retired in 2009 and she died in 2013.

The Diamond Jubilee World Tour: The Diamond Jubilee World is the concert tour by American recording artist, Frank Sinatra, with Steve Lawrence and Eydie Gormé.

Ken Greengrass: Ken Greengrass (June 22, 1926 – April 10, 2014) was an Emmy-winning American music and television producer, perhaps best known as a manager of such musical performers as Eydie Gormé and Steve Lawrence, Art Garfunkel and Florence Henderson.

Together Again Tour: The Diamond Jubilee World is the concert tour by American recording artist, Frank Sinatra, with Dean Martin and Sammy Davis Jr..

Footsteps (Steve Lawrence song): "Footsteps" is a hit single by American singer and actor Steve Lawrence released in 1960 through ABC-Paramount Records in the US and via the HMV label in the UK.  The song was written by Barry Mann and Hank Hunter.  Lawrence's single, which also features Lawrence's wife, Eydie Gormé, as a backing vocalist, peaked on the US Singles Chart at No.7 in April 1960, and the UK Singles Chart at No.4 in June 1960.

Steve Lawrence: Steven Lawrence (born July 8, 1935) is an American singer and actor, best known as a member of a duo with his wife Eydie Gormé, billed as "Steve and Eydie."  The two appeared together since appearing regularly on "Tonight Starring Steve Allen" in the mid-1950s until Gormé's retirement in 2009.

Frank Sinatra's Greatest Hits: Frank Sinatra's Greatest Hits!  is Frank Sinatra's first compilation released on his own Reprise Records.  It concentrates on mostly single releases from the mid to late 60's, which fluctuates between adult contemporary pop and jazzy swing.  The album opens up with Sinatra's recent number one hit "Strangers in the Night" and continues through the varied styles of music Sinatra recorded in the 60's, from easy listening ballads like "It Was a Very Good Year" and "Softly, as I Leave You" to contemporary pop like "When Somebody Loves You" and "That's Life".  "Greatest Hits" was a modest hit, peaking at #55 on the album charts in late 1968.  A second volume was issued in 1972, "Frank Sinatra's Greatest Hits, Vol.  2".  Both albums have since been supplanted with newer and more cohesive compilations.

Golden Rainbow (musical): Golden Rainbow was the title of a Broadway musical that opened in 1968.  It starred Steve Lawrence and Eydie Gormé for its entire run until it closed in early 1969.

Question: The Diamond Jubilee World is the concert tour by American recording artist, Frank Sinatra, with Steve Lawrence and Eydie Gormé, Gormé was an American singer who performed solo as well as with her husband, who , in popular ballads and swing?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "concert_tour_name": {
      "type": "string",
      "description": "The name of the concert tour."
    },
    "main_artist": {
      "type": "string",
      "description": "The primary recording artist for the tour."
    },
    "featured_artists": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of artists who performed with the main artist on the tour."
    },
    "eydie_gorme_details": {
      "type": "object",
      "properties": {
        "full_name": {
          "type": "string",
          "description": "Eydie Gorm\u00e9's full name."
        },
        "performing_partner_name": {
          "type": "string",
          "description": "The name of Eydie Gorm\u00e9's performing partner and husband."
        },
        "performing_partner_relationship": {
          "type": "string",
          "description": "The relationship of the performing partner to Eydie Gorm\u00e9."
        },
        "genres_performed": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Genres of music Eydie Gorm\u00e9 performed."
        }
      },
      "required": [
        "full_name",
        "performing_partner_name",
        "performing_partner_relationship",
        "genres_performed"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "concert_tour_name",
    "main_artist",
    "featured_artists",
    "eydie_gorme_details"
  ],
  "additionalProperties": false
}
