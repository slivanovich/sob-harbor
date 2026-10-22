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
Van Wesenbekestraat: Chinatown is located on Van Wesenbekestraat a street in Antwerp, Belgium.  Historically supporting the Chinese community that settled in Antwerp post-World War II, today Chinatown is well known for its pan-Asian atmosphere.  The district houses an abundance of restaurants offering a variety of Asian cuisines such as Chinese, Japanese, Indian, Pakistani, Thai and Nepali.  Pan-Asian organisations and businesses supporting the Chinese, Nepali, Indonesian and Filipino communities for example are found throughout the district and the biggest Asian supermarket in the country (named "Sun Wah" which stocks items from China, Thailand, Japan, Korea, Philippines, Malaysia, Singapore, Vietnam, Indonesia and India) is also found in Chinatown.  A Buddhist temple and a school for mastering kungfu are other commodities also found in the district.  Chinese presence is still dominant.  However, traders from Thailand, Nepal and other Asian countries have also settled in the district resulting in some dubbing it as Asiatown to reflect the changing demographics.  Both at the entrance and the end of the street, two Chinese lions guard the street.  A paifang known as the "Pagodepoort" (Pagoda Gate) was erected at the southern entrance to the street in 2010 after four years of planning.

Diaoyu Fortress: The Diaoyu Fortress or Diaoyucheng () is one of the great ancient battlefields of China, located on the Diaoyu Mountain in Heyang Town, Hechuan District, Chongqing.  It is famous for its resistance to the Mongol armies in the latter half of the Song Dynasty.  One of the most notable events was the death of Mongol leader Möngke Khan near the city, which forced the immediate withdrawal of Mongol troops from Syria and East Asia and prevented the Mongolian Empire from expanding towards Africa.

Oxford Commercial Historic District: The Oxford Commercial Historic District is a nationally recognized historic district located in Oxford, Iowa, United States.  It was listed on the National Register of Historic Places in 1997.  At the time of its nomination it consisted of 20 resources, which included 16 contributing buildings and four non-contributing buildings.  This district reflects a typical central business district found in a Midwest town.  It represents a transitional period from a frontier town to a settled community, and from the horse as the primary means of transportation to the automobile and mechanized farming.  Most of the buildings in Oxford's business district were constructed between 1883 and 1917.  Some replaced the wood frame structures from the town's frontier days, while others replaced those destroyed by a major fire that consumed the north side of the district in 1890.  They are one to two stories in height, and their exteriors are composed of common brick.  While simple in composition, many feature ornate decorative cornices.  The Italianate and Romanesque Revival styles dominate.

Similkameen Country: The Similkameen Country, also referred to as the Similkameen Valley or Similkameen District, but generally referred to simply as The Similkameen or more archaically, Similkameen, is a region roughly coinciding with the basin of the river of the same name in the Southern Interior of British Columbia.  The term "Similkameen District" also refers to the Similkameen Mining District, a defunct government administrative district, which geographically encompasses the same area, and in more casual terms may also refer to the Similkameen electoral district, which was combined with the Grand Forks-Greenwood riding by the time of the 1966 election.  The Similkameen Country has deep historical connections to the Boundary Country and the two are sometimes considered one region, partly as a result of the name of the electoral district.  It is also sometimes classed as being part of the Okanagan region, which results from shared regional district and other administrative boundaries and names.  The term "Similkameen District" may also historically refer to the Similkameen Division Yale Land District, which also includes Osoyoos and the Boundary Country to Osoyoos' east.

Maimal: Maimal are a Muslim community found in the state of Assam in India.  They are a community of inland fishermen found in Western Assam.  A few are also found in the Sylhet District of Bangladesh.  It should be worth mentioned that the "Maimal" were there in Shylhet district in the undivided India, and after the Independence some parts of that Shylhet district were merged with the state of Assam in free India.  Now, this community people are spreading more or less everywhere in the Barak Valley districts in Assam.

Hezhou Prefecture: Hezhou or He Prefecture (合州) was a "zhou" (prefecture) in imperial China centering on modern Hechuan District, Chongqing, China.  It existed (intermittently) from 556 to 1913.

Hechuan District: Hechuan () is a district in the northern part of Chongqing Municipality, People's Republic of China, located at the meeting point of the Jialing, Fu and Qu rivers, with a history of 1,500 years.  Hechuan is 54 km away from downtown Chongqing's Yuzhong District.

De Huet: De Huet is a large district found in the city of Doetinchem, mostly built in the 1980s.  The district is found south-west of the city centre, and south of the Oude IJssel river.

Religion in Nigeria: Nigeria, the most populous African country (with a population of over 182 million in 2015), is nearly equally divided between Christianity and Islam, though the exact ratio is uncertain.  There is also a growing population of non-religious Nigerians who accounted for the remaining 5 percent.  The majority of Nigerian Muslims are Sunni and are concentrated in the northern region of the country, while Christians dominate in the south.  The Pew Forum in a 2010 report compared reports from several sources.  The 1963 Nigerian census found that 36% of the population was Christian, 38% Muslim, and 26% other; the 2008 MEASURE Demographic and Health Survey (DHS) found 53% Muslim, 45% Christian, and 2% other; the 2008 Afrobarometer poll found 50% Christian, 49% Muslim, and 1% other; Pew's own survey found 52% Muslim, 46% Christian, and 1% other.

Wenling: Wenling (Wenling dialect: Uen-lin Zy ] ; ) is a coastal county-level city in the municipal region of Taizhou, in southeastern Zhejiang province, China.  It borders Luqiao and Huangyan to the north, Yuhuan to the south, Yueqing to the west, looks out to the East China Sea to the east.  Wenling locates on 28°22'N, 121°21'E, approximately 300 km south of Shanghai.

Question: What country are both Wenling and Hechuan District found in?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "country_name": {
      "type": "string",
      "description": "The name of the country where both locations are found."
    },
    "locations_found": {
      "type": "array",
      "description": "A list of the locations specified in the question.",
      "items": {
        "type": "string"
      }
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of how the country was identified for both locations."
    }
  },
  "required": [
    "country_name",
    "locations_found",
    "reasoning"
  ],
  "additionalProperties": false
}
