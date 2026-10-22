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
Lindy Hood: James Marcus "Lindy" Hood (July 30, 1907 – October 17, 1972) was a college basketball All-American center for the University of Alabama.  At Alabama, Hood is noted for being their first All-American men's basketball player in 1931 and as the leader of the undefeated 1929–30 Crimson Tide squad.  Hood's nickname "Lindy" came during his playing days with Alabama during a trip to New Orleans to play Tulane.  As he entered a hotel lobby, a crowd mistook Hood for Charles Lindbergh and thus the nickname "Lindy" was given to him.  Hood was posthumously inducted into the Alabama Sports Hall of Fame in 1990.

2003 Ontario Scott Tournament of Hearts: The 2003 Ontario Scott Tournament of Hearts, the provincial women's championship in Ontario was held January 25-February 2 at the Hershey Centre in Mississauga.  The Anne Dunn rink from Cambridge, Ontario won the event.  She and her rink of Lindy Marchuk, Gloria Campbell and Fran Todd would go on to represent Ontario at the 2003 Scott Tournament of Hearts.  The event was held in conjunction with the 2003 Ontario Nokia Cup, the Ontario men's curling championship.

Lindy's Sports: Lindy’s Sports, also known as Lindy's, is a sports magazine.  It was established in 1982, and is located in Birmingham, Alabama.

Lindy Delapenha: Lloyd Lindbergh "Lindy" Delapenha (5 May 1927 – 26 January 2017) was a Jamaican footballer and sports journalist.  He was the first Jamaican to play professional football in England.  Between 1948 and 1960, he played league football for Portsmouth, Middlesbrough and Mansfield Town.

Matt Lindenmuth: Matt Lindenmuth (born March 1, 1981) is an American formerly top-ranked professional vert skater, as well as a professional snowboarder.  He is most known for being the first action sports athlete in the world to do a double backflip on a vert ramp, often referred to as a "Double Lindy".  At the 2002 Summer X-Games Lindenmuth attempted but failed to pull off the first ever triple backflip on a vert ramp.

Rick Lindy: Rick Lindy (born June 30, 1967) is an actor and Country/Rockabilly musician from Chicago, Illinois.  He currently performs with the Big Guitars from Memphis as well as leading his own band, Rick Lindy and the Wild Ones.  His previous band, the Cyclones, backed up Hayden Thompson for a show on Oct 2, 1992.  Lindy's first solo single, "Working Man Blues" (1990), was produced by John Capps and featured DJ Fontana on drums.

GO (American magazine): GO (previously GO NYC), is a "cultural roadmap for the city girl," and is the nation's most widely distributed, free, lesbian magazine.  Based out of New York City, GO distributes 30,000 copies in 10 major cities, and receives 250,000 unique web hits monthly.  The publication offers information on nightlife, arts & entertainment, news & current events, lifestyle, travel, advice, and celebrity Q&As.

Here We Go Again (Demi Lovato album): Here We Go Again is the second studio album by American singer Demi Lovato.  It was released on July 21, 2009, through Hollywood Records.  Unlike her previous album, "Don't Forget" (2008), Lovato did not collaborate with the Jonas Brothers, as she wanted to work with different people and give the album a personal approach.  Lovato collaborated for the album with established songwriters and producers, such as E. Kidd Bogart, Gary Clark, Toby Gad, John Mayer, Jon McLaughlin, Lindy Robbins and John Fields, who produced her previous album "Don't Forget".  Lovato also collaborated with The Academy Is... lead singer William Beckett to write a song about a strained relationship with her father, which was originally set to appear on the album, but was later dropped.  The song later appeared on her third album "Unbroken" (2011).

Tuff Monks: Tuff Monks was a short-lived band consisting of Nick Cave, Mick Harvey and Rowland S. Howard (each a member of The Birthday Party) with Robert Forster, Lindy Morrison and Grant McLennan (each a member of The Go-Betweens).  Their only release was the 1982 7" 45 rpm single "After the Fireworks", on the Australian label Au Go Go Records.

Here We Go Again (Demi Lovato song): "Here We Go Again" is a song performed by American singer Demi Lovato.  It was written by Isaac Hasson, Lindy Robbins and Mher Filian and produced by SuperSpy, for Lovato's second studio album of the same name.  It was released as the album's lead single on June 23, 2009, through Hollywood Records.  The song was the only single from "Here We Go Again" released in North America.  "Here We Go Again" is a power pop song with guitar lines and pop hooks and the lyrics speak of the protagonist's on-off relationship with a hesitant boyfriend.

Question: Are GO and Lindy's Sports from the same country?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "are_from_same_country": {
      "type": "boolean",
      "description": "True if both entities are from the same country, false otherwise."
    },
    "first_entity_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the first entity."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the first entity is based."
        }
      },
      "required": [
        "name",
        "country_of_origin"
      ],
      "additionalProperties": false
    },
    "second_entity_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the second entity."
        },
        "country_of_origin": {
          "type": "string",
          "description": "The country where the second entity is based."
        }
      },
      "required": [
        "name",
        "country_of_origin"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "are_from_same_country",
    "first_entity_details",
    "second_entity_details"
  ],
  "additionalProperties": false
}
