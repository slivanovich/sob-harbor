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
Dancing on Ice (series 6): The sixth series of Dancing on Ice started on 9 January 2011 and ended on 27 March 2011 on ITV.  Phillip Schofield and Holly Willoughby return as hosts whilst Jayne Torvill and Christopher Dean return to mentor the celebrities.  This series saw a huge revamp of the show which included the show moving from Elstree to Shepperton Studios, acquiring a new look set, and was broadcast in high definition for the first time on ITV1 HD, STV HD and UTV HD.

Phillip Schofield: Phillip Bryan Schofield (born 1 April 1962) is an English television presenter currently employed by ITV.  He is most recognised for presenting the lifestyle programme "This Morning", which he has co-hosted since 2002, and has also hosted other programmes on the channel.

Arts Plus: Arts Plus was a weekly Lifestyle programme showing the tradition and culture of India.  It ran in 1996 on Star Plus.  It had a total of 13 episodes which were telecast once a week.

Gudesens Conditori: Gudesens Conditori was a lifestyle programme shown on TV 2 from 1993 to 1995 presented by Egil Svartdahl.

Jamie &amp; Jimmy's Friday Night Feast: Jamie & Jimmy's Friday Night Feast is a UK food lifestyle programme which aired on Channel 4 in 2014.  A second series began in January 2015.  A third series began in January 2016.  A fourth series began in December 2016.

Top Billing (TV show): Top Billing is a South African lifestyle television programme that airs on SABC3 on Thursday evenings from 20:30 - 21:30 and repeats on Sunday at 13:00.  It was founded by Basetsana Kumalo and Patience Stevens, who own the "Tswelopele Production" company.  The show is the longest-running lifestyle programme in South Africa, broadcasting since 1996.  In addition to a variety of presenters, there is a voice-over guide throughout the programme.  A magazine of the same name was launched in March 2004, containing similar content to the show.

Burke's Backyard: Burke's Backyard is an Australian gardening and lifestyle programme presented by horticulturist Don Burke, broadcast on both radio and television.  On television, it was a regular weekly series on the Nine Network from 1987 to 2004.

Jamie's 15-Minute Meals: Jamie's 15-Minute Meals is a UK food lifestyle programme which aired on Channel 4 in 2012.  In each half-hour episode, host Jamie Oliver creates two meals, with each meal taking 15 minutes to prepare.

Top Billing (magazine): In March 2004, the South African television show "Top Billing" announced that it would launch a magazine version of the lifestyle programme.  In June 2004, "Top Billing" magazine was being sold nationwide for R19.95.  The "Top Billing" magazine contains celebrity interviews, behind-the-scenes previews, fashion, food, travel and entertainment news of local and international status.

Our Place (Australian TV series): Our Place is an Australian weekly live variety lifestyle programme broadcast on the Nine Network during early 2005.

Question: Which host of Dancing on Ice is most recognized for presenting the lifestyle programme "This Morning"?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "host_name": {
      "type": "string",
      "description": "The name of the host."
    },
    "show_hosted": {
      "type": "string",
      "description": "The name of the show they hosted, as mentioned in the question."
    },
    "recognized_for_program": {
      "type": "string",
      "description": "The name of the program the host is most recognized for."
    },
    "recognized_program_type": {
      "type": "string",
      "description": "The type of the program the host is most recognized for (e.g., lifestyle programme)."
    },
    "recognition_start_year": {
      "type": "integer",
      "description": "The year the host started co-hosting the recognized program."
    }
  },
  "required": [
    "host_name",
    "show_hosted",
    "recognized_for_program",
    "recognized_program_type",
    "recognition_start_year"
  ],
  "additionalProperties": false
}
