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
Guanyu Zhou: Guanyu Zhou, also known as Zhou Guan Yu (周冠宇 born 30 May 1999) is a Chinese racing driver, who competed in the Italian F4 Championship and ADAC Formula 4 Championships for Prema Powerteam and the European Formula 3 Championship with Motopark in 2016 and Prema in 2017.  He is a member of the Ferrari Driver Academy.

Ralf Aron: Ralf Aron (born 21 March 1998) is a Estonian racing driver, who competed in the Italian F4 Championship, ADAC Formula 4 and European Formula 3 championships for Prema Powerteam and Hitech GP.

Harrison Newey: Harrison Newey (born 25 July 1998) is a British racing driver and the son of Marigold Newey and famed Formula One engineer Adrian Newey.  He made his ADAC Formula 4 debut in 2015, partnering Mick Schumacher, son of world champion driver Michael Schumacher, at Van Amersfoort Racing.  He is also competing in BRDC Formula 4 alongside his ADAC F4 campaign, partnering Will Palmer and Sisa Ngebulana at HHC Motorsport.

Van Amersfoort Racing: Van Amersfoort Racing is an auto racing team based in The Netherlands.  In 2017, the team will compete in the European Formula 3 Championship, the German ADAC Formula 4 Championship and will make its debut in the Italian F4 Championship.

Sophia Flörsch: Sophia Flörsch (sometimes spelt Floersch, born 1 December 2000) is a racing driver from Germany.  Flörsch currently competes in the ADAC Formula 4 championship and the Italian F4 Championship with BWT Mücke Motorsport.  In her debut race, she became the first female to score points in an ADAC Formula 4 race.  She previously drove in the Ginetta Junior Championship driving for HHC Motorsport where she won two races and had a further two podiums.  She broke several records by becoming the youngest driver to win a Ginetta Junior race, and also the first rookie to win two out of two races in one weekend.

Prema Powerteam: Prema Powerteam (competing as Prema Racing in the FIA Formula 2 Championship) is a motorsport team from Italy.  It mainly operates in the FIA Formula 3 European Championship as well as various junior championships.  The team was founded in 1984.  Also this team was a part of Toyota Driver Programme.  Currently the team has strong ties with Mercedes and Ferrari, running many of the current Ferrari Driver Academy drivers.  Its most recent success is winning the GP2 Drivers' title with Pierre Gasly and Teams' championship.

ADAC Formel Masters: ADAC Formel Masters was an ADAC sanctioned open wheel racing series based in Germany, held annually from 2008 to 2014.  It was replacement of the local Formula BMW championship.  The first season was in 2008 and is the main feeder series to the ATS Formula 3 Cup (German Formula Three Championship).  Like Formula Ford, French F4 Championship and Formula Abarth, the Formel Masters is aimed at karting graduates.  In 2015 it was replaced by the ADAC Formula 4.

Juan Manuel Correa: Juan Manuel Correa (born 9 August 1999) is an Ecuadorian-American racing driver who competes with Prema Powerteam in the Italian F4 and ADAC Formula 4 championships.

ADAC Formula 4: ADAC Formula 4 (German: "ADAC Formel 4" ) is a racing series regulated according to FIA Formula 4 regulations.  The inaugural season was the 2015 ADAC Formula 4.  It replaced the ADAC Formel Masters, held from 2008 to 2014.

Marcus Armstrong: Marcus Armstrong (born 29 July 2000), is a New Zealand motor racing driver currently competing in the ADAC Formula 4 and the Italian F4 Championship driving for Prema Powerteam.

Question: What country is the motorsport team for which Guanyu Zhou competed in the Italian F4 Championship and ADAC Formula 4 Championships from?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "driver_name": {
      "type": "string",
      "description": "The name of the racing driver."
    },
    "team_name": {
      "type": "string",
      "description": "The name of the motorsport team."
    },
    "team_country": {
      "type": "string",
      "description": "The country where the motorsport team is based."
    },
    "championships_competed_in": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of championships the driver competed in with the specified team."
    }
  },
  "required": [
    "driver_name",
    "team_name",
    "team_country",
    "championships_competed_in"
  ],
  "additionalProperties": false
}
