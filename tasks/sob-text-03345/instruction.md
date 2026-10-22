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
Statistical inference: Statistical inference is the process of deducing properties of an underlying probability distribution by analysis of data.  Inferential statistical analysis infers properties about a population: this includes testing hypotheses and deriving estimates.  The population is assumed to be larger than the observed data set; in other words, the observed data is assumed to be sampled from a larger population.

Riverview, New Brunswick: Riverview is a Canadian town in Albert County, New Brunswick, Canada.  Riverview is located on the south side of the Petitcodiac River, across from the larger cities of Moncton and Dieppe.  Riverview has an area of 34 km2 , and a population density of 564.6 PD/km2 .  Riverview's slogan is "A Great Place To Grow".  With a population of 19,667, Riverview is the fifth largest municipality in New Brunswick, having a larger population than the cities of Edmundston, Bathurst, Campbellton, and Miramichi, despite its designation of "town".

Elkhart, Indiana: Elkhart is a city in Elkhart County, Indiana, United States.  The city is located 15 mi east of South Bend, Indiana, 110 mi east of Chicago, Illinois, and 150 mi north of Indianapolis, Indiana.  Elkhart has the larger population of the two principal cities of the Elkhart-Goshen Metropolitan Statistical Area, which in turn is part of the South Bend-Elkhart-Mishawaka Combined Statistical Area, in a region commonly known as Michiana.  The population was 50,949 at the 2010 census.  Despite the shared name, it is not the county seat of Elkhart County; that position is held by the city of Goshen, located about 10 mi southeast of Elkhart.

Wollongong: Wollongong ( ), informally referred to as "The Gong", is a seaside city located in the Illawarra region of New South Wales, Australia.  Wollongong lies on the narrow coastal strip between the Illawarra Escarpment and the Pacific Ocean, 82 kilometres (51 miles) south of Sydney.  Wollongong had an estimated urban population of 295,842 at June 2016, making it the third largest city in New South Wales after Sydney and Newcastle, and the tenth largest city in Australia.

Paisley, Florida: Paisley is a census-designated place (CDP) in Lake County, Florida, United States.  The population was 734 at the 2000 census.  It is part of the Orlando–Kissimmee Metropolitan Statistical Area.  Paisley is home to Boy Scout Camp La-No-Che on the north shore of Lake Norris, which at times during the summer and other special events has a larger population than the CDP itself.

Walpole (CDP), Massachusetts: Walpole is a small census-designated place (CDP) located within the much larger town (21 square miles in size) of Walpole in Norfolk County, Massachusetts, United States.  Walpole Town as it is called by the US Census Bureau, also includes a much larger population (24,070 in 2010).  The population of the Census Designated Place was 5,918 at the 2010 census.

Woodinville, Washington: Woodinville is a city in King County, Washington, United States.  The population was 10,938 at the 2010 census.  It is part of the Seattle metropolitan area.  There is also a much larger population with Woodinville mailing addresses in adjacent unincorporated areas of King (Cottage Lake) and Snohomish (Maltby) counties.  Woodinville has waterfront parks on the Sammamish River, sweeping winery and brewery grounds, and densely wooded residential areas.

Founder effect: In population genetics, the founder effect is the loss of genetic variation that occurs when a new population is established by a very small number of individuals from a larger population.  It was first fully outlined by Ernst Mayr in 1942, using existing theoretical work by those such as Sewall Wright.  As a result of the loss of genetic variation, the new population may be distinctively different, both genotypically and phenotypically, from the parent population from which it is derived.  In extreme cases, the founder effect is thought to lead to the speciation and subsequent evolution of new species.

Coniston, New South Wales: Coniston is a suburb of Wollongong in New South Wales.  At the 2016 census , it had a population of 2,268.

Shia Muslims in the Arab world: Islam is historically divided into two major sects, Sunni and Shia Islam, each with its own sub-sects.  Large numbers of Shia Arab Muslims live in some Arab countries including Lebanon, Yemen, Iraq, Saudi Arabia, Kuwait, Oman, the UAE, and Qatar.  Shia Muslims are a numerical majority in Iraq and Bahrain.  Approximately half of the population in Yemen are Shia Muslims.  Exactly half of Muslims in Lebanon are Shia Muslims.  There is also a very large population of Shia Muslims living in the Arab Persian Gulf countries especially in Saudi Arabia.  Approximately the whole population of East Saudi Arabia, the Eastern Province are Shia Muslims.  Although government statistics claim that roughly only 20-40% of the Muslim population are Shia Muslims, there has been dispute to the authenticity of this figure and recent reports and investigations indicate that there is in fact a much larger population of Shia Muslims present, with estimate figures over 45% or even making the majority of Muslim population.  Saudi Arabia follows a strict recently established sect of Islam, Wahhabism, there is little freedom of religion between the different sects even whilst all of the population are Muslims.  Smaller Shia groups are present in Egypt and Jordan.  Despite the heavy presence of Shia Muslims in some Arab countries, particularly among the population of the Persian Gulf Arab countries, they have been treated poorly throughout history.  Additionally, in recent times, Shia Muslims along with Kurds have faced genocide by the pan-Arabist regime of Saddam Hussein.  For both historical and political reasons, the Shia have fared rather poorly in much of the Arab world, and the topic of Shi‘ism and Shia groups is one of the most sensitive issues for the Sunni elite.  This article discusses both the history of Shī‘a Islam in the Arab world from the dawn of Islam and their current situation in the Arabic-speaking world.

Question: In what year did the census show that Wollongong had a larger population that Coniston?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "census_year": {
      "type": "integer",
      "description": "The year the census was conducted for both locations."
    },
    "city_with_larger_population": {
      "type": "string",
      "description": "The name of the city that had the larger population."
    },
    "city_with_larger_population_count": {
      "type": "integer",
      "description": "The population count of the city with the larger population."
    },
    "city_with_smaller_population": {
      "type": "string",
      "description": "The name of the city that had the smaller population."
    },
    "city_with_smaller_population_count": {
      "type": "integer",
      "description": "The population count of the city with the smaller population."
    },
    "population_difference": {
      "type": "integer",
      "description": "The difference in population between the two cities."
    }
  },
  "required": [
    "census_year",
    "city_with_larger_population",
    "city_with_larger_population_count",
    "city_with_smaller_population",
    "city_with_smaller_population_count",
    "population_difference"
  ],
  "additionalProperties": false
}
