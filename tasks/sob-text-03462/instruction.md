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
Ezechiel Joseph: Ezechiel Joseph is a Saint Lucian politician who represented the constituency of Babonneau for the United Workers Party from 2006 to 2011.  Joseph won the seat at the general election held on 11 December 2006.  In the government of Prime Minister John Compton, sworn in on 19 December 2006, he was appointed Minister for Agriculture, Forestry and Fisheries.  Joseph lost the seat at the general election held on 28 November 2011.  He was sworn in as an opposition member of the Senate on 5 January 2012.  He resigned from the Senate effective 31 December 2015.  Joseph regained the Babonneau seat in the general election held on 6 June 2016.

South Norfolk by-election: South Norfolk by-election may refer to one of three by-elections held for the British House of Commons constituency of South Norfolk:

South Norfolk Historic District: South Norfolk Historic District is a national historic district located at Chesapeake, Virginia.  The district encompasses 668 contributing buildings and 1 contributing site in what started as a planned community of Norfolk County, Virginia and grew to become an independent city.  South Norfolk was never part of Norfolk, Virginia.  In fact, the two cities are separated by the Eastern Branch of the Elizabeth River.  South Norfolk is a primarily residential district that was developed between 1890 and 1930.  The dwellings include representative examples of the Colonial Revival, Stick Style, and Queen Anne styles.  The district also includes several churches, a school, a park, and a small local business district.

William Broderick: William Joseph Broderick (20 May 1877 – 1 June 1957) was an Irish politician and farmer.  He was first elected to Dáil Éireann as a Cumann na nGaedheal Teachta Dála (TD) for the Cork East constituency at the 1932 general election.  He was re-elected at the 1933 general election but lost his seat at the 1937 general election.  At the 1938 general election, he was elected as a Fine Gael TD for the Waterford constituency.  At the 1943 general election, he moved to the Cork South-East constituency, and was re-elected for this constituency at the 1944 general election.  He did not contest the 1948 general election.

John Sandeman Allen (Birkenhead West MP): John Sandeman Allen (30 May 1892 – 29 September 1949) was a British Conservative Party politician.  He was a Member of Parliament (MP) for Birkenhead West from 1931 to 1945.  At the 1945 general election he stood in the previously Conservative-held South Norfolk constituency, but the seat was won by the Labour candidate.

John Sandeman Allen (Liverpool West Derby MP): Sir John Sandeman Allen (26 September 1865 – 3 June 1935) was a British Conservative Party politician.  He was a Member of Parliament (MP) for Liverpool West Derby from 1924 until he died in office in 1935.

Liverpool West Derby by-election, 1935: The Liverpool West Derby by-election of 1935 was held on 6 July 1935.  The by-election was held due to the death of the incumbent Conservative MP, John Sandeman Allen.  It was won by the Conservative candidate David Maxwell Fyfe.

United Kingdom general election, 1931: The United Kingdom general election held on Tuesday 27 October 1931 saw a landslide election victory for the National Government which had been formed two months previously after the collapse of the previous Labour government.  The bulk of the National Government's support came from the Conservative Party, and the Conservatives won 470 seats.  The Labour party suffered its greatest defeat, losing four out of five seats compared with the previous election.  The Liberal Party, split into three factions, continued to shrink and the Liberal National faction never reunited.  Ivor Bulmer-Thomas said the results "were the most astonishing in the history of the British party system".  It was the last election where one party (the Conservatives) received an absolute majority of the votes cast and the last UK general election not to take place on a Thursday.

United Kingdom general election, 1945: The United Kingdom general election of 1945 was held on 5 July 1945, with polls in some constituencies delayed until 12 July and in Nelson and Colne until 19 July, because of local wakes weeks.  The results were counted and declared on 26 July, to allow time to transport the votes of those serving overseas.

South Norfolk by-election, 1955: The South Norfolk by-election, 1955 was a by-election held on 13 January 1955, for the British House of Commons constituency of South Norfolk.

Question: John Sandeman Allen was part of the South Norfolk constituency in the UK general election held on what date?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "politician_name": {
      "type": "string",
      "description": "The name of the politician."
    },
    "constituency": {
      "type": "string",
      "description": "The constituency the politician was associated with."
    },
    "election_details": {
      "type": "object",
      "properties": {
        "election_year": {
          "type": "integer",
          "description": "The year of the general election."
        },
        "election_date": {
          "type": "string",
          "format": "date",
          "description": "The specific date the general election was held."
        }
      },
      "required": [
        "election_year",
        "election_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "politician_name",
    "constituency",
    "election_details"
  ],
  "additionalProperties": false
}
