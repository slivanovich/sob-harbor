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
Scout Association of Hong Kong: The Scout Association of Hong Kong () is the largest scouting organisation in Hong Kong.  Scout training was first introduced in Hong Kong in 1909 and 1910 by the Protestant based Boys' Brigade, Chums Scout Patrols and British Boy Scouts.  The Catholic St. Joseph's College, formed its Boy Scout Troop in 1913, and registered with the Boy Scouts Association of the United Kingdom in 1914.  The Boy Scouts Association formed its Hong Kong Local Association in July 1915 which became its Hong Kong Branch.  After changes to the name of the United Kingdom organisation in 1967, the branch name was changed to The Scout Association Hong Kong Branch.  In 1977 The Scout Association of Hong Kong was constituted as an autonomous association and successor to The Scout Association's Hong Kong Branch and became the 111th member of the World Organization of the Scout Movement (WOSM) in 1977.

Hong Kong Chief Executive election, 2012: The 2012 Hong Kong Chief Executive election was held on 25 March 2012 to select the Chief Executive of Hong Kong (CE), the highest office in the Hong Kong Special Administrative Region (HKSAR), by a 1,193-member Election Committee (EC) to replace the incumbent Chief Executive.  Won by the former non-official convenor of the Executive Council of Hong Kong Leung Chun-ying, the election was the most competitive as it was the first election with more than one pro-Beijing candidate since the 1996 election.

Right of abode in Hong Kong: The right of abode in Hong Kong is the right to legally reside in Hong Kong without any limit or condition of stay being imposed by the Hong Kong Immigration Department.  As the People's Republic of China stood to resume sovereignty over Hong Kong from the United Kingdom, the nationality of Hong Kong people as well as their right of abode in the territory was formalised prior to the 1997 handover.  Since Hong Kong has never been an independent country, there is no provision for its own citizenship status.  Hong Kong Permanent Resident is the legal status for those who have the right of abode in Hong Kong, which is the "de-facto" citizenship status in Hong Kong.  Most citizen rights in Hong Kong (such as the right to vote) are granted to all permanent residents, while some (such as the right to hold a HKSAR passport, or becoming a high-rank public officer such as the Chief Executive) are restricted to permanent residents who are also Chinese citizens.

5th Legislative Council of Hong Kong: The Fifth Legislative Council of Hong Kong is the former meeting of the legislative branch of the Hong Kong Special Administrative Region Government.  The membership of the LegCo is based on the 2012 election.  The term of the session is from 1 October 2012 to 30 September 2016, during the term in office of the Chief Executive Leung Chun-ying.  Due to the new arrangements agreed in a contentious LegCo vote in 2010, the session consists of the new total of 70 seats in LegCo, ten more than previously, with 35 members elected in geographical constituencies through direct elections, and 35 members in functional constituencies, in which five District Council (Second) functional constituency seats each represent all 18 District Councils of Hong Kong voted for by all resident voters in Hong Kong (who did not have a vote in any other functional constituency).  The Democratic Alliance for the Betterment and Progress of Hong Kong remained the largest party while the pan-democrats secured the one-third crucial minority.  Notable new members of the LegCo members include Gary Fan from the new established party Neo Democrats and first openly gay councillor, People Power's Ray Chan Chi-chuen.

Hong Kong local elections: The Hong Kong local elections () are elections in Hong Kong for the members of District Councils (District Boards before 1997).  First held in 1982, the elections are held at 4-year intervals when the 18 district councils, totalling 412 elected members (as at 2011, up from 405 elected members in 2007) require renewal.  The last election was on 22 November 2015.  The elections are conducted by simple plurality, with an average constituency having a population of around 17,000 people.  The councils range from 11 to 37 elected members, depending on that district's population.  The Chief Executive may appoint up to a prescribed number of members to each council, totalling 102.  The councils in the New Territories also have 27 "ex officio" members who are chairpersons of rural committees.

Chief Executive of Hong Kong: The Chief Executive of the Hong Kong Special Administrative Region is the head and representative of the Hong Kong Special Administrative Region and head of the Government of Hong Kong.  The position was created to replace the Governor of Hong Kong, the representative of the Monarch of the United Kingdom during British rule.  The office, stipulated by the Hong Kong Basic Law, formally came into being on 1 July 1997 when the sovereignty of Hong Kong was transferred from the United Kingdom to the People's Republic of China.

Lau Kong-wah: Lau Kong-wah, JP (born 22 June 1957, Hong Kong), also called Ray Lau, is a former member of the Legislative Council of Hong Kong.  On 14 October 2008, Donald Tsang, the Chief Executive of Hong Kong, made Lau a member of the Executive Council of Hong Kong, filling the vacancy left by the resignation of Jasper Tsang upon the latter becoming President of the Legislative Council of Hong Kong.  By the end of June 2012, Lau ceased to be a member of the Executive Council of Hong Kong.

Sha Tin Community Network: Sha Tin Community Network () is a localist political group in Hong Kong.  It was formed by a group of Sha Tin residents and former member of the Chinese University of Hong Kong Local Society was inspired by 2014 Occupy protests.  It uses "pragmatism, locality and democracy" and aimed to win back the District Councils from the pro-Beijing camp.  It won a seat in the Hong Kong district council elections, 2015.

Governor of Hong Kong: The Governor of Hong Kong was the representative in Hong Kong of the British Crown from 1843 to 1997.  In this capacity, the governor was president of the Executive Council and Commander-in-Chief of the British Forces Overseas Hong Kong.  The governor's roles were defined in the Hong Kong Letters Patent and Royal Instructions.  Upon the end of British rule and the transfer of Hong Kong to the People's Republic of China in 1997, most of the civil functions of this office went to the Chief Executive of Hong Kong, and military functions went to the Commander of the People's Liberation Army Hong Kong Garrison.

Hong Kong local elections, 1982: The 1982 Hong Kong local elections, commonly known as 1982 Hong Kong District Board elections, were the first ever local elections under the new creation of 18 district boards.

Question: During the Hong Kong local elections, the Chief Executive may appoint up to how many members to each council?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_type": {
      "type": "string",
      "description": "The entity performing the action."
    },
    "action": {
      "type": "string",
      "description": "The action being described."
    },
    "election_type": {
      "type": "string",
      "description": "The type of election where the appointments occur."
    },
    "maximum_appointed_members_total": {
      "type": "integer",
      "description": "The total maximum number of members the Chief Executive may appoint across all councils."
    }
  },
  "required": [
    "entity_type",
    "action",
    "election_type",
    "maximum_appointed_members_total"
  ],
  "additionalProperties": false
}
