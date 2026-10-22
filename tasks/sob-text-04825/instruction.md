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
School Daze: School Daze is a 1988 American musical comedy drama film, written and directed by Spike Lee, and starring Larry Fishburne, Giancarlo Esposito, and Tisha Campbell-Martin.  Based in part on Spike Lee's experiences at Atlanta's Morehouse College, Spelman College, Morris Brown College and Clark Atlanta University, it is a story about fraternity and sorority members clashing with other students at a historically black college during homecoming weekend.  It also touches upon issues of colorism and hair texture bias within the African-American community.  The second feature film by Spike Lee, "School Daze" was released on February 12, 1988 by Columbia Pictures.

George O. Gore II: George O. Gore II (born December 15, 1982) is an American actor.  He is best known for portraying Michael Kyle, Jr. ("Big Head Junior") on the ABC sitcom "My Wife and Kids", Gore's television credits include guest roles on "Law & Order" and "Touched by an Angel".  He was also a main character in the cast of the comedy Second Generation Wayans.  For his role as G, the young son of Malik Yoba's character, in "New York Undercover", he received three NAACP Image Award nominations.

Rita Rocks: Rita Rocks is a Lifetime original sitcom that ran from October 20, 2008 to December 7, 2009.  It was the network's first original comedy in over a decade.  The series debuted alongside re-runs of "Reba" as part of a new comedy hour for Tuesday nights, which later changed to Monday nights.  The show stars Nicole Sullivan as Rita, Tisha Campbell-Martin, Richard Ruccolo, Raviv Ullman, and Kelly Gould.

Holly Flax: Hollis "Holly" Partridge Scott (née Flax) is a fictional character from the US television series "The Office" played by Amy Ryan.  She was an original character, and not based on a character from the British version of the show.  Initially, she served as a replacement HR Representative for the Scranton branch of Dunder Mifflin when Toby Flenderson left for Costa Rica.  Later, her character was developed into a friend and romantic interest for Steve Carell's character Michael Scott.  She and Michael have a shared sense of humor and similar personality traits, though Holly does prove to be more rational than Michael.  In the office, she is noticeably more acquiescent to Michael's antics and ideas than was her predecessor, Toby.  At the office, Michael proposes to her with the help of their co-workers.  She and Michael eventually get back together, move to Colorado, marry and start a family together.

Mike Kyle: Michael Kyle (born March 31, 1980) is an American professional mixed martial artist currently competing in the Heavyweight division.  A professional competitor since 2001, Kyle has competed for the UFC, the WEC, Strikeforce, the World Series of Fighting, Absolute Championship Berkut, Pancrase, King of the Cage, and is the former King of the Cage Light Heavyweight Champion.

My Wife and Kids: My Wife and Kids is an American television sitcom that ran on ABC from March 28, 2001, until May 17, 2005.  Produced by Touchstone Television (now ABC Studios), it starred Damon Wayans and Tisha Campbell-Martin, and centers on the character of Michael Kyle, a loving husband and modern-day patriarch who rules his household with a unique and distinct parenting style.  As he teaches his three children some of life's lessons, he does so with his own brand of humor.  Wayans and veteran television writer/producer Don Reo co-created and executive produced the series.

Homeward Bound II: Lost in San Francisco: Homeward Bound II: Lost in San Francisco is a 1996 American adventure comedy film and a sequel to the 1993 film "".  Directed by David R. Ellis, the film features the three animals from the first film, Shadow the Golden Retriever (voiced by Ralph Waite, replacing Don Ameche, who died in 1993), Sassy the Himalayan cat (Sally Field), and Chance the American Bulldog (Michael J. Fox).  It also features the voice work of Sinbad, Carla Gugino, Tisha Campbell-Martin, Stephen Tobolowsky, Jon Polito, Adam Goldberg, Al Michaels, Tommy Lasorda, and Bob Uecker.

Stan Zimmerman: Stan Zimmerman is an American television producer, director and screenwriter.  Zimmerman has written for many television series including "The Golden Girls", "Roseanne" and "Gilmore Girls" and the 1996 feature film "A Very Brady Sequel".  Zimmerman is also the creator and executive producer of the sitcom "Rita Rocks", starring Nicole Sullivan and Tisha Campbell-Martin which ran on Lifetime Television.

Tisha Campbell-Martin: Tisha Campbell–Martin (born Tisha Michelle Campbell; October 13, 1968) is an American actress and singer.  Campbell is best known for her starring roles on television such as Regina "Gina" Waters–Payne on the FOX series, "Martin" which originally ran from 1992 to 1997; and as Janet "Jay" Marie Johnson-Kyle on the ABC television sitcom, "My Wife and Kids", from 2001 until 2005.

James Berg: James Berg is an American television producer and writer.  He has written for many television series including "The Golden Girls", "Roseanne" and "Gilmore Girls" and the 1996 feature film "A Very Brady Sequel".  He has frequently collaborated with fellow producer and writer Stan Zimmerman.  Berg and Zimmerman were also the creators and executive producers of the sitcom, "Rita Rocks", starring Nicole Sullivan and Tisha Campbell-Martin which ran on Lifetime Television.

Question: Who starred with Tisha Campbell-Martin in an American sitcom as the character Michael Kyle?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who played the specified character."
    },
    "character_name": {
      "type": "string",
      "description": "The name of the character played by the actor."
    },
    "sitcom_details": {
      "type": "object",
      "properties": {
        "title": {
          "type": "string",
          "description": "The title of the American sitcom."
        },
        "co_star_name": {
          "type": "string",
          "description": "The name of the co-star mentioned in the question."
        },
        "network": {
          "type": "string",
          "description": "The television network the sitcom ran on."
        },
        "run_start_year": {
          "type": "integer",
          "description": "The year the sitcom started its run."
        },
        "run_end_year": {
          "type": "integer",
          "description": "The year the sitcom ended its run."
        }
      },
      "required": [
        "title",
        "co_star_name",
        "network",
        "run_start_year",
        "run_end_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "actor_name",
    "character_name",
    "sitcom_details"
  ],
  "additionalProperties": false
}
