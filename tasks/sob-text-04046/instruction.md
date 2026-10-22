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
Dark Holler: Old Love Songs and Ballads: Dark Holler: Old Love Songs and Ballads is a 2005 compilation album released by Smithsonian Folkways.  The album is composed of Appalachian folk music 1960's recordings made and compiled by musicologist John Cohen in Madison County, North Carolina.  Most of the songs are done in an a cappella style.

William A. Barnhill: William A. Barnhill (November 26, 1889 – December 7, 1987) was an American photographer best known for his work in the Appalachian Mountains of western North Carolina in the early 1900s.  His love of hiking and photography took him to the mountains of western North Carolina between 1914 and 1917.  The photographs he took during those trips have been featured in "American Heritage" and "Life" magazines, as well as in the collections of the Library of Congress, the New York Public Library, the Pack Memorial Public Library of Asheville, North Carolina, and various college libraries.

Wallin Family: The Wallin Family is an American family of traditional ballad singers from Madison County, North Carolina.  Their repertoire of Appalachian folk ballads— many of which were rooted in "Old World" ballads traceable to the British Isles— brought them to the attention of folk music enthusiasts during the American folk music revival of the 1960s.  Wallin family members have recorded numerous times over a period of nearly four decades, and have appeared in several independent documentaries.

Dock Boggs: Moran Lee "Dock" Boggs (February 7, 1898 – February 7, 1971) was an influential old-time singer, songwriter and banjo player.  His style of banjo playing, as well as his singing, is considered a unique combination of Appalachian folk music and African-American blues.  Contemporary folk musicians and performers consider him a seminal figure, at least in part because of the appearance of two of his recordings from the 1920s, "Sugar Baby" and "Country Blues", on Harry Smith's 1951 collection "Anthology of American Folk Music".  Boggs was first recorded in 1927 and again in 1929, although he worked primarily as a coal miner for most of his life.  He was "rediscovered" during the folk music revival of the 1960s and spent much of his later life playing at folk music festivals and recording for Folkways Records.

High Atmosphere: High Atmosphere: Ballads and Banjo Tunes from Virginia and North Carolina is a 1975 compilation album released by Rounder Records.  The album is composed of Appalachian folk music recordings gathered by musicologist John Cohen in North Carolina and Virginia in 1965.

Emmy Rossum: Emmanuelle Grey "Emmy" Rossum (born September 12, 1986) is an American actress and singer-songwriter.  She is known for the Phantom of the Opera (2004), and her portrayal of Fiona Gallagher in the television series "Shameless".  Rossum has starred in movies including "Songcatcher" (2000), "An American Rhapsody", (2001) and "Passionada" (2002).  Her role in "Mystic River" (2003) garnered her wider recognition.  She starred in the science fiction film "The Day After Tomorrow" (2004) and received critical acclaim for her performance in the leading role of Christine Daaé in "The Phantom of the Opera" (2004).  She has since starred in "Poseidon" (2006), "Dragonball Evolution" (2009), "Dare" (2009), "Beautiful Creatures" (2013), "Before I Disappear" (2014), "You're Not You" (2014) and "Comet" (2014).

Appalachian temperate rainforest: The Appalachian temperate rainforest is located in the southern Appalachian Mountains of the eastern U.S.  About 351,500 square kilometers (135,000 square miles) of forest land is spread across southwestern Virginia, western North Carolina, northern Georgia, and eastern Tennessee.  The annual precipitation is more than 60 inches (over 1500mm).  The Southern Appalachian spruce–fir forest is a temperate rainforest located in the higher elevations in southwestern Virginia and western North Carolina.  Fir is dominant at higher elevation, spruce at middle elevation, and mixed forests at low elevation.

Songcatcher: Songcatcher is a 2000 drama film directed by Maggie Greenwald.  It is about a musicologist researching and collecting Appalachian folk music in the mountains of western North Carolina.  Although "Songcatcher" is a fictional film, it is loosely based on the work of Olive Dame Campbell, founder of the John C. Campbell Folk School in Brasstown, North Carolina, and that of the English folk song collector Cecil Sharp, portrayed at the end of the film as professor Cyrus Whittle.

Tweetsie Railroad: Opened in 1957, Tweetsie Railroad began as an excursion train ride pulled by steam locomotive #12, the only surviving narrow gauge engine of the East Tennessee and Western North Carolina Railroad (ET&WNC).  Built in 1917 by the Baldwin Locomotive Works, #12 is a narrow gauge 4-6-0 coal-fired locomotive that was used from 1918 to 1940 to haul passengers and freight over the ET&WNC's 66 mi line running through the Appalachian Mountains from Johnson City to Boone, North Carolina.  The name "Tweetsie" was given to the original East Tennessee and Western North Carolina Railroad by area residents who became accustomed to the shrill "tweet, tweet" of the train whistles that echoed through the mountains.  The nickname stuck with the railroad and its trains, and became more identifiable than the railroad's original name.

Western North Carolina: Western North Carolina (often abbreviated as WNC) is the region of North Carolina which includes the Appalachian Mountains, thus it is often known geographically as the state's Mountain Region.  It contains the highest mountains in the Eastern United States.  Western North Carolina is sometimes included with upstate South Carolina as the "Western Carolinas", which is also counted as a single media market.  The region covers an area of about 11000 sqmi , and is roughly the size of the state of Massachusetts.  The population of the region, as measured by the 2010 U.S. Census, is 1,473,241, which is approximately 15% of North Carolina's total population.

Question: What year did Emmy Rossum star in a film about a musicologist researching and collecting Appalachian folk music in the mountains of western North Carolina?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "film_title": {
      "type": "string",
      "description": "The title of the film."
    },
    "film_release_year": {
      "type": "integer",
      "description": "The year the film was released."
    },
    "film_plot_summary": {
      "type": "string",
      "description": "A summary of the film's plot related to the question."
    },
    "actor_name": {
      "type": "string",
      "description": "The name of the actor who starred in the film."
    },
    "year_actor_starred": {
      "type": "integer",
      "description": "The year the actor starred in the film."
    }
  },
  "required": [
    "film_title",
    "film_release_year",
    "film_plot_summary",
    "actor_name",
    "year_actor_starred"
  ],
  "additionalProperties": false
}
