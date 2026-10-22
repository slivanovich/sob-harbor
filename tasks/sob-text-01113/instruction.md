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
List of Rocket Monkeys episodes: This is a list of episodes for the Teletoon animated series, "Rocket Monkeys".  The series first premiered on January 10, 2013 on Teletoon in Canada.  It has been acquired by Nickelodeon in the United States and its global networks and premiered on the channel on March 4, 2013.

Total Drama Action: Total Drama Action is a Canadian animated television series.  It is the second season of the "Total Drama" series, which began with "Total Drama Island".  The show premiered in Teletoon at 6:30 pm ET/PT on January 11, 2009.  This series was also created by the makers of "6teen", another Teletoon program.  This is the only season for Teletoon to not air a new episode every week.

Rocket Monkeys: Rocket Monkeys is a Canadian animated television series that was created by Dan Abdo and Jason Patterson and premiered on Teletoon in Canada on January 10, 2013.  The series premiered on Nickelodeon in the United States on March 4, 2013.  The series is produced by Breakthrough Entertainment in association with Teletoon Canada Inc., Atomic Cartoons and Hornet Films.  The series ended on November 23, 2016

Spliced (TV series): Spliced is a Canadian animated television series produced by Teletoon and Nelvana.  The series made its world premiere on Jetix in Latin America on April 20, 2009.  The series has aired in Canada on Teletoon, in the United States on Qubo, in Australia on ABC3, in the United Kingdom on Nicktoons, in Latin America on Disney XD, and in Sweden on Nickelodeon.  The series began airing in the United States on Qubo on September 19, 2009 until the network dropped it from its lineup on October 24, 2009 but returned on September 28, 2010 as part of its "Night Owl" block and was discontinued on March 31, 2012.  Beginning early in 2014, YTV began airing reruns on weekdays.  In 2014, the series was added onto the "Always On" digital platform of Cartoon Network in the United States.  It was removed in early 2015.

The Hunger Strike: "The Hunger Strike" is a second season episode of the Adult Swim animated television series "The Boondocks".  It was set to premiere on January 7, 2008, between "The Story of Thugnificent" and "Attack of the Killer Kung-Fu Wolf Bitch", but has not aired in the United States.  In Canada, the episode was aired on March 16, 2008, on the network Teletoon, with a disclaimer stating that "the views in this program do not reflect that of Teletoon Canada or its parent companies".  The episode also aired globally elsewhere, and has appeared on Netflix streaming in Canada.  According to Aaron McGruder on an introduction video for the episode found on the DVD set, this episode was originally set to be titled "BET Sucks".

Yakkity Yak: Yakkity Yak is an Australian–Canadian animated television series created by Mark Gravas that ran on Teletoon in Canada and on Nickelodeon in Australia from November 9, 2002 to December 12, 2003.  The series was known for its surreal humor and featured animation incongruous with Nickelodeon's typical style.  The story centers around an anthropomorphic yak named Yakkity who aspires to become a famous comedian and his friends, Keo (an anthropomorphic pineapple) and Lemony (a young human girl).

Mark Gravas: Mark Gravas (born 29 September 1966) is an Australian animator, director and producer.  He is the creator/director of "Yakkity Yak" (2002/2003), an Australian/Canadian co-production.  Mark co-owns Sydney based media production company Kapow Pictures with his partner Sandra Walters.

The Bagel and Becky Show: The Bagel and Becky Show (also known as Dave Cooper's The Bagel and Becky Show or simply Bagel and Becky) is an animated children's television series created by Dave Cooper (co-creator of Nickelodeon's "Pig Goat Banana Cricket") for Teletoon.  The series debuted on Teletoon+ in Poland on November 14, 2016.  On November 15, 2017, the series will air on Universal Kids.

The Ripping Friends: The Ripping Friends: The World's Most Manly Men!  (also known as The Ripping Friends) is a Canadian animated television series, created by John Kricfalusi, who was well known for creating "The Ren & Stimpy Show" on Nickelodeon.  The show premiered September 22, 2001 on Fox Kids, but was cancelled in September 2002.  Adult Swim later picked up the show.  The series occasionally airs in Canada on Teletoon.  The series also aired briefly in the UK on the CNX channel and on ABC in Australia.  The show was rated TV-Y7 on Fox Kids and TV-PG on [adult swim] in the United States, and C8 to 14+ on Teletoon in Canada.

Mission Hill: Mission Hill (originally titled The Downtowners) is an American animated television series that ran on The WB from September 24, 1999, to July 16, 2000, and on Adult Swim from July 14 to August 11, 2002.  Although 18 episodes were planned, only 13 episodes were produced.  The show was put on hiatus by the WB Network after two episodes due to poor ratings.  It returned to the WB in the summer of 2000 but was canceled after four additional episodes.  The show went on to develop a cult following, thanks to repeated airings of all 13 episodes on Teletoon's "Teletoon Unleashed" block, Cartoon Network's popular late night programing block, Adult Swim and Too Funny To Sleep, a late night programing block on TBS.  "Mission Hill" was formerly known as "The Downtowners", although MTV's production of the similarly titled "Downtown" forced a name change.

Question: What does the creator of the television series that ran on Teletoon in Canada and on Nickelodeon in Australia (2002 to 2003) co-own with Sandra Walters?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "creator_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the creator."
        },
        "created_series": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of TV series created by this person."
        }
      },
      "required": [
        "name",
        "created_series"
      ],
      "additionalProperties": false
    },
    "co_owned_entity": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the entity co-owned."
        },
        "type": {
          "type": "string",
          "description": "The type of the entity (e.g., media production company)."
        },
        "location": {
          "type": "string",
          "description": "The location of the entity."
        },
        "co_owner_name": {
          "type": "string",
          "description": "The name of the person with whom the entity is co-owned."
        }
      },
      "required": [
        "name",
        "type",
        "location",
        "co_owner_name"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The direct answer to the question."
    }
  },
  "required": [
    "creator_details",
    "co_owned_entity",
    "final_answer"
  ],
  "additionalProperties": false
}
