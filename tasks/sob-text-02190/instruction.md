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
Elephant Jokes: Elephant Jokes is the 12th studio album released by singer-songwriter Robert Pollard on August 11, 2009, and the 8th full-length album to be released by Pollard (along with several EP's and singles) since the break-up of his band Guided by Voices in 2004.  Unlike recent Pollard albums, Todd Tobias does not play all the instruments on "Elephant Jokes", as Pollard plays some guitar on this album.

Born in '58: "Born in '58" is the last single from Bruce Dickinson's debut solo album, "Tattooed Millionaire", released on March 25 1991.  The song is about Bruce Dickinson's early life, growing up with his Grandparents in Worksop (Dickinson was born in 1958).

Weatherman and Skin Goddess: Weatherman and Skin Goddess is a limited EP from singer-songwriter Robert Pollard.  Only 1,000 CDs and 500 12 inch LPs were put into production and were made available exclusively on Pollard's website.  Released on April 15, this marks the first release from Robert Pollard's record label Guided by Voices Inc.

The Wicker Man (song): "The Wicker Man" is a song by Iron Maiden, released as the first single and opening track from their album "Brave New World" in April 2000.  It is also the first single by the band since the returns of vocalist Bruce Dickinson and guitarist Adrian Smith in 1999.  It was co-written by Smith, Dickinson and Steve Harris.  It was co-produced by Kevin Shirley and Harris.  The title is inspired by the British cult film of the same name.  The song should not be confused with "Wicker Man" from Dickinson's solo career, the lyrics of which are more closely themed around the film.  The latter song can be found on the 2 disc edition of "The Best of Bruce Dickinson".

Bruce Dickinson: Paul Bruce Dickinson (born 7 August 1958), known professionally as Bruce Dickinson, is an English singer, songwriter, musician, airline pilot, entrepreneur, author and broadcaster.  He is the lead singer of the heavy metal band Iron Maiden and is renowned for his wide-ranging operatic vocal style and energetic stage presence.

Robert Pollard: Robert Ellsworth Pollard Jr. (born October 31, 1957) is an American musician and singer-songwriter who is the leader and creative force behind indie rock group Guided by Voices.  In addition to his work with Guided by Voices, he continues to have a prolific solo career with 22 solo albums released so far.

Choreographed Man of War: Choreographed Man of War is an album by Robert Pollard and the Soft Rock Renegades, released in 2001.  The album features Robert Pollard (vocals, guitar), Greg Demos (bass), and Jim Macpherson (drums).

The Crawling Distance: The Crawling Distance is 11th studio album released by singer-songwriter Robert Pollard on January 20, 2009.  Similar to many of Pollard's releases since "Fiction Man" in 2004, all instrumentation on the album was performed by producer Todd Tobias.  "The Crawling Distance" has a 64/100 score on metacritic and thus was Pollard's lowest rated album on the site, until 2011's "Space City Kicks" which has a 62.  

Robert Pollard Is Off to Business: Robert Pollard Is Off to Business is 10th studio album released by singer-songwriter Robert Pollard on June 2, 2008.  This is the first LP release from Robert Pollard's new record label "Guided by Voices Inc".  All instrumentation on the album was performed by producer Todd Tobias.  Many of the songs on the album were over three minutes in length, which is unusual for a Pollard release.

Kid Marine: Kid Marine is 3rd album by Robert Pollard, released in 1999.  It is the first release of Robert Pollard's Fading Captain Series.  Pollard has stated that the album is about Jeff "Kid Marine" Davis, the person pictured on the cover .  Robert told Mojo magazine, "My personal favorite, a weird record, almost a concept album, about the typical Ohio male and what he does - drink, watch television, eat pizza.  It got mixed reviews, there are people who hate it and others who think it's our best record and I'm on their side.  I just love the songs.  It feels like one piece, like it all fits together.  I like the cover and I like the

Question: Which singer has more careers in other industries, Bruce Dickinson or Robert Pollard?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_with_more_non_music_careers": {
      "type": "string",
      "description": "The name of the person who has more careers outside of the music industry."
    },
    "comparison_details": {
      "type": "object",
      "properties": {
        "bruce_dickinson": {
          "type": "object",
          "properties": {
            "non_music_career_count": {
              "type": "integer",
              "description": "The number of non-music related careers for Bruce Dickinson."
            },
            "non_music_careers": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "A list of Bruce Dickinson's non-music related careers."
            }
          },
          "required": [
            "non_music_career_count",
            "non_music_careers"
          ],
          "additionalProperties": false
        },
        "robert_pollard": {
          "type": "object",
          "properties": {
            "non_music_career_count": {
              "type": "integer",
              "description": "The number of non-music related careers for Robert Pollard."
            },
            "non_music_careers": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "description": "A list of Robert Pollard's non-music related careers."
            }
          },
          "required": [
            "non_music_career_count",
            "non_music_careers"
          ],
          "additionalProperties": false
        }
      },
      "required": [
        "bruce_dickinson",
        "robert_pollard"
      ],
      "additionalProperties": false
    },
    "total_people_compared": {
      "type": "integer",
      "description": "The total number of people whose careers were compared."
    }
  },
  "required": [
    "person_with_more_non_music_careers",
    "comparison_details",
    "total_people_compared"
  ],
  "additionalProperties": false
}
