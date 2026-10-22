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
Colonel Jack: Colonel Jack is a novel by Daniel Defoe, first published in 1722.  The considerably longer title under which it was originally published is "The History and Remarkable Life of the truly Honourable Col. Jacque, commonly call<nowiki>'</nowiki>d Col. Jack, who was Born a Gentleman, put <nowiki>'</nowiki>Prentice to a Pick−Pocket, was Six and Twenty Years a Thief, and then Kidnapp<nowiki>'</nowiki>d to Virginia, Came back a Merchant; was Five times married to Four Whores; went into the Wars, behav<nowiki>'</nowiki>d bravely, got Preferment, was made Colonel of a Regiment, came over, and fled with the Chevalier, is still abroad compleating a Life of Wonders, and resolves to dye a General."

Battle of Black Jack: The Battle of Black Jack took place on June 2, 1856, when anti-slavery forces, led by the noted abolitionist John Brown, attacked the encampment of Henry C. Pate near Baldwin City, Kansas.  The battle is cited as one incident of "Bleeding Kansas" and a contributing factor leading up to the American Civil War of 1861 to 1865.

Post-Soviet conflicts: This article lists the Post-Soviet conflicts, the violent political and ethnic conflicts in the countries of the former Soviet Union since shortly before its official breakup in December 1991.  Some of these conflicts such as the 1993 Russian constitutional crisis or the 2013 Euromaidan protests in Ukraine were due to political crises in the successor states.  Others involved separatist movements attempting to break away from one of the successor states.  Some of these conflicts ended in a stalemate or without a peace treaty, and are referred to as frozen conflicts.  This means that a number of former-Soviet states are left sovereign over the entirety of their territory in name only.  In reality, they do not exercise full control over areas still under the control of rebel factions.  Rebel groups are essentially left independent over large chunks of the territories they claim.  In many instances, they have created institutions which are similar to those of fully fledged independent states, albeit with little or no international recognition.  Notable such cases include Abkhazia and South Ossetia in Georgia; Nagorno-Karabakh on the border between Azerbaijan and Armenia; Transnistria in land near to Moldova's eastern border with Ukraine; and Novorossiya (a confederation of the Donetsk People's Republic and the Luhansk People's Republic, breakaway areas in Ukraine).  The Republic of Crimea is also arguably part of this group of unrecognised states, as the annexation of Crimea by the Russian Federation remains unrecognized by a majority of UN member states and is contested by the government of Ukraine.

East-Central Kansas: East-Central Kansas is a region of Kansas.  Extending roughly from Osage County, Franklin County, and Miami County in the north to Coffey County, Anderson County and Linn County in the south.  The eastern border is Missouri.  The region then extends westward towards the Flint Hills to Lyon County.  The region is rich with Kansas history, as many locations of this region saw battles in Bleeding Kansas.  The infamous abolitionist John Brown and his men battled in Osawatomie.  The region geographically features rolling hills and deep forested river valleys.  The main crop of this predominantly agricultural region is corn.  Much of the area is powered by Wolf Creek Nuclear Generating Station which is located near Burlington.  The area is more forested and more moist compared to the rest of the state.

August Bondi: August Bondi (Jewish name Anshl)(July 21, 1833, Vienna, Austria – 1907, United States) was involved in what he called the Border War, but is now usually called Bleeding Kansas, and latter the American Civil War.  In Kansas he fought with abolitionist John Brown.

List of Stargate SG-1 episodes: "Stargate SG-1" is a Canadian-American military science fiction television series created by Brad Wright and Jonathan Glassner.  The series resumes the story of the 1994 "Stargate" film, where a military team led by Colonel Jack O'Neill and supported by the archeologist Daniel Jackson use an ancient alien artifact called the Stargate to travel to a planet where an alien named Ra oppressed the planet's people by posing as a god.  After the Earth team defeated Ra, O'Neil returns to Earth while Daniel Jackson stays on the planet.  The series pilot, which takes place roughly one year after the events of the film, reveals that Ra was not the only alien to use Stargates to transport human slaves to many worlds for thousands of years.

John D. Henderson: John D. "Colonel Jack" Henderson was an American editor, rancher, businessman, and pro-slavery politician in the Kansas Territory.  He was a Colonel in the Border Wars of Bleeding Kansas.

Bleeding Kansas: Bleeding Kansas, Bloody Kansas or the Border War was a series of violent political confrontations in the United States between 1854 and 1861 involving anti-slavery "Free-Staters" and pro-slavery "Border Ruffian", or "southern" elements in Kansas.

Battle of Osawatomie: The Battle of Osawatomie took place on August 30, 1856 when 250-400 Border Ruffians led by John W. Reid attacked the town of Osawatomie.  Reid was intent on destroying the free state settlement and then moving on to Topeka and Lawrence to do more of the same.  John Brown first learned of the raiders when they shot his son Frederick.  With 40 or so men, Brown tried to defend the town against the pro-slavery partisans, but had to withdraw; the town of Osawatomie was then looted and burned.  This was one event in series of clashes between abolitionists and pro-slavery Missourians in what has been known as Bleeding Kansas.

John Brown (abolitionist): John Brown (May 9, 1800 – December 2, 1859) was an American abolitionist who believed and advocated that armed insurrection was the only way to overthrow the institution of slavery in the United States.  Brown first gained attention when he led small groups of volunteers during the Bleeding Kansas crisis of 1856.  Dissatisfied with the pacifism of the organized abolitionist movement, he said, "These men are all talk.  What we need is action—action!"  During the Kansas campaign, Brown commanded forces at the Battle of Black Jack and the Battle of Osawatomie.  He and his supporters killed five supporters of slavery in the Pottawatomie massacre of May 1856 in response to the sacking of Lawrence by pro-slavery forces.

Question: John D. "Colonel Jack" Henderson was a Colonel in the Border Wars of Bleeding Kansas, a series of violent political confrontations in the United States between what years?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "conflict_name": {
      "type": "string",
      "description": "The name of the historical conflict."
    },
    "start_year": {
      "type": "integer",
      "description": "The starting year of the conflict."
    },
    "end_year": {
      "type": "integer",
      "description": "The ending year of the conflict."
    },
    "conflict_description": {
      "type": "string",
      "description": "A brief description of the nature of the conflict."
    }
  },
  "required": [
    "conflict_name",
    "start_year",
    "end_year",
    "conflict_description"
  ],
  "additionalProperties": false
}
