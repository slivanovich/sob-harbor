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
Hein van Aken: Hein van Aken, also called Hendrik van Aken or van Haken, was the parish priest in Korbeek-Lo, between Leuven and Brussels.  He was born in Brussels, probably in the thirteenth century.  He translated the "Roman de la Rose" by Guillaume de Lorris and Jean de Meun to Dutch, with the title "Het Bouc van der Rosen", and is probably also the poet of the "Historie van Saladyn".  With less reason, some also attribute the "Natuurkunde van het Geheel-al" to him, but a poem by him must be kept in the Comburger manuscript.  In the "Leeckenspeigel", some work by him has been intertwined, amongst others his rhymed essay "Over de Dichtkunst" ("On Poetry"), which has been called remarkable by skilled reviewers because of the common sense that prevails in it.

Flemish people: The Flemish or Flemings (Dutch: "Vlamingen" ) are a Germanic ethnic group native to Flanders, in modern Belgium, who speak Dutch, especially any of its dialects spoken in historical Flanders, known collectively as Flemish Dutch.  They are one of two principal ethnic groups in Belgium, the other being the French-speaking Walloons.  Flemish people make up the majority of the Belgian population (about 60%).  Historically, all inhabitants of the medieval County of Flanders were referred to as "Flemings", irrespective of the language spoken.  The contemporary region of Flanders comprises a part of this historical county, as well as parts of the medieval duchy of Brabant and the medieval county of Loon.

Dutch people: The Dutch (Dutch:    ), occasionally referred to as Netherlanders—a term that is cognate to the Dutch word for Dutch people, "Nederlanders"—are a Germanic ethnic group native to the Netherlands.  They share a common culture and speak the Dutch language.  Dutch people and their descendants are found in migrant communities worldwide, notably in Aruba, Suriname, Guyana, Curaçao, Chile, Argentina, Brazil, Canada, Australia, South Africa, New Zealand, and the United States.

Jan van Aken (writer): Jan van Aken (Herwen en Aerdt, August 9, 1961) is a Dutch writer, who worked in the cultural sector and in automation.  He is currently a docent at the Schrijversvakschool in Amsterdam.

Jan van Aken (politician): Jan Paul van Aken (born 1 May 1961 in Reinbek) is a German activist for Greenpeace and a politician with the Left Party.  He is a member of the Foreign Affairs Committee and the Subcommittee on Disarmament, Arms Control and Non-Proliferation in the German Bundestag.  Jan van Aken entered the 17th Bundestag in 2009 after he was listed on the Left electoral lists in Hamburg.  Since June 2012 he has been a deputy chairperson of the Left Party.  He was one of the eight lead candidates for the Left in the 2013 federal election and was therefore also elected to the 18th Bundestag.

Jan van Steffeswert: Jan van Steffeswert or alternatively Jan van Steffenswert or Jan van Stevensweert (born c. 1460 - died c. 1531) was a Flemish sculptor and woodcarver based in Maastricht.  Contrary to the customs of the time, he signed almost all the works he produced using variously Jan Bieldesnider, Jan van Weerd or Jan van Steffeswert.  To date, fourteen works have been positively identified as his. .

Lee – Van Aken (RTA Rapid Transit station): Lee - Van Aken is a station on the RTA Blue Line in Cleveland, Ohio, USA.  It is located at the intersection of Lee Road and Van Aken Boulevard in Shaker Heights.

Germans: Germans (German: "Deutsche" ) are a Germanic ethnic group native to Germany and other parts of Central Europe, who share a common German ancestry, culture and history.  German is the shared mother tongue of a substantial majority of ethnic Germans.

Luxembourgers: Luxembourgers are a Germanic ethnic group native to Luxembourg who share the culture of Luxembourg, speak Luxembourgish and are of Luxembourgish descent.  Luxembourgers were, much like Austrians, historically considered to be a regional subgroup of ethnic Germans and viewed themselves as such until the collapse of the German Confederation.  Following the collapse of the confederation, Duchy of Luxembourg entered a personal union with the Netherlands through Treaty of London in 1839; the union ended in 1890.

Jan van Beers (artist): Jean Marie Constantin Joseph "Jan" van Beers (27 March 1852 – 17 November 1927) was a Belgian painter and illustrator, the son of the poet Jan van Beers.  They are sometimes referred to as "Jan van Beers the elder" and "Jan van Beers the younger".  In 1884, Jan Van Beers produced the pen-and-ink sketches for the "edition de luxe" of his father's poetry.

Question: Jan van Aken is a writer belonging to which Germanic ethnic group native to the Netherlands?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "person_name": {
      "type": "string",
      "description": "The name of the person."
    },
    "occupation": {
      "type": "string",
      "description": "The occupation of the person."
    },
    "ethnic_group": {
      "type": "string",
      "description": "The Germanic ethnic group the person belongs to."
    },
    "ethnic_group_native_to": {
      "type": "string",
      "description": "The country or region where the ethnic group is native to."
    }
  },
  "required": [
    "person_name",
    "occupation",
    "ethnic_group",
    "ethnic_group_native_to"
  ],
  "additionalProperties": false
}
