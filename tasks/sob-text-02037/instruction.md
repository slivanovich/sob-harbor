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
Mr. Lonely: His Greatest Songs Today: Mr. Lonely: His Greatest Songs Today is a collection of previously recorded songs by Bobby Vinton for Curb Records.  The first five tracks might be misleading to people of the baby boomer generation, as they are not the singles that Vinton had during the 1960s and the year of 1974 but re-recordings that Vinton made for Curb.  For this collection, five songs were taken from Vinton's self-explanatory album and four from his album "Timeless".  Re-recorded versions of "Mr. Lonely" and "Roses Are Red" make their first album appearance on this collection.

Lonely (Akon song): "Lonely" (also known as "Mr. Lonely") is a song by Senegalese-American R&B and rapper Akon; it appears on his debut album, "Trouble".  The single was released in 2005 and was his first worldwide hit.  It reached number one in several countries, including in the United Kingdom and Germany (where it stayed there for eight weeks), and Australia.  It was also highly popular in France where it reached number two, and in the United States when it peaked at #4.  An edited version was on Radio Disney and on "Radio Disney Jams, Vol.  8".

The Best of Bobby Vinton (1985 album): The Best of Bobby Vinton is a 12-track collection of previously recorded songs by Bobby Vinton; it was released in 1985.  This collection contains three songs that Vinton recorded for ABC Records ("Killing Me Softly With Her Song", "My Melody of Love", and "My Special Angel"), six for Epic Records ("Roses Are Red (My Love)", "Mr. Lonely", "Blue Velvet", "There!  I've Said It Again", "Blue on Blue", and "I Love How You Love Me"), and one for the Canadian label of Ahed Records ("Medley").  The last two songs, "Will You Still Love Me Tomorrow" and "Don't You Know", make their first album appearances on this collection.

Mr. Lonely (album): Mr. Lonely is Bobby Vinton's tenth studio album, released in 1964.  It was released right after the success of his fourth and final #1 US hit "Mr. Lonely," a 1962 song that was released as a single after its appearance on "Bobby Vinton's Greatest Hits".  Cover versions on this album include "Laughing on the Outside (Crying on the Inside)" and "I'll Never Smile Again".  After the success of the single, Vinton released "Bobby Vinton Sings for Lonely Nights", an album of songs devoted to the subject of loneliness.

Who Dat Boy: "Who Dat Boy" is a song by American rapper Tyler, The Creator.  It was released on June 30, 2017 alongside, "911 / Mr. Lonely" through Columbia Records, as the lead singles from his fourth studio album "Flower Boy".  The song features vocals from ASAP Rocky.

Mr. Lonely: "Mr. Lonely" is a song co-written and recorded by Bobby Vinton.  The song was first released on Vinton's 1962 album "Roses Are Red".

911 / Mr. Lonely: "911 / Mr. Lonely" is a song by American rapper Tyler, The Creator.  It was released on June 30, 2017 alongside, "Who Dat Boy" through Columbia Records, as the lead singles from his fourth studio album "Flower Boy".  The song was produced by Tyler himself and features vocals from Frank Ocean, The Internet's Steve Lacy and Norwegian singer Anna of the North.

Anita Skorgan: Anita Skorgan (born 13 November 1958) is a Norwegian singer-songwriter.  She was once married to Jahn Teigen, another successful Norwegian singer-songwriter; constantly in the tabloids the two were considered the first superstar celebrity couple in Norway.  Together they have a daughter.

Bobby Vinton Sings for Lonely Nights: Bobby Vinton Sings for Lonely Nights is Bobby Vinton's eleventh studio album, released in 1965.  This album was released to capitalize on the success of Vinton's big hit "Mr. Lonely" and his album of the same name by containing only songs that refer to loneliness.  There were two singles from this album: "Long Lonely Nights" (previously a minor hit for Lee Andrews & the Hearts then for Clyde McPhatter in 1957 and then for The Four Seasons in 1964) and Vinton's self-penned "L-O-N-E-L-Y".  Cover versions include "Saturday Night (Is the Loneliest Night of the Week)", "All Alone Am I", "Oh, How I Miss You Tonight", "In the Still of the Night", "I'll Walk Alone" and "Have You Ever Been Lonely (Have You Ever Been Blue?) ".

Anna of the North: Anna Lotterud (born 8 June 1989), better known by her stage name Anna of the North, is an Oslo-based Norwegian singer-songwriter from Gjøvik.  Her music has been regarded as "soft, soul-bearing electro-pop".

Question: 911 / Mr. Lonely features vocals by the Norwegian singer-songwriter from what city?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song in question."
    },
    "featured_artist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The stage name of the featured artist."
        },
        "nationality": {
          "type": "string",
          "description": "The nationality of the featured artist."
        },
        "role": {
          "type": "string",
          "description": "The role of the artist in the song (e.g., singer-songwriter)."
        },
        "city_of_origin": {
          "type": "string",
          "description": "The city from which the artist originates."
        }
      },
      "required": [
        "name",
        "nationality",
        "role",
        "city_of_origin"
      ],
      "additionalProperties": false
    },
    "answer_city": {
      "type": "string",
      "description": "The specific city that answers the question."
    }
  },
  "required": [
    "song_title",
    "featured_artist",
    "answer_city"
  ],
  "additionalProperties": false
}
