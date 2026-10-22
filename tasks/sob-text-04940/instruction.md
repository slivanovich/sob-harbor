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
After the Thrones: After the Thrones is an American live television aftershow that premiered on April 25, 2016 and ended on June 28, 2016.  It was hosted by Andy Greenwald and Chris Ryan who discussed episodes of the HBO television series "Game of Thrones".  The talk show is executive produced by Bill Simmons and Eric Weinberger.  Greenwald and Ryan previously hosted a podcast version of the show titled "Watch the Thrones" on Simmons' Grantland website.  A similar talk show called "Thronecast" airs on British channel Sky Atlantic, which also discusses episodes of "Game of Thrones".

Game of Thrones Ascent: Game of Thrones Ascent is a strategy video game developed by Disruptor Beam for iOS, Facebook, Kongregate, and Android.  The game was a 2013 Facebook Game of the Year in the Staff Picks category and a winner of a 2013 Friendie Award.  The game is an adaptation of the novel series "A Song of Ice and Fire" by George R. R. Martin and the HBO TV series "Game of Thrones", and is the first such social network game.  According to Martin, the game features "alliance building, treachery, marriages, murders, and most of all the constant struggle to be the greatest house in Westeros."  The game includes the ability to engage in the dynamic political and social intrigue featured in the books and television show.  The game has over 9 million players.

Gemma Whelan: Gemma Elizabeth Whelan (born 23 April 1981) is an English actress and comedian, known for playing Yara Greyjoy in the HBO fantasy-drama series "Game of Thrones".

Game of Thrones Theme: "Game of Thrones" Theme", also referred to as "Game of Thrones" Main Title Theme", is the theme music of the television series "Game of Thrones".  It plays during the title sequence and was composed by Ramin Djawadi in 2011, after series creator David Benioff and D. B. Weiss approached him requesting a theme.  Asked to avoid flutes and violins, which the producers felt were overused in fantasy themes, Djawadi used the cello as the lead instrument.  The piece begins in a minor key, then switches between corresponding major and minor keys repeatedly.  Djawadi was shown a preliminary rendering of the title sequence before composing this music to accompany it.  Several artists have covered or parodied the music, sometimes adding lyrics to the originally instrumental work.

Game of Thrones (2012 video game): Game of Thrones is an action role-playing video game based on "A Game of Thrones", the first of the "A Song of Ice and Fire" novels by George R. R. Martin, and in part also on the novels' TV adaptation by HBO, "Game of Thrones".

Thronecast: Thronecast is a British television series on Sky Atlantic which is presented by Sue Perkins and Jamie East.  It is an aftershow to "Game of Thrones", which also airs on the channel.  Each episode is an hour in length and features interviews with members of the cast and crew, interaction with the audience and social media alongside analysis of the previous episode and a preview of the next episode of "Game of Thrones".  It was the only official aftershow for the American series until HBO aired "After the Thrones" in 2016 - a show which was cancelled after only one series.

Game of Thrones: Season 6 (soundtrack): The soundtrack album of the sixth season of HBO series "Game of Thrones", titled Game of Thrones: Season 6, was released digitally on June 24, 2016, and later released on CD on July 29, 2016.  The album reached No. 1 on the "Billboard"' s Soundtracks chart, and the track from the season finale "Light of the Seven" reached No. 1 on "Billboard"' s Spotify Viral 50 chart.  The "Light of the Seven" is the first time piano is used in the music for "Game of Thrones".  The album was composed by Ramin Djawadi.  The soundtrack has received favorable reviews and peaked at #1 on the U.S. Soundtrack Albums chart and #27 on the U.S. Billboard 200.  It won a International Film Music Critics Association for "Best Original Score for a Television Series".

Rise of Nations: Thrones and Patriots: Rise of Nations: Thrones and Patriots is the official expansion pack to the real-time strategy video game "Rise of Nations".  The game is the second in a series of "Rise of Nations" games by Big Huge Games.  "Thrones and Patriots" had its premiere release for Microsoft Windows on April 27, 2004 in North America.  It was ported to and released for Mac OS X in November 2004.  "Rise of Nations: Extended Edition" was released on Steam on June 12, 2014 and includes both the original game and "Thrones and Patriots" with updated graphics and Steamworks integration for multiplayer.

Game of Thrones: Season 4 (soundtrack): The soundtrack album of the fourth season of HBO series "Game of Thrones", titled Game of Thrones: Season 4 was released digitally on June 10, 2014, and on CD on July 1, 2014.  Season 4 of "Game of Thrones" saw the Icelandic band Sigur Rós perform their rendition of "" in a cameo appearance at King Joffrey's wedding in the second episode, "The Lion and the Rose".

The Moorside: The Moorside is a 2017 two-part British television drama.  Written by Neil McKay and directed by Paul Whittington, it stars Sheridan Smith, Gemma Whelan, Sian Brooke and Siobhan Finneran and was broadcast on BBC One in two one-hour episodes in February 2017.  The drama is based on the 2008 disappearance of 9-year-old Shannon Matthews and the successful search for her by police and volunteers in Dewsbury, West Yorkshire, along with the revelation of mother Karen's involvement in Shannon's kidnapping.

Question: What actress was in Game of Thrones and The Moorside?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actress_name": {
      "type": "string",
      "description": "The name of the actress who appeared in both productions."
    },
    "productions": {
      "type": "array",
      "description": "A list of productions the actress was involved in.",
      "items": {
        "type": "object",
        "properties": {
          "title": {
            "type": "string",
            "description": "The title of the production."
          },
          "role_description": {
            "type": "string",
            "description": "A description of the actress's role or involvement in the production."
          }
        },
        "required": [
          "title",
          "role_description"
        ],
        "additionalProperties": false
      }
    },
    "common_productions_count": {
      "type": "integer",
      "description": "The number of productions found that the actress was in, matching the query criteria."
    }
  },
  "required": [
    "actress_name",
    "productions",
    "common_productions_count"
  ],
  "additionalProperties": false
}
