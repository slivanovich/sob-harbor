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
Matt Sydal: Matthew Joseph Korklan (born March 19, 1983), also known by the ring name Matt Sydal, is an American professional wrestler currently signed to Global Force Wrestling.  He is known for his time in WWE under the ring name Evan Bourne.

Bruce Prichard: Bruce Prichard (born March 7, 1963) is a professional wrestling personality currently signed to Global Force Wrestling as both an on-air talent and in a backstage advisory role.  He is perhaps best known as a manager and producer for World Wrestling Entertainment (WWE, formerly the World Wrestling Federation).  As a manager for the promotion, Prichard performed under the ring name Brother Love and served as the original manager of The Undertaker.  During Prichard's run as Brother Love, he hosted his own segment "The Brother Love Show" where he would usually support the heel wrestlers.  After leaving WWE, Prichard was the Senior Vice President of Programming and Talent Relations for Total Nonstop Action Wrestling (TNA, now Global Force Wrestling).  Prichard and Conrad Thompson co-host the podcast "Something to Wrestle with Bruce Prichard."

Reno Scum: Reno Scum are an American professional wrestling tag team consisting of Adam Thornstowe and Luster the Legend.  They are best known for their work on the independent circuit and are best friends in real life.  They are currently signed to Global Force Wrestling.  They have also worked for Ring of Honor (ROH) and the original Global Force Wrestling (2014–2017).  Though best known as a tag team, Reno Scum has also been a stable, which included, in addition to Luster and Thornstowe, Christina Von Eerie, Paul Isadora and Shane Dynasty.  Scum has been said to stand for Socially Corrupt Underground Militia.

Sonjay Dutt: Retesh Bhalla (born April 7, 1982) is an Indo-American professional wrestler, better known by his ring name, Sonjay Dutt.  He is currently signed with Global Force Wrestling.  He also competed for the original Global Force Wrestling, where he was a former GFW NEX*GEN Champion.  His ring name is modeled after that of famous Bollywood actor Sanjay Dutt.

Bram (wrestler): Thomas Raymond Latimer (born 6 August 1986) is an English professional wrestler and occasional actor, signed to Global Force Wrestling under the ring name Bram.  Before signing to Global Force Wrestling (formerly Total Nonstop Action Wrestling), he performed under the ring name Kenneth Cameron for WWE's developmental territories FCW and NXT as a member of The Ascension.

Generation Next: Generation Next and also (simply stylized as GenNext) was a professional wrestling stable in the Ring of Honor (ROH) promotion.  Formed in Philadelphia, PA at the event Generation Next, on May 22, 2004, by Alex Shelley, the original Generation Next consisted of Shelley, Austin Aries, Sabin, Roderick Strong and Jack Evans.  Shelley and Sabin was eventually kicked out of the group and replaced by Aries as the leader, who would later added Matt Sydal to the faction in the summer of 2005.  On June 3, 2006 at "Destiny", Aries officially disbanded Generation Next, with the four wrestling as a faction for one last time on July 29, 2006 at "Generation Now".

Noam Dar: Noam David Dar (Hebrew: נועם דר; born 28 July 1993) is an Israeli born Scottish professional wrestler currently signed to WWE, where he performs on the Raw brand.  He first competed for WWE in the 2016 Cruiserweight Classic.  He has also worked for Total Nonstop Action Wrestling (TNA) and its "British Boot Camp" series, Progress Wrestling, Preston City Wrestling (PCW), Insane Championship Wrestling (ICW), Dragon Gate UK (DGUK), Revolution Pro Wrestling (RPW), Westside Xtreme Wrestling (wXw), Global Force Wrestling (GFW) and Ring of Honor (ROH).  Dar is a former two time ICW Zero-G Champion and a former PCW Cruiserweight Champion, among other championships and accomplishments.  Dar is the first Israeli wrestler to perform in WWE.

Allie (wrestler): Laura Dennis (born September 3, 1987) is a Canadian professional wrestler currently signed to Global Force Wrestling under the ring name Allie, where she is a former TNA Knockouts Champion.  She is well known for working for Great Canadian Wrestling, NCW Femmes Fatales, Shimmer Women Athletes, Shine Wrestling, Women Superstars Uncensored (WSU) and Combat Zone Wrestling (CZW) under the ring name Cherry Bomb.  With tag team partner Kimber Lee, collectively known as The Kimber Bombs, they have held the Shine Tag Team Championship and the Shimmer Tag Team Championship both once.  She is also A former 1 time WSU Champion.

Jax Dane: Jackson Dane (born April 10, 1981) is an American professional wrestler currently signed to Global Force Wrestling under the ring name Wilcox.  He is perhaps best known for his tenure with various National Wrestling Alliance member promotions.  Within the NWA he is the former NWA World Heavyweight Champion and a former NWA National Heavyweight, NWA North American Heavyweight and NWA World Tag Team Champion.  He has also worked for New Japan Pro Wrestling (NJPW) and Ring of Honor (ROH).

Braxton Sutter: Jesse Guilmette (born June 3, 1980) is an American professional wrestler currently signed to Global Force Wrestling under the ring name Braxton Sutter.  Guilmette is also known for his time on the independent circuit under the ring name Pepper Parks, most notably in Combat Zone Wrestling (CZW), where he was a one-time CZW World Tag Team Champion with Blk Jeez.

Question: What is the birthdate of this American professional wrestler currently signed to Global Force Wrestling, who was added to Generation Next wrestling stable in the summer of 2005?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "wrestler_name": {
      "type": "string",
      "description": "The professional wrestling name of the wrestler."
    },
    "real_name": {
      "type": "string",
      "description": "The real name of the wrestler."
    },
    "birth_date": {
      "type": "object",
      "properties": {
        "month": {
          "type": "string",
          "description": "The month of birth."
        },
        "day": {
          "type": "integer",
          "description": "The day of birth."
        },
        "year": {
          "type": "integer",
          "description": "The year of birth."
        }
      },
      "required": [
        "month",
        "day",
        "year"
      ],
      "additionalProperties": false
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the wrestler."
    },
    "current_promotion": {
      "type": "string",
      "description": "The professional wrestling promotion the wrestler is currently signed with."
    },
    "stable_history": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "stable_name": {
            "type": "string",
            "description": "The name of the wrestling stable."
          },
          "join_year": {
            "type": "integer",
            "description": "The year the wrestler joined the stable."
          }
        },
        "required": [
          "stable_name",
          "join_year"
        ],
        "additionalProperties": false
      },
      "description": "A list of wrestling stables the wrestler was a member of."
    }
  },
  "required": [
    "wrestler_name",
    "real_name",
    "birth_date",
    "nationality",
    "current_promotion",
    "stable_history"
  ],
  "additionalProperties": false
}
