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
Mayday PAC: Mayday PAC is an American crowd-funded non-partisan Super PAC created by Harvard Law School professor and activist Lawrence Lessig.  Its purpose is to help elect candidates to the Congress to pass campaign finance reform.  It is notable for raising large sums from numerous contributors in a short span of time nearly $11 million in 2014 and was described in the "Los Angeles Times" as the "super PAC to end all super PACs."  The group spent over $10 million in the November 2014 elections, but its strategic plan of electing candidates friendly to campaign finance reform failed.

Vote Climate U.S. PAC: Vote Climate U.S. PAC is an American super PAC founded in 2013 and directed by American political activist Karyn Strickler.  Its mission is "to elect candidates to get off fossil fuels, transition to clean, renewable energy and put a price on carbon, in order to slow global warming and related weather extremes."  Strickler has named the implementation of a carbon tax as a principal goal.  As a super PAC (a type of political action committee), the organization cannot contribute to candidates but can make independent expenditures on their behalf.

Priorities USA Action: Priorities USA Action is the largest Democratic Party super PAC.  Founded in 2011, it supported Barack Obama's 2012 re-election campaign.  It was the primary super PAC supporting Hillary Clinton's 2016 presidential campaign.  It focused mainly on high-dollar donors.  As of September 2016, it had amassed $132 million in support of Clinton.  The top six donors to the super PAC have given $43.5 million, which is a third of the money collected by Priorities USA Action in the 2016 election cycle.  The super PAC raised $21.7 million in August 2016, marking its largest monthly fundraising haul.

LPAC: LPAC is a Super PAC founded in 2012 to represent the interests of lesbians in the United States, and to campaign on LGBT and women's rights issues.  According to its chair it was the first Super PAC of its kind.  Its supporters include Billie Jean King, Jane Lynch, Laura Ricketts and Urvashi Vaid.  On its first day of operations, LPAC raised $200,000.  In April 2015 LPAC endorsed Hillary Clinton's 2016 presidential campaign.

Colbert Super PAC: Americans for a Better Tomorrow, Tomorrow (better known as the Colbert Super PAC) was a United States political action committee (PAC) established by Stephen Colbert, who portrayed Dr. Stephen T. Colbert, a mock-conservative political pundit on Comedy Central's satirical television series "The Colbert Report".  As a super PAC the organization could raise unlimited sums of money from corporations, unions and other groups, as well as wealthy individuals.  Speaking in character, Colbert said the money would be raised not only for political ads, but also "normal administrative expenses, including but not limited to, luxury hotel stays, private jet travel, and PAC mementos from Saks Fifth Avenue and Neiman Marcus."

Stockmann, Helsinki centre: The Stockmann department store is a culturally significant business building and department store located in the centre of Helsinki, Finland.  It is one of many department stores owned by the Stockmann corporation.  It is the largest department store in the Nordic countries in terms of area and total sales.  The store is known for carrying all the internationally recognised luxury brands, and Stockmann's enjoys a reputation as the primary high-end department store in Finland.  "Stockmannin Herkku", the food and beverage department located at the basement level, is renowned for the quality and choice of its foodstuffs.  The Stockmann logo represents a set of escalators, which are commonly, but wrongly believed represent the first escalators in Finland.  The first escalators in Finland were installed in the Forum department store, Turku (1926)

Run for Courage: Run for Courage is a nonprofit organization that combats human trafficking.  The organization is based in Sacramento, California and raises money for human trafficking victims and their families.  Ashlie Bryant is the executive director of Run for Courage.  The founder was Vicki Zito, whose daughter was abducted at age seventeen and sexually trafficked in the East Bay.  The organization was founded in 2009 and holds a charity run annually, raising more than $550,000 within its first four years.  In 2010, the funds raised were donated to Courage House, a building in Roseville, California that houses teen sex trafficking victims.  Approximately 2000 people participated in the 2011 run.  That year, the funds raised went to Agape International Missions, A New Day For Children, Courage To Be You, and WIND Youth Services.  In 2014, FreeFall Stage produced performances of "She Has a Name", a play about human trafficking, and Run for Courage partnered in this initiative, having representatives at each performance.

Saks Fifth Avenue: Saks Fifth Avenue is an American luxury department store owned by the oldest commercial corporation in North America, the Hudson's Bay Company.  Its main flagship store is located on Fifth Avenue in Midtown Manhattan, New York City.

Congressional Leadership Fund: The Congressional Leadership Fund (CLF) is a Super PAC dedicated to electing Republicans to the U.S. House of Representatives.  The Super PAC, which is closely linked to former House Speaker John Boehner and House GOP leadership, was founded in 2011 and spent nearly $10 million in the 2012 cycle electing Republican candidates.  Following Boehner's resignation from the U.S. Congress and the election of Paul D. Ryan as Speaker of the House, Congressional Leadership Fund has become closely linked to Ryan.  The Super PAC is currently headed by Corwin Albert "Corry" Bliss who serves as Executive Director to both CLF and the linked American Action Network.

Make America Number 1: Make America Number 1 is a super PAC (political action committee) that supported the presidential campaigns of Ted Cruz and Donald Trump in the 2016 United States presidential election.  During the primary campaign, the super PAC was known as Keep the Promise I.  In the general election, it informally termed itself Defeat Crooked Hillary PAC.  The PAC is run by Rebekah Mercer, the second daughter of its largest donor Robert Mercer .

Question: Colbert Super PAC joked that funds raised would be used to purchase mementos from which luxury department store?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "pac_name": {
      "type": "string",
      "description": "The name of the Super PAC."
    },
    "fund_usage_category": {
      "type": "string",
      "description": "The category of expenses for which funds would be used, as joked by the PAC."
    },
    "item_type": {
      "type": "string",
      "description": "The type of item to be purchased with the funds."
    },
    "luxury_department_stores": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of luxury department stores from which items would be purchased."
    },
    "primary_department_store_for_mementos": {
      "type": "string",
      "description": "The specific luxury department store identified for mementos in the question's known answer."
    }
  },
  "required": [
    "pac_name",
    "fund_usage_category",
    "item_type",
    "luxury_department_stores",
    "primary_department_store_for_mementos"
  ],
  "additionalProperties": false
}
