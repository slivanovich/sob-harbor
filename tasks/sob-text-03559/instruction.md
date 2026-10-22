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
Eric Knowles: Eric Knowles (born 19 February 1953 in Nelson, Lancashire, England) is a British antiques expert whose main interest is in ceramics.

Marsha Bemko: Marsha Bemko is an American television producer.  She is the executive producer of the PBS series "Antiques Roadshow".  In addition to "Antiques Roadshow", Bemko is also executive producer for PBS's antiques series "Market Warriors".

Flog It!: Flog It!  is a television series broadcast on the BBC since 27 May 2002, presented by Paul Martin (although the first five episodes were presented by Mark Harnden).  The show follows a similar formula to "Antiques Roadshow", with members of the public bringing their antiques to be viewed and valued by a team of experts.  However, unlike "Antiques Roadshow", they are then given the option to sell their items at an auction.

Going for a Song: Going for a Song was an antiques quiz show broadcast by the BBC from 1965-1977.  It was a forerunner of the "Antiques Roadshow".  The original television series was hosted by presenter Max Robertson, with Arthur Negus appearing as the resident expert and antique valuer.  Revivals of the programme were made in the 1990s, hosted by Michael Parkinson (1995-1999), and Anne Robinson (2000), with Eric Knowles as the resident antiques expert, and in 2001 by Michael Aspel.

Antiques Roadshow (U.S. TV series): Antiques Roadshow is an American television program broadcast on Public Broadcasting Service (PBS) Public television stations.  The series features local antiques owners who bring in items to be appraised by experts.  Provenance, history, and value of the items are discussed.  Based on the original British "Antiques Roadshow" – which premiered in 1979 – the American version first aired in 1997.  When taping locations are decided, they are announced on the series website raising the profile of various small to mid-size cities, such as Billings, Montana; Biloxi, Mississippi; Bismarck, North Dakota; Chattanooga, Tennessee; Hot Springs, Arkansas; and Rapid City, South Dakota.  "Antiques Roadshow" has been nominated 14 times for a Primetime Emmy.

Belvoir Media Group: Belvoir Media Group LLC is publisher of newsletters, magazines and websites.  Based in Norwalk, Connecticut, its titles include "MaryJamesFram"; "Antiques Roadshow Insider," a newsletter licensed by WGBH-TV, producer of "Antiques Roadshow"; and "Practical Sailor".

John Sandon: John Sandon (born 1959 in Worcester) is a British expert and prolific author on ceramics and glass.  He is best known as an expert on the BBC's "Antiques Roadshow", which he joined in 1985.

Antiques Roadshow: Antiques Roadshow is a British television show in which antiques appraisers travel to various regions of the United Kingdom (and occasionally in other countries) to appraise antiques brought in by local people.  It has been running since 1979, based on a 1977 documentary series.  The series has spawned versions in other countries with the same TV format, including Canada and the United States.  s of 2017 it is presented by Fiona Bruce and is in its 39th series.

Antikrundan: Antikrundan is the Swedish version of the original BBC format "Antiques Roadshow".  The show visits different locations in Sweden and lets people bring their antiques to be valued by experts.  It remains popular and often has more than 2 million viewers.  The 19th season was shown in 2009.  Most of the experts have been with the programme since the start.  Jesper Aspegren was the original host.  He left in 1999 and was succeeded by Anne Lundberg.

Lara Spencer: Lara Christine Von Seelen (known professionally as Lara Spencer) (born June 19, 1969) is an American television presenter.  She is best known for being the co-anchor for ABC's "Good Morning America".  She is also a correspondent for "Nightline" and ABC News.  Previously, she was the host of the syndicated entertainment newsmagazine "The Insider" from 2004 to 2011, and was a regular contributor to CBS's "The Early Show".  Before then, she was the national correspondent for "Good Morning America" and spent several years as a lifestyle reporter for WABC-TV.  She also hosted "Antiques Roadshow" on PBS for the 2004 and 2005 seasons, and "Antiques Roadshow FYI", a spin-off of "Antiques Roadshow", during 2005.  She hosts the show "Flea Market Flip" on both HGTV and the Great American Country channel.

Question: hich of Anne Robinson's Antiques Roadshow's co-workers has a main interest of ceramics?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "co_worker_name": {
      "type": "string",
      "description": "The name of Anne Robinson's co-worker."
    },
    "co_worker_main_interest": {
      "type": "string",
      "description": "The main interest of the co-worker."
    },
    "show_details": {
      "type": "object",
      "properties": {
        "show_name": {
          "type": "string",
          "description": "The name of the show where Anne Robinson and the co-worker appeared together."
        },
        "co_worker_role": {
          "type": "string",
          "description": "The role of the co-worker in the specified show."
        },
        "anne_robinson_role": {
          "type": "string",
          "description": "The role of Anne Robinson in the specified show."
        }
      },
      "required": [
        "show_name",
        "co_worker_role",
        "anne_robinson_role"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "co_worker_name",
    "co_worker_main_interest",
    "show_details"
  ],
  "additionalProperties": false
}
