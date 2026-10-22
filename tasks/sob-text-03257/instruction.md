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
Mister Belgium Personality: Mister Belgium Personality is the oldest national male beauty pageant in Belgium, responsible for selecting the country's representatives to Mister International, Men Universe Model and Manhunt International pageants.  The organization established in 2013.  Since 2014 it organizes national pageant Mister Belgium Personality.  The winner expected to promote "Mister" (to be a-year long promotion carries himself and appearances), "Model" (to become role model of his country), and "Personality" (to represent his strong and pleasant personality).  The last winner is Fabio Ronti (Brussels).

Misters of Puerto Rico: "Mister Puerto Rico" is the common name or sash used to identify a Puerto Rican representative in an international male beauty pageant.  It is an annual male pageant held in San Juan, Puerto Rico.  Currently, "Mister Puerto Rico Model" and "Mister Puerto Rico Teenager" are the most important male beauty pageant event.  Each year both events are held to select the representatives from the island.

Gabriel Soto: Gabriel Soto-Borja Díaz (born April 17, 1975 in Mexico City, Distrito Federal) is a Mexican actor, model.  He is known for winning the national male pageant El Modelo Mexico, placing first runner-up in Mister World 1996, being a member of the former Mexican boy band Kairo, and for acting in telenovelas.

Mister Brazil: The Mister Brazil (Portuguese: Mister Brasil ) pageant is the major male beauty pageant held in Brazil.  Its organizer, MMB Productions and Events, led by Henrique Fontes and Co.  The country is the first in official ranking of Mister World.  Besides sending Brazilian representatives to Mister World, the national competition elects for Manhunt International and Mister International.

Mister International: Mister International is an annual male beauty pageant founded in 2006.  It is owned and organized by the Mister International Organization which also organizes the annual Mister Singapore pageant.  Along with its rival contest, Mister World, this pageant is one of the two largest male beauty pageants in the world in terms of the number of national-level competitions.  Since the first edition, 76 countries have sent their representative to this pageant, with an annual average of 31 contestants.  Mister International Organization licenses local organizations that wish to select the Mister International contestant for their country, and approves the selection method for national contestants.

Grasim Mr. India: Grasim Mr. India ("formerly Adonis - Graviera Man Of The Year") was a national Male beauty pageant in India that annually selected representatives to compete globally at Mr. International, Mister World, Mr. Intercontinental and Best Model Of the World.  In the years 1996 and 1998, the winner of the contest represented India at Mister World contest.  Later the title was changed to "Mr. India" International and the winner was sent to compete at Mr. International pageant.  Later in 2007, Hayward 5000 organized Mr India pageant and the winner was sent to Mister World.  In 2010 and 2012, Grasim Mr. India again sent its winner to Mister World and the title was renamed Mr India World.  Since 2014, The Times Group owns the right to organize Mr India World contest and its winner represents India at Mister World.

Mr World Mexico: Mr World Mexico refers to the pageant title given to the Mexican men chosen to represent Mexico at the international male beauty pageant Mister World.  The nation has taken part in every edition of Mister World ever since its establishment in 1996, debut year in which Mexico's Gabriel Soto placed second (first runner-up) — the highest placement achieved by a Mexican contestant in that event to this day.

Juan García Postigo: Juan García Postigo (born January 19, 1982) is a male beauty pageant contestant from Málaga, Spain.  He was proclaimed Mister World 2007 on March 31, 2007 in Sanya, People's Republic of China.  He beat 56 other contestants to capture the male pageant title.  A year before, he was elected Mister Spain 2006.

Mister World: The Mister World competition is a male beauty pageant sponsored by the Miss World Organization.  The competition is biennial and was founded in 1996.  The entrants compete in various activities including waterskiing, mountain biking, and marathon running.  The current Mister World is Rohit Khandelwal of India who was crowned on July 19, 2016 in Southport, England.  He is the first ever Asian to be crowned Mister World in the 2016 contest.  Traditionally, Mister World lives in London during his reign.

Mr. World Canada: Mr. World Canada (sometimes informally referred to as Mr. Canada) is a Canadian male beauty pageant that runs in parallel with the Miss World Canada pageant, the two sending their winners to compete in the Mister World and Miss World pageants respectively.  Darren Storsley, the organizer of the Miss B.C. World pageant, was named Mr. World Canada in 2007.  Ron Wear of Edmonton, Alberta won the competition in 2010.  Wear went on to compete in Mister World 2010, but he did not win.  Wear attested to his Mr. World Canada duties preventing him from pursuing an acting career to the extent that he would have liked.  In 2012, Frankie Cena of Burnaby, British Columbia won the Mr. World Canada competition.  Cena was an undergraduate student at the University of British Columbia at the time, and went on to use his title to model, act, and represent Canada to other nations.  At Mister World 2012, Cena ranked first at the talent show, second in the multimedia competition, and tenth overall.  While Mr. World Canada, Cena sang at the Warmth of Light Musical Banquet hosted by Miss World Canada contestant Selina Yue.

Question: Mr World Mexico refers to the pageant title given to the Mexican men chosen to represent Mexico at the international male beauty pageant Mister World, the nation has taken part in every edition of Mister World ever since its establishment in 1996, debut year in which Mexican actor, model, placed second?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "contestant_name": {
      "type": "string",
      "description": "The full name of the contestant."
    },
    "nationality": {
      "type": "string",
      "description": "The nationality of the contestant."
    },
    "pageant_details": {
      "type": "object",
      "properties": {
        "pageant_name": {
          "type": "string",
          "description": "The name of the international beauty pageant."
        },
        "year": {
          "type": "integer",
          "description": "The year the pageant took place."
        },
        "placement": {
          "type": "string",
          "description": "The contestant's final placement in the pageant (e.g., 'winner', 'second', 'first runner-up')."
        },
        "is_debut_year_for_country": {
          "type": "boolean",
          "description": "Indicates if it was the country's debut year in the pageant."
        }
      },
      "required": [
        "pageant_name",
        "year",
        "placement",
        "is_debut_year_for_country"
      ],
      "additionalProperties": false
    },
    "contestant_professions": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of professions held by the contestant."
    }
  },
  "required": [
    "contestant_name",
    "nationality",
    "pageant_details",
    "contestant_professions"
  ],
  "additionalProperties": false
}
