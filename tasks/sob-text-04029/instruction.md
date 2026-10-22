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
Rifeh: Rifeh or Deir Rifeh (also known as Rifa) is a village in Egypt.  The name refers today most often to a series of Ancient Egyptian cemeteries nearby.  These are the burial grounds of the ancient town Shashotep.  The cemeteries date from the end of the First Intermediate Period to the Roman Period.  Especially important are the burials of the Middle Kingdom.  In this period Shashotep was the capital of the 11th Upper Egyptian province.  Several decorated rock cut tombs were carved into the rocky hills.  They belong to the local governors of the period.  Nakht-Khnum and Nefer-Khnum are the two whose names survived.  In front of these tombs were burials of lower officials that were working for these local governors.  One of them is the Tomb of two Brothers, that was found undisturbed and still contained an array of important artcfacts.  Further away and closer to the Nile were the burials of the more common people.  Typical for many of these burials dating to the Middle Kingdom model clay houses, once placed on top of the burial.  They are called in Egyptology "soul houses".  Further burials belong to the Second Intermediate Period and to the New Kingdom, when Shashotep was no longer the capital of a province.

Maastricht: Maastricht (] ; Limburgish : "Mestreech" ; French: "Maestricht" ; Spanish: "Mastrique" ) is a city and a municipality in the southeast of the Netherlands.  It is the capital and largest city of the province of Limburg, as well as the largest city in the historical duchy of Limburg, that today spans the Netherlands and Belgium.

TV Patrol Palawan: TV Patrol Palawan (formerly Palawan TV Patrol) is a local news program of the ABS-CBN Regional Network Group in Palawan, an island province, which is part of Mimaropa in the Philippines but doesn't belong to the coverage area of TV Patrol Southern Tagalog.  The newscast delivers news headlines about current events in Palawan's capital Puerto Princesa City and its surrounding areas similar to TV Patrol Negros.  It is aired live daily from ABS-CBN TV-7 Newscenter Palawan at 5:00 pm Monday to Friday.  It is also on radio via DYAP Radyo Patrol 765 Palawan.  TV Patrol Palawan is the first and official news program of ABS-CBN in Palawan.  TV Patrol Palawan has been given a Special Citation for Best Regional News Program in the 2014 UPLB Gandingan Awards, and was a finalist for the Best News Program (Provincial) in the 2013 KBP's Golden Dove Awards.

Kingdom of Crystal: The Kingdom of Crystal (Swedish: "Glasriket", "The glass realm") is a geographical area today containing a total of 14 glassworks in the municipalities of Emmaboda, Nybro, Uppvidinge, and Lessebo in southern Sweden.  The two municipalities Emmaboda and Nybro belong to Kalmar County and Lessebo and Uppvidinge belong to Kronoberg County.  The area is part of the province Småland, and Nybro is considered the capital of the Kingdom of Crystal area.  The Kingdom of Crystal is known for its handblown glass with a continuous story since 1742. The glassworks have become part of the culture of Sweden; examples can be found in many Swedish homes, recognisable by a small sticker at the bottom with the name Orrefors, Kosta, etc.  The height of glass production was the end of the 19th century during which 77 glass factories were established with more than half of them situated in Småland.

List of railway stations in Belgium: This is a list of the busiest railway stations in Belgium sorted by the average number of passengers boarding daily on weekdays in 2014.  The province is also listed, unless the station lies within the Brussels Capital Region and therefore does not belong to any province.

Municipalities of Belgium: Belgium comprises 589 municipalities (Dutch: "gemeenten" ; French: "communes" ; German: "Gemeinden" ) grouped into five provinces in each of two regions and into a third region, the Brussels-Capital Region, comprising 19 municipalities that do not belong to a province.  In most cases, the municipalities are the smallest administrative subdivisions of Belgium, but in municipalities with more than 100,000 inhabitants, on the initiative of the local council, sub-municipal administrative entities with elected councils may be created.  As such, only Antwerp, having over 500,000 inhabitants, became subdivided into nine districts (Dutch: "districten" ).  The Belgian arrondissements (also in French as well as in Dutch), an administrative level between province (or the capital region) and municipality, or the lowest judicial level, are in English sometimes called districts as well.

Bafia: Bafia is a Cameroonian town and commune in the Centre Province region.  It is the capital of the Mbam-et-Inoubou department.  It lies 120 km north of the country's capital Yaoundé.  Bafia has approximately 55,700 inhabitants, making it the third largest city in the province after Yaoundé and Mbalmayo.  Most citizens belong to either the Bafia people or the Yambassa people.  It is the see of the eponymous diocese.

Berdychiv: Berdychiv (Ukrainian: Бердичів , Polish: Berdyczów, Russian: Берди́чев , "Berdíchev") is a historic city in the Zhytomyr Oblast (province) of northern Ukraine.  Serving as the administrative center of the Berdychiv Raion (district), the city itself is of direct oblast subordinance, and does not belong to the district.  It is located 44 km south of the oblast capital, Zhytomyr.  Population:  (2013 est.)

Meuse-Inférieure: Meuse-Inférieure ("Lower Meuse"; Dutch: "Nedermaas" or "Beneden-Maas"; German: "Niedermaas" ) was a department of the First French Empire in present-day Belgium, Netherlands and Germany.  It was named after the river Meuse.  Its capital was Maastricht.  Its territory corresponded largely with the present-day provinces of Belgian and Dutch Limburg.

Milne Bay Province: Milne Bay is a province of Papua New Guinea.  Its capital is Alotau.  The province covers 14,345 km² of land and 252,990 km² of sea, within the province there are more than 600 islands, about 160 of which are inhabited.  The province has about 276,000 inhabitants, speaking about 48 languages, most of which belong to the Eastern Malayo-Polynesian branch of the Austronesian language family.  Economically the province is dependent upon tourism, oil palm, and gold mining on Misima Island; in addition to these larger industries there are many small-scale village projects in cocoa and copra cultivation.  The World War II Battle of Milne Bay took place in the province.

Question: What province does the capital of Meuse-Inférieure belong to?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "historical_department": {
      "type": "string",
      "description": "The name of the historical department."
    },
    "capital_city": {
      "type": "string",
      "description": "The capital city of the historical department."
    },
    "current_province": {
      "type": "string",
      "description": "The current province to which the capital city belongs."
    }
  },
  "required": [
    "historical_department",
    "capital_city",
    "current_province"
  ],
  "additionalProperties": false
}
