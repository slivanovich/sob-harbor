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
Midlands Today: Midlands Today is the BBC's regional television news service for the West Midlands.  It was launched in 1964 and is presented on alternating nights by Mary Rhodes or Nick Owen.

Nick Owen: (born 1 November 1947) is an English television presenter and newsreader, best known for presenting the breakfast television programme "TV-am" and the BBC's local news show "Midlands Today" since 1997.  He was also the Chairman of Luton Town Football Club between 2008 and 2017.

Lukwesa Burak: Lukwesa Burak is a news and weather presenter for BBC News.  Previously, she was a presenter and interviewer for Al Jazeera, Sky News and before that "Africa Edition" on eNCA (formerly known as "eNews Channel"), based in South Africa.  She was formerly a weather forecaster and then news presenter in the United Kingdom, for "East Midlands Today", a regional television news programme covering the Midlands area of Central England, followed by news presenter for "Sky News", the 24-hour television news service operated by Sky Television, part of British Sky Broadcasting, based in London.  She became a news presenter for eNCA in August 2012.

Matt Cooke (journalist): Matthew 'Matt' Cooke (born 28 August 1982 in Kingston-upon-Thames) is a British journalist who currently works for BBC News reporting at "BBC London News" and presenting "60 Seconds" on BBC Three.  He formerly presented at "BBC Midlands Today", the regional bulletin for the West Midlands.

East Midlands Today: East Midlands Today is the BBC's regional television news programme for the East Midlands.

Sarah Bishop: Sarah Bishop (previously Falkland) is a British television journalist, working as a reporter and newsreader for BBC "Midlands Today" for the West Midlands Region.

Shefali Oza: Shefali Oza (born 24 September 1967) is an Indian TV personality and is the main weather presenter on BBC Birmingham's "Midlands Today", the regional news programme broadcast in the Midlands of England, but also carries out some news presentation work.  She began her career with the team as "Midlands Today"<nowiki>'</nowiki>s first ever weather presenter in January 1993.

Sara Blizzard: Sara Louise Blizzard (born 1970 in Coventry, Warwickshire) is a weather presenter for East Midlands Today.  Sara regularly presents the weather forecasts for Midlands Today and BBC North West Tonight.

Alan Towers: Alan Towers (1934 – 24 May 2008) was a former presenter of "Midlands Today", BBC Midlands' regional news programme.

Michael Collie: Michael Collie is a British television and radio presenter who appears on BBC News.  He is also a former presenter of the weekly politics programme, the Politics Show, in addition to his work presenting BBC Midlands Today, produced by the BBC's West Midlands region.

Question: Which of the hosts of Midlands Today is also on "TV-am"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "presenter_name": {
      "type": "string",
      "description": "The name of the presenter who hosted both Midlands Today and TV-am."
    },
    "birth_year": {
      "type": "integer",
      "description": "The birth year of the presenter."
    },
    "midlands_today_involvement": {
      "type": "object",
      "properties": {
        "is_host": {
          "type": "boolean",
          "description": "True if the presenter is a host of Midlands Today."
        },
        "start_year": {
          "type": "integer",
          "description": "The year the presenter started hosting Midlands Today."
        }
      },
      "required": [
        "is_host",
        "start_year"
      ],
      "additionalProperties": false
    },
    "tv_am_involvement": {
      "type": "object",
      "properties": {
        "is_host": {
          "type": "boolean",
          "description": "True if the presenter is a host of TV-am."
        }
      },
      "required": [
        "is_host"
      ],
      "additionalProperties": false
    },
    "other_significant_roles": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "role": {
            "type": "string",
            "description": "The role held by the presenter."
          },
          "organization": {
            "type": "string",
            "description": "The organization where the role was held."
          },
          "start_year": {
            "type": "integer",
            "description": "The start year of the role."
          },
          "end_year": {
            "type": "integer",
            "description": "The end year of the role."
          }
        },
        "required": [
          "role",
          "organization",
          "start_year",
          "end_year"
        ],
        "additionalProperties": false
      },
      "description": "Other notable roles or affiliations of the presenter."
    }
  },
  "required": [
    "presenter_name",
    "birth_year",
    "midlands_today_involvement",
    "tv_am_involvement"
  ],
  "additionalProperties": false
}
