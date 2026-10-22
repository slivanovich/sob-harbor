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
Republican Party presidential primaries, 2008: The 2008 Republican presidential primaries were the selection process by which voters of the Republican Party chose its nominee for President of the United States in the 2008 U.S. presidential election.  Senator John McCain of Arizona was selected as the nominee through a series of primary elections and caucuses culminating in the 2008 Republican National Convention held from Monday, September 1, through Thursday, September 4, 2008, in St. Paul, Minnesota.

Barack Obama presidential campaign, 2008: The 2008 presidential campaign of Barack Obama, then junior United States Senator from Illinois, was announced on February 10, 2007 in Springfield, Illinois.  After winning a majority of delegates in the Democratic primaries of 2008, on August 23, leading up to the convention, the campaign announced that Senator Joe Biden of Delaware would be the Vice Presidential nominee.  At the 2008 Democratic National Convention on August 27, Barack Obama was formally selected as the Democratic Party nominee for President of the United States in 2008.  He was the first African American in history to be nominated on a major party ticket.

John McCain presidential campaign, 2008: The 2008 presidential campaign of John McCain, the longtime senior U.S. Senator from Arizona, was launched with an informal announcement on February 28, 2007 during a live taping of the "Late Show with David Letterman", and formally launched at an event on April 25, 2007.  His second candidacy for the Presidency of the United States, he had previously run for his party's nomination in the 2000 primaries and was considered as a potential running mate for his party's nominee, then-Governor George W. Bush of Texas.  After winning a majority of delegates in the Republican primaries of 2008, on August 29, leading up to the convention, McCain selected Governor Sarah Palin of Alaska as his running mate for Vice President.  Five days later, at the 2008 Republican National Convention, McCain was formally selected as the Republican Party presidential nominee in the 2008 presidential election.

Jeff Flake: Jeffry Lane Flake (born December 31, 1962) is an American politician and member of the Republican Party who since 2013 has served as the Junior United States Senator from Arizona alongside former 2008 presidential nominee John McCain.

United States presidential election, 2008: The United States presidential election of 2008 was the 56th quadrennial presidential election.  It was held on Tuesday, November 4, 2008.  Democratic Party nominees Barack Obama, a U.S. Senator from Illinois, and his running mate Joe Biden, a long-time U.S. Senator from Delaware, defeated Republican Party nominees John McCain, a long-time and current U.S. Senator from Arizona, and his running mate Sarah Palin, a Governor of Alaska.  Obama became the first African American ever to be elected president of the United States, and Joe Biden became the first Roman Catholic ever elected vice president.

Political positions of Sarah Palin: Sarah Palin is an American politician, commentator and author who served as the ninth Governor of Alaska, from 2006 to 2009.  Palin was the Republican Party nominee for Vice President in the 2008 presidential election alongside Arizona Senator John McCain.

Political party strength in Arizona: The U.S. state of Arizona is the home of Senators Jeff Flake and John McCain, and the state is widely regarded as a Republican Party stronghold.

McCain Institute: The McCain Institute for International Leadership is a Washington, D.C.-based think tank in cooperation with Arizona State University whose mission is to "advance leadership based on security, economic opportunity, freedom, and human dignity, in the United States and around the world."  The institute was formed in 2012 and is named after U.S. Senator and 2008 Republican Party presidential nominee John McCain from Arizona.  Based in Washington, D.C., the McCain Institute is part of Arizona State University.  The current executive director of the McCain Institute is Kurt Volker.

Sarah Palin: Sarah Louise Palin ( ; née Heath; born February 11, 1964) is an American politician, commentator, and author who served as the ninth Governor of Alaska from 2006 until her resignation in 2009.  As the Republican Party nominee for Vice President of the United States in the 2008 election alongside presidential nominee, Arizona Senator John McCain, she was the first Alaskan on the national ticket of a major political party and the first Republican woman selected as a vice presidential candidate.  Her book "Going Rogue" has sold more than two million copies.

Cindy McCain: Cindy Lou Hensley McCain (born May 20, 1954) is an American businesswoman, philanthropist, and humanitarian, and the wife of long-time United States Senator and 2008 Republican presidential nominee John McCain of Arizona.

Question: The U.S. state of Arizona is the home of which Senator, an American politician and member of the Republican Party who since 2013 has served as the Junior United States Senator from Arizona, alongside former 2008 presidential nominee John McCain?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "senator_name": {
      "type": "string",
      "description": "The full name of the Senator."
    },
    "political_party": {
      "type": "string",
      "description": "The political party the Senator belongs to."
    },
    "state_represented": {
      "type": "string",
      "description": "The U.S. state the Senator represents."
    },
    "senator_role": {
      "type": "string",
      "description": "The specific role or title of the Senator."
    },
    "service_start_year": {
      "type": "integer",
      "description": "The year the Senator began serving in their current role."
    },
    "served_alongside_nominee": {
      "type": "object",
      "properties": {
        "nominee_name": {
          "type": "string",
          "description": "The name of the presidential nominee the senator served alongside."
        },
        "nominee_election_year": {
          "type": "integer",
          "description": "The year of the presidential election for which the individual was a nominee."
        }
      },
      "required": [
        "nominee_name",
        "nominee_election_year"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "senator_name",
    "political_party",
    "state_represented",
    "senator_role",
    "service_start_year",
    "served_alongside_nominee"
  ],
  "additionalProperties": false
}
