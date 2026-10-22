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
InfoGear: InfoGear Technology Corporation, founded in 1995, was an American technology and services company which developed and marketed an early type of desktop phone which it named iPhone.  The company and its trademark of the iPhone name were acquired in 2000 by Cisco Systems.  In 2007, Apple Inc. and Cisco reached an agreement allowing Apple to use the iPhone name on its own distinct iPhone products.

Swedish neutrality: Swedish neutrality refers to Sweden's former policy of neutrality in armed conflicts, which was in effect from the early 19th century, until 2009, when Sweden entered into various mutual defence treaties with the EU, and other Nordic countries.  In 2016 Sweden became a "NATO Affiliate" (not member), and signed a treaty allowing NATO operations to take place within the country's borders.  Sweden's previous neutrality policy had originated largely as a result of Sweden's involvement in the Napoleonic Wars during which over a third of the country's territory was lost, including the traumatic loss of Finland to Russia.  Resentment towards the old king precipitated a "coup d'état" and the new regime formulated a new foreign policy which became known as "The Policy of 1812".  Since the time of the Napoleonic Wars, Sweden has not initiated any direct armed combat.  However, Sweden's military and government have been involved in major peacekeeping actions and other military support functions around the world.  The accession to the European Union in 1995 meant that neutrality as a principle was abolished.  Sweden is still today a neutral and non-aligned country in regard to foreign and security policy.  However, it maintains strong links to NATO.

AMC Dine-In Kabuki 8: AMC Dine-In Kabuki 8 is a movie theater in the Japan Center complex in San Francisco's Japantown neighborhood.  Formerly the AMC Kabuki Cinema 8, it was acquired by Robert Redford's Sundance Cinemas chain in 2006 as part of an anti-trust agreement allowing AMC to acquire Loews.  Sundance renovated the theater, and reopened it under its current name in December 2007, as the chain's second theater.  On October 6, 2015, it was announced that Carmike Cinemas has acquired Sundance Cinemas for $36 million.  On November 15, 2016 Carmike was purchased by AMC Theatres (which is owned by the China-based Wanda Group) for $1.2 Billion, bringing the theater back into AMC's control.  AMC announced on March 1, 2017 that the Carmike owned brands will be retired and all theaters would be placed under one of three new AMC brands.  It was announced on the merger page for Carmike to AMC that the Sundance Kabuki as of April 2017 was to be renamed the AMC Dine-In Kabuki 8.

Open border: An open border is a border that enables free movement of people between different jurisdictions with limited or no restrictions on movement, that is to say lacking substantive border control.  A border may be an open border due to a lack of legal controls or intentional legislation allowing free movement of people across the border ("de jure"), or a border may be an open border due to lack of adequate enforcement or adequate supervision of the border ("de facto").  An example of the former is the Schengen Agreement between most members of the European Economic Area (EFTA and the EU).  An example of the latter has been the border between Bangladesh and India, which is becoming controlled.  The term "open borders" applies only to the flow of people, not the flow of goods and services, and only to borders between political jurisdictions, not to mere boundaries of privately owned property.

2013 Nordic storms: 2013 Nordic storms were a series of storms affecting predominantly the Nordic nations with other northern European nations also affected.  The first storm in the series Hilde, named Otto by Free University of Berlin, and Eino in Finland was an extratropical cyclone affecting parts of northern Europe, causing disruption to electricity supplies and transportation across mid Norway, northern Sweden and central Finland in 15.  – 18.  November 2013.  The storm brought a new record average wind speed to Sweden (at altitude), however wind speeds at lower altitudes were less than seen during the Dagmar storm of 2011.  Most damage was caused by falling trees along the storms path likely exacerbated by unfrozen ground.  The total cost of damage is likely to be low, as the storm passed over relatively unpopulated regions of the Nordic nations.

Clinton Rickard: Clinton Rickard (1882-1971) was a Tuscarora chief known for founding the Indian Defense League, and for promoting Native American sovereignty.  He worked for free passage of Native Americans across the US-Canada border, and to prevent the flooding of the Tuscarora Reservation.

Neum Agreement: The Neum Agreement is an unimplemented treaty between Croatia and Bosnia and Herzegovina granting free passage of transit traffic between the territory of Dubrovnik-Neretva County around the city of Dubrovnik and forming a pene-exclave of Croatia and the reaining Croatian territory through the municipality of Neum.

Nordic Passport Union: The Nordic Passport Union allows citizens of the Nordic countriesIceland, Denmark, Norway, Sweden, and Finlandto travel and reside in another Nordic country (excluding Greenland and Svalbard) without any travel documentation (e.g. a passport or national identity card) or a residence permit.  Since 25 March 2001, all five states have also been within the Schengen Area.  The Faroe Islands are part of the Nordic Passport Union but not the Schengen Area, while Greenland and Svalbard are outside both.

UNITED for Intercultural Action: UNITED for Intercultural Action is a European network against nationalism, racism, fascism and in support of migrants and refugees, in which over 560 organisations from 48 European countries cooperate.  UNITED was founded in 1992 (officially registered as charitable organisation under Dutch law in 1993) and provides a forum for active solidarity and cooperation between a wide variety of organisations in Europe and their activists across European borders.

Finland–Sweden border: The Finnish-Swedish border is the border between the countries of Finland and Sweden.  Almost the entire border runs through water: along the Tornio River and its tributaries, and in the Gulf of Bothnia.  Only a few kilometres of the border are on dry land.  Because of the Schengen treaty and the Nordic Passport Union, the border can be crossed mostly freely.

Question: What's the name of the agreement allowing free passage across northern European borders including the one between Finland and Sweden?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "agreement_name": {
      "type": "string",
      "description": "The name of the agreement allowing free passage."
    },
    "purpose": {
      "type": "string",
      "description": "The primary purpose of the agreement regarding movement."
    },
    "countries_involved": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of countries whose citizens are covered by the agreement."
    },
    "border_example_mentioned": {
      "type": "string",
      "description": "A specific border mentioned in the context where this agreement applies."
    },
    "is_part_of_schengen_area": {
      "type": "boolean",
      "description": "Indicates if the states involved in the agreement are also part of the Schengen Area."
    }
  },
  "required": [
    "agreement_name",
    "purpose",
    "countries_involved",
    "border_example_mentioned",
    "is_part_of_schengen_area"
  ],
  "additionalProperties": false
}
