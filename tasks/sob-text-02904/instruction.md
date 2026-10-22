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
Live at Sir George Williams University: Live at Sir George Williams University is a live album by Dave Van Ronk, re-released in 1997.  This recording was done live as a joint concert of the folk music societies of McGill and Sir George Williams Universities in 1967, at Sir George Williams University, in Montreal, Quebec, Canada, and also featured Rev. Gary Davis on the same bill.

Sir George Simpson (condominiums): Le Sir George Simpson (also known as "Sir George Simpson") is a condominium building located at 1485 Sherbrooke Street West in the Golden Square Mile district of Montreal, Quebec, Canada.  Construction officially started in 2006 and the building was completed in 2010.  The Sir George Simpson project was developed by developer Rene Lépine Sr., head of Groupe Lépine.

George Coles (entrepreneur): Sir George James Coles, CBE (28 March 1885 – 4 December 1977) was an Australian entrepreneur.  He was the founder of what was to become the Coles Group shopping empire, at one time the largest chain store group in Australia.

Sir George Williams affair: The Sir George Williams affair (also referred to as "The Sir George Williams Computer Riot") was a 1969 event at Sir George Williams University in Montreal, Quebec, Canada, now a part of Concordia University.  It was the largest student occupation in Canadian history.

Cullum Welch: Lieutenant-Colonel Sir George James Cullum Welch, 1st Baronet, {'1': ", '2': ", '3': ", '4': "} (20 October 1895 - 28 July 1980), commonly known as Sir Cullum Welch, was a British Army officer, businessman, and member of the City of London Corporation, who served as Lord Mayor of London between 1956 and 1957.

George Frampton: Sir George James Frampton, RA (18 June 1860 – 21 May 1928) was a notable British sculptor and leading member of the New Sculpture movement.

Coles Group: Coles Group Limited (formerly Coles Myer Limited) was an Australian public company that operated numerous retail chains.  It was Australia's second-largest retailer, behind Woolworths Limited.  It was acquired by Western Australian public company Wesfarmers, with transfer of ownership on 23 November 2007.  The corporate operations ceased at head office in Melbourne from that point, now based at Wesfarmers head office in Perth.

George Giffard: General Sir George James Giffard (27 September 1886 – 17 November 1964) was a British military officer, who had a distinguished career in command of African troops in World War I, rising to command an Army Group in South East Asia in World War II.

George James Turner: Sir George James Turner (1798–1867) was an English barrister, politician and judge.  He became a Lord Justice of Appeal in chancery,

Sir George Clark, 2nd Baronet: Sir George Ernest Clark, 2nd Baronet, DL (1882–1950) was the son of Sir George Clark, 1st Baronet of Dunlambert, Belfast.  Sir George was educated at Cambridge and was a naval architect.  He was Honorary Colonel of the 3rd Searchlight Regiment, Royal Artillery (Territorial Army) between 1939 and 1946 and a High Sheriff of Counties Antrim (1940) and Down (1941).

Question: What type of company did Sir George James Coles found? 

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "founder_name": {
      "type": "string",
      "description": "The full name of the founder."
    },
    "company_name": {
      "type": "string",
      "description": "The name of the company founded."
    },
    "company_type": {
      "type": "string",
      "description": "The type of company founded."
    },
    "company_industry": {
      "type": "string",
      "description": "The industry in which the company operates."
    }
  },
  "required": [
    "founder_name",
    "company_name",
    "company_type",
    "company_industry"
  ],
  "additionalProperties": false
}
