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
Arab Spring: The Arab Spring, (Arabic: الربيع العربي‎ ‎ "ar-Rabīʻ al-ʻArabī") also referred to as Arab revolutions (Arabic: الثورات العربية‎ ‎ "aṯ-'awrāt al-ʻarabiyyah"), was a revolutionary wave of both violent and non-violent demonstrations, protests, riots, coups and civil wars in North Africa and the Middle East that began on 17 December 2010 in Tunisia with the Tunisian Revolution.

Occupy Dataran: Occupy Dataran was an autonomous grassroots movement based in Kuala Lumpur, that aims to create a platform to experiment participatory democracy based on the popular assembly model.  "The Malaysian Insider" reported that Occupy Dataran were an offshoot of Occupy Wall Street.  The online news portal also reported that the Malaysian protesters were expressing solidarity with the New York protest movement as part of the 15 October 2011 global protests.  However, it is widely acknowledged that the first Occupy Dataran assembly was held on 30 July 2011, seven weeks before Occupy Wall Street.

Occupy Ashland: Occupy Ashland included a peaceful protest and demonstration against economic inequality, corporate greed and the influence of corporations and lobbyists on government which has taken place in Ashland, Oregon, United States since 6 October 2011.  The protests began in solidarity with the Occupy Wall Street protests in New York.  The protests included an occupation of the downtown Plaza and a daily picket outside the JPMorgan Chase branch in Ashland.

Occupy Eugene: Occupy Eugene was a collaboration that occurred in Eugene, Oregon based on the Occupy Wall Street movement which began in New York City on September 17, 2011.  Occupy Eugene included peaceful protests and demonstrations.  Protesters were concerned about fairness issues regarding wealth-distribution, banking regulation, housing issues and corporate greed.  The first protest march was held on October 15, 2011.  The march started at the Wayne Morse Free Speech Plaza and continued downtown before marching over Ferry Street Bridge.  It was reported that close to 2000 people were in attendance from all over the state of Oregon.  Occupy Eugene continues to hold regular protests and actions.  Protesters have stated that they do not have a set group of leaders.  Occupy Eugene General Assemblies have met from as frequently as twice a day at times during active occupations, and as infrequently as weekly.  Many committees have met since at least the third General Assembly - typically weekly, and of course informal conversations are essentially non-stop.  Decisions are made through a process known as consensus.  Occupy Eugene's consensus process operates in a similar fashion to how consensus is being handled in New York City by protesters involved in Occupy Wall Street.  Although the exact method varies from Occupation to Occupation.  As of October 18, 2011, The Eugene police department is allowing protesters to camp in downtown Eugene, although city law prohibits it.  Eugene police also stated that downtown camping won't be permanently allowed.

Occupy Chicago: Occupy Chicago was an ongoing collaboration that has included peaceful protests and demonstrations against economic inequality, corporate greed and the influence of corporations and lobbyists on government which has been taking place in Chicago since September 24, 2011.  The protests began in solidarity with the Occupy Wall Street protests in New York.

Occupy Seattle: Occupy Seattle was a collaboration that has included direct action demonstration with occasional activity at Westlake Park and Seattle City Hall in downtown Seattle, Washington.  Occupy Seattle is inspired by the Occupy Wall Street protests in New York City in September 2011, which in turn was inspired by the Arab Spring.  The protest, like the one in New York, is against wealth inequality, perceived corporate greed, and corruption in the banking and economic systems in the United States.

Occupy Berlin: Occupy Berlin was a collaboration in Berlin, Germany that has included peaceful protests and demonstrations against unregulated financial markets and other alleged social injustices.  It began as a part of the 15 October 2011 global protests.  The protest began in solidarity with the Occupy Wall Street protests in New York, United States.  It has established three encampments: outside of the church Parochialkirche, in Boxhagener Platz and the biggest one on the Bundespressestrand.

Occupy the Hood: The Occupy the Hood movement is a nationwide grassroots movement in the United States that is an extension of Occupy Wall Street and of the Occupy Movement generally.  The movement started in response to how the Occupy Wall Street movement was developing after its initial encampment in Zuccotti Park.  Occupy the Hood seeks to represent the interests of oppressed people and to bring people of color into the Occupy Movement.  The movement has been especially active in its attempts to decolonize the Occupy Movement.  Occupy the Hood was created by Malik Rhasaan, from Jamaica, Queens.  Occupy the hood chapters exist in the U.S. cities of Atlanta, Boston, Indianapolis, Los Angeles, Milwaukee, New York City, New York, and other major metropolitan cities.

List of Occupy movement protest locations: The Occupy Wall Street protests have inspired a wide international response.  There have been hundreds of Occupy movement protests worldwide over time, intended and organized as non-violent protest.  This is a list of some of their locations.  Months before the Occupy movement began, the Movimiento 15-M planned to hold events in many nations on October 15, 2011.  The Occupy movement joined in and also held many events in many nations on that day.  A list of proposed events for the 15 October 2011 global protests listed events in 951 cities in 82 countries.  Reportedly the large manifestation in Rome ended in violence.  Protest camps were built at many of the protest locations from Honolulu to Zeulenroda, often near banking institutions or stock markets.  Many locations had further manifestations at the following weekends until "Guy-Fawkes" day since the Guy Fawkes mask had become protester fashion.  Many US-American Occupy groups kept activity alive until spring 2012, some are still active.

Occupy Oslo: Occupy Oslo was a collaboration, peaceful protest and demonstration against social injustice, corporate greed and the influence of corporations and lobbyists on government.  It occurred in Oslo, Norway, and started as a part of the global protests of October 15th, 2011.  The protest began in solidarity with the Occupy Wall Street protests in New York, United States, and is a part of the global occupy movement.

Question: Which event triggered this revolutionary wave that became the inspiration for the Occupy Wall Street protests?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "triggering_event": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the event that triggered the revolutionary wave."
        },
        "start_date": {
          "type": "string",
          "description": "The start date of the triggering event."
        },
        "location": {
          "type": "string",
          "description": "The country where the triggering event began."
        }
      },
      "required": [
        "name",
        "start_date",
        "location"
      ],
      "additionalProperties": false
    },
    "revolutionary_wave": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the broader revolutionary wave."
        },
        "description": {
          "type": "string",
          "description": "A brief description of the revolutionary wave."
        }
      },
      "required": [
        "name",
        "description"
      ],
      "additionalProperties": false
    },
    "inspired_movement": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the movement that was inspired by the revolutionary wave."
        }
      },
      "required": [
        "name"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "triggering_event",
    "revolutionary_wave",
    "inspired_movement"
  ],
  "additionalProperties": false
}
