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
Mağara, Silifke: Mağara (former Mara or Kırobası) is a village in Silifke district of Mersin Province, Turkey.  It is situated in the Taurus Mountains.  It is about 45 km from Silifke and 125 km from Mersin.  The population of village is 233 as of 2010, but boasted a much higher population during medieval times.  The Greeks who made up a part of the population were deported to Greece during the compulsory population exchange between Greece and Turkey (Turkish: "mübadele" ) in 1920s.  Modern day Mağara is known for its annual commemoration day for Marshal Fevzi Çakmak.

Racial threat: Broadly speaking, the term racial threat refers to how people react to those of a different race.  More specifically, the racial threat hypothesis or racial threat theory proposes that a higher population of members of a minority race results in the dominant race imposing higher levels of social control on the subordinate race, which, according to this hypothesis, occurs as a result of the dominant race fearing the subordinate race's political, economic, or criminal threat.  Research has shown a strong association between the size of a state's nonwhite prison population and the likelihood of that state enacting a felon disenfranchisement law, which supports a link between racial threat and the passage of such laws.

Datong: Datong () is a prefecture-level city in northern Shanxi province, People's Republic of China, located in a basin at an elevation of 1040 m and bordering Inner Mongolia to the north and west and Hebei to the east.  It had a population of 3,318,057 at the 2010 census of whom 1,629,035 lived in the built up area made of 3 out of 4 urban districts, namely Chengqu, Kuangqu and Nanjiao District.

Demography of the United Kingdom: According to the 2011 census, the total population of the United Kingdom was around 63,182,000. <ref name="2http://www.ons.gov.uk/ons/dcp171778_292378.pdf |title=2011 Census: Population Estimates for the United Kingdom |publisher=Office for National Statistics |date=27 March 2011 |accessdate=18 December 2012 }}</ref> It is the 22nd-largest in the world.  Its overall population density is 259 people per square kilometre (671 people per sq mi), with England having a significantly higher population density than Wales, Scotland and Northern Ireland.  Almost one-third of the population lives in England's southeast, which is predominantly urban and suburban, with about 8 million in the capital city of London, the population density of which is just over 5,200 per square kilometre (13,468 per sq mi).

Higher Population Council (Jordan): The Higher Population Council-General Secretariat (HPC/GS) is a specialized agency of the Jordanian government, acting as the authority for all reproductive health issues and programs in Jordan.  The HPC is headquartered in Amman, Jordan.  It was established on December 3, 2002 with a mandate to deal with the population challenges facing Jordan and to enhance the implementation of the National Population Strategy.

Lake View, Chicago: Lake View, also spelled Lakeview, is one of the 77 community areas of Chicago, Illinois, located on the city's North Side.  It is bordered by West Diversey Parkway on the south, West Irving Park Road on the north, North Ravenswood Avenue on the west, and the shore of Lake Michigan on the east.  The Uptown community area is to Lakeview's north, Lincoln Square to its northwest, North Center to its west and Lincoln Park to its south.  The 2014 population of Lakeview was 97,968 residents, making it the second largest of the Chicago community areas by population, following Austin which has 98,514 residents.  Lakeview, though, has a higher population density than the larger-in-area Austin neighborhood.

Permanent Population Committee: The Permanent Population Committee (PPC) (Arabic: اللجنة الدائمة للسكان) is a national authority in the state of Qatar whose mission is to realize the aptness of population requirements to sustainable development.  To do so, PPC bases its action on Islamic Sharia principles and communal values and traditions in line with the political foundations of the Qatar Permanent Constitution, the National Vision, the relevant Millennium Development Goals (MDGs), the Cooperation Council for the Arab States of the Gulf (GCC) Population Policies and other related regional and international guidelines.  The PPC is charged with the responsibility for the implementation of the outcomes identified by the general framework of the GCC population strategy adopted by the GCC Supreme Council during its Nineteenth Session, held in Abu Dhabi UAE in 1998.  This strategy prompted each member state to establish a higher population committee responsible for developing national population policies.  Accordingly, the PPC was established by the Council of Ministers decision number (24) in 2004 with defined responsibilities and committee membership.  His Highness Sheikh Tamim bin Hamad Al Thani, the Deputy Emir and Heir Apparent, endorsed the decision.

Eco-cities: An eco-city is a city built from the principles of living within environment means.  The ultimate goal of many eco-cities is to eliminate all carbon waste (zero-carbon city), to produce energy entirely through renewable resources, and to merge the city harmoniously with the natural environment; however, eco-cities also have the intentions of stimulating economic growth, reducing poverty, using higher population densities, and therefore obtaining higher efficiency, and improving health.

Zhuozhou: Zhuozhou () is a county-level city with 628,000 inhabitants in Hebei province, bordering Beijing to the north.  It is administered by Baoding prefecture-level city.  Zhuozhou has 3 subdistricts, 6 towns, 5 townships, and 1 development zone.

Repartition of Ireland: The repartition of Ireland has been suggested as a possible solution to the continuing political disagreement in Northern Ireland.  The essential problem was that the partition of Ireland was gerrymandered, and as a result Northern Ireland contains a large Irish nationalist minority.  Much of the Irish nationalist population lives in the south and west of the region, but a significant percentage lives in Belfast and some smaller communities in the north and east, whilst Irish unionists constitute a majority of the population in the north and east of the region with some smaller communities in the south and west.  The geographical area in which unionists are a majority is less than half of Northern Ireland (see graphic below), but eastern areas have a much higher population density.  Collectively, Northern Ireland is split, with unionists comprising approximately 48% of the population, and falling quickly.  At the last general election unionists secured precisely 50% of the seats.  None of these proposals are currently supported by any political party in Ireland.

Question: Which has the higher population Zhuozhou or Datong?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "comparison_result": {
      "type": "string",
      "description": "Indicates which city has the higher population."
    },
    "city_populations": {
      "type": "array",
      "description": "List of cities and their respective populations.",
      "items": {
        "type": "object",
        "properties": {
          "city_name": {
            "type": "string",
            "description": "Name of the city."
          },
          "population": {
            "type": "integer",
            "description": "Total population of the city."
          }
        },
        "required": [
          "city_name",
          "population"
        ],
        "additionalProperties": false
      }
    },
    "higher_population_city": {
      "type": "object",
      "description": "Details of the city with the higher population.",
      "properties": {
        "city_name": {
          "type": "string",
          "description": "Name of the city with the higher population."
        },
        "population": {
          "type": "integer",
          "description": "Population of the city with the higher population."
        }
      },
      "required": [
        "city_name",
        "population"
      ],
      "additionalProperties": false
    }
  },
  "required": [
    "comparison_result",
    "city_populations",
    "higher_population_city"
  ],
  "additionalProperties": false
}
