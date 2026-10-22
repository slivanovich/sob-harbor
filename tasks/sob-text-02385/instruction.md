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
Human rights in the Solomon Islands: Solomon Islands is a sovereign country in the South West Pacific consisting of many islands with a population of 561,231 (2013).  It became self-governing from the United Kingdom in 1976 after three previous attempts at forming a Constitution.  The Constitution of Solomon Islands was enacted in 1978.  This however led to conflicts between cultures and armed conflict in the late 1990s forced a review of the 1978 Constitution.  This review resulted in the Federal Constitution of the Solomon Islands Bill 2004 (SI) and various other amendments, the Human Rights Chapter however remained unchanged.

Hope Strachan: Hope Strachan (born 1 December 1960) is a politician from The Bahamas who is the Member of Parliament for the Sea Breeze Constituency.  Strachan is also a Cabinet Minister, serving in the administration of Prime Minister Perry Christie as Minister of Financial Services and Local Government and also has responsibility for Trade and Industry.

Gulf of Morbihan: The Gulf of Morbihan is a natural harbour on the coast of the Département of Morbihan in the south of Brittany, France.  This English name is taken from the French version: "le golfe du Morbihan".  It is more accurately called 'the Morbihan' directly from its Breton name which is "Ar Mor Bihan", meaning 'the little sea' (Compare the Welsh "y môr bychan"), as opposed to the Atlantic Ocean outside, ("Ar Mor Bras").  Legend says that there are as many islands in the Gulf as there are days of the year.  However, this is untrue and the gulf has about 40, depending on the tide.  Many islands are private property, except the largest two, l'Île-aux-Moines and l'Île-d'Arz.

Aldabra giant tortoise: The Aldabra giant tortoise ("Aldabrachelys gigantea"), from the islands of the Aldabra Atoll in the Seychelles, is one of the largest tortoises in the world.  Historically, giant tortoises were on many of the western Indian Ocean islands, as well as Madagascar, and the fossil record indicates giant tortoises once occurred on every continent and many islands with the exception of Australia and Antarctica.  Many of the Indian Ocean species were thought to be driven to extinction by over-exploitation by European sailors, and they were all seemingly extinct by 1840 with the exception of the Aldabran giant tortoise on the island atoll of Aldabra.  Although some remnant individuals of "A. g. hololissa" and "A. g. arnoldi" may remain in captivity, in recent times, these have all been reduced as subspecies of "A. g. gigantea".

The Bahamas: The Bahamas ( ), known officially as the Commonwealth of The Bahamas, is an archipelagic state within the Lucayan Archipelago.  It consists of more than 700 islands, cays, and islets in the Atlantic Ocean and is located north of Cuba and Hispaniola (Haiti and the Dominican Republic); northwest of the Turks and Caicos Islands; southeast of the US state of Florida and east of the Florida Keys.  The capital is Nassau on the island of New Providence.  The designation of "the Bahamas" can refer either to the country or to the larger island chain that it shares with the Turks and Caicos Islands.  As stated in the mandate/manifesto of the Royal Bahamas Defence Force, the Bahamas territory encompasses 180000 sqmi of ocean space.

Many Islands, Arkansas: Many Islands is an unincorporated community in eastern Fulton County, Arkansas.  Many Islands is located along the Spring River, 7.4 mi south of Mammoth Spring.

List of Bergen Light Rail stations: The Bergen Light Rail is a light rail system serving Bergen, Norway.  Scheduled to open on , the first state consist of 15 stations along a 9.8 km line.  Stage two opened 21 June 2013 and expanded the system with another five stations over 3.6 kilometres to Lagunen.  Stage three is scheduled to open in 2016.

List of islands in the Persian Gulf: The Persian Gulf is home to many islands, mostly small, distributed in the gulf's entire geographic area and administered by the neighbouring nations.  Most islands are sparsely populated, with some being barren, and some utilized for communication, military, or as ship docks.  Some of the islands in the Persian Gulf are artificially constructed islands.  The artificial islands often serve as tourist resorts, housing developments, or hotels.  Despite their small sizes, some of these artificial islands have caused serious hazards for the already fragile ecosystem of the Gulf and its dwindling wildlife mass.  A few of the Gulf islands are also historically significant, having been utilized by the ancient empires, neighbouring kingdoms, and in the recent times, colonial powers such as the British empire, and the Portuguese empire.  Recent globalization, and discovery of oil, has made some of the Persian Gulf islands very significant for developed nations as a source of oil and raw industrial material.  Recent wars, and political unrest has also made these islands strategic military locations for foreign powers from America and Europe.

Guayaneco Archipelago: The Guayaneco Archipelago (Spanish: Archipiélago Guayaneco ) is an archipelago in southern Chile.  It was heavily glaciated during the most recent ice age.  These glaciers dissected these mountain islands into a series of deep river valleys and glacial troughs.  Today these glacial troughs are deep channels and fjords.  The islands of the Guayaneco Archipelago comprise a series of elongated islands and deep bays that are the traces of a drowned coastal range.  A number of deep channels are traversing generally north to south through the islands.  These include the Messier Channel in the lower left portion of the image, and the Fallos Channel near the center of the image.  Forests cover the lower slopes of the mountains throughout the many islands.  Human settlement on these islands is scarce.

Five Bridges of Amakusa: Five Bridges of Amakusa (天草五橋 , Amakusa Gokyō ) are five road bridges at the south tip of Japan, linking the Kyushu mainland (Kumamoto Prefecture) and the Amakusa Islands.  The bridges connect to the islands of Ooyano-jima, Nagaura-jima, Ike-jima, and Maeshima, and were completed on September 24, 1966.  The Five Bridges gave hope and confidence in the development of Japan's bridge-construction technology, and changed the lives of those living at the Amakusa Islands (see survey below: Evaluation).  Many tourists come to view the scenic beauty of the many islands, and the roads are called the Amakusa Pearl Line, based on the products of cultured pearls.

Question: How many islands does Hope Strachan's state consist of?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "entity_name": {
      "type": "string",
      "description": "The name of the country or state associated with Hope Strachan."
    },
    "entity_type": {
      "type": "string",
      "description": "The type of entity, e.g., 'country' or 'state'."
    },
    "island_count_description": {
      "type": "string",
      "description": "A descriptive phrase for the number of islands."
    },
    "island_count_minimum": {
      "type": "integer",
      "description": "The minimum number of islands if specified."
    }
  },
  "required": [
    "entity_name",
    "entity_type",
    "island_count_description",
    "island_count_minimum"
  ],
  "additionalProperties": false
}
