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
Kim Allen: Kim Bryant Allen (born April 5, 1953 in Fontana, California) is a former Major League Baseball player.  After playing college baseball for the UC Riverside Highlanders and having a nondescript minor league career, Allen briefly earned prospect status with the Seattle Mariners on the strength of his spectacular 1980 season for the Triple-A Spokane Indians.  That season he registered a 35-game hitting streak and stole 84 bases, the most in the Pacific Coast League since 1913.  He was called up to the Mariners in September 1980 and swiped 10 bags in 23 games.

Tupou College: Tupou College is a Methodist boys' secondary boarding school in Toloa on the island of Tongatapu, Tonga. It is located on the Eastern District of Tongatapu near the village of Malapo.  The school is owned by the Free Weslyan Church of Tonga.  Established in 1866 by James Egan Moulton, it claims to be the oldest secondary school in the Pacific Islands.  Enrolment is some 1,000 pupils.  Tupou College was first established at Nuku'alofa at the location on which Queen Salote College stands today.  From there it moved to Nafualu, Sia'atoutai on the site where Sia'atoutai Theological College now stands.  In 1948, the school last moved to Toloa in the Eastern District of Tongatapu where it still stands today.  Tupou College's Brother school is Newington College which is in Sydney, Australia.

Nat Rogers: William Nathaniel Rogers (born June 7, 1893 in Spartanburg, South Carolina - "unknown") was a baseball player in the Negro Leagues.  He would play outfielder, catcher, and infielder and played from 1923 to 1946.  In 1927 Rogers had a 31-game hitting streak for the Chicago American Giants.

Vince DiMaggio: Vincent Paul "Vince" DiMaggio (September 6, 1912 – October 3, 1986) was an American Major League Baseball center fielder.  During a 10-year baseball career, he played for the Boston Bees (1937–1938), Cincinnati Reds (1939–1940), Pittsburgh Pirates (1940–1945), Philadelphia Phillies (1945–1946), and New York Giants (1946).  Vince was the older brother of Joe and Dom DiMaggio.

Ken Keltner: Kenneth Frederick Keltner (October 31, 1916 – December 12, 1991) was an American professional baseball player.  He played almost his entire Major League Baseball career as a third baseman with the Cleveland Indians, until his final season when he played 13 games for the Boston Red Sox.  He batted and threw right-handed.  A seven-time All-Star, Keltner is remembered for being one of the best fielding third basemen in the 1940s and for helping to end Joe DiMaggio's 56-game hitting streak on July 17, 1941.

Hitting streak: In baseball, a hitting streak is the number of consecutive official games in which a player appears and gets at least one base hit.  According to the Official Baseball Rules, such a streak is ended when a player has at least 1 plate appearance and no hits.  A streak shall not be terminated if all official plate appearances result in a base on balls, hit by pitch, defensive interference or a sacrifice bunt.  The streak shall terminate if the player has a sacrifice fly and no hit.

Damian Costantino: Damian Costantino (born c. 1978) is an American baseball player who set the record for the longest hitting streak in National Collegiate Athletic Association baseball history, with a 60-game streak that ran through the 2001, 2002 and 2003 seasons playing for the Division III Salve Regina Seahawks and broke the mark set in 1987 by Robin Ventura with 58.

1990–91 Portland Trail Blazers season: The 1990–91 NBA season was the 21st season for the Portland Trail Blazers in the National Basketball Association.  During the offseason, the Blazers acquired Danny Ainge from the Sacramento Kings.  The Blazers won their first eleven games on their way to a franchise best start at a record of 27–3.  They would post a 16-game winning streak near the end of the season as they finished with a league best record at 63–19, setting a franchise-high win total that still stands today, and made their ninth consecutive trip to the NBA Playoffs.  It was their first Pacific Division title since the 1977–78 season, and ended the Los Angeles Lakers' streak of nine straight years as Pacific Division champions and number-one seed in the Western Conference.

Charles Radbourn: Charles Gardner Radbourn (December 11, 1854 – February 5, 1897), nicknamed "Old Hoss", was an American professional baseball pitcher who played 12 seasons in Major League Baseball (MLB).  He played for the Buffalo Bisons (1880), Providence Grays (1881–1885), Boston Beaneaters (1886–1889), Boston Reds (1890), and Cincinnati Reds (1891).  In 1884, Radbourn became only the second National League (NL) pitcher to win a Triple Crown; in the process, he broke the single-season wins record, which still stands today.  Radbourn was inducted into the National Baseball Hall of Fame in 1939.

Joe DiMaggio: Joseph Paul DiMaggio (November 25, 1914 – March 8, 1999), nicknamed "Joltin' Joe" and "The Yankee Clipper", was an American Major League Baseball center fielder who played his entire 13-year career for the New York Yankees.  He is perhaps best known for his 56-game hitting streak (May 15 – July 16, 1941), a record that still stands.

Question: This famous baseball player played the same position as his older brother, Vince, and was best know. For a hitting streak that still stands today 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "player_full_name": {
      "type": "string",
      "description": "The full name of the famous baseball player."
    },
    "player_position": {
      "type": "string",
      "description": "The primary playing position of the player."
    },
    "hitting_streak_details": {
      "type": "object",
      "properties": {
        "streak_length_games": {
          "type": "integer",
          "description": "The number of games in the player's famous hitting streak."
        },
        "is_current_record": {
          "type": "boolean",
          "description": "Indicates if the hitting streak record still stands today."
        },
        "streak_start_date": {
          "type": "string",
          "description": "The start date of the hitting streak."
        },
        "streak_end_date": {
          "type": "string",
          "description": "The end date of the hitting streak."
        }
      },
      "required": [
        "streak_length_games",
        "is_current_record",
        "streak_start_date",
        "streak_end_date"
      ],
      "additionalProperties": false
    },
    "brother_details": {
      "type": "object",
      "properties": {
        "brother_full_name": {
          "type": "string",
          "description": "The full name of the player's older brother."
        },
        "brother_position": {
          "type": "string",
          "description": "The primary playing position of the player's older brother."
        },
        "played_same_position": {
          "type": "boolean",
          "description": "Indicates if the player played the same position as his older brother."
        }
      },
      "required": [
        "brother_full_name",
        "brother_position",
        "played_same_position"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "player_full_name",
    "player_position",
    "hitting_streak_details",
    "brother_details"
  ],
  "additionalProperties": false
}
