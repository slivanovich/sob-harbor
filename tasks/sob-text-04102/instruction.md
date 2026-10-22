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
James Ronald: James Black Ronald (27 August 1861 – 27 July 1941) was an Australian politician.  Born in Scotland, he was educated at Edinburgh University and became a Presbyterian clergyman.  Migrating to Australia in 1888, he became a clergyman in Melbourne.  In 1901, he attempted to gain Protectionist endorsement to contest the Australian House of Representatives seat of Southern Melbourne; when he was unsuccessful, he turned to the Labor Party, which endorsed him instead.  Ronald won the seat, one of only two Victorian Labor members elected in the first federal election.  Ronald's seat was abolished in 1906, and he attempted to gain Labor endorsement to contest the neighbouring Melbourne Ports.  When this endorsement was given to James Mathews instead, Ronald contested the seat as an independent Labor candidate, but was unsuccessful.  He rejoined the ALP after the election, but was one of many Labor members to leave in 1916 over the issue of conscription, eventually ending up in the Nationalist Party.  Ronald died in 1941.

Massachusetts gubernatorial election, 1944: The 1944 Massachusetts gubernatorial election was held on November 7, 1944.  Democrat Maurice J. Tobin defeated Republican Horace T. Cahill, Socialist Labor candidate Henning A. Blomen, and Prohibition candidate Guy S. Williams.  Incumbent Governor Leverett Saltonstall did not run for reelection.  In the race for Lieutenant Governor, Republican Robert F. Bradford defeated Democrat John B. Carr, Socialist Labor candidate George L. McGlynn, and Prohibition candidate Alfred Erickson.

Division of Wentworth: The Division of Wentworth is an Australian electoral division in the state of New South Wales.  It was proclaimed in 1900 and was one of the original 75 federation divisions contested at the first federal election.  The division is named after William Charles Wentworth (1790–1872), an Australian explorer and statesman.  In 1813 he accompanied Blaxland and Lawson on their crossing of the Blue Mountains.

Elizabeth state by-election, 1994: A by-election was held for the South Australian House of Assembly seat of Elizabeth on 9 April 1994.  This was triggered by the resignation of former state Labor MHA Martyn Evans, who moved to the federal seat of Bonython at the 1994 by-election.  The seat, created at the 1969 redistribution and first contested at the 1970 state election, was held by Labor from 1970 until 1984, when Evans won it as an independent Labor candidate.  In 1993, he rejoined the Labor Party.

Jack Cremean: John Lawrence "Jack" Cremean (26 January 1907 – 11 August 1982) was an Australian politician.  Born in Melbourne, he was educated at Catholic schools before becoming a clerk.  He was secretary to federal Labor minister Arthur Calwell from 1942–45, secretary of the Fire Brigades Employees Union 1945-48, and also sat on Richmond City Council.  In 1945, Cremean's brother Bert Cremean died after surgery, and Jack was elected as a Labor member of the Victorian Legislative Assembly for Clifton Hill in the resulting by-election, where he remained until 1949.  In that year, he transferred to federal politics, winning the new seat of Hoddle in the Australian House of Representatives.  In 1955, Cremean was one of seven MPs who left the ALP and formed the Australian Labor Party (Anti-Communist), the precursor to the Democratic Labor Party.  Cremean's seat of Hoddle was abolished for the 1955 election, so he contested its successor, Scullin, as an Anti-Communist, but was defeated by the Labor candidate, Ted Peters, the member for Burke.  Cremean died in 1982.

Dale state by-election, 1988: A by-election for the seat of Dale in the Legislative Assembly of Western Australia was held on 7 May 1988.  It was triggered by the resignation of Cyril Rushton (the sitting Liberal member and a former deputy premier) on 25 February 1988.  The seat was retained by the Liberal Party, with their candidate, Fred Tubby, winning 59.1 percent of the two-candidate-preferred (2CP) vote.  The Labor Party did not stand at the election, despite having lost the seat by less than 400 votes at the 1986 state election.  A former Labor candidate, Michael Marsh, won 40.9 percent of the 2CP vote standing as an independent.

Amha Selassie: Amha Selassie, GCMG, GCVO, GBE (27 July 1914 – 17 February 1997) was the last reigning monarch of Ethiopia.  First proclaimed Emperor during the unsuccessful coup attempt by the Imperial Guards against his father Haile Selassie I in December 1960, he initially went along with this proclamation under duress.  The coup collapsed within days and the Emperor Haile Selassie was restored.  Amha Selassie was again proclaimed on the deposition of his father by the Derg on 12 September 1974, but he never accepted this proclamation as legitimate, and in any case this brief reign was ended with the abolition of the Ethiopian monarchy in March 1975.  He was again proclaimed in exile on 8 April 1989.  This time he sanctioned the proclamation and accepted its legitimacy.

Bairnsdale: Bairnsdale ( , locally [ˈbeːnzdæɪl] ) is a city in East Gippsland, Victoria, Australia.  The estimated population of Bairnsdale urban area was 14,271 at June 2015.  The city is a major regional centre of eastern Victoria along with Traralgon and Sale and the commercial centre for the East Gippsland region and the seat of local government for the Shire of East Gippsland.  Bairnsdale was first proclaimed a shire on 16 July 1868 and it was proclaimed as a city on 14 July 1990.

George Newhouse: George Newhouse is an Australian human rights lawyer and a former local councillor.  In addition to his private practice, Newhouse is currently an Adjunct Professor of Law at Macquarie University.  He was the Mayor of Waverley in the eastern suburbs of Sydney from 2006 to 2007, and the Labor candidate for the seat of Wentworth at the 2007 Australian federal election.  Newhouse is the principal solicitor of the National Justice Project, a human rights and social justice legal service.  He is also a certified practicing accountant (CPA).

Joe Gander: Joseph Herbert Gander (1888 – 22 November 1954) was an Australian politician.  Born in Dubbo, New South Wales, Australia, he received a primary education before becoming a billiardmaker and public servant.  He was involved in local politics in Sydney, being elected to Newtown Council.  In 1931, he was elected to the Australian House of Representatives as the member for Reid, a member of the Lang Labor party; he defeated Percy Coleman, the Labor member.  When, in 1936, the Lang Labor members rejoined the Labor party, Gander was one of them.  However, in 1940, the Labor Party split again, and Gander was among the members to join the Langite Australian Labor Party (Non-Communist).  However, he was defeated in the election of that year by the federal Labor candidate, Charles Morgan, and retired from politics, returning to public service.  Gander died in 1954.

Question: George Newhouse was the Labor candidate for the seat that was first proclaimed in what year?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "candidate_name": {
      "type": "string",
      "description": "The name of the political candidate."
    },
    "electoral_division": {
      "type": "string",
      "description": "The name of the electoral division the candidate ran for."
    },
    "proclamation_year": {
      "type": "integer",
      "description": "The year the electoral division was first proclaimed."
    },
    "country": {
      "type": "string",
      "description": "The country where the electoral division is located."
    }
  },
  "required": [
    "candidate_name",
    "electoral_division",
    "proclamation_year",
    "country"
  ],
  "additionalProperties": false
}
