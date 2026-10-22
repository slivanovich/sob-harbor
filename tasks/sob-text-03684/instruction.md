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
List of Flip or Flop episodes: "Flip or Flop" is a television series airing on HGTV hosted by real estate agents and real life husband and wife Tarek El Moussa and Christina El Moussa.

Flip or Flop Vegas: Flip or Flop Vegas is a television series airing on HGTV hosted by real estate agent Aubrey Marunde and her husband/contractor Bristol.  It's a spin-off of the HGTV series "Flip or Flop".  It premiered on April 6, 2017, and was filmed in Las Vegas, Nevada.  On June 5, 2017, HGTV announced Flip or Flop Vegas would be renewed for a second season, with 16 episodes.

Flip or Flop Fort Worth: Flip or Flop Fort Worth is an upcoming television series airing on HGTV hosted by real estate agents Andy and Ashley Williams.  It will be a spin-off of the HGTV series "Flip or Flop".  It will premiere on November 2, 2017 and will be held in the Dallas metropolitan area, especially in Fort Worth.

Flip or Flop Atlanta: Flip or Flop Atlanta is a television series airing on HGTV hosted by real estate agents Ken and Anita Corsini.  It is a spin-off of the HGTV series "Flip or Flop".  It premiered on July 20, 2017 and is held in Atlanta, Georgia area.  On August 21, 2017, HGTV announced Flip or Flop Atlanta would be renewed for a second season, with 14 episodes, which is expected to debut in 2018.

Flip or Flop Paradise: Flip or Flop Paradise is an upcoming television series airing on HGTV hosted by real estate agents David and Chenoa Rivera.  It will be a spin-off of the HGTV series "Flip or Flop".  It will premiere in April 2018 and be held in Paradise, California.

Flip or Flop: Flip or Flop is a television series airing on HGTV hosted by real estate agents and real-life divorced couple Tarek and Christina El Moussa, and the original show in the "Flip or Flop" franchise.

Bristol Marunde: Bristol Marunde (born April 20, 1982) is an American mixed martial artist currently competing in the Welterweight division.  He was a contestant on "", and has competed for the UFC, Strikeforce, Titan FC, M-1 Global, and the Seattle Tiger Sharks of the International Fight League.

Flip or Flop Nashville: Flip or Flop Nashville is an upcoming television series airing on HGTV hosted by real estate agents DeRon Jenkins and Page Turner.  It will be a spin-off of the HGTV series "Flip or Flop".  It will premiere in February 2018 and be held in Nashville, Tennessee.

Selling LA: Selling Los Angeles is an American television series airing on HGTV. It features real estate brokers from Los Angeles in affluent areas who chronicle selling real estate to various clientele, some of whom are celebrities.  Season 1 premiered in October 13, 2011 has been renewed by the network HGTV for four seasons.  It is produced by Canadian production company, JV Productions Inc who also produces the show Selling New York in the same franchise.  The West Coast show was inspired by the East Coast affiliated show Selling New York and later inspired a European spin-offs on HGTV titled "Selling London".  There are several celebrity real estate professionals who have appeared on the show.

Flip or Flop Chicago: Flip or Flop Chicago is an upcoming television series airing on HGTV hosted by real estate agents Mark and Liz Perez.  It will be a spin-off of the HGTV series "Flip or Flop".  It will premiere in February 2018 and be held in Chicago, Illinois.

Question: Flip or Flop Vegas is a television series airing on HGTV hosted by real estate agent Aubrey Marunde and her husband, Bristol Marunde, an American mixed martial artist currently competing in which division?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "show_name": {
      "type": "string",
      "description": "The name of the television series."
    },
    "network": {
      "type": "string",
      "description": "The television network airing the series."
    },
    "host_details": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the host who is also a mixed martial artist."
        },
        "occupation": {
          "type": "string",
          "description": "The primary occupation of the host."
        },
        "mma_competition_division": {
          "type": "string",
          "description": "The division in which the mixed martial artist competes."
        }
      },
      "required": [
        "name",
        "occupation",
        "mma_competition_division"
      ],
      "additionalProperties": false
    },
    "co_host_name": {
      "type": "string",
      "description": "The name of the co-host."
    }
  },
  "required": [
    "show_name",
    "network",
    "host_details",
    "co_host_name"
  ],
  "additionalProperties": false
}
