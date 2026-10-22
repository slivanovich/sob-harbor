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
Pat Toomey: Patrick Joseph Toomey (born November 17, 1961) is an American businessman, politician, and the junior United States Senator from Pennsylvania, in office since 2011.  A member of the Republican Party, Toomey served as the United States Representative for Pennsylvania 's 15 congressional district for three terms, from 1999 to 2005, but he did not seek a fourth term in compliance with a term limits pledge he had made while running for office in 1998.

Kirsten Gillibrand: Kirsten Elizabeth Gillibrand (née Rutnik; ; born December 9, 1966) is an American attorney and politician who since 2009, has served as the junior United States Senator from New York, alongside the Democratic Leader of the United States Senate, Chuck Schumer.  Before the Senate, she served for two years (2007-09) in the United States House of Representatives, representing New York's 20th congressional district.  She is a member of the Democratic Party.

Tammy Duckworth: Ladda Tammy Duckworth (born March 12, 1968) is an American politician and retired U.S. Army Lieutenant Colonel, serving as the junior United States Senator for Illinois since 2017.  A member of the Democratic Party, she earlier represented Illinois' 8th district for two terms (2013–2017) in the United States House of Representatives.  Before seeking elective office, she served as Assistant Secretary for Public and Intergovernmental Affairs in the United States Department of Veterans Affairs (2009-2011), and she was the Director of the Illinois Department of Veterans Affairs (2006-2009).  In the 2016 election, Duckworth defeated incumbent Republican Senator Mark Kirk for the seat in the United States Senate.

Bob Corker: Robert Phillips Corker Jr. (born August 24, 1952) is an American businessman, politician and the junior United States Senator from Tennessee, serving since 2007.  Corker, a member of the Republican Party, is the chairman of the United States Senate Committee on Foreign Relations in the 115th Congress.

David Perdue: David Alfred Perdue Jr. (born December 10, 1949) is an American businessman and politician; he is the junior United States Senator from Georgia, having been elected in 2014 to the seat previously held by Saxby Chambliss, who retired.  Perdue won the Republican primary and defeated Democratic nominee Michelle Nunn on November 4, 2014, taking office on January 3, 2015.  He is a first cousin of Sonny Perdue, former governor of Georgia and current Secretary of Agriculture.

Mike Rounds: Marion Michael Rounds (born October 24, 1954) is an American businessman, politician and the junior United States Senator from South Dakota, since January 2015.  A member of the Republican Party, Rounds served as the 31st Governor of South Dakota from 2003 to 2011, having previously served in the South Dakota Senate from 1991 to 2001.

John Neely Kennedy: John Neely Kennedy (born November 21, 1951) is an American attorney and politician who is the junior United States Senator from Louisiana, serving since 2017.  A member of the Republican Party, he served terms as Louisiana state treasurer and took office as Louisiana's junior senator in the United States Senate on January 3, 2017, alongside the state's senior senator Bill Cassidy.  He defeated Democratic candidate Foster Campbell in the Senate election runoff by more than 21 percentage points, about a month after prevailing in the state's jungle primary, along with Campbell.

Steve Daines: Steven David Daines (born August 20, 1962) is an American businessman, entrepreneur, and the junior United States Senator from Montana.  He was the United States Representative for Montana's at-large congressional district from 2013 to 2015.  In the 2014 election, he won an open U.S. Senate seat, defeating Democrat Amanda Curtis.

Candy Desk: The Candy Desk has been a tradition of the United States Senate since 1968, whereby a senator who sits at a particular desk near a busy entrance keeps a drawer full of candy for members of the body.  The current occupant of the Candy Desk is Pennsylvania Senator Pat Toomey.

Tom Cotton: Tom Cotton (born Thomas Bryant Cotton; May 13, 1977) is an American politician who is the junior United States Senator from Arkansas.  A member of the Republican Party, Cotton has served in the Senate since January 3, 2015.  At age 40 , he is currently the youngest U.S. Senator.

Question: Since when did this American businessman, politician, and the junior United States Senator serve in the Senate who currently occupies the Candy Desk?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "senator_name": {
      "type": "string",
      "description": "The full name of the senator."
    },
    "senate_service_start_year": {
      "type": "integer",
      "description": "The year the senator began their service in the United States Senate."
    },
    "roles": {
      "type": "array",
      "description": "A list of roles or professions attributed to the senator.",
      "items": {
        "type": "string"
      }
    },
    "occupies_candy_desk": {
      "type": "boolean",
      "description": "Indicates whether the senator currently occupies the Candy Desk."
    }
  },
  "required": [
    "senator_name",
    "senate_service_start_year",
    "roles",
    "occupies_candy_desk"
  ],
  "additionalProperties": false
}
