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
Macanese legislative election, 2017: The 2017 Macanese general election took place on 17 September 2017 according to the provisions of the Basic Law of Macau.  Out of a total of 33 seats, 14 were directly elected by universal suffrage under the highest averages method, while 12 were voted on from the Functional constituency, and 7 from nomination by the Chief Executive.

Macanese legislative election, 2013: The 2013 Macanese general election took place on 15 September 2013 according to the provisions of the Basic Law of Macau.  This election was the first of its kind succeeding the reform of the Legislative Assembly that created four new seats; two new geographical constituency seats and two new functional constituency seats.  Out of a total of 33 seats, 14 were elected by universal suffrage under the highest averages method, while 12 were voted on from the Functional constituency, and 7 from nomination by the Chief Executive.

Co-operative Commonwealth Federation (Ontario): The Co-operative Commonwealth Federation (Ontario) – The Farmer-Labor Party of Ontario, or more commonly known as the Ontario CCF, was a democratic socialist political party that existed from 1932 to 1961.  It was the provincial wing of the national CCF.  The party had no leader in the beginning, and was governed by a provincial council and executive.  The party first Member of the Legislative Assembly (MLA) was elected by voters in the 1934 Ontario general election.  In the 1937 general election, no CCF members were elected to the Ontario Legislature.  In 1942, the party elected Toronto lawyer Ted Jolliffe as its first leader.  He led the party to within a few seats of forming the government in the 1943 general election; instead, it formed the Official Opposition.  In that election, the first two women were elected as CCFers to the Ontario Legislature, Agnes Macphail and Rae Luckock.  The 1945 election was a setback, as the party lost most of its seats in the Legislature, including Jolliffe's seat.  The party again became the Official Opposition after the 1948 general election, and defeated the Conservative premier George Drew in hisseat, when Bill Temple unexpectedly won in the High Park constituency.  The middle and late 1940s were the peak years for the Ontario CCF.  After that time, its electoral performances were dismal, as it was reduced to a rump of two seats in the 1951 election, three seats in the 1955 election, and five seats in the 1959 election.  Jolliffe stepped down as leader in 1953, and was replaced by Donald C. MacDonald.

Members of the 32nd Dáil: This is a list of the members elected to the 32nd Dáil Éireann, the lower house of the Oireachtas (legislature) of Ireland.  These TDs (members of parliament) were elected at the 2016 general election on 26 February.  That general election took place throughout the state to elect 158 members of Dáil Éireann, a reduction of 8 from the prior number of 166.  This followed the passing of the Electoral (Amendment) (Dáil Constituencies) Act 2013.

Blackpool Borough Council election, 2015: The 2015 Blackpool Borough Council election took place on 7 May 2015 to elect members of Blackpool Borough Council in England.  All 21 wards of 2 seats each on the council were contested with newly elected members next due to serve a four-year term and next contest their seats in 2019.  The council is made up oThis election took place on the same day as other local elections as well as the 2015 UK General Election.

Northampton Borough Council election, 2015: The 2015 Northampton Borough Council election took place on 7 May 2015 as a four-yearly public decision to elect all members of the council.  This took place on the same day as other local elections and the United Kingdom general election, 2015 - when there is a general election on the same day as the local elections, turnout across the country is with fewer than 1% of exceptions higher than if there is no general election.  Voters could cast between one and three votes depending on the number of councillors per ward.

John Keating (Irish politician): John Keating (2 August 1869 – 8 July 1956) was an Irish politician and farmer.  Keating was first elected to Dáil Éireann as a National League Party Teachta Dála (TD) for the Wexford constituency at the June 1927 general election.  He lost his seat at the September 1927 general election but was elected as a Cumann na nGaedheal TD at the 1932 general election and was re-elected at the 1933 general election.  He was elected as a Fine Gael TD at the 1937 and 1938 general elections.  He lost his seat at the 1943 general election but was re-elected at the 1944 general election.  He stood as an independent candidate at the 1948 general election but did not retain his seat.

Northwest Territories general election, 1975: The Northwest Territories general election, 1975 was the 13th general election in the Northwest Territories history.  The election took place on March 10, 1975.  This was the first general election since 1902 that all the members of the assembly were elected.  Fifteen members were elected to the Legislative Council.

Indonesian legislative election, 1955: Indonesia's first parliamentary general election was held on 29 September 1955.  The candidates were seeking to be elected to the 257-seat People's Representative Council, which would replace the existing provisional legislature.  Despite hopes that the election would bring about political stability, the legislature elected only lasted four years before being dissolved by presidential decree.

Elections in Macau: Macau elects on national level a legislature.  The Legislative Assembly is made up of 33 members, of whom 14 are elected by popular vote and proportional representation, 12 elected from functional constituencies and 7 appointed by the Chief Executive.

Question: When the Macanese general election took place, was the legislature elected on national level?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "is_national_level_election": {
      "type": "boolean",
      "description": "Indicates whether the legislature elected was on a national level."
    },
    "election_type": {
      "type": "string",
      "description": "The type of election that took place."
    },
    "location": {
      "type": "string",
      "description": "The geographical location where the election occurred."
    },
    "legislature_details": {
      "type": "object",
      "properties": {
        "legislature_name": {
          "type": "string",
          "description": "The name of the legislature."
        },
        "total_seats": {
          "type": "integer",
          "description": "The total number of seats in the legislature."
        },
        "seat_allocation_methods": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "method": {
                "type": "string",
                "description": "The method by which seats are allocated."
              },
              "number_of_seats": {
                "type": "integer",
                "description": "The number of seats allocated by this method."
              }
            },
            "required": [
              "method",
              "number_of_seats"
            ],
            "additionalProperties": false
          },
          "description": "A breakdown of how seats in the legislature are allocated."
        }
      },
      "required": [
        "legislature_name",
        "total_seats",
        "seat_allocation_methods"
      ],
      "additionalProperties": false
    },
    "source_of_national_level_information": {
      "type": "string",
      "description": "The specific context section confirming the national level election."
    }
  },
  "required": [
    "is_national_level_election",
    "election_type",
    "location",
    "legislature_details",
    "source_of_national_level_information"
  ],
  "additionalProperties": false
}
