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
UFC Fight Night: Namajunas vs. VanZant: UFC Fight Night: Namajunas vs. VanZant (also known as UFC Fight Night 80) was a mixed martial arts event held on December 10, 2015, at The Chelsea at The Cosmopolitan in Las Vegas, Nevada.

UFC Fight Night: Silva vs. Irvin: UFC Fight Night: Silva vs. Irvin (also known as UFC Fight Night 14) was a mixed martial arts event held by the Ultimate Fighting Championship (UFC) on July 19, 2008 at the Palms Casino Resort in Las Vegas, Nevada.

UFC Fight Night: Thomas vs. Florian: UFC Fight Night: Thomas vs. Florian (also known as UFC Fight Night 11) was a mixed martial arts (MMA) event held by the Ultimate Fighting Championship (UFC) on Wednesday, September 19, 2007 at the Palms Casino Resort in Las Vegas, Nevada.  It was broadcast live in the United States and Canada on Spike TV as a lead-in to the debut of "The Ultimate Fighter 6".

UFC Fight Night: Marquardt vs. Palhares: UFC Fight Night: Marquardt vs. Palhares (also known as UFC Fight Night 22) and originally scheduled as UFC Fight Night: Maia vs. Belcher, was a mixed martial arts event held by the Ultimate Fighting Championship on September 15, 2010 at the Frank Erwin Center in Austin, Texas.  The event also served as a lead in to the season premiere of "".

Cosmopolitan of Las Vegas: The Cosmopolitan of Las Vegas (commonly referred to simply as The Cosmopolitan or The Cosmo) is a luxury resort casino and hotel on the Las Vegas Strip in Paradise, Nevada.  The resort opened on December 15, 2010, and is located just south of the Bellagio on the west side of Las Vegas Boulevard.

UFC Fight Night: Swick vs. Burkman: UFC Fight Night: Swick vs. Burkman (also known as UFC Fight Night 12) was a mixed martial arts (MMA) event held by the Ultimate Fighting Championship (UFC) on January 23, 2008 at the Palms Casino Resort in Las Vegas, Nevada.

UFC Fight Night: Florian vs. Gomi: UFC Fight Night: Florian vs. Gomi (also known as UFC Fight Night 21) was a mixed martial arts event held by the Ultimate Fighting Championship on March 31, 2010 at Bojangles Coliseum in Charlotte, North Carolina, This was the third time the UFC held an event in Charlotte, but the first since UFC 5.

UFC Fight Night: Gustafsson vs. Manuwa: UFC Fight Night: Gustafsson vs. Manuwa (also known as UFC Fight Night 37) was a mixed martial arts event held on March 8, 2014, at The O2 Arena in London, England.  The event was shown live in the UK on Channel 5 and BT Sport and in the United States on UFC Fight Pass.

UFC Fight Night 6: UFC Fight Night: Sanchez vs. Parisyan (also known as UFC Fight Night 6) was a mixed martial arts event held by the Ultimate Fighting Championship on August 17, 2006.  The event took place at the Red Rock Resort Spa and Casino in Las Vegas, Nevada, and was broadcast live on Spike TV in the United States and Canada.  It acted as a lead-in to the season four premiere of "The Ultimate Fighter".  The two-hour broadcast of UFC Fight Night 6 on Spike TV drew a 1.5 overall rating. 

Fox UFC: Fox UFC Fight Night (previously referred as Fox UFC Saturday for broadcasts on Fox or FS1 UFC Fight Night for broadcasts on other Fox-owned properties) is the branding used for telecasts of mixed martial art competitions from the Ultimate Fighting Championship (UFC) that are produced by Fox Sports.  Previously, "UFC on Fox" was also used as a blanket title for UFC events aired on the Fox network, although since the concurrent launch of Fox Sports 1 and rebranding of Fuel TV as Fox Sports 2 in August 2013, all live UFC broadcasts on Fox-owned networks (including preliminaries, "UFC Fight Night" and "The Ultimate Fighter Finale") have since used the name.

Question: When did the resort where UFC Fight Night: Namajunas vs. VanZant was held open?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "event_name": {
      "type": "string",
      "description": "The full name of the UFC Fight Night event."
    },
    "event_date": {
      "type": "string",
      "format": "date",
      "description": "The date the UFC event was held."
    },
    "venue_details": {
      "type": "object",
      "properties": {
        "venue_name": {
          "type": "string",
          "description": "The name of the specific venue within the resort."
        },
        "resort_name": {
          "type": "string",
          "description": "The name of the resort where the event was held."
        },
        "resort_opening_date": {
          "type": "string",
          "format": "date",
          "description": "The date the resort opened."
        }
      },
      "required": [
        "venue_name",
        "resort_name",
        "resort_opening_date"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "event_name",
    "event_date",
    "venue_details"
  ],
  "additionalProperties": false
}
