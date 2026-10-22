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
Super heavyweight (MMA): The super heavyweight division in mixed martial arts has no weight limit but generally refers to competitors weighing above 265 lb (120 kg).  This is the definition used by the Nevada State Athletic Commission and the Association of Boxing Commissions.

Atomweight (MMA): The atomweight division in mixed martial arts generally refers to competitors weighing at or less than 105 lb .  It sits below the heavier strawweight division and is the lightest weight class widely recognized within MMA.  The atomweight division in mixed martial arts is not defined by the Unified Rules and is used almost exclusively for Women's MMA.

Chris Brennan: Chris "The Westside Strangler" Brennan (born October 12, 1971) is an American mixed martial artist who competes in the Lightweight division.  He has competed for the UFC, PRIDE, King of the Cage and Shooto.  He is a former King of the Cage Middleweight Champion and former King of the Cage Middleweight Superfight Champion.  He is also one of 18 fighters to compete in the -77 kg division at the ADCC Submission Wrestling World Championships in 2005.  Chris was also the founder of Nogi Industries, a Mixed martial arts clothing company.  In 2014 Chris was inducted in to the Mixed Martial Arts Hall of Fame.

JJ Aldrich: JJ Aldrich is an American mixed martial artist who competes in the Strawweight division.  She is currently signed with the Ultimate Fighting Championship and has fought for Invicta FC.

Strawweight (MMA): The strawweight division in mixed martial arts generally refers to competitors weighing between 106 and 115 lb (48 to 52 kg).  It sits between the lighter atomweight division and the heavier flyweight division.

Lee Hasdell: Lee Hasdell (born 13 December 1966) is a British martial artist, promoter and former professional kickboxer and mixed martial artist.  Hasdell is considered by many as a true pioneer of UK mixed martial arts, as he was the main driving force and innovator in the 1990s.  Hasdell promoted the first professional Mixed martial arts events in the United Kingdom and has helped develop many of the standards within the British MMA scene of today.

Tatiana Suarez: Tatiana Suarez (born December 19, 1990) is a female American professional mixed martial artist with a background in wrestling.  She defeated Chel-c Bailey, JJ Aldrich, and Kate Jackson during the of "The Ultimate Fighter" reality show, en route to becoming TUF strawweight tournament winner.

Masakatsu Ueda: Masakatsu Ueda (born December 21, 1977) is a professional Japanese mixed martial artist who currently competes in the bantamweight division (known as featherweight in Shooto) for Shooto where he is the former Featherweight champion.  Ueda won the vacant title after defeating Koetsu Okazai on March 28, 2008, by Unanimous Decision at Shooto's Back To Our Roots 8 show.  Ueda was also a college level wrestler in Japan where holds a win over fellow mixed martial artist and Japanese Superstar Norifumi Yamamoto, better known as "Kid" Yamamoto.  Ueda has also won many national titles in Combat Wrestling.  He also won the All Japan Shooto Grappling championship, and both A and B class Shooto Rookie Tournaments.  He is a blue belt in Brazilian Jiu-Jitsu under Yuki Nakai.

Mohammed &quot;The Hawk&quot; Shahid: Mohammed Shahid (born July 8, 1989) is an entrepreneur and a mixed martial artist from Bahrain.  He is the CEO of KHK MMA and the President of the Bahrain based mixed martial arts organisation, Brave Combat Federation owned and supported by His Highness Sheikh Khalid bin Hamad Al Khalifa.  Mohammed Shahid was the first mixed martial artist from Bahrain to compete in global MMA events.  He was assigned a managerial role to develop mixed martial arts in Bahrain as the CEO of KHK MMA.  Bahrain established a national team alongside bringing global talent to facilitate the growth of MMA in Bahrain.

Murilo Rua: Murilo "Ninja" Milani Rua (] ; born May 22, 1980) is a retired Brazilian mixed martial artist who fought in Pride Fighting Championships.  He is the older brother of former UFC Light Heavyweight Champion Mauricio "Shogun" Rua.  He is known for his aggressive Muay Thai style.  Rua is a veteran of Pride Fighting Championships, where he once enjoyed a reputation as one of the best middleweights in the world.  Rua regularly fought at 185 pounds, but has also fought at 205 pounds and heavyweight.  He is the former (and first ever) EliteXC Middleweight Champion.  He also had a successful career in mixed martial arts in England appearing on both Cage Rage and BAMMA cards.  He is of Portuguese and Italian descent, but was born in Brazil.

Question: Mixed martial artist JJ Aldrich competes in a division for competitors weighing between 106 and how many pounds?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "fighter_name": {
      "type": "string",
      "description": "The name of the mixed martial artist."
    },
    "division_name": {
      "type": "string",
      "description": "The name of the weight division the fighter competes in."
    },
    "weight_limits": {
      "type": "object",
      "properties": {
        "lower_bound_lb": {
          "type": "integer",
          "description": "The lower weight limit of the division in pounds."
        },
        "upper_bound_lb": {
          "type": "integer",
          "description": "The upper weight limit of the division in pounds."
        }
      },
      "required": [
        "lower_bound_lb",
        "upper_bound_lb"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "fighter_name",
    "division_name",
    "weight_limits"
  ],
  "additionalProperties": false
}
