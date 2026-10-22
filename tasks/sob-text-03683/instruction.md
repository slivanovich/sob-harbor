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
Ben Bruce: Benjamin Paul "Ben" Bruce (born 31 October 1988) is an English musician.  He is a solo artist and also the lead guitarist and backing vocalist of metalcore band Asking Alexandria.  Bruce co-founded the band with lead vocalist Danny Worsnop.

Stand Up and Scream: Stand Up and Scream is the debut studio album by English metalcore band Asking Alexandria, released on 15 September 2009 through Sumerian Records.  The album has charted at number 170 on the Billboard 200, number 29 on Top Independent albums, and number 5 on Top Heatseekers.  The record managed to remain at the Top Heatseekers chart at position number 36 until the end of July 2010.  The album received mixed to positive reviews from critics, with Danny Worsnop's unclean vocals, and the loud guitars and drums being praised.  However, the lyrics, Worsnop's clean vocals and electronic elements were subject of criticism.  The album has gone on to sell over 100,000 copies worldwide.

We Are Harlot: We Are Harlot, often shortened to just Harlot, is a hard rock supergroup organized by singer Danny Worsnop, of Asking Alexandria and Jeff George who was formerly Sebastian Bach's guitarist.  The lineup also includes bassist Brian Weaver from Silvertide and drummer Bruno Agra formerly of Revolution Renaissance.  Formed in 2011, they released their first single titled "Denial" in 2014 and released their debut self-titled album on March 30, 2015 in the US (earliest release March 27 in Germany), which debuted in US and UK charts and sold 5,000 copies in the US in its first week.

ESP LTD TA-200: ESP LTD TA-200 is an electric bass model distributed by ESP.  It is the mass-produced version of the custom signature model ESP Tom Araya, endorsed and used by Tom Araya of Slayer.

Tom Araya: Tomás Enrique Araya Díaz (born June 6, 1961) is a Chilean American musician, best known as the vocalist and bassist of the American thrash metal band Slayer.  Araya is ranked fifty-eighth by "Hit Parader" on their list of the 100 Greatest Metal Vocalists of All Time.

Asking Alexandria: Asking Alexandria are an English rock band from York, North Yorkshire consisting of lead vocalist Danny Worsnop, guitarists Ben Bruce and Cameron Liddell, drummer James Cassells and bassist Sam Bettley.

Digital Renegade: Digital Renegade (stylized as [digital_renegade]) is the third studio album by American electronicore band I See Stars.  It was released on March 13, 2012 through Sumerian Records.  It features guest vocals by Danny Worsnop from the English metalcore band Asking Alexandria and Cassadee Pope from the American rock band Hey Monday.

ESP Tom Araya (bass): ESP Tom Araya is an electric bass model distributed by ESP.  Araya originally discovered ESP, when his fellow musicians from Slayer, Jeff Hanneman and Kerry King used ESP guitars (Hanneman has his own signature model).  He was approached by ESP, who wanted to make him a signature model.  Araya said that this was fine as long as the bass he plays is the same a fan would point out at a music store and buy.  He also wanted to have the lower end models be just as good as the high end models, because he said that "not all the fans can afford a bass that costs an arm and a leg" He wanted the bass to have a thin neck, like a guitar so it would be easier to play for him rather than having a really fat neck that would require more effort to reach with fingers.

The Black (Asking Alexandria album): The Black is the fourth studio album by English rock band Asking Alexandria.  It was released on 25 March 2016, and is their first and only album to feature second lead vocalist Denis Stoff, who replaced original lead vocalist Danny Worsnop.  Worsnop returned to the band in October of 2016.  The album was preceded by the singles "I Won't Give In" released on 26 May 2015, "Undivided" released on 25 September 2015, and the album's eponymous track "The Black" released on 2 February 2016.  The first song on the album, "Let It Sleep", was released on 3 March 2016, with a music video for the track being released the following day.

Danny Worsnop: Danny Robert Worsnop (born 4 September 1990) is a British musician, singer and songwriter, prominently known as the lead vocalist of rock bands Asking Alexandria and We Are Harlot.  He has worked with several artists including I See Stars, With One Last Breath, Breathe Carolina and Memphis May Fire, providing guest vocals on several songs.

Question: Are Tom Araya and Danny Worsnop of the same nationality?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "question_asked": {
      "type": "string",
      "description": "The original question asked."
    },
    "musicians": {
      "type": "array",
      "description": "Details about the musicians mentioned in the question.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The name of the musician."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the musician."
          }
        },
        "required": [
          "name",
          "nationality"
        ],
        "additionalProperties": false
      }
    },
    "same_nationality": {
      "type": "boolean",
      "description": "True if both musicians share the same nationality, false otherwise."
    }
  },
  "required": [
    "question_asked",
    "musicians",
    "same_nationality"
  ],
  "additionalProperties": false
}
