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
Bill Gurley: Bill Gurley (born May 10, 1966) is a general partner at Benchmark, a Silicon Valley venture capital firm in Menlo Park, California.  He is listed consistently on the Forbes Midas List and is considered one of technology’s top dealmakers.

James D. Robinson IV: James D. Robinson IV (also known as James D. Robinson, or Jim Robinson, born June 13, 1962) is an American venture capitalist and entrepreneur.  Robinson has been a director of many private and several public companies.  He has been listed on the Forbes Midas List of top venture capital investors, and the Institutional Investor Fintech 35.

Peter Thiel: Peter Andreas Thiel ( ; born October 11, 1967) is an American entrepreneur, venture capitalist, philanthropist, political activist, and author.  He was ranked No. 4 on the "Forbes" Midas List of 2014, with a net worth of $2.2 billion, and No. 246 on the "Forbes" 400 in 2016, with a net worth of $2.7 billion.

Jenny Lee (venture capitalist): Jenny Lee (born 1972) is a Singaporean venture capitalist.  A managing partner of GGV Capital based in Shanghai, Lee was No. 10 and the first woman venture capitalist in the top 10 of Forbes Midas List 2015.

Theresia Gouw: Theresia Gouw is an entrepreneur and venture capital investor in the technology sector.  She worked at Bain & Company, Release Software and Accel Partners before co-founding Aspect Ventures, a female-led VC firm, in 2014.  Gouw was named one of the 40 most influential minds in tech by TIME Magazine.  and has been recognized six times on the Forbes Midas List as one of the "world's smartest tech investors".

Peter Fenton (venture capitalist): Peter Fenton (born July 1972) is an American venture capitalist based in Silicon Valley.  He is a general partner at Benchmark, a venture capital firm.  Fenton has steadily worked his way up the Forbes Midas List of the 100 top technology investors, starting at no. 94 in 2007, then rising to no. 62 in 2008 and no. 50 in 2009.  Fenton was ranked no. 4 when Forbes resumed publishing its Midas List in 2011 and was described as the “most productive venture capitalist on our list.”  In 2012, Fenton was ranked no. 5 on the Forbes Midas List and was no. 2 in 2015.

Thiel Foundation: The Thiel Foundation is a private foundation created and funded by billionaire Peter Thiel, known as a co-founder of PayPal and early investor in Facebook.

Josh B. Stein: Josh Stein (born May 3, 1973) is an American businessman and venture capitalist.  He is a partner at DFJ and was featured in the Forbes Midas List in 2013, 2014 and 2015 in recognition of his accomplishments as an investor.  Stein has been a board member and investor in Box (company), Chartbeat, LendKey, SugarCRM, and Talkdesk—and led Box’s first round of institutional investment.

Kevin Harvey (venture capitalist): Kevin Harvey is a founding member of and general partner at Benchmark, a Silicon Valley venture capital firm.  He was ranked No. 27 on the 2011 Forbes Midas List and was No. 59 in 2012.

Matt Cohler: Matt Cohler (born March 27, 1977) is an American venture capitalist based in Silicon Valley.  He worked as Vice President of Product Management for Facebook until June 2008 and is currently a general partner at Benchmark.  Cohler was named to the 2012 Forbes Midas List of top technology investors.  Cohler made the Forbes 'America's 40 Richest Entrepreneurs Under 40' list in 2015.

Question: The Thiel Foundation was created and funded by what philanthropist who was ranked No. 4 on the Forbes Midas List of 2014?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "philanthropist": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the philanthropist."
        },
        "roles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of roles or professions held by the individual."
        },
        "forbes_midas_list_rankings": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "year": {
                "type": "integer",
                "description": "The year of the Forbes Midas List ranking."
              },
              "rank": {
                "type": "integer",
                "description": "The rank on the Forbes Midas List for that year."
              }
            },
            "required": [
              "year",
              "rank"
            ],
            "additionalProperties": false
          },
          "description": "A list of Forbes Midas List rankings for the individual."
        }
      },
      "required": [
        "name",
        "roles",
        "forbes_midas_list_rankings"
      ],
      "additionalProperties": false
    },
    "foundation": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the foundation."
        },
        "creator_name": {
          "type": "string",
          "description": "The name of the person who created and funded the foundation."
        }
      },
      "required": [
        "name",
        "creator_name"
      ],
      "additionalProperties": false
    },
    "question_details": {
      "type": "object",
      "properties": {
        "target_midas_list_year": {
          "type": "integer",
          "description": "The specific year of the Forbes Midas List mentioned in the question."
        },
        "target_midas_list_rank": {
          "type": "integer",
          "description": "The specific rank on the Forbes Midas List mentioned in the question."
        }
      },
      "required": [
        "target_midas_list_year",
        "target_midas_list_rank"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "philanthropist",
    "foundation",
    "question_details"
  ],
  "additionalProperties": false
}
