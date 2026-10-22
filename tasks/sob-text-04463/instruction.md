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
Ignite (game engine): The Ignite game engine (styled as IGNITE) is a collection of video game technologies built by Electronic Arts and designed to make video game sports "alive".  The technology was announced at Microsoft's Xbox One reveal event in May 2013 for four EA Sports franchise games for Xbox One and PlayStation 4: "FIFA 14", "EA Sports UFC", "Madden NFL 25" and "NBA Live 14", all released in Fall 2013.

EA Sports UFC: EA Sports UFC is a mixed martial arts sports video game developed by EA Canada and SkyBox Labs for the PlayStation 4 and Xbox One.  It is based on the Ultimate Fighting Championship (UFC) brand and was released on June 17, 2014.  A playable demo was released on the PlayStation Network and Xbox Marketplace on June 3, 2014, with cover athletes Jon Jones and Alexander Gustafsson as playable fighters.  It is the first UFC game since THQ sold the license to Electronic Arts.

Cricket 07: Cricket 07 is a cricket simulation computer game developed by HB Studios and published by Electronic Arts under the label of EA Sports.  It is available for Windows and PlayStation 2.  The game was released in the United Kingdom on 24 November 2006 and in Australia on 14 November 2006.  The cover art for "Cricket 07" features England and Lancashire cricketer Andrew Flintoff, and the Australian release cover pictures The Ashes urn with the Australian and English flags behind it.  This is the most recent cricket game published by EA Sports.

EA Sports Big: EA Sports Big was a brand name used by Electronic Arts from 2000 to 2008 to distribute casual and extreme sports games that featured non-realistic, arcade features similar to Midway's sports games. " SSX" was the first game to be published by EA Sports Big.  Later games such as "FIFA Street" (2012) and "SSX" (2012) dropped the EA Sports BIG branding and were released simply under EA Sports.  The EA Sports Big name and branding was conceived by Steven Rechtschaffner, the Executive Producer of "SSX", "SSX Tricky", "SSX 3", and "NBA Street Vol.  2".  The EA Sports Big intro voice that boomed the word "BIG" was voiced by human beatbox and former member of The Roots, Rahzel.

EA Sports NASCAR series: The EA Sports NASCAR series, alternately known as the NASCAR Thunder Series, was a series of NASCAR video games published by EA Sports.  The series began with "NASCAR 98" and "NASCAR 99" in 1997 and 1998.  EA Sports released "NASCAR Thunder 2002" in 2001, and ever since then, Jeff Gordon (2002), Dale Earnhardt Jr. (2003), and Tony Stewart (2004) were on the cover.  In 2004, they changed the name of the game to "" and added the new features to make the game more up-to-date with the recent changes to NASCAR.  Kevin Harvick was on the cover.  The next year, they changed the name yet again to "".  Jeff Gordon and Hendrick Motorsports teammate Jimmie Johnson were on the cover.  The new features were swapping cars with teammates and voice-recognition support for use with the crew chief.  The following year, the game was titled "NASCAR 07" and features Elliott Sadler on the cover.  The new features include a new speed blur effect and an all-new momentum system, used to describe drivers' strong and weak racetrack types.  In 2004, the feature was a "Grudges and Alliances" feature in which if the player hits a car, they could retaliate.  The feature received a mixed reaction.

Ronda Rousey: Ronda Jean Rousey ( ; born February 1, 1987) is an American mixed martial artist, judoka, and actress.

Go Get It: "Go Get It" is a song by American hip hop recording artist T.I., released July 17, 2012, as the first single from his eighth studio album "" (2012).  The song was produced by Canadian hip hop and R&B producer T-Minus, who T.I. previously collaborated with on "Poppin Bottles", featuring Drake, from his seventh studio album "No Mercy" (2010).  Before its official release, the song had leaked online earlier in June.  This song is featured on EA Sports UFC 2.

EA Sports UFC 2: EA Sports UFC 2 is a mixed martial arts fighting video game developed by EA Canada, and published in March 2016 by Electronic Arts for the PlayStation 4 and Xbox One.  The sequel to 2014's "EA Sports UFC", it is based on the Ultimate Fighting Championship (UFC) brand.  The game's cover art features Ronda Rousey and Conor McGregor.

Don't Forget Who You Are: Don't Forget Who You Are is the second studio album by indie-rock musician Miles Kane.  It was released in June 2013 under Columbia Records.  The album title is the second song off the album, "Don't Forget Who You Are" and featured on EA Sports' EA Trax in the video game FIFA 14, while "Give Up" is featured in EA Sports UFC.

NHL 12: NHL 12 is an ice hockey video game developed by EA Canada and published by EA Sports.  The game was featured in the 2011 Electronic Entertainment Expo (E3).  Steven Stamkos was announced as the game's cover athlete on June 22, 2011, at the NHL Awards Show in Las Vegas, Nevada.  The game notably includes more interactive goalies (i.e. players can have real contact with the goalies and vice versa, and the goalies and skaters may fight each other), better physics engine, improved Be a Pro mode, and the ability to play the 2011 NHL Winter Classic.  Along with several other new EA Sports titles, "NHL 12" was made available three days prior the official release dates to purchasers of the EA Sports Season Ticket, a new digital program allowing users with a PlayStation 3 and/or an Xbox 360 to download and test the full version of new EA Sports titles for a three-day trial period by paying an annual fee of $24.99 or 2,000 Microsoft points.  Users who pre-ordered the retail version of the game may have received a code for a goalie boost pack, which improves certain parts of the player's goalie in the "Be a Pro" mode.  Gary Thorne (play-by-play) and Bill Clement (color) return to provide commentary for "NHL 12".

Question: EA Sports UFC 2's cover art features what A,erican mixed martial artist, judoka, and actress?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "game_title": {
      "type": "string",
      "description": "The title of the video game."
    },
    "cover_athletes": {
      "type": "array",
      "description": "A list of athletes featured on the game's cover art.",
      "items": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "description": "The full name of the athlete."
          },
          "nationality": {
            "type": "string",
            "description": "The nationality of the athlete."
          },
          "professions": {
            "type": "array",
            "description": "A list of professions or roles of the athlete.",
            "items": {
              "type": "string"
            }
          },
          "is_answer_to_question": {
            "type": "boolean",
            "description": "Indicates if this athlete is the specific one asked about in the question."
          }
        },
        "required": [
          "name",
          "is_answer_to_question"
        ],
        "additionalProperties": false
      }
    },
    "answer_athlete_name": {
      "type": "string",
      "description": "The name of the American mixed martial artist, judoka, and actress featured on the cover."
    }
  },
  "required": [
    "game_title",
    "cover_athletes",
    "answer_athlete_name"
  ],
  "additionalProperties": false
}
