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
Women's Educational Equity Act: The Women's Educational Equity Act (WEEA) of 1974 is one of the several landmark laws passed by the United States Congress outlining federal protections against the gender discrimination of women in education.  WEEA was enacted as Section 513 of P.L. 93-380.  Introduced in the United States House of Representatives by Congresswoman Patsy Mink of Hawaiʻ i, the legislation was conceived and drafted by Arlene Horowitz, a staff assistant to the education subcommittee on which Mink served.  WEEA was intended to combat sex-role stereotyping in elementary and secondary schools.

Latin Americans: Latin Americans (Spanish: "latinoamericanos" , Portuguese: "latino-americanos" , French: "latino-américains" ) are the citizens of the Latin American countries and dependencies.  Latin American countries are multi-ethnic, home to people of different ethnic and national backgrounds.  As a result, some Latin Americans don't take their nationality as an ethnicity, but identify themselves with both their nationality and their ancestral origins.  Aside from the indigenous Amerindian (aka Native American) population, all Latin Americans or their ancestors immigrated within the past five centuries.  Latin America has the largest diasporas of Spaniards, Portuguese, Black Africans, Italians, Lebanese and Japanese in the world.  The region also has large German (second largest after the United States), French, Chinese and Jewish diasporas.

BALANCE Act: The Benefit Authors without Limiting Advancement or Net Consumer Expectations (BALANCE) Act of 2003 is a bill that would amend Title 17 of the United States Code, "to safeguard the rights and expectations of consumers who lawfully obtain digital entertainment."  The bill was proposed in the 108th Congress as H.R. 1066 by Congresswoman Zoe Lofgren (D-CA).  In the 109th Congress, the bill was reintroduced and is numbered H.R. 4536.  It has not been introduced into the 110th Congress.

National Dance Day: National Dance Day is on July 29 and was created by Nigel Lythgoe, the co-creator of "So You Think You Can Dance" and co-president of the Dizzy Feet Foundation.  It takes place in the United States on the last Saturday in July.  It was founded and officially recognized in 2010 when American congresswoman Eleanor Holmes Norton introduced a National Dance Day resolution to promote dance education and physical fitness.

Public Access to Public Science (PAPS) Act: The Public Access to Public Science (PAPs) public access to research funded by specific Federal agencies under the jurisdiction of the House Science committee, including National Aeronautics and Space Administration (NASA), the National Science Foundation (NSF), the National Institute of Standards and Technology (NIST) and the National Weather Service (NWS).  The Bill was introduced to the 113th Congress by Congressman Jim Sensenbrenner (R.-WI.)  and Congresswoman Eddie Bernice Johnson (D-TX) and was referred to the Subcommittee on Research and Technology December 13, 2013.  It has been endorsed by the Association of Public and Land-Grant Universities (APLU) and the Association of American Universities (AAU).

Meet the Ancestors: Meet the Ancestors aka Ancestors was a BBC Television documentary series that documented the archaeological excavation and scientific reconstruction of human remains.  The series was introduced by archaeologist Julian Richards and often included facial reconstructions by Caroline Wilkinson.

Argentines: Argentines, also known via circumlocution as Argentinians (Spanish: "argentinos" ; feminine "argentinas "), are the citizens of the Argentine Republic, or their descendants abroad.  Argentina is a multiethnic society, which means that it is home to people of many different ethnic backgrounds.  As a result, Argentines do not consider their nationality as an ethnicity but as a citizenship with various ethnicities.  Aside from the Indigenous population, nearly all Argentines or their ancestors immigrated within the past five centuries.  In fact, among countries in the world that have received the most immigrants in modern history, Argentina, with 6.6 million, ranks second to the United States (27 million), and ahead of other immigrant destinations such as Canada, Brazil, and Australia.

Early Childhood Education Act: The Early Childhood Education Act is the name of various landmark laws passed by the United States Congress outlining federal programs and funding for childhood education from pre-school through kindergarten.  The first such act was introduced in the United States House of Representatives by Congresswoman Patsy Mink of Hawaiʻ i in the 1960s.  The theory behind the act is that the years before a child reaches kindergarten are the most critical to influence learning.  Many children do not have access to early education before entering kindergarten.  The goal of the act is to provide a comprehensive set of services for children from birth until they enter kindergarten.

Patsy Mink: Patsy Matsu Takemoto Mink (竹本 まつ , Takemoto Matsu , December 6, 1927 – September 28, 2002) was an American politician from the U.S. state of Hawaii.  Mink was a third generation Japanese American and member of the Democratic Party.  She also was the Assistant Secretary of State for Oceans and International Environmental and Scientific Affairs.

Women's Progress Commemorative Commission: The Women's Progress Commemorative Commission is a U.S. bipartisan commission established pursuant to the Women's Progress Commemoration Act (Public Law 105-341, 1998-10-31) under President Bill Clinton.  The bill was introduced by Congresswoman Louise Slaughter and Senator Chris Dodd.  The commission was tasked with identifying and preserving websites significant to American women's history.  It was established in honor of the 150 year anniversary of the Seneca Falls Convention.  The commission's first meeting was held 2000-07-12 in Seneca Falls, New York to develop a scope.  Subsequent meetings, some sponsored by the National Park Service, included discussions regarding assistance from United State governors as well as problems with data collection.

Question: What nationality were the ancestors of the congresswoman who introduced WEEA?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "congresswoman_name": {
      "type": "string",
      "description": "The name of the congresswoman who introduced the act."
    },
    "act_introduced": {
      "type": "string",
      "description": "The name of the act introduced by the congresswoman."
    },
    "ancestor_nationality": {
      "type": "string",
      "description": "The nationality of the congresswoman's ancestors."
    },
    "generation_american": {
      "type": "string",
      "description": "The generation of American the congresswoman represents."
    }
  },
  "required": [
    "congresswoman_name",
    "act_introduced",
    "ancestor_nationality",
    "generation_american"
  ],
  "additionalProperties": false
}
