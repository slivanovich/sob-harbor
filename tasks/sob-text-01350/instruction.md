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
Generation Next (BBC series): BBC Generation Next was a week-long special running primarily on the BBC World Service but also on BBC Television aimed at understanding and exploring how under-18s view the world.  The series ran from 2 to 10 December 2006, and broadcasters Darryl Morris & Kate Tozer presented the week long event, linking the shows and events together after being head hunted to do so by the BBC.  Robin Lustig hosted a key five-part documentary for Generation Next on the World Service.  As part of the series, the BBC also ran School Day 24, which linked up teenagers from schools across a divide (like in Kosovska Mitrovica between Serbs and Albanians or between rural, semi-urban and urban school students in the People's Republic of China) and The Next Big Thing, a competition to find the best teen band in the world.

LittleBigPlanet (2008 video game): LittleBigPlanet, commonly abbreviated LBP, is a puzzle-platformer video game, based on user-generated content, for the PlayStation 3 first announced on 7 March 2007, by Phil Harrison at the 2007 Game Developers Conference (GDC) in San Francisco, California.  It was developed under the title "The Next Big Thing" by Media Molecule and was published by Sony Computer Entertainment Europe.  Many saw the game as an important title for Sony's PlayStation 3.

Already: Already is the fourth album by the British rock band Jesus Jones in 1997.  The album followed a working hiatus by the band following the relative failure of 1993's "Perverse" compared to their international breakthrough album "Doubt" (1991).  Although the band had come up with ideas that they requested to Food Records, the label rejected them before finally accepting the released "Already".  It was their last album for EMI, and two singles were released from the album, "The Next Big Thing" and "Chemical #1".  "Already" only reached No. 161 in the UK Albums Chart, although lead single "The Next Big Thing" had some radio play reaching No. 49 in the UK Singles Chart.  EMI re-issued on the album on 1 March 2003.

Bloomberg L.P.: Bloomberg L.P. is a privately held financial software, data, and media company headquartered in Midtown Manhattan, New York City.  Bloomberg L.P. was founded by Michael Bloomberg in 1981 with the help of Thomas Secunda, Duncan MacMillan, Charles Zegar, and a 30% ownership investment by Merrill Lynch.

William Zhou: William Zhou (Chinese: 周惟正; born February 18, 1992) is a Canadian internet entrepreneur.  In 2012, Zhou co-founded Chalk.com, a K-12 education software company.  He has appeared as a frequent commentator on major networks, a speaker at Bloomberg Next Big Thing Conference, and was named in Forbes 30 Under 30.

Suhit Gosain: Suhit Gosain (born 17 October 1985 in Bhopal, India) is an Indian pop-singer, actor, and performer.  He was a contestant on "Indian Idol 3", a reality musical show aired on Sony Entertainment Television, modeled on "Pop Idol".  He was a favourite of Alisha Chinai, who was a judge of the same show.  He was a part of the F4 boy-band which also included- Abhishek, Parleen and Meiyang Chang.  The band earned great public appreciation.  F4 was also declared 'The Next Big Thing' on Channel V.  Despite such popularity, the band presently exists no more.  Suhit holds a Management Degree from Flame School of Management, Pune, Maharashtra, India.  After stints with Media Companies like Reliance & Times of India Group, he spent some time with a Mumbai-based Event management Company viz.  7ty7 Entertainment.  Presently, Suhit is associated with Geometry Global Encompass Private Limited, a WPP Group Company as a Conceptualiser.  Being associated with Media set-ups, Suhit carries his creative passion in to his job assignments.  He continues to create his own music at his home recording studio.

Football's Next Star (Ireland): Football's Next Star is a television programme broadcast on RTÉ Two under the TRTÉ brand in Ireland.  The show aimed to find a young football player who could be the "next big thing" and reward them with a professional contract at Celtic F.C. in Scotland.

Next Big Thing (song): "Next Big Thing" is a song co-written and recorded by American country music artist Vince Gill.  It was released in November 2002 as the first single and title track from the album "Next Big Thing".  The song reached #17 on the "Billboard" Hot Country Singles & Tracks chart.  The song was written by Gill, Al Anderson and John Hobbs.

Model N (company): Model N, Inc. is a public American software company founded in 1999 and headquartered in Redwood City, California.  The name "Model N" refers to "model next", as in 'the next big thing', according to founder Zack Rinat.  The company's focus is on revenue management software, based on developments by Rinat, initially for pharmaceutical and medical device companies.

Tabula (company): Tabula was a fabless semiconductor company based in Santa Clara, California.  Founded in 2003 by Steve Teig (ex-CTO of Cadence), it raised $215 million in venture funding.  The company designed and built three dimensional field programmable gate arrays (3-D FPGAs) and ranked third on the Wall Street Journal's annual "Next Big Thing" list in 2012.

Question: What year was the company, which hosts the Bloomberg Next Big Thing Conference, founded?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string",
      "description": "The name of the company that hosts the conference."
    },
    "conference_hosted": {
      "type": "string",
      "description": "The name of the conference hosted by the company."
    },
    "company_description": {
      "type": "string",
      "description": "A brief description of the company's primary business."
    },
    "founding_details": {
      "type": "object",
      "properties": {
        "founding_year": {
          "type": "integer",
          "description": "The year the company was founded."
        },
        "primary_founder": {
          "type": "string",
          "description": "The name of the primary founder of the company."
        }
      },
      "required": [
        "founding_year",
        "primary_founder"
      ],
      "additionalProperties": false
    },
    "answer_founding_year": {
      "type": "integer",
      "description": "The founding year of the company that hosts the specified conference."
    }
  },
  "required": [
    "company_name",
    "conference_hosted",
    "company_description",
    "founding_details",
    "answer_founding_year"
  ],
  "additionalProperties": false
}
