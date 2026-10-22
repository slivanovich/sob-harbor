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
Revolutions of 1830: The Revolutions of 1830 were a revolutionary wave in Europe which took place in 1830.  It included two "romantic nationalist" revolutions, the Belgian Revolution in the United Kingdom of the Netherlands and the July Revolution in France along with revolutions in Congress Poland and Switzerland.  It was followed eighteen years later, by another and possibly even stronger wave of revolutions known as the Revolutions of 1848.

Dignity Battalions: The Dignity Battalions were a paramilitary militia created by Panama's government in the 1980s to help defend Panama against both invasion by the United States and internal subversive activity.  They were formed in early April 1988 and were de facto dissolved along with the Panamanian Defense Forces on February 10, 1990.

The Netherlands in World War I: The Kingdom of the Netherlands was neutral during World War I.  This was part of a strict policy of neutrality in international affairs that started in 1830 with the secession of Belgium, or the Southern Netherlands, from the north.  It would end with the German invasion of 10 May 1940.  In World War I the Netherlands would be in a tight spot as the country was relatively close to the Western Front and geographically positioned in between the German Empire, German-occupied Belgium and the United Kingdom.  Both warring factions would regularly intimidate the Netherlands and put demands on it.

List of Belgian classical composers: This is a list of Belgian classical composers, alphabetically sorted by surname, then by other names.  It includes composers of classical music who were born within Belgium (after the establishment of the country in 1830) or became permanent residents there.  It also includes those living before 1830 who were born or resident within the borders of modern Belgium (see Southern Netherlands).

Colonel Borremans: Colonel Borremans (also known as Van den Elsken) founded a unit of volunteers, known as Les Chasseurs de Bruxelles (the Hunters of Brussels), at the time of the 1830 Belgian revolution, a coup that led to the separation of the provinces of the South from the United Kingdom of the Netherlands and therefore to the birth of the present Belgian state.  Borremans participated in the attempts of the Orangist party to put an end to the acts of the usurpers.

Louis de Potter: Louis Joseph Antoine de Potter (26 April 1786 – 22 July 1859), was a Belgian journalist, revolutionary, politician and writer.  Out of the more than 100 books and pamphlets, one of the most notable works was his famous "Letter to my Fellow Citizens" in which he promoted democracy, universal electoral rights and the unity among Belgian liberals and Catholics.  As one of the heroes of the Belgian Revolution, he proclaimed the independence of Belgium from the Netherlands (from the terrace of the Brussels City Hall on 28 September 1830), and inaugurated the first Belgian parliamentary assembly (on 10 November 1830), on behalf of the outgoing Belgian provisional government.

Orangism (Belgium): Orangism was a political current in what is now Belgium that supported its inclusion in the short-lived United Kingdom of the Netherlands (1815–1830).  After the secession of Belgium in 1830, Orangist sentiment in Flanders and Wallonia for a time sought a restoration of the United Kingdom of the Netherlands.  It was a movement directed by William I of the Netherlands as part of his "Volhardingspolitiek" and containing most of the Belgian elites (nobility, industrials).  Some of the most prominent Flemish Orangists were Jan Frans Willems and Hippolyte Metdepenningen.  Although refusing the partake in parliamentary elections as they deemed the Belgian institutions as illegitimate, the Orangists did take part in local elections (province and municipal) from which they activated against the new Belgian state through political actions and an activist press.  At least three Orangist coups were foiled during the 1830s.  Although losing Dutch financial and political support after the Treaty of London (1839) and William I's abdication (1840), the weakening Belgian Orangism survived well into the 1850s, strongly opposing the Belgian Revolution and rallying against independence.

Garde Civique: The Garde Civique or Burgerwacht (French and Dutch; "Civic Guard") was a Belgian paramilitary militia created in October 1830 shortly after the Belgian Revolution.  The "Garde" was founded through the amalgamation of various militia groups created by the middle classes during the anarchy following the revolution.  It acted as a quasi-military "gendarmerie", with the primary role of maintaining social order within Belgium, until its disestablishment in 1920.

Belgian Revolution: The Belgian Revolution (French: "Révolution belge" , Dutch: "Belgische Revolutie/opstand/omwenteling" , German: "Belgische Revolution" ) was the conflict which led to the secession of the southern provinces (mainly the former Southern Netherlands) from the United Kingdom of the Netherlands and the establishment of an independent Kingdom of Belgium.

Iron Cross (Belgium): The Iron Cross (French: "Croix de fer" , Dutch: "IJzeren Kruis" ) was established by law in 1833 following the end of the Belgian Revolution to recognise serious wounds received and bravery in battle by Belgian citizens taking part in the fight for Belgian independence from the United Kingdom of the Netherlands between 25 August 1830 and 4 February 1831.  A further royal decree of 22 August 1834 created a second class to the Iron Cross for award to all wounded combatants.  Due to the lower perceived importance of the second class award and discontent among recipients, the Iron Cross second class was short lived and amalgamated to the Iron Cross first class by decree of 21 February 1835.  All recipients now received the (original) first class award.

Question: The Garde Civique or Burgerwacht, was a Belgian paramilitary militia created in October 1830 shortly after the Belgian Revolution, it was the conflict which led to the secession of the southern provinces (mainly the former Southern Netherlands) from the United Kingdom of the Netherlands and the establishment of an independent Kingdom of which country nation?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "revolution_name": {
      "type": "string",
      "description": "The name of the revolution that led to the country's independence."
    },
    "year_of_revolution": {
      "type": "integer",
      "description": "The year the revolution took place or concluded, leading to the new state."
    },
    "established_country": {
      "type": "string",
      "description": "The name of the independent kingdom established as a result of the revolution."
    },
    "seceded_from_country": {
      "type": "string",
      "description": "The country from which the new kingdom seceded."
    },
    "outcome_summary": {
      "type": "string",
      "description": "A brief summary of the political outcome of the revolution."
    }
  },
  "required": [
    "revolution_name",
    "year_of_revolution",
    "established_country",
    "seceded_from_country",
    "outcome_summary"
  ],
  "additionalProperties": false
}
