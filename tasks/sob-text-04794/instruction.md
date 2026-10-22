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
Richard B. Spencer: Richard Bertrand Spencer (born May 11, 1978) is an American white supremacist.  He is president of the National Policy Institute, a white supremacist think tank, as well as Washington Summit Publishers.  Spencer has stated that he rejects the label of white supremacist, and prefers to describe himself as an identitarian.  He has advocated for a white homeland for a "dispossessed white race" and called for "peaceful ethnic cleansing" to halt the "deconstruction" of European culture.

Jared Taylor: Samuel Jared Taylor (born September 15, 1951) is an American white nationalist and white supremacist.  He is the founder and editor of "American Renaissance", a white supremacist magazine.  Taylor is also an author and the president of "American Renaissance"' s parent organization, New Century Foundation, through which many of his books have been published.  He is a former member of the advisory board of "The Occidental Quarterly", and a former director of the National Policy Institute, a Virginia-based white nationalist think tank.  He is also a board member and spokesperson of the Council of Conservative Citizens.

Matthew F. Hale: Matthew F. "Matt" Hale (born July 27, 1971) is an American white supremacist leader and a convicted felon.  Hale was the founder of the East Peoria, Illinois-based white separatist group then known as the World Church of the Creator (now called The Creativity Movement), and he declared himself its "Pontifex Maximus" (Latin for "highest priest") in continuation of the Church of the Creator organization founded by Ben Klassen in 1973.

David Lane (white supremacist): David Eden Lane (November 2, 1938 – May 28, 2007) was an American white supremacist leader and convicted felon.  A member of The Order, he was convicted and sentenced to 190 years in prison for racketeering, conspiracy, and for violating the civil rights of Alan Berg, a Jewish radio talk show host, who was murdered on June 18, 1984.  He died while incarcerated in the Federal Correctional Complex in Terre Haute, Indiana.

Aryan Brotherhood of Texas: The Aryan Brotherhood of Texas (ABT) is an American white supremacist prison gang.  According to the Anti-Defamation League and the Southern Poverty Law Center, the Aryan Brotherhood of Texas is one of the largest and most violent white supremacist prison gangs in the United States, responsible for numerous murders and other violent crimes.

David Duke: David Ernest Duke (born July 1, 1950) is an American white supremacist and white nationalist, politician, antisemitic conspiracy theorist, Holocaust denier, convicted felon, and former Grand Wizard of the Ku Klux Klan.

88 Precepts: 88 Precepts is an essay or manifesto written by David Lane, a member of the white supremacist organization The Order.  Written while Lane was serving a 190-year prison sentence, 88 Precepts is a treatise on natural law, religion and politics from the view point of David Lane including guidelines for securing, protecting, preserving and establishing white territorial imperatives in North America and Eastern Europe, distributing propaganda, calls for a night-watchman state and are an expansion upon Lane's Fourteen Words.

Jamie Kelso: Jamie Kelso (June 8, 1948) is an American white supremacist and former Church of Scientology member of the elite Sea Org.  He hosts daily web radio programs, including "The Jamie Kelso Show" on the Voice of Reason Broadcast Network, and is a senior moderator of the white supremacist Stormfront website, where he uses the name Charles A. Lindberg.  Kelso became a moderator at Stormfront in 2002 and was instrumental in its rapid growth, partially by encouraging senior figures in the white supremacist movement to post.

Identity Evropa: Identity Evropa is a white supremacist group in the United States, established in March 2016.  Part of the broader white supremacist alt-right movement, the group is identified as a racist white supremacist organization by the Anti-Defamation League and is designated by the Southern Poverty Law Center as a hate group.  Relatively small in size, the group is seen as one of several groups contributing to a rising spike of white nationalism in the U.S. since 2015.  The group particularly targets college campuses, by distributing white nationalist slogans on fliers, posters, and stickers.

James Ellison (polygamist): James Ellison (  1937 ) was an American white supremacist leader from San Antonio, Texas.  In 1971, he founded the radical organization The Covenant, The Sword, and the Arm of the Lord (CSA).  Ellison purchased a 250 acre strip of land near Elijah, Missouri to serve as his compound.  He was also a close associate of both Richard Wayne Snell and Timothy McVeigh.

Question: Which group was this American white supremacist leader and convicted felon, who wrote the essay "88 Precepts," a member of?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "leader_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the white supremacist leader."
        },
        "status": {
          "type": "string",
          "description": "The legal status of the leader."
        },
        "essay_authored": {
          "type": "string",
          "description": "The title of the essay written by the leader."
        }
      },
      "required": [
        "name",
        "status",
        "essay_authored"
      ],
      "additionalProperties": false
    },
    "group_membership": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the group the leader was a member of."
        },
        "type": {
          "type": "string",
          "description": "The type of organization the group is."
        }
      },
      "required": [
        "name",
        "type"
      ],
      "additionalProperties": false
    },
    "final_answer": {
      "type": "string",
      "description": "The name of the group that the leader was a member of."
    }
  },
  "required": [
    "leader_details",
    "group_membership",
    "final_answer"
  ],
  "additionalProperties": false
}
