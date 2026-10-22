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
Dewan Farid Gazi: Dewan Farid Gazi (1924 – 19 November 2010) was a Bangladeshi politician born in Devpara, Nabiganj Upazila, Sylhet.  He was elected as Member of Parliament for the Habiganj-1 (Nabigonanj-Bahuball) constituency in 1996, 2001 and 2008, representing the Awami League, of which he was an Advisory Council member.  He served as chairman of the Parliamentary Standing Committee on the Ministry of Primary and Mass Education.

Shaun Bailey: Shaun Bailey (born 1971 in North Kensington, London) is a British Afro-Caribbean youth worker and Conservative politician.  He stood for the London constituency of Hammersmith as a Conservative at the 2010 general election, and served as the Prime Minister's Special Adviser on Youth and Crime from 2010–2013.  In 2016, he was elected as a list candidate for the Conservative Party for the London Assembly.

Sir William Mount, 1st Baronet: Sir William Arthur Mount, 1st Baronet CBE (Hartley, Hampshire, 3 August 1866 – 8 December 1930) was a British Conservative Party politician and Member of Parliament for the Newbury constituency.  He is the great-grandfather of Conservative politician David Cameron, who was Prime Minister of the United Kingdom from 2010 to 2016.

Jim Prior: James Michael Leathes Prior, Baron Prior, PC (11 October 1927 – 12 December 2016), usually known as Jim Prior, was a British Conservative politician.  A member of parliament from 1959 to 1987, he represented the Suffolk constituency of Lowestoft until 1983 and then the renamed constituency of Waveney from 1983 to 1987, when he stood down from the House of Commons and was made a life peer.  He served in two Conservative Cabinets, and outside parliament was Chairman of the Arab British Chamber of Commerce from 1996 to 2004.

A. M. Raja (politician): A. M. Raja [Ayyampalayam Masagounder Rajagounder] is an Indian politician born in 1928 and former Member of the Legislative Assembly of Tamil Nadu.  He was elected to the Tamil Nadu legislative assembly as a Dravida Munnetra Kazhagam candidate from Bhavani constituency in 1967, and 1971 elections.  He was one of the first in his family to graduate from University (with a degree in Tamil History and Literature).  He spent much of his adult life in Madras where he owned construction companies that built bridges, and corporate buildings.  His lifelong interest in politics made him an important person at the statewide level especially with education reform and bringing access to higher education for all castes.  He had many advisory rolls at the state level in the DMK, and was a personal acquaintance of several Chief Ministers.  He has 3 children and 4 granddaughters.  The second oldest granddaughter is named Bhavani.

Vasant Parikh: Dr. Vasant Parikh (1929–2007) was an Indian politician born at Vadnagar in Mehsana district, Gujarat.  He was an eye surgeon by profession.  He was also a writer and Social worker.  He was a MLA in Gujarat legislative assembly during 1967-1972, winning from Kheralu assembly constituency as an independent candidate.  He is considered to be one of Narendra Modi's political gurus and is credited with coining the term 'One vote, One note'.  He established Karuna Setu trust along with his Late wife Ratnaprabha Maniar in 1984.

José Endundo Bononge: José Endundo Bononge (born 8 August 1943) is a politician born in Équateur province in the Democratic Republic of the Congo (DRC).  He is the chairman of the Christian Democratic Party ("Parti Démocrate Chrétien" - PDC) and was elected MP for the constituency of Mbandaka.

Antoinette Sandbach: Antoinette Geraldine Mackeson-Sandbach (born 15 February 1969), known in politics as Antoinette Sandbach, is a Conservative Party politician who was elected as the Member of Parliament for Eddisbury at the 2015 general election.  The following day, 8 May 2015, she resigned as the Welsh Assembly Member for the North Wales region.  having been elected as a North Wales regional Assembly Member at the May 2011 election.

Eddisbury (UK Parliament constituency): Eddisbury is a constituency in Cheshire represented in the House of Commons of the UK Parliament since 2015 by Antoinette Sandbach, a Conservative.

Nick Bourne: Nicholas Henry Bourne, Baron Bourne of Aberystwyth (born 1 January 1952) is a Welsh Conservative politician.  He served as the Leader of the Welsh Conservative Party and as a member of the National Assembly for Wales for the Mid and West Wales electoral region from August 1999 until May 2011.  During the 2011 assembly elections he unexpectedly lost his regional list seat, due to Conservative gains at constituency level.  He was elevated to the House of Lords in September 2013, and the following year, became a government whip.

Question:  When was the conservative politician born who's constituency is the Eddisbury?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "politician": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The full name of the politician."
        },
        "political_party": {
          "type": "string",
          "description": "The political party the politician belongs to."
        },
        "constituency": {
          "type": "string",
          "description": "The constituency the politician represents or represented."
        },
        "birth_date_full": {
          "type": "string",
          "description": "The full birth date of the politician."
        },
        "birth_year": {
          "type": "integer",
          "description": "The birth year of the politician."
        },
        "birth_month": {
          "type": "string",
          "description": "The birth month of the politician."
        },
        "birth_day": {
          "type": "integer",
          "description": "The birth day of the politician."
        }
      },
      "required": [
        "name",
        "political_party",
        "constituency",
        "birth_date_full",
        "birth_year",
        "birth_month",
        "birth_day"
      ],
      "additionalProperties": false
    },
    "query_context": {
      "type": "string",
      "description": "The specific context or criteria used to identify the politician in the question."
    },
    "final_answer": {
      "type": "string",
      "description": "The final answer to the question, which is the politician's birth date."
    }
  },
  "required": [
    "politician",
    "query_context",
    "final_answer"
  ],
  "additionalProperties": false
}
