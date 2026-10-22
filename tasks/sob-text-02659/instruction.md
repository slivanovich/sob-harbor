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
Paul Holloway: Paul Holloway (born 20 August 1949) is an Australian politician who represented the South Australian Branch of the Australian Labor Party in the South Australian House of Assembly seat of Mitchell from 1989 to 1993, and in the South Australian Legislative Council from 1995 to 2011.

Berthold Teusner: Berthold Teusner was an Australian politician who represented the South Australian House of Assembly seat of Angas from 1944 to 1970 for the Liberal and Country League.  He served as Speaker of the South Australian House of Assembly from 1956 to 1962.

Reg Hurst: Reginald Hurst was an Australian politician who represented the South Australian House of Assembly seat of Semaphore for the Australian Labor Party from 1964 to 1973.  He was Speaker of the South Australian House of Assembly for the Don Dunstan Labor government from 1970 to 1973.

Independent politician: An independent or nonpartisan politician is an individual politician not affiliated with any political party.  There are numerous reasons why someone may stand for office as an independent.

William Fisk (politician): William Fisk (17 July 1871 – 18 December 1940) was an Australian politician who represented the South Australian House of Assembly seat of Glenelg from 1938 to 1940 as an independent.

Gabe Bywaters: Gabriel Alexander (Gabe) Bywaters (died 2 November 2004) was an Australian politician who represented the South Australian House of Assembly seat of Murray from 1956 to 1968 for the Australian Labor Party.

Elder Whittle: Elder Whittle (8 January 1886 – 31 May 1965) was an Australian politician who represented the South Australian House of Assembly seat of Prospect from 1938 to 1944 and 1947 to 1953 for the Liberal and Country League.

Lyn Breuer: Lynette Ruth "Lyn" Breuer (born 28 March 1951), Australian politician, represented the electoral district of Giles in the South Australian House of Assembly for the Australian Labor Party from 1997 to 2014.  Breuer became Speaker of the South Australian House of Assembly for the Mike Rann and Jay Weatherill Labor governments following the 2010 election.  Breuer was the first female Speaker of the South Australian House of Assembly from 2010 to 2013.

Jules Langdon: Jules Langdon (31 May 1871 – 2 November 1942) was an Australian politician who represented the South Australian House of Assembly seat of Thebarton from 1938 to 1942 as an independent.

Bruce Eastick: Bruce Charles Eastick (born 25 October 1927) is a former South Australian politician and South Australian Leader of the Opposition from 1972 to 1975.  He was a member of the Liberal and Country League (LCL) which was succeeded in 1974 by the South Australian Division of the Liberal Party of Australia.  He represented the South Australian House of Assembly seat of Light from 1970 to 1993.

Question: Jules Langdon (31 May 1871 – 2 November 1942) was an Australian politician who represented the South Australian House of Assembly seat of Thebarton from 1938 to what year, as an independent or nonpartisan politician is an individual politician?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "politician_name": {
      "type": "string",
      "description": "The name of the politician."
    },
    "political_affiliation": {
      "type": "string",
      "description": "The political party or status of the politician."
    },
    "seat_represented": {
      "type": "string",
      "description": "The electoral seat represented by the politician."
    },
    "term_start_year": {
      "type": "integer",
      "description": "The start year of the politician's term."
    },
    "term_end_year": {
      "type": "integer",
      "description": "The end year of the politician's term."
    }
  },
  "required": [
    "politician_name",
    "political_affiliation",
    "seat_represented",
    "term_start_year",
    "term_end_year"
  ],
  "additionalProperties": false
}
