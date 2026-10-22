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
Alexander Gustafsson: Alexander L. Gustafsson (born 15 January 1987) is a Swedish professional mixed martial artist.  He is currently signed to the Ultimate Fighting Championship (UFC) where he competes in their light heavyweight division.  As of 20 July 2017, Gustafsson is the #1 ranked light heavyweight contender in official UFC rankings.

EA Sports UFC: EA Sports UFC is a mixed martial arts sports video game developed by EA Canada and SkyBox Labs for the PlayStation 4 and Xbox One.  It is based on the Ultimate Fighting Championship (UFC) brand and was released on June 17, 2014.  A playable demo was released on the PlayStation Network and Xbox Marketplace on June 3, 2014, with cover athletes Jon Jones and Alexander Gustafsson as playable fighters.  It is the first UFC game since THQ sold the license to Electronic Arts.

NHL 12: NHL 12 is an ice hockey video game developed by EA Canada and published by EA Sports.  The game was featured in the 2011 Electronic Entertainment Expo (E3).  Steven Stamkos was announced as the game's cover athlete on June 22, 2011, at the NHL Awards Show in Las Vegas, Nevada.  The game notably includes more interactive goalies (i.e. players can have real contact with the goalies and vice versa, and the goalies and skaters may fight each other), better physics engine, improved Be a Pro mode, and the ability to play the 2011 NHL Winter Classic.  Along with several other new EA Sports titles, "NHL 12" was made available three days prior the official release dates to purchasers of the EA Sports Season Ticket, a new digital program allowing users with a PlayStation 3 and/or an Xbox 360 to download and test the full version of new EA Sports titles for a three-day trial period by paying an annual fee of $24.99 or 2,000 Microsoft points.  Users who pre-ordered the retail version of the game may have received a code for a goalie boost pack, which improves certain parts of the player's goalie in the "Be a Pro" mode.  Gary Thorne (play-by-play) and Bill Clement (color) return to provide commentary for "NHL 12".

EA Sports UFC 2: EA Sports UFC 2 is a mixed martial arts fighting video game developed by EA Canada, and published in March 2016 by Electronic Arts for the PlayStation 4 and Xbox One.  The sequel to 2014's "EA Sports UFC", it is based on the Ultimate Fighting Championship (UFC) brand.  The game's cover art features Ronda Rousey and Conor McGregor.

UFC 2009 Undisputed: UFC 2009 Undisputed is a mixed martial arts video game featuring Ultimate Fighting Championship properties and fighters developed by Yuke's Osaka and published by THQ.  The game was released in the US on May 19, 2009, for the Xbox 360 and PlayStation 3.  It is the first game to be released under THQ's 2007 agreement with the UFC, and it is to be the first UFC game released since "" in 2004.  A playable demo of "UFC 2009" was released onto Xbox Live and PlayStation Network on April 23, 2009, and featured a tutorial and exhibition matchup between Chuck Liddell and Mauricio Rua.  A sequel, "UFC Undisputed 2010" was released on May 25, 2010.

UFC 140: UFC 140: Jones vs. Machida was a mixed martial arts event held by the Ultimate Fighting Championship on December 10, 2011 at the Air Canada Centre in Toronto, Ontario, Canada.  It was the penultimate event for the UFC in 2011.  The event featured eight bouts televised internationally, seven preliminary bouts aired on cable in the United States and Canada, and three preliminary bouts streamed live on Facebook.  In the co-main event, Frank Mir, who was the first man to knock out Antônio Rodrigo Nogueira at UFC 92, became the first man to submit Nogueira.  Mir accomplished the feat with a kimura that ultimately broke Nogueira's arm.  In the main event, Lyoto Machida also suffered his first ever submission loss at the hands of Jon Jones.  In doing so, Jones retained the UFC Light Heavyweight Championship title.

Volkan Oezdemir: Volkan Özdemir (born September 19, 1989 in Fribourg) is a Swiss professional mixed martial artist and kickboxer currently competing in the Light Heavyweight division of the Ultimate Fighting Championship.  A professional competitor since 2010, Oezdemir formerly competed for Bellator.  As a kickboxer, he competed for Superkombat Fighting Championship in their heavyweight division.  He is currently #2 in the UFC's light heavyweight rankings.

Vinny Magalhães: Vinicius de Magalhães (] ; born July 2, 1984), is a Brazilian mixed martial artist who competes in the World Series of Fighting's Light Heavyweight division.  He was a finalist in "" and has fought five times within two stints with the Ultimate Fighting Championship.  He is the former Titan FC Light Heavyweight Champion, M-1 Global Light Heavyweight Champion and is also a multiple time jiu-jitsu gi and no-gi world champion.  Magalhães currently fights in the light heavyweight division of the Absolute Championship Berkut.

Maurício Rua: Maurício "Shogun" Milani Rua (] ; born November 25, 1981) is a Brazilian professional mixed martial artist currently competing in the Light Heavyweight division of the Ultimate Fighting Championship.  A professional competitor since 2002, Rua is the former UFC Light Heavyweight Champion and was the 2005 PRIDE Middleweight Grand Prix Champion.  As of September 28, 2017, Rua is #5 in the official UFC Light Heavyweight rankings.

Dan Henderson: Daniel Jeffery Henderson (born August 24, 1970) is an American former mixed martial artist and Olympic wrestler, who last competed as a middleweight in the Ultimate Fighting Championship.  He was the last Strikeforce Light Heavyweight Champion and was the last Welterweight (80 kg ) and Middleweight (95 kg ) champion of Pride Fighting Championships.  Additionally, Henderson was the Brazil Open '97 Tournament Champion, the UFC 17 Middleweight Tournament Champion, the Rings: King of Kings 1999 Tournament Champion and the Pride Weltwerweight Grand Prix Tournament Champion.  During his career, Henderson also challenged for the UFC Middleweight Championship (2x), the UFC Light Heavyweight Championship and the Strikeforce Middleweight Championship.  He was the first mixed martial artist to concurrently hold two titles in two different weight classes in a major MMA promotion.  At the time of his retirement after UFC 204, he was the oldest fighter on the UFC roster.  Known to be one of the greatest mixed martial artists of all time having defeated a total of seventeen MMA world champions across four major MMA promotions (UFC, PRIDE FC, Strikeforce, and RINGS).

Question: EA Sports UFC is a mixed martial arts sports video game developed by EA Canada and SkyBox Labs, a playable demo was released on the PlayStation Network and Xbox Marketplace on June 3, 2014, with cover athletes Jon Jones and which Swedish professional mixed martial artist, what is currently signed to the Ultimate Fighting Championship (UFC) where he competes in their light heavyweight division?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fighter_name": {
      "type": "string",
      "description": "The name of the mixed martial artist."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the fighter."
    },
    "current_organization": {
      "type": "string",
      "description": "The professional organization the fighter is currently signed with."
    },
    "division": {
      "type": "string",
      "description": "The weight division the fighter competes in."
    },
    "game_details": {
      "type": "object",
      "properties": {
        "game_title": {
          "type": "string",
          "description": "The title of the video game."
        },
        "role": {
          "type": "string",
          "description": "The fighter's role in the game, e.g., cover athlete."
        },
        "demo_release_date": {
          "type": "string",
          "description": "The release date of the game's playable demo."
        }
      },
      "required": [
        "game_title",
        "role",
        "demo_release_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "fighter_name",
    "nationality",
    "current_organization",
    "division",
    "game_details"
  ],
  "additionalProperties": false
}
