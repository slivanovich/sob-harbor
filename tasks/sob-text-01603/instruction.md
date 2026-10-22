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
Vibeology: "Vibeology" was the fourth single released worldwide from Paula Abdul's "Spellbound" album.  The song was written by Peter Lord, Sandra St. Victor and V. Jeffrey Smith.  It was released as the third single from the album in Australia and the UK, and as the fourth single in North America.  "Vibeology" was first released as a single in November 1991 in Australia, followed by a European and North American release in January 1992.

Whoa, Nelly!: Whoa, Nelly!  is the debut studio album by Canadian singer-songwriter Nelly Furtado.  It was released in North America on October 24, 2000 by DreamWorks Records.  It peaked at number twenty-four on the US "Billboard" 200 chart, and opened to critical acclaim.  It produced three international singles: "I'm Like a Bird", "Turn Off the Light" and "...on the Radio (Remember the Days)".  "Party's Just Begun (Again)" was a club-only single released exclusively in the US before the album's availability in stores, and it was included on the soundtrack of the 1999 film "Brokedown Palace".  When "Party's Just Begun (Again)" was released, Furtado's label was unsure about the genre in which to market her.  They eventually remixed "Party's Just Begun (Again)" and included it on this album as "Party".  The DreamWorks label released "Trynna Finda Way" as the fourth single in Mexico and South America, and "Hey, Man! " as the fourth single in the UK and Germany.  The album spent seventy-eight weeks on the "Billboard" 200.  It hit double-platinum status in the US in January 2002.

Celebration (AnnaGrace song): "Celebration" is the fourth single released by the Belgian duo AnnaGrace, formerly known as Ian Van Dahl.  The track is the group's fourth single following their 2008 debut single "You Make Me Feel", 2009 second single "Let the Feelings Go" and 2009 third single "Love Keeps Calling".

These Days (Bon Jovi song): “These Days” is a song by American rock band Bon Jovi.  It was released in February 1996 as the fourth single from their 1995 album "These Days".  It was the fourth single released from the album, and showcases the darker tone that Jon Bon Jovi and Richie Sambora’s lyrics sought to achieve with the album.  The song which begins with a haunting piano progression, deals with homelessness, loss of innocence and the difficulty of keeping up a relationship in the modern age.  It is about people out there trying to be understood, to live their dreams.

Did I Tell You: "Did I Tell You" is the fourth single released by The Spinto Band, as well as the fourth single from the album "Nice and Nicely Done".

Walking Down Your Street: "Walking Down Your Street" is a song by The Bangles.  It is the fourth single from their album "Different Light".  It was released as a single in 1987 and charted at #11 on the "Billboard" Hot 100, #16 on the UK Singles Chart, and #56 on the Australian Kent Music Report chart.  The next single, "Following", was only released in the UK, making "Walking Down Your Street" the final single from "Different Light" in the US.  The original LP version varies slightly from the 7" single version and the version included with their "Greatest Hits" compilation.

Song for Clay (Disappear Here): "Song for Clay (Disappear Here)" is the opening track from Bloc Party's second album "A Weekend in the City" and was set to be the fourth single released from the album.  The band had even begun work on a music video for the song.  It was replaced as the fourth single by a newly recorded song "Flux".

The Bangles: The Bangles are an American pop rock band formed in Los Angeles in 1981.  They scored several hit singles as that decade continued.  The band's hits include "Walk Like an Egyptian", "Billboard" magazine's number-one single of 1987, as well as two number-two hits, "Manic Monday" and "Hazy Shade of Winter", and their 1989 number-one single "Eternal Flame".

More Than Meets the Eye (song): "More Than Meets the Eye" is a 1989 single released by the Swedish rock Europe.  It was the fourth single released from the band's fourth studio album "Out of This World".  It was only released in France, Spain and Japan.

Hump de Bump: "Hump de Bump" is a song by the Red Hot Chili Peppers from their 2006 double album, "Stadium Arcadium".  The song is the fifth and final single released from "Stadium Arcadium" and final single the band would release with John Frusciante, who quit the band two years later.  Originally expected to be the fourth single for the US, Canada and Australia, ("Desecration Smile" was the fourth single released internationally) the Red Hot Chili Peppers decided to make the single and video a worldwide release thanks to the positive feedback on the video, which was directed by comedian and good friend Chris Rock.  The single was released in the US on April 7, 2007 while it was released May 10, 2007 in the rest of the world.

Question: "Walking Down Your Street" is the fourth single released by a band that formed where?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "song_title": {
      "type": "string",
      "description": "The title of the song."
    },
    "band_name": {
      "type": "string",
      "description": "The name of the band that released the song."
    },
    "band_origin": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "The city where the band was formed."
        },
        "country": {
          "type": "string",
          "description": "The country where the band was formed."
        },
        "year_formed": {
          "type": "integer",
          "description": "The year the band was formed."
        }
      },
      "required": [
        "city",
        "country",
        "year_formed"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "song_title",
    "band_name",
    "band_origin"
  ],
  "additionalProperties": false
}
