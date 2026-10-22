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
36 (TV series): 36 is a sports documentary television show that airs on NBCSN and TSN.  The show is a 36-hour documentary series following a specific athlete such as Patrick Kane.  The show typically airs before the spotlighted player competes on the NBC Sports Network.  The show is akin to "HBO 24/7".  On March 14, 2012, "36" expanded to have an episode about Zab Judah calling the show, "Fight Night 36".  Meanwhile, a "36" episode about IndyCar Series with Tony Kanaan first aired on April 1, 2012.  "MLS 36" debuted August 5, 2012 following Major League Soccer player Chris Wondolowski during the 2012 MLS All-Star Game.  "F1 36" debuted on March 29, 2013 featuring Formula One champion Sebastian Vettel.

Alex Browne (filmmaker): Alex Browne is a documentary film producer, noted for co-producing the sports documentary "A League of Ordinary Gentlemen".

Daniel Lindsay: Daniel Lindsay is a documentary filmmaker.  He is the co-director, producer and an editor of the 2011 sports documentary Undefeated, which received the 2011 Oscar for Best Documentary Feature.

Brian Robbins: Brian Levine (born November 22, 1963), best known as Brian Robbins, is an American actor, film director, film producer, television director, television producer and occasional screenwriter.  He often collaborates with producer Michael Tollin.

Aussie Rules the World: Aussie Rules the World is a 2014 Australian sports documentary film produced by Second Nature Films, directed by Michael Stringer McIntyre and includes interviews with various Australian Football League identities including, among others, former Sydney Swans premiership coach and current Melbourne coach Paul Roos, four-time Essendon premiership coach and foundation Greater Western Sydney coach Kevin Sheedy, former AFL CEO Andrew Demetriou, current Richmond player Bachar Houli and incumbent Australian of the Year Adam Goodes.

Hardwood Dreams: Hardwood Dreams is a 1993 basketball sports documentary written, directed and produced by Michael Tollin and narrated by Wesley Snipes.  It follows five Morningside High School (MHS) seniors during their last high school basketball season, as they dream of the National Basketball Association (NBA).

The Band That Wouldn't Die: The Band That Wouldn't Die is a sports documentary film released in 2009 and created and directed by Barry Levinson as a part of ESPN's "30 for 30" documentary series.  The film follows the story of Baltimore's Marching Ravens, a marching band that has supported three separate American football franchises since 1947 and witnessed the controversial relocation of the National Football League's (NFL) Baltimore Colts franchise to Indianapolis in 1984.

Once Brothers: Once Brothers (Serbian Cyrillic: "Једном браћа"/Jednom braća, Croatian: "Jednom braća") is a 2010 sports documentary film written and directed by Michael Tolajian.  It was co-produced by ESPN and NBA Entertainment for ESPN's "30 for 30" series.

Michael Tollin: Michael "Mike" Tollin (born October 6, 1955) is an American film and television producer/director.  His career highlights included "Radio", "Coach Carter", and "Varsity Blues".  He has created and produced such shows as "All That", "The Amanda Show", "Kenan & Kel", "One Tree Hill", "Smallville", "What I Like About You", "The Bronx is Burning", and "".  He is currently the Co-Chairman of Mandalay Sports Media.

Hank Aaron: Chasing the Dream: Hank Aaron: Chasing the Dream is a 1995 American documentary film directed by Michael Tollin.  The story follows baseball slugger Hank Aaron's pursuit of Babe Ruth's all-time record for home runs.  It was nominated for an Academy Award for Best Documentary Feature.

Question: Michael Tollin thewriter, producer and director of Hardwood Dreams, a sports documentary, is Co-Chairman of which company?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person in question."
    },
    "role": {
      "type": "string",
      "description": "The role the person holds at the company."
    },
    "company_name": {
      "type": "string",
      "description": "The name of the company where the person holds the specified role."
    },
    "documentary_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the documentary associated with the person."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "The roles the person had in the documentary."
        }
      },
      "required": [
        "title",
        "roles"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "person_name",
    "role",
    "company_name",
    "documentary_details"
  ],
  "additionalProperties": false
}
