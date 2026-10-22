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
Guang'an: Guang'an () is a prefecture-level city in eastern Sichuan province.  It is most famous as the birthplace of China's former paramount leader Deng Xiaoping.  Guang'an lies between the hills of central Sichuan and the gorges area of the east.Guang'an is the only "Sichuan Chongqing Cooperation Demonstration Zone" in Sichuan and the nearest prefecture level city from the main city of Chongqing.  It has been incorporated into the 1 hour economic circle of Chongqing.Because of its strategic location, it is called the "Gateway to Eastern Sichuan". Its population in 2014 was 3,231,600.

Location as a service: Location as a service (LaaS) is a location data delivery model where privacy protected physical location data acquired through multiple sources including carriers, Wi-Fi, IP addresses and landlines is available to enterprise customers through a simple API.  The vast amount of location data provided in a LaaS model can be accessed by organizations to realize greater operational efficiencies, increase security, reduce costs and optimize customer engagement while achieving higher return on investment.  Location data is critical to many businesses as well as government organizations to drive real insight from data tied to a specific location where activities take place.  The spatial patterns that location data can provide is one of its most useful aspect where location is a common denominator in all of these activities and can be leveraged to better understand patterns and relationships.

Qingzhen: Qingzhen (Chinese: 清镇; Pinyin: Qīngzhèn) is a county-level city under the administration of Guiyang in Guizhou province, China.

Dong Guang Xinwen Tai: Dong Guang Xinwen Tai (Chinese: 东广新闻台), whose full callsign is Dong Guang News Radio of Shanghai People's Radio Station (Chinese: 上海人民广播电台东广新闻资讯广播), is a news radio channel in Shanghai in the People's Republic of China, broadcasting at both 90.9 and 1296 AM.

Heli-logging: Heli-Logging, or Helicopter Logging, is a method of logging that uses helicopters to remove cut trees from forests by lifting them on cables attached to a helicopter.  Helicopter logging is often used in inaccessible areas of forests.  Because the use of helicopters reduces the level of infrastructure required to log in a specific location, the method also helps to reduce the environmental impact of logging.  It also can increase the productivity in these remote areas.

Body load: Body load is the specific tactile sensations brought on by psychoactive drugs, especially psychedelics.  Generally, body load is an unpleasant physical sensation that is difficult to describe either in terms of other sensations or in its specific location.  However, it could be likened to an instinct of the body sensing it is about to be placed under exceptional stress, a state of pre-shock.  Nausea may be present with, or as a part of, body load.  Different drugs may cause different body load sensations which vary in intensity and duration.

Chromatin immunoprecipitation: Chromatin immunoprecipitation (ChIP) is a type of immunoprecipitation experimental technique used to investigate the interaction between proteins and DNA in the cell.  It aims to determine whether specific proteins are associated with specific genomic regions, such as transcription factors on promoters or other DNA binding sites, and possibly defining cistromes. ChIP also aims to determine the specific location in the genome that various histone modifications are associated with, indicating the target of the histone modifiers.

Guang'an District: Guang'an District (Chinese: 广安区; Pinyin: Guǎng'ān Qū) is a district in Guang'an City, Sichuan, China.

Standard Point Location Code: The Standard Point Location Code® (SPLC™) is a 9 digit geographic code used by North American transportation industries, especially rail.  SPLC is owned and maintained by the National Motor Freight Traffic Association.  SPLC exist for terminals within the United States, Canada, and Mexico.  For the US and Canada, the first two digits refer to a state, province or territory.  The second two digits refer to a county or its equivalent.  The third two digits refer to a city or municipal region.  The remaining three digits refer to a specific location within the city.  For Mexican SPLC, the first three digits refer to the state and the second three digits refer to a municipal region within the state.  Like the US and Canadian SPLC, the last three digits refer to a specific location within the city.  If the last three digits are "000" then the SPLC is not defined beyond city.

China Club of Seattle: The China Club of Seattle, founded in 1916 by Judge Thomas Burke, was an advocate for American investment in China and the development of Seattle’s trade with Asia, as well as a cultural and political organization.  The China Club’s economic goals included the expansion and renovation of Seattle’s port, the development of Chinese infrastructure, and the creation of connections between American businesses and contacts within China.  These efforts were ultimately intended to provide American businesses with access to and domination over Chinese markets.  Its cultural programs, focused in higher education, were largely connected to its economic programs.  The Club’s political advocacy originally focused on the creation of legislation regulating and prohibiting the use and sale of opiates.  During World War II, it would become involved in anti-Japanese protests, and It became an advocate for support of Taiwan after the Chinese Civil War.

Question: Which city in China,  Qingzhen or Guang'an, is the more specific location in terms of the hierarchy of Chinese infrastructure?

Respond with JSON matching this schema:
{
  "type": "object",
  "properties": {
    "more_specific_city": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the city identified as more specific."
        },
        "administrative_level": {
          "type": "string",
          "description": "The administrative level of the more specific city."
        }
      },
      "required": [
        "name",
        "administrative_level"
      ],
      "additionalProperties": false
    },
    "less_specific_city": {
      "type": "object",
      "properties": {
        "name": {
          "type": "string",
          "description": "The name of the city identified as less specific."
        },
        "administrative_level": {
          "type": "string",
          "description": "The administrative level of the less specific city."
        }
      },
      "required": [
        "name",
        "administrative_level"
      ],
      "additionalProperties": false
    },
    "comparison_result": {
      "type": "string",
      "description": "The name of the city that is the more specific location in terms of hierarchy."
    },
    "reasoning": {
      "type": "string",
      "description": "Explanation of why one city is considered more specific based on its administrative hierarchy within China."
    },
    "administrative_levels_involved": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "A list of administrative levels mentioned in the context that are relevant to the comparison."
    }
  },
  "required": [
    "more_specific_city",
    "less_specific_city",
    "comparison_result",
    "reasoning",
    "administrative_levels_involved"
  ],
  "additionalProperties": false
}
